from typing import List

def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    def fill(x, y):
        # You can combine the two if statements below into one, but I think it's easier to read this way.
        if x < 0 or x >= len(input_board) or y < 0 or y >= len(input_board[0]) or input_board[x][y] != old:
            return
        # if x < 0 or x >= len(input_board) or y < 0 or y >= len(input_board[0]):
        #     return
        # if input_board[x][y] != old:
        #     return
        input_board[x] = input_board[x][:y] + new + input_board[x][y + 1:]
        fill(x - 1, y)
        fill(x + 1, y)
        fill(x, y - 1)
        fill(x, y + 1)

    fill(x, y)

    return input_board

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for row in modified_board:
    print(row)