import aiohttp
import json

WLED_HOST = "192.168.0.100"
WLED_STATE_URL = f"http://{WLED_HOST}/json/state"

async def triggerLED(message):
    if message == "":
        print("No function")
        return False
    
    # Defaults -----

    message["transition"] = 1

    if "seg" in message and type(message["seg"]) is dict:
            message["seg"] = [message["seg"]]
            if "bri" not in message:
                message["bri"] = 255

    if "seg" in message:
        for item in message["seg"]:
            if "fx" in item and item["fx"] != 0 and not "sx" in item:
                item["sx"] = 80

    if "seg" in message:
        if len(message["seg"]) == 1 and not "id" in message["seg"][0]:
            newMessage = []
            message["seg"] = message["seg"][0]
            newMessage.insert(0, {"id":4, "start":320, "stop":400, "on":True} | message["seg"])
            newMessage.insert(0, {"id":3, "start":240, "stop":320, "on":True} | message["seg"]) 
            newMessage.insert(0, {"id":2, "start":160, "stop":240, "on":True} | message["seg"])
            newMessage.insert(0, {"id":1, "start":80, "stop":160, "on":True} | message["seg"])
            newMessage.insert(0, {"id":0, "start":0, "stop":80, "on":True} | message["seg"])
            message["seg"] = newMessage
        elif len(message["seg"]) == 1 and "id" in message["seg"][0]:
            newMessage = []
            newMessage.append({"id":4, "start": 10, "stop":0})
            newMessage.append({"id":3, "start": 10, "stop":0}) 
            newMessage.append({"id":2, "start": 10, "stop":0})
            newMessage.append({"id":1, "start": 10, "stop":0})
            newMessage.append({"id":0, "start": 10, "stop":0})
            newMessage.append(message["seg"][0])
            message["seg"] = newMessage
    # --------------

    print(message)
        
    print("Sending WLED request...")
    headers = {'Content-Type': 'application/json'}
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(WLED_STATE_URL, headers=headers, data=json.dumps(message)) as response:
                if response.status == 200:
                    print("Device triggered successfully.")
                    return True
                else:
                    text = await response.text()
                    print(f"Failed to trigger on device. Status code: {response.status}, Response: {text}")
                    return False
        except Exception as e:
            print(f"<! Error during request !>")
            return False

import asyncio
import obsws_python as obs
from obsws_python.error import OBSSDKError

OBS_HOST = "localhost"   # or the PC running OBS
OBS_PORT = 4455
OBS_PASSWORD = None      # set to your OBS WebSocket password string if enabled

def _switch_scene_sync(scene_name: str) -> bool:
    client = obs.ReqClient(host=OBS_HOST, port=OBS_PORT, password=OBS_PASSWORD, timeout=5)
    try:
        # Optional sanity check. Uncomment if you want to verify connection.
        # client.get_version()
        client.set_current_program_scene(scene_name)
        print(f"Switched to OBS scene '{scene_name}'")
        return True
    except OBSSDKError as e:
        print(f"OBS error: {e}")
        return False
    except Exception as e:
        print(f"Failed to switch scene: {e}")
        return False
    finally:
        try:
            client.close()
        except Exception:
            pass

async def triggerVideo(scene_name: str) -> bool:
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, _switch_scene_sync, scene_name)
