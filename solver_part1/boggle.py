from random import choice
from string import ascii_uppercase
import logging
logging.basicConfig(level=logging.INFO)


def get_grid():
    return {(x, y): choice(ascii_uppercase) for x in range(size[0])
            for y in range(size[1])}



def draw_grid(size, grid_list):
    the_grid = []
    for row in range(size[0]):
        pass


def get_neighbors():
    neighbors = {}
    for position in grid:
        x, y = position
        positions = [(x-1, y-1), (x, y-1), (x+1, y-1), (x+1, y),
                     (x+1, y+1), (x, y+1), (x-1, y+1), (x-1, y)]
        neighbors[position] = [p for p in positions if
                               0 <= p[0] < size[0] and 0 <= p[1] < size[1]]
    return neighbors


size = X, Y = 2, 2
grid = get_grid()
neighbors = get_neighbors()
# print(grid)
logging.info('grid %s' % str(grid))
# print(neighbors[(0, 0)], neighbors[(1, 0)], neighbors[(1, 1)])

# recursive code

paths = []


def path_to_word(path):
   return ''.join([grid[p] for p in path])


def get_dictionary():
   with open('words.txt') as f:
       return [word.strip().upper() for word in f]

def search(path):
    logging.debug('%s: %s' % (path, path_to_word(path)))
    # if len(path) > size[0] * size[1]:
    #    return
    word = path_to_word(path)
    if word in dictionary:
        paths.append(path)
    for next_pos in neighbors[path[-1]]:
        # print(path, next_pos)
        if next_pos not in path:
            # print(path, next_pos)
            search(path + [next_pos])
        else:
            logging.debug('%s: skipping %s because in path' % (path, grid[next_pos]))

dictionary = get_dictionary()
for position in grid:
    logging.info('searching %s' % str(position))
    search([position])


print([path_to_word(p) for p in paths])

# Non recursive code.
# as the grid grows more for loops would be needed
# paths = []
# path = []
#
# for letter1 in grid:
#     path.append(letter1)
#     paths.append(path[:])
#
#     for letter2 in neighbors[letter1]:
#         path.append(letter2)
#         paths.append(path[:])
#
#         for letter3 in neighbors[letter2]:
#             path.append(letter3)
#             paths.append(path[:])
#
#             for letter4 in neighbors[letter3]:
#                 path.append(letter4)
#                 paths.append(path[:])
#                 path.pop()
#
#             path.pop()
#         path.pop()
#     path.pop()
#
# for path in paths:
#     print ''.join([grid[p] for p in path])
