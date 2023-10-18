# Flood Fill Algorithm

This project implements a Flood Fill algorithm in Python. The algorithm replaces old values with new values through a flood filling process, starting from the specified coordinates.

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine.

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository to your local machine.
2. Change your directory to the project folder.
### Usage

To use the Flood Fill algorithm, you can call the `flood_fill` function with the following parameters:

- `input_board`: A list of strings representing the initial board.
- `old`: The value to be replaced.
- `new`: The value that replaces the old.
- `x`: The X-coordinate of the flood start point.
- `y`: The Y-coordinate of the flood start point.

Example usage:

```python
from typing import List

# Define the board
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

# Call the flood_fill function
modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

# Print the modified board
for row in modified_board:
    print(row)
Expected Output
The above code will replace all occurrences of . with ~ through the flood filling process, starting from the specified coordinates.
......................
......##########......
......#~~~~~~~~#......
......#~~~~~~~~#......
......#~~~~~~~~#####..
....###~~~~~~~~~~~~#..
....#~~~~~~~~~~~~###..
....##############....