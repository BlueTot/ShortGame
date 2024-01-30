import random, msvcrt, os, emoji, json, itertools, collections
N = 5
def is_connected(squares):
    queue, visited = collections.deque([squares[0]]), set()
    while queue:
        x, y = queue.popleft()
        visited.add((x, y))
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)): 
            if (x+dx, y+dy) not in visited and (x+dx, y+dy) in squares: queue.append((x+dx, y+dy))
    return len(visited) == len(squares)
def possible_room_combinations(grid, room_squares):
    for x in range(N):
        for y in range(N):
            if len(set(grid) & (adjusted_room_squares := set([(i+x, j+y) for i, j in room_squares]))) == 0 and is_connected(list((squares := adjusted_room_squares | grid) - {(N-1, N-1)})) and all([0 <= i < 5 and 0 <= j < 5 for i, j in adjusted_room_squares]): yield x, y, squares
def generate_rooms(rooms = {(0, 0): "start", (N-1, N-1): "end"}, grid = {(0, 0), (N-1, N-1)}, empty_squares = [(i, j) for i, j in itertools.product(range(N), repeat=2) if (i, j) not in [(0, 0), (N-1, N-1)]]):
    with open("room_squares.json") as f: room_squares = json.load(f)
    while empty_squares:
        try:
            room_choice = random.choice([i for i in room_squares if i not in ("start", "end")])
            x, y, grid = random.choice([poss for poss in possible_room_combinations(grid, set(map(tuple, room_squares[room_choice])))])
            rooms[(x, y)] = room_choice
            for i, j in room_squares[room_choice]:
                empty_squares.remove((x+i, y+j))
        except IndexError: continue
    return rooms
def generate_grid(grid = {}):
    with open("rooms.json") as f: rooms = json.load(f)
    for coord, room_name in generate_rooms().items():
        for room_coord, symbol in rooms[room_name].items(): grid[(coord[0]*10 + int(room_coord.split(",")[0]), coord[1]*10 + int(room_coord.split(",")[1]))] = symbol
    return grid
def print_grid(): 
    os.system("cls")
    for y in range(player_y - fov, player_y + fov + 1): 
        for x in range(player_x - fov, player_x + fov + 1): print((emoji.emojize(grid[(x, y)]) if (x, y) in grid else emoji.emojize(":black_large_square:")) if (x, y) != (player_x, player_y) else emoji.emojize(":downwards_button:"), end='\n' if x == player_x + fov else '')
player_x, player_y, fov, grid, = 5, 5, 10, generate_grid()
while True:
    print_grid()
    try:
        user_input = msvcrt.getch().decode("utf-8").lower()
        dx, dy = {"w": (0, -1), "a": (-1, 0), "s": (0, 1), "d": (1, 0)}[user_input]
        if grid[(player_x + dx, player_y + dy)] in (":dark_skin_tone:", ":black_square_button:"): player_x, player_y = player_x + dx, player_y + dy
    except Exception: pass