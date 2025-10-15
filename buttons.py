from enum import Enum

class mType(Enum):
    LED = 1
    VID = 2


colorArray = ["FFFFFFFF" for _ in range(360)]

brightnessScale=0.20

buttonsDict = {
    0: {
        0: {
            "color": [63, 63, 63],
            "type": mType.LED,
            "message": {"seg":{"sx":"~5"},"v":True,"time":1759468444},
            "name": "+ Speed"
        },
        1: {
            "color": [63, 63, 63],
            "type": mType.LED,
            "message": {"seg":{"sx":"~-5"},"v":True,"time":1759468444},
            "Name": "- Speed"
        },
        2: {
            "color": [63, 63, 63],
            "type": mType.LED,
            "message": {"seg":{"sx":"0"},"v":True,"time":1759468444},
            "name": "Low"
        },
        3: {
            "color": [63, 63, 63],
            "type": mType.LED,
            "message": {"seg":{"sx":"120"},"v":True,"time":1759468444},
            "name": "Med"
        },
        4: {
            "color": [63, 63, 63],
            "type": mType.LED,
            "message": {"seg":{"sx":"255"},"v":True,"time":1759468444},
            "name": "High"
        },
        5: {
            "color": [63, 63, 63],
            "type": mType.LED,
            "message": {"bri": 255}
        },
        6: {
            "color": [27, 27, 27],
            "type": mType.LED,
            "message": {"bri": 100}
        },
        7: {
            "color": [6, 6, 6],
            "type": mType.LED,
            "message": {"bri": 20}
        },
    },
    1: {
        0: {
            "color": [30, 33, 63],
            "type": mType.LED,
            "message": {"on":True,"seg":{"fx":0,"fxdef":False},"v":True,"time":1759527492},
            "name": "Solid"
        },
        1: {
            "color": [0, 33, 63],
            "type": mType.LED,
            "message": {"on":True,"seg":{"fx":76,"sx":255,"fxdef":False},"v":True,"time":1759527492},
            "name": "Meteor"
        },
        2: {
            "color": [30, 33, 63],
            "type": mType.LED,
            "message": {"on":True,"seg":{"fx":159,"sx":200,"fxdef":True},"v":True,"time":1759528910},
            "name": "DJ"
        },
        3: {
            "color": [0, 33, 63],
            "type": mType.LED,
            "message": {"on":True,"seg":{"fx":96,"sx":200,"fxdef":True},"v":True,"time":1759528910},
            "name": "Drip"
        },
        4: {
            "color": [30, 33, 63],
            "type": mType.LED,
            "message":  {"on":True,"seg":{"fx":110,"sx":200,"fxdef":True},"v":True,"time":1759528910},
            "name": "OutfLow"
        },
        5: {
            "color": [0, 33, 63],
            "type": mType.LED,
            "message": {"on":True,"seg":{"fx":109,"sx":200,"fxdef":True},"v":True,"time":1759528910},
            "name": "Phased"
        },
        6: {
            "color": [30, 33, 63],
            "type": mType.LED,
            "message": {"on":True,"seg":{"fx":134,"sx":230,"ix":220,"fxdef":True},"v":True,"time":1759528910},
            "name": "Rain"
        },
        7: {
            "color": [0, 33, 63],
            "type": mType.LED,
            "message": ""
        },
        8: {
            "color": [30, 63, 0],
            "type": mType.LED,
            "message": {"on":True,"v":True,"time":1759467828},
            "name": "On"
        }
    },
    2: {
        0: {
            "color": [0, 33, 63],
            "type": mType.LED,
            "message": {"on":True,"seg":{"fx":23,"fxdef":True,"sx":250},"v":True,"time":1759525746},
            "name": "Strobe"
        },
        1: {
            "color": [30, 33, 63],
            "type": mType.LED,
            "message": {"on":True,"seg":{"fx":74,"fxdef":True},"v":True,"time":1759468444},
            "name": "Pixels"
        },
        2: {
            "color": [0, 33, 63],
            "type": mType.LED,
            "message": {"on":True,"seg":{"fx":111,"fxdef":True},"v":True,"time":1759525746},
            "name": "Chun"
        },
        3: {
            "color": [30, 33, 63],
            "type": mType.LED,
            "message": {"on":True,"seg":{"fx":112,"fxdef":True},"v":True,"time":1759526757},
            "name": "Dance"
        },
        4: {
            "color": [0, 33, 63],
            "type": mType.LED,
            "message": {"on":True,"seg":{"fx":38,"sx":200,"fxdef":True},"v":True,"time":1759526757},
            "name": "Aurora"
        },
        5: {
            "color": [30, 33, 63],
            "type": mType.LED,
            "message": {"on":True,"seg":{"fx":43,"sx":250, "ix":200,"fxdef":True},"v":True,"time":1759526757},
            "name": "Birds"
        },
        6: {
            "color": [0, 33, 63],
            "type": mType.LED,
            "message": ""
        },
        7: {
            "color": [30, 33, 63],
            "type": mType.LED,
            "message": ""
        },
        8: {
            "color": [63, 0, 0],
            "type": mType.LED,
            "message": {"on":False,"v":True,"time":1759467828},
            "name": "Off"
        },
    },
    3: {
        0: {
            "color": [63, 0, 0],
            "type": mType.LED,
            "message": {"seg":{"pal":2,"col":[[255,15,35,0],[],[]]},"v":True,"time":1759467828}
        },
        1: {
            "color": [0, 63, 0],
            "type": mType.LED,
            "message": {"seg":{"pal":2,"col":[[20,255,35,0],[],[]]},"v":True,"time":1759467828}
        },
        2: {
            "color": [0, 0, 63],
            "type": mType.LED,
            "message": {"seg":{"pal":2,"col":[[10,15,255,0],[],[]]},"v":True,"time":1759467828}
        },
        3: {
            "color": [63, 63, 0],
            "type": mType.LED,
            "message": {"seg":{"pal":2,"col":[[255,255,0,0],[],[]]},"v":True,"time":1759467828}
        },
        4: {
            "color": [63, 20, 63],
            "type": mType.LED,
            "message": {"seg":{"pal":2,"col":[[255,100,255,0],[],[]]},"v":True,"time":1759467828}
        },
        5: {
            "color": [43, 20, 63],
            "type": mType.LED,
            "message": {"seg":{"pal":2,"col":[[155,100,255,0],[],[]]},"v":True,"time":1759467828}
        },
        6: {
            "color": [0, 63, 63],
            "type": mType.LED,
            "message": {"seg":{"pal":2,"col":[[0,255,255,0],[],[]]},"v":True,"time":1759467828}
        },
        7: {
            "color": [63, 63, 63],
            "type": mType.LED,
            "message": {"seg":{"pal":2,"col":[[255,255,255,0],[],[]]},"v":True,"time":1759467828}
        },
        8: {
            "color": [63, 63, 63],
            "type": mType.LED,
            "message": {"on":"t","v":True,"time":1759467828},
            "name": "Tog",
            "double": True
        }
    },
    4: {
        0: {
            "color": [0, 52, 63],
            "type": mType.LED,
            "message": {"seg":{"pal":50},"v":True,"time":1759524800},
            "name": "Aurora"
        },
        1: {
            "color": [60, 13, 2],
            "type": mType.LED,
            "message": {"seg":{"pal":8},"v":True,"time":1759524800},
            "name": "Lava"
        },
        2: {
            "color": [13, 43, 63],
            "type": mType.LED,
            "message": {"seg":{"pal":7},"v":True,"time":1759524800},
            "name": "Cloud"
        },
        3: {
            "color": [49, 0, 63],
            "type": mType.LED,
            "message": {"seg":{"pal":18},"v":True,"time":1759524800},
            "name": "R-B"
        },
        4: {
            "color": [63, 33, 33],
            "type": mType.LED,
            "message": {"seg":{"pal":28},"v":True,"time":1759524800}, 
            "name": "Bubl"
        },
        5: {
            "color": [63, 63, 63],
            "type": mType.LED,
            "message": {"seg":{"pal":12},"v":True,"time":1759524800},
            "name": "RGB"
        },
        6: {
            "color": [0, 33, 63],
            "type": mType.LED,
            "message": {"seg":{"pal":5},"v":True,"time":1759524800},
            "name": "Single"
        },
        7: {
            "color": [0, 33, 63],
            "type": mType.LED,
            "message": ""
        },
    },
    5: {
        0: {
            "color": [30, 0, 63],
            "type": mType.VID,
            "message": "Scene",
            "name": "berlin"
        },
        1: {
            "color": [60, 0, 3],
            "type": mType.VID,
            "message": "Scene 2",
            "name": "red"
        },
        2: {
            "color": [60, 20, 20],
            "type": mType.VID,
            "message": "Scene 3",
            "name": "square"
        },
        3: {
            "color": [60, 0, 3],
            "type": mType.VID,
            "message": "Scene 4",
            "name": "trip 1"
        },
        4: {
            "color": [60, 0, 3],
            "type": mType.VID,
            "message": "Scene 5",
            "name": "trip 2"
        },
        5: {
            "color": [40, 0, 3],
            "type": mType.VID,
            "message": "Scene 6",
            "name": "hills"
        },
        6: {
            "color": [5, 63, 3],
            "type": mType.VID,
            "message": "Scene 7",
            "name": "plants"
        },
        7: {
            "color": [10, 10, 10],
            "type": mType.VID,
            "message": "Logo Overlay",
            "name": "logo"
        },
    },
    6: {
        0: {
            "color": [60, 10, 20],
            "type": mType.VID,
            "message": ""
        },
        1: {
            "color": [60, 10, 20],
            "type": mType.VID,
            "message": ""
        },
        2: {
            "color": [60, 10, 20],
            "type": mType.VID,
            "message": ""
        },
        3: {
            "color": [60, 10, 20],
            "type": mType.VID,
            "message": ""
        },
        4: {
            "color": [60, 10, 20],
            "type": mType.VID,
            "message": ""
        },
        5: {
            "color": [60, 10, 20],
            "type": mType.VID,
            "message": ""
        },
        6: {
            "color": [60, 10, 20],
            "type": mType.VID,
            "message": ""
        },
        7: {
            "color": [60, 10, 20],
            "type": mType.VID,
            "message": ""
        },
    },
    7: {
        0: {
            "color": [30, 0, 63],
            "type": mType.VID,
            "message": ""
        },
        1: {
            "color": [30, 0, 63],
            "type": mType.VID,
            "message": ""
        },
        2: {
            "color": [30, 0, 63],
            "type": mType.VID,
            "message": ""
        },
        3: {
            "color": [30, 0, 63],
            "type": mType.VID,
            "message": ""
        },
        4: {
            "color": [30, 0, 63],
            "type": mType.VID,
            "message": ""
        },
        5: {
            "color": [30, 0, 63],
            "type": mType.VID,
            "message": ""
        },
        6: {
            "color": [30, 0, 63],
            "type": mType.VID,
            "message": ""
        },
        7: {
            "color": [30, 0, 63],
            "type": mType.VID,
            "message": ""
        },
    },
    8: {
        0: {
            "color": [60, 10, 20],
            "type": mType.VID,
            "message": ""
        },
        1: {
            "color": [60, 10, 20],
            "type": "vidvid",
            "message": ""
        },
        2: {
            "color": [60, 10, 20],
            "type": mType.VID,
            "message": ""
        },
        3: {
            "color": [60, 10, 20],
            "type": mType.VID,
            "message": ""
        },
        4: {
            "color": [60, 10, 20],
            "type": mType.VID,
            "message": ""
        },
        5: {
            "color": [60, 10, 20],
            "type": mType.VID,
            "message": ""
        },
        6: {
            "color": [60, 10, 20],
            "type": mType.VID,
            "message": ""
        },
        7: {
            "color": [60, 10, 20],
            "type": mType.VID,
            "message": ""
        },
    },
}