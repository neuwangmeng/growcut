""" Python implementation of growcut """

import numpy as np

NEIGHBOURS = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def iterNeighbours((r, c), shape, neighbours=NEIGHBOURS):
    """ Yield the point neighborhood """
    for (dr, dc) in neighbours:
        yield (r + dr) % shape[0], (c + dc) % shape[1]


def iterGrid(grid):
    """ Iterate through a grid """
    for point in np.ndindex(grid.shape):
        values = [grid[x] for x in iterNeighbours(point)]
        print '{}: {}'.format(point, values)


# from scipy import ndimage
# from scipy import misc

# # Numpy approach.
# def vonNeumannSampler(shape):
#     sr = []
#     sc = []
#     for (r, c) in np.ndindex(shape):
#         sr.append([r-1, r+1, r, r])
#         sc.append([c, c, c+1, c-1])
#     return np.array(sr), np.array(sc)

