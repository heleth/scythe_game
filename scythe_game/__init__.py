
# reference : ../_sample_python-chess/chess/__init__.py

from collections import defaultdict

#FILE_NAMES = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]  # not used
#FILE_INDICES = range(len(FILE_NAMES))  # not used

#RANK_NAMES = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]  # not used
#RANK_INDICES = range(len(RANK_NAMES))  # not used

TERRAIN_NAMES = [
    "Polania home base",
    "Albion home base",
    "Nordic home base",
    "Rusviet home base",
    "Togawa home base",
    "Crimea home base",
    "Saxony home base",
    "FARM",
    "FOREST",
    "MOUNTAIN",
    "TUNDRA",
    "VILLAGE",
    "LAKE",
    "FACTORY",
    ]
TERRAINS = range(len(TERRAIN_NAMES))

HEXAGON_NAMES = [
                      "d1",                               "j1",                               
                "c2",       "e2",       "g2",       "i2",       "k2",       "m2",            
          "b3",       "d3",       "f3",       "h3",       "j3",       "l3",       "n3",       
    "a4",       "c4",       "e4",       "g4",       "i4",       "k4",       "m4",       "o4",
          "b5",       "d5",       "f5",       "h5",       "j5",       "l5",       "n5",       
    "a6",       "c6",       "e6",       "g6",       "i6",       "k6",       "m6",            
          "b7",       "d7",       "f7",       "h7",       "j7",       "l7",       "n7",       
    "a8",       "c8",       "e8",       "g8",       "i8",       "k8",       "m8",       "o8",
                                  "f9",       "h9",                                           
    ]
HEXAGONS = range(len(HEXAGON_NAMES))
HEXAGON_TERRAINS = [None for x in HEXAGONS]
HEXAGON_TERRAINS[0] = 1

def hexagon_name(hexagon):
    return HEXAGON_NAMES[hexagon]

def hexagon_terrain(hexagon):
    return HEXAGON_TERRAINS[hexagon]

def hexagon_terrain_name(terrain):
    return TERRAIN_NAMES[terrain]

def graph():
    """Return graph of hexagonal map
    TODO : consider optional condition (e.g. riverwalk)
    TODO : use hexagon:int in stead of hexagon_name:str for saving time
    """
    graph = {
        47: [48, 53],
        48: [40, 47, 53],
        52: [47, 53],
        53: [47, 48],
        }
    return graph

def search_paths(graph, start_hexagon, cnt_move_remain, path_so_far=[]):
    """Return possible paths (list of path:list[str]) from given graph, start_hexagon, cnt_move)

    Returns
    -------
    paths : list[list[str]] or None
        None if no possible path exists.

    Notes
    -----
    recursive
    reference: https://www.python.org/doc/essays/graphs/
    """
    #print("func called: search_paths(graph, ", start_hexagon, cnt_move_remain, path_so_far, ")", end="")  # debug
    path_so_far = path_so_far + [start_hexagon]  # path_so_far : list[str]
    paths = [path_so_far]
    if cnt_move_remain <= 0 or (start_hexagon not in graph):
        #print(" -> end (return ", paths, ")")  #  debug
        return paths
    else:
        #print(" -> call another")  # debug
        for adjacent_hexagon in graph[start_hexagon]:
            #print("func being call: search_paths(graph, ", adjacent_hexagon, cnt_move_remain-1, path_so_far, ")")  # debug
            for new_path in search_paths(graph, adjacent_hexagon, cnt_move_remain-1, path_so_far):
                paths.append(new_path)
        return paths

def search_shortest_path(graph, start_hexagon, end_hexagon, path_so_far=[]):
    """Return shortest path from given graph, start_hexagon, end_hexagon)

    Returns
    -------
    path : list[list[str]] or None
        None if no possible path exists.

    Notes
    -----
    recursive
    reference: https://www.python.org/doc/essays/graphs/
    """
    path_so_far = path_so_far + [start_hexagon]
    if start_hexagon == end_hexagon:
        return path_so_far
    elif start_hexagon not in graph:
        return None
    else:
        path = None
        for adjacent_hexagon in graph[start_hexagon]:
            if adjacent_hexagon not in path_so_far:
                new_path = search_shortest_path(graph, adjacent_hexagon, end_hexagon, path_so_far)
                if new_path:
                    if not path or len(new_path) < len(path):
                        path = new_path
        return path

