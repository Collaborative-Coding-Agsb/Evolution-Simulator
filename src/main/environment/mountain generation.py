import numpy as np

def generate_mountain(width, height):
    terrain_grid = np.zeros([height, width], dtype=int)
    for y in range(height):
        for x in range(width):
            terrain_grid[y][x] = '-'
    
    return terrain_grid

print(generate_mountain(10,10))
