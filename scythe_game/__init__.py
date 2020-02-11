
# reference : ../_sample_python-chess/chess/__init__.py

FACTIONS = [WHITE, GREEN, BLUE, RED, PURPLE, YELLOW, BLACK] = range(1, 8)
FACTION_NAMES = [
    "Polania",
    "Albion",
    "Nordic",
    "Rusviet",
    "Togawa",
    "Crimea",
    "Saxony",
    ]

PIECE_TYPES = [CHARACTER, MECH, PAWN] = range(1, 4)
PIECE_SYMBOLS = [None, "C", "M", "P"]
PIECE_NAMES = [None, "character", "mech", "pawn"]

def piece_symbol(piece_type):
    return PIECE_SYMBOLS[piece_type]

def piece_name(piece_type):
    return PIECE_NAMES[piece_type]

FILE_NAMES = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]
FILE_INDICES = range(len(FILE_NAMES))

RANK_NAMES = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
RANK_INDICES = range(len(RANK_NAMES))

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
HEXAGONS = [
    (
        FILE_NAMES.index(hexagon_name[0]),
        RANK_NAMES.index(hexagon_name[1])
        )
    for hexagon_name
    in HEXAGON_NAMES
    ]  # list[tuple[int,int]]

def hexagon(file_index, rank_index):
    """return a hexagon of specified file and rank index (return None if not exists)"""
    if (file_index, rank_index) in HEXAGONS:
        return (file_index, rank_index)
    else:
        return None

def hexagon_file(hexagon):
    return hexagon[0]

def hexagon_rank(hexagon):
    return hexagon[1]

def hexagon_name(hexagon):
    return HEXAGON_NAMES[HEXAGONS.index(hexagon)]

class Status(object):
    """Game status (board, figure, panel etc.)
    Including:
      - (WIP) action generation
      - (WIP) action validation
      - (WIP) state evaluation
      - (WIP) move counter
      - (WIP) capability to make a move
    (WIP) Initialized at the start.
    """

    def __init__(self):
        a = len(HEXAGONS)
        b = hexagon(1,2)
        c = hexagon_name((1,2))
        print(a,b,c)