def calculate_distance(graph, start_hexagon, end_hexagon):
    """Calculate length of shortest path from given graph, start_hexagon, end_hexagon)

    Returns
    -------
    distance : int or None
        None if no possible path exists.

    """
    shortest_path = search_shortest_path(graph, start_hexagon, end_hexagon)
    if shortest_path:
        return len(shortest_path)-1
    else:
        return None


FACTIONS = [WHITE, GREEN, BLUE, RED, PURPLE, YELLOW, BLACK] = range(7)
FACTION_NAMES = [
    "Polania",
    "Albion",
    "Nordic",
    "Rusviet",
    "Togawa",
    "Crimea",
    "Saxony",
    ]

def faction_name(faction):
    return FACTION_NAMES[faction]

PIECE_TYPE_NAMES = [
    "character",
    "mech",
    "worker",
    "monument",
    "mill",
    "mine",
    "armory",
    "food",
    "wood",
    "iron",
    "oil",
    "encounter",
    "flag",
    "trap1(armed)",
    "trap1(disarmed)",
    "trap2(armed)",
    "trap2(disarmed)",
    "trap3(armed)",
    "trap3(disarmed)",
    "trap4(armed)",
    "trap4(disarmed)",
    "tunnel",
    ]
PIECE_TYPE_SYMBOLS = [
    "character",
    "mech",
    "worker",
    "monument",
    "mill",
    "mine",
    "armory",
    "food",
    "wood",
    "iron",
    "oil",
    "encounter",
    "flag",
    "trap1(armed)",
    "trap1(disarmed)",
    "trap2(armed)",
    "trap2(disarmed)",
    "trap3(armed)",
    "trap3(disarmed)",
    "trap4(armed)",
    "trap4(disarmed)",
    "tunnel",
    ]
PIECE_TYPES = range(len(PIECE_TYPE_NAMES))  # TODO: inicrease types

def piece_type_symbol(piece_type):
    return PIECE_TYPE_SYMBOLS[piece_type]

def piece_type_name(piece_type):
    return PIECE_TYPE_NAMES[piece_type]

class Piece:
    """Pieces (of all type, placeable on the board)

    Notes
    -----
    * piece placeable on board
        - character
        - mech
        - worker
        - structure (4 types)
        - resource (4 types)
        - encounter (front or back)
        - flag (front or back)
        - trap (front or back, 4 types)
    """

    def __init__(self, faction, piece_type):
        self.faction = faction
        self.piece_type = piece_type

    def type_symbol(self):
        return piece_type_symbol(self.piece_type)

    def type_name(self):
        return piece_type_name(self.piece_type)

    def faction_name(self):
        return faction_name(self.faction)

    def info(self):
        return "{faction_name} {piece_type_name}".format(
            faction_name=self.faction_name(),
            piece_type_name=self.type_name(),
            )

    # TODO
    # implement method below
    #   - __hash__()
    #   - __repr__()
    #   - __str__()
    #   - __repr_svg__()
    #   - __eq__()


class Board():
    """Game board (with all pieces on it)
    """

    def __init__(self):
        self.board = {hexagon:[] for hexagon in HEXAGONS}

    def pieces(self, hexagon):
        """Return all pieces on given hexagon"""
        return self.board[hexagon]

    def put(self, hexagon, piece):
        """Put a piece on a hexagon"""
        self.board[hexagon].append(piece)


class Game():
    """Game status (board, figure, panel etc.)

    TODOS
    -----
    member variable needed
      - factions
      - pieces
      - faction mat
      - player mat
      - star
      - power
      - combat card
      - popularity
      - coin
    """

    def __init__(self, factions=[0,1]):
        
        self.factions = factions
        self.board = Board()

    def faction_names(self):
        """Return name of factions on game"""
        return [faction_name(faction) for faction in self.factions]

    def describe_hexagon(self, hexagon):
        """Return information of given hexagon"""
        print("{hexagon_name} ({terrain}) : {pieces}".format(
            hexagon_name=hexagon_name(hexagon),
            terrain=hexagon_terrain_name(hexagon),
            pieces=", ".join([piece.info() for piece in self.board.pieces(hexagon)]),
            ))

    def test(self):
        """test"""
        #graph_ = graph()
        #print(search_shortest_path(graph_, 52, 40))
        #print(calculate_distance(graph_, 52, 40))

        #print(Piece(0, 0).info())

        #print(self.faction_names())

        self.board.put(0, Piece(0,0))
        self.board.put(0, Piece(1,10))
        self.describe_hexagon(0) 

