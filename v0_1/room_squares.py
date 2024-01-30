import json
d = {"start": [(0, 0)],
     "1x1": [(0, 0)],
     "1x2": [(0, 0), (1, 0)],
     "2x2": [(0, 0), (1, 0), (0, 1), (1, 1)]
     }
with open("room_squares.json", "w") as f:
    f.write(json.dumps(d, indent=4))