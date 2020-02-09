
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

FILE_NAMES = ["a", "b", "c", "d", "e", "f", "g", "h"]
RANK_NAMES = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# WIP #STARTING_STATUS = ""

HEXAGONS = [
        b1,         e1,            
        b2, c2, d2, e2, f2, g2,    
    a3, b3, c3, d3, e3, f3, g3,    
    a4, b4, c4, d4, e4, f4, g4, h4,
    a5, b5, c5, d5, e5, f5, g5,    
    a6, b6, c6, d6, e6, f6, g6,    
    a7, b7, c7, d7, e7, f7, g7,    
    a8, b8, c8, d8, e8, f8, g8, h8,
            c9, d9,                
    ] = range(54)

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
        print(n_of_hexagon)
