class Board:
    """
    A class representing a bitboard
    """
    def __init__(self):
        self.white_pawns = 65280    # 1111111100000000 in binary (A2 to H2)
        self.white_rooks = 129      # 10000001 in binary (A1 and H1)
        self.white_knights = 66     # 01000010 in binary (B1 and G1)
        self.white_bishops = 0      # 00100100 in binary (C1 and F1)
        self.white_queen = 0        # 00010000 in binary (D1)
        self.white_king = 0         # 00001000 in binary (E1)
        
        self.black_pawns = 0        # (A7 to H7)
        self.black_rooks = 0        # (A8 and H8)
        self.black_knights = 0      # (B8 and G8)
        self.black_bishops = 0      # (C8 and F8)
        self.black_queen = 0        # (D8)
        self.black_king = 0         # (E8)
