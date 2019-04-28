from pygame import QUIT, K_ESCAPE
from pygame import K_KP8, K_KP2, K_KP4, K_KP6, K_KP7, K_KP9, K_KP1, K_KP3

# General settings
cell = 16
window_size = (800, 600)

# Acceptable input
move_keys = (K_KP8, K_KP2, K_KP4, K_KP6, K_KP7, K_KP9, K_KP1, K_KP3)
move_values = ((0, -1), (0, 1), (-1, 0), (1, 0),
               (-1, -1), (1, -1), (-1, 1), (1, 1))

quit_input = (QUIT, K_ESCAPE)
