import pygame
import pygame.gfxdraw

GRID_W = 9
GRID_H = 9
CELL = 92
GAP = 3
PAD = 24

BG_COLOR = (12, 12, 14)
GRID_COLOR = (30, 30, 34)

INNER_PAD = 8
ELEV = 4  # vertical lift for the lighter top face

SHADOW_OFFSET = (4, 4)
SHADOW_ALPHA = 80
SHADOW_BLUR = 6  # soft spread

FONT_NAME = "departuremononerdfontmono"
FONT_BOLD = True


def _scale_color(rgb_0_63):
    r, g, b = rgb_0_63
    k = 255 / 63.0
    return (min(255, int(round(r * k))),
            min(255, int(round(g * k))),
            min(255, int(round(b * k))))


def _get_name(cell_data):
    if not isinstance(cell_data, dict):
        return ""
    return cell_data.get("name") or cell_data.get("Name") or ""


def _relative_luminance(rgb):
    r, g, b = rgb
    return 0.2126*r + 0.7152*g + 0.0722*b


def _choose_text_color(bg):
    return (255, 255, 255) if _relative_luminance(bg) < 150 else (30, 30, 30)


def _darken(c, amt=28):
    return (max(0, c[0]-amt), max(0, c[1]-amt), max(0, c[2]-amt))


def _lighten(c, amt=22):
    return (min(255, c[0]+amt), min(255, c[1]+amt), min(255, c[2]+amt))


# ---------- Antialias helpers ----------

def _draw_circle_aa(surface, center, radius, color):
    x, y = center
    pygame.gfxdraw.filled_circle(surface, x, y, radius, color)
    pygame.gfxdraw.aacircle(surface, x, y, radius, color)


def _draw_roundrect_aa(surface, rect, color, radius):
    """Antialiased rounded rect using 2x supersampling + smoothscale."""
    if radius <= 0:
        # fallback to a simple filled rect
        pygame.draw.rect(surface, color, rect)
        return

    # Create 2x surface with alpha
    upscale = 2
    w2, h2 = rect.width * upscale, rect.height * upscale
    temp = pygame.Surface((w2, h2), pygame.SRCALPHA)
    temp.fill((0, 0, 0, 0))

    r2 = radius * upscale
    # Draw on temp at 2x
    pygame.draw.rect(temp, color, pygame.Rect(0, 0, w2, h2), border_radius=r2)

    # Smooth down to target size
    aa = pygame.transform.smoothscale(temp, (rect.width, rect.height))
    surface.blit(aa, rect.topleft)


def _draw_shape_aa(surface, rect, color, shape, radius):
    if shape == "circle":
        center = rect.center
        rad = min(rect.width, rect.height) // 2
        _draw_circle_aa(surface, center, rad, color)
    else:
        _draw_roundrect_aa(surface, rect, color, radius)


# ---------- Shadows ----------

def _draw_shadow(surface, rect, shape="rect", radius=16):
    # Shadow drawn on its own alpha surface to control softness
    w = rect.width + SHADOW_BLUR*2
    h = rect.height + SHADOW_BLUR*2
    shadow = pygame.Surface((w, h), pygame.SRCALPHA)
    shadow.fill((0, 0, 0, 0))

    inner = pygame.Rect(SHADOW_BLUR, SHADOW_BLUR, rect.width, rect.height)
    col = (0, 0, 0, SHADOW_ALPHA)

    _draw_shape_aa(shadow, inner, col, "circle" if shape == "circle" else "rect", radius)

    surface.blit(shadow, (rect.x + SHADOW_OFFSET[0] - SHADOW_BLUR,
                          rect.y + SHADOW_OFFSET[1] - SHADOW_BLUR))


# ---------- Text ----------

def _render_text_fit(surface, text, rect, max_size=26, min_size=8, color=(255,255,255)):
    if not text:
        return
    size = max_size
    while size >= min_size:
        font = pygame.font.SysFont(FONT_NAME, size, bold=FONT_BOLD)
        surf = font.render(text, True, color)  # antialiased text
        if surf.get_width() <= rect.width - 6 and surf.get_height() <= rect.height - 6:
            x = rect.x + (rect.width - surf.get_width()) // 2
            y = rect.y + (rect.height - surf.get_height()) // 2
            surface.blit(surf, (x, y))
            return
        size -= 1
    font = pygame.font.SysFont(FONT_NAME, min_size, bold=FONT_BOLD)
    surf = font.render(text, True, color)
    x = rect.x + (rect.width - surf.get_width()) // 2
    y = rect.y + (rect.height - surf.get_height()) // 2
    surface.blit(surf, (x, y))


# ---------- Main draw ----------

def draw_buttons_grid(buttons_dict, screen=None):
    """Draw the grid with antialiased shapes, soft shadow, and 3D lip."""
    if not pygame.get_init():
        pygame.init()
        pygame.font.init()

    W = PAD * 2 + GRID_W * CELL + (GRID_W - 1) * GAP
    H = PAD * 2 + GRID_H * CELL + (GRID_H - 1) * GAP

    if screen is None:
        # If you want MSAA via OpenGL, you can try enabling it here:
        # pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        # pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)
        # screen = pygame.display.set_mode((W, H), pygame.OPENGL | pygame.DOUBLEBUF)
        screen = pygame.display.set_mode((W, H))
        pygame.display.set_caption("Launchpad Buttons Viewer")

    screen.fill(BG_COLOR)

    # Grid background cells
    for row in range(GRID_H):
        for col in range(GRID_W):
            x = PAD + col * (CELL + GAP)
            y = PAD + row * (CELL + GAP)
            rect = pygame.Rect(x, y, CELL, CELL)
            _draw_roundrect_aa(screen, rect, GRID_COLOR, radius=14)

    # Buttons with darker base + lifted lighter top
    for row in range(GRID_H):
        for col in range(GRID_W):
            x = PAD + col * (CELL + GAP)
            y = PAD + row * (CELL + GAP)
            rect = pygame.Rect(x, y, CELL, CELL)
            cell = buttons_dict.get(row, {}).get(col, None)

            base_col = _scale_color(cell["color"]) if isinstance(cell, dict) and "color" in cell else (0, 0, 0)
            dark_base = _darken(base_col, 36)
            light_top = _lighten(base_col, 18)

            inner = rect.inflate(-INNER_PAD, -INNER_PAD)
            shape = "circle" if row == 0 or col == GRID_W - 1 else "rect"

            # Shadow
            _draw_shadow(screen, inner, shape=shape, radius=16)

            # Dark base at inner
            _draw_shape_aa(screen, inner, dark_base, shape, radius=16)

            # Lighter top face lifted up
            top_rect = inner.move(0, -ELEV)
            _draw_shape_aa(screen, top_rect, light_top, shape, radius=16)

            # Text centered on the top face
            name = _get_name(cell)
            if name:
                text_color = _choose_text_color(light_top)
                _render_text_fit(screen, name, top_rect, color=text_color)

    pygame.display.flip()
    return screen
