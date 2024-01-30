import json
BLOCK_WIDTH = 10
with open("rooms.json", "r") as f:
    rooms = json.load(f)
coords = {}
with open("space.txt") as f:
    drawing_space = f.read().splitlines()

# for y in range(0, BLOCK_WIDTH):
#     for x in range(0, BLOCK_WIDTH):
#         if x == 0 or x == BLOCK_WIDTH-1 or y == 0 or y == BLOCK_WIDTH-1:
#             coords[f"{x},{y}"] = ":white_large_square:"
for r, row in enumerate(drawing_space):
    for c, char in enumerate(row):
        coord = f"{c},{r}"
        if char == "@":
            coords[coord] = ":green_square:"
        elif char == "$":
            coords[coord] = ":red_square:"
        elif char == "#":
            coords[coord] = ":brick:"
        elif char == ".":
            coords[coord] = ":dark_skin_tone:"
        elif char == ":":
            coords[coord] = ":black_square_button:"

rooms["end"] = coords
with open("rooms.json", "w") as f:
    f.write(json.dumps(rooms, indent=4))

#start
'''@@@@@@@@@@
@........@
@........@
@........@
@........@
@........@
@........@
@........@
@........@
@@@@::@@@@'''

#end
'''$$$$::$$$$
$........$
$........$
$........$
$........$
$........$
$........$
$........$
$........$
$$$$$$$$$$'''

#1x1
'''####::####
#........#
#........#
#........#
:........:
:........:
#........#
#........#
#........#
####::####'''

#1x2
'''####::########::####
#..................#
#..................#
#..................#
:..................:
:..................:
#..................#
#..................#
#..................#
####::########::####'''

#2x2
'''####::########::####
#..................#
#..................#
#..................#
:..................:
:..................:
#..................#
#..................#
#..................#
#..................#
#..................#
#..................#
#..................#
#..................#
:..................:
:..................:
#..................#
#..................#
#..................#
####::########::####'''