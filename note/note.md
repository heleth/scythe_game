# Note

## ミス
* classのメンバー変数の第1引数をselfにするのを忘れないこと

## Work note
* all hebagon names
    "a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1", "i1", "j1", "k1", "l1", "m1", "n1", "o1",
    "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2", "i2", "j2", "k2", "l2", "m2", "n2", "o2",
    "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3", "i3", "j3", "k3", "l3", "m3", "n3", "o3",
    "a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4", "i4", "j4", "k4", "l4", "m4", "n4", "o4",
    "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5", "i5", "j5", "k5", "l5", "m5", "n5", "o5",
    "a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6", "i6", "j6", "k6", "l6", "m6", "n6", "o6",
    "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7", "i7", "j7", "k7", "l7", "m7", "n7", "o7",
    "a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8", "i8", "j8", "k8", "l8", "m8", "n8", "o8",
    "a9", "b9", "c9", "d9", "e9", "f9", "g9", "h9", "i9", "j9", "k9", "l9", "m9", "n9", "o9",

* old code of hexagon (file and rank coordinate)
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
