grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
# Output: 1

grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
# Output: 3

# iterative pass through the grid o(nXm)
# consider an array of visited flags
# if you see a 1 then determine if it is connected to an existing island.
# count the total islands you've encountered


def island_count(grid):
    count = 0
    if not grid:
        return count

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "1":
                # either need to increment count
                # determine if the 1 is part of an existing island
                if i == 0 or (i > 0 and grid[i - 1][j] == "0"):
                    if j == 0 or (j > 0 and grid[i][j - 1] == "0"):
                        count += 1
    return count


assert island_count(grid1) == 1
assert island_count(grid2) == 3
