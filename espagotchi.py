import ugfx
import random
import time
import math
import badge
import virtualtimers

# Constants
WALKSIZE = 6
MENUSIZE = 8
STRING_SIZE = 11
WHITE = 0xff
BLACK = 0x00

# Converted Sprites
splash1 = bytearray([
    0, 0, 0, 0, 0, 0, 0, 57, 192, 0, 0, 0, 0, 57, 192, 0, 0, 0, 0, 57, 192, 0, 0, 0, 0, 56, 0, 0, 0, 0, 0, 56, 0, 0, 0, 0, 7, 185, 206, 120, 15, 192, 15, 249, 207, 252, 31, 224, 31, 249, 207, 254, 63, 240, 60, 121, 207, 30, 56, 120, 56, 57, 206, 14, 112, 56, 56, 57, 206, 14, 112, 56, 56, 57, 206, 14, 112, 56, 56, 57, 206, 14, 112, 56, 56, 57, 206, 14, 112, 56, 60, 121, 206, 14, 120, 112, 31, 249, 206, 14, 63, 240, 15, 249, 206, 14, 31, 224, 0, 0, 0, 0, 0, 0, 0, 2, 0, 16, 0, 16, 37, 55, 83, 144, 225, 184, 41, 34, 81, 208, 147, 144, 25, 34, 82, 80, 146, 16, 17, 35, 115, 208, 241, 152, 0, 0, 0, 0, 128, 0, 0, 0, 0, 0, 0, 0
])

splash2 = bytearray([
    0, 0, 0, 0, 0, 0, 0, 15, 128, 0, 0, 0, 0, 0, 0, 0, 0, 31, 255, 0, 0, 0, 0, 0, 0, 0, 0, 57, 255, 224, 0, 0, 0, 0, 0, 0, 0, 59, 255, 248, 0, 0, 0, 0, 0, 0, 0, 63, 225, 252, 0, 0, 0, 0, 0, 0, 0, 127, 254, 62, 0, 0, 0, 0, 0, 0, 0, 94, 193, 222, 0, 0, 0, 0, 0, 0, 0, 125, 128, 47, 0, 0, 0, 0, 0, 0, 0, 58, 0, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 63, 0, 0, 0, 0, 0, 0, 0, 0, 0, 254, 0, 0, 0, 0, 0, 0, 0, 0, 1, 250, 0, 0, 0, 0, 0, 0, 31, 128, 7, 244, 0, 0, 0, 0, 0, 0, 245, 224, 31, 232, 0, 0, 0, 0, 0, 7, 170, 188, 127, 208, 0, 0, 0, 0, 0, 61, 85, 95, 255, 160, 0, 0, 0, 0, 0, 234, 170, 175, 255, 64, 0, 0, 0, 0, 3, 213, 85, 255, 254, 128, 0, 0, 0, 0, 7, 171, 174, 191, 253, 0, 0, 0, 0, 0, 31, 95, 223, 255, 250, 0, 0, 0, 0, 0, 63, 238, 251, 111, 244, 0, 0, 0, 0, 0, 255, 255, 255, 255, 232, 0, 0, 0, 0, 1, 255, 247, 255, 255, 208, 0, 0, 0, 0, 7, 255, 255, 255, 255, 160, 0, 0, 0, 0, 31, 255, 255, 255, 253, 192, 0, 0, 0, 0, 255, 223, 255, 254, 254, 128, 0, 0, 0, 31, 255, 239, 239, 255, 127, 0, 0, 0, 3, 255, 255, 159, 223, 255, 191, 0, 0, 0, 255, 255, 252, 31, 161, 252, 127, 128, 0, 15, 255, 255, 224, 31, 176, 3, 191, 128, 0, 31, 255, 128, 0, 15, 192, 0, 0, 0, 0, 126, 0, 0, 0, 0, 0, 0, 0, 0, 0, 112, 0, 0, 0, 0, 0, 0, 0, 0, 0, 224, 0, 0, 0, 0, 0, 0, 0, 0, 0, 192, 0, 0, 0, 0, 0, 0, 0, 0, 0, 200, 0, 0, 0, 0, 0, 0, 0, 0, 0, 112, 0, 0, 0, 0, 0, 0, 0, 0, 0
])

grass_front = bytearray([
    0, 1, 0, 0, 0, 0, 128, 128, 0, 8, 137, 192, 72, 92, 80, 132, 156, 72, 80, 34, 136, 128, 68, 34, 64, 132, 46, 33, 73, 36, 164, 177
])

grass = bytearray([
    255, 238, 187, 85, 170, 17
])

trees = bytearray([
    0, 0, 0, 0, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 5, 0, 0, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 40, 21, 0, 0, 85, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 84, 85, 64, 0, 85, 64, 0, 0, 0, 0, 0, 0, 0, 128, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 84, 21, 4, 64, 21, 0, 0, 0, 0, 0, 0, 0, 2, 160, 0, 0, 1, 16, 0, 8, 0, 0, 0, 0, 1, 0, 0, 0, 40, 132, 36, 64, 4, 0, 0, 0, 0, 0, 4, 64, 0, 130, 0, 0, 1, 16, 0, 4, 64, 0, 0, 0, 1, 0, 2, 32, 0, 0, 0, 65, 0, 16, 0, 0, 0, 0, 4, 64, 0, 136, 130, 64, 145, 4, 36, 65, 16, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 68, 68, 17, 4, 16, 17, 4, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 0, 0, 2, 0, 0, 0, 4, 0, 0, 2, 16, 0, 128, 0, 0, 8, 0, 4, 0, 0, 0, 0, 0, 64, 0, 0, 4, 0, 8, 0, 32, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 8
])

mountains = bytearray([
    0, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 224, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 1, 240, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 3, 248, 3, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 63, 7, 116, 7, 128, 16, 0, 0, 128, 0, 6, 128, 0, 0, 0, 0, 213, 14, 194, 13, 192, 40, 1, 1, 193, 0, 31, 64, 0, 0, 0, 1, 40, 29, 19, 27, 96, 84, 3, 131, 163, 128, 54, 32, 0, 0, 0, 6, 208, 58, 65, 180, 48, 226, 204, 247, 87, 192, 216, 16, 0, 0, 0, 25, 32, 104, 132, 73, 25, 161, 54, 93, 42, 161, 160, 16, 0, 0, 0, 230, 64, 210, 16, 164, 12, 128, 140, 26, 21, 87, 64, 136, 0, 0, 31, 56, 128, 73, 8, 0, 6, 2, 192, 36, 24, 11, 128, 5, 11, 140, 224, 35, 0, 160, 32, 0, 17, 0, 0, 72, 132, 132, 2, 32, 93, 243, 0, 205, 192, 80, 0, 4, 4, 1, 68, 0, 0, 8, 0, 0, 48, 4, 7, 16, 32, 0, 0, 0, 0, 4, 0, 0, 0, 0, 8, 0, 0, 64, 64, 0, 16, 64, 2, 0, 0, 0, 0, 0, 129, 0, 0, 0, 1, 17, 1, 0, 0, 0, 0, 0, 0, 64, 0, 0, 0, 0, 0, 128, 128, 0, 0, 32, 2
])

cloud2 = bytearray([
    4, 112, 24, 0, 110, 251, 124, 238, 255, 255, 253, 255, 111, 251, 56, 238, 7, 112, 82, 0
])

# Walking Sprites
# walk right

dinoWalk0 = bytearray([
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 192, 96, 0, 0, 0, 31, 241, 240, 0, 0, 0, 63, 255, 184, 0, 0, 0, 123, 255, 252, 0, 0, 0, 255, 255, 216, 0, 0, 3, 255, 127, 224, 0, 0, 15, 247, 222, 0, 0, 0, 127, 248, 60, 0, 0, 0, 0, 188, 122, 0, 0
])

dinoWalk1 = bytearray([
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 192, 96, 0, 0, 0, 31, 241, 240, 0, 0, 0, 55, 255, 184, 0, 0, 0, 127, 255, 252, 0, 0, 0, 255, 127, 216, 0, 0, 3, 255, 255, 224, 0, 0, 15, 191, 218, 0, 0, 0, 127, 248, 60, 0, 0, 0, 0, 48, 24, 0, 0
])

dinoWalk2 = bytearray([
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 192, 96, 0, 0, 0, 27, 241, 240, 0, 0, 0, 63, 255, 184, 0, 0, 0, 127, 127, 252, 0, 0, 0, 255, 255, 216, 0, 0, 3, 255, 255, 224, 0, 0, 15, 191, 250, 0, 0, 0, 127, 120, 60, 0, 0, 0, 0, 244, 94, 0, 0
])

# walk left
dinoWalk3 = bytearray([
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 224, 0, 0, 0, 15, 143, 248, 0, 0, 0, 29, 255, 252, 0, 0, 0, 63, 255, 222, 0, 0, 0, 27, 255, 255, 0, 0, 0, 7, 254, 255, 192, 0, 0, 0, 123, 239, 240, 0, 0, 0, 60, 31, 254, 0, 0, 0, 94, 61, 0, 0
])

dinoWalk4 = bytearray([
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 224, 0, 0, 0, 15, 143, 248, 0, 0, 0, 29, 255, 236, 0, 0, 0, 63, 255, 254, 0, 0, 0, 27, 254, 255, 0, 0, 0, 7, 255, 255, 192, 0, 0, 0, 91, 253, 240, 0, 0, 0, 60, 31, 254, 0, 0, 0, 24, 12, 0, 0
])

dinoWalk5 = bytearray([
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 224, 0, 0, 0, 15, 143, 216, 0, 0, 0, 29, 255, 252, 0, 0, 0, 63, 254, 254, 0, 0, 0, 27, 255, 255, 0, 0, 0, 7, 255, 255, 192, 0, 0, 0, 95, 253, 240, 0, 0, 0, 60, 30, 254, 0, 0, 0, 122, 47, 0, 0
])

# --------- GAME SPRITES ----------
dinoJump = bytearray([
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 192, 96, 0, 0, 0, 31, 241, 240, 0, 0, 0, 59, 255, 184, 0, 0, 0, 127, 223, 252, 0, 0, 0, 255, 255, 216, 0, 0, 3, 255, 255, 224, 0, 0, 15, 255, 254, 0, 0, 0, 125, 248, 31, 0, 0, 0, 3, 192, 7, 128, 0
])

obstacle1 = bytearray([
    0, 0, 30, 0, 47, 0, 94, 128, 95, 192, 183, 192
])

obstacle2 = bytearray([
    20, 0, 8, 0, 82, 0, 52, 0, 105, 64, 240, 128
])

poop = bytearray([
    128, 136, 1, 129, 2, 224, 39, 16, 11, 240, 28, 8
])

# Eating

eating1 = bytearray([
    0, 0, 0, 0, 0, 0, 0, 0, 7, 252, 0, 0, 0, 0, 31, 255, 0, 0, 0, 0, 31, 255, 128, 0, 0, 0, 63, 255, 224, 0, 0, 0, 127, 255, 240, 0, 0, 0, 255, 255, 248, 0, 0, 1, 255, 255, 252, 0, 0, 3, 124, 127, 254, 0, 0, 2, 249, 255, 254, 0, 0, 12, 243, 255, 255, 0, 0, 31, 244, 127, 255, 128, 0, 127, 240, 127, 255, 192, 0, 255, 248, 255, 255, 192, 3, 255, 255, 255, 255, 192, 15, 255, 255, 255, 255, 224, 31, 231, 255, 224, 255, 224, 63, 223, 255, 222, 255, 240, 127, 191, 255, 191, 127, 240, 127, 127, 254, 119, 191, 248, 127, 127, 249, 247, 191, 252, 63, 255, 231, 239, 191, 254, 95, 254, 31, 31, 191, 255, 103, 241, 249, 31, 191, 255, 56, 15, 232, 63, 191, 255, 31, 255, 224, 63, 191, 255, 14, 254, 64, 191, 111, 255, 4, 84, 0, 255, 87, 255, 0, 16, 1, 254, 171, 255, 0, 24, 1, 253, 85, 255, 0, 24, 5, 250, 170, 255, 0, 29, 39, 241, 85, 95, 0, 15, 127, 224, 170, 175, 0, 7, 255, 128, 85, 87, 0, 3, 254, 0, 42, 171, 0, 1, 240, 0, 21, 85, 0, 0, 0, 0, 10, 170, 0, 0, 0, 0, 5, 85, 0, 0, 0, 0, 2, 170, 0, 0, 0, 0, 1, 85
])

eating2 = bytearray([
    0, 0, 0, 0, 0, 0, 0, 0, 7, 252, 0, 0, 0, 0, 31, 255, 0, 0, 0, 0, 31, 255, 128, 0, 0, 0, 63, 255, 224, 0, 0, 0, 127, 255, 240, 0, 0, 0, 255, 255, 248, 0, 0, 1, 255, 255, 252, 0, 0, 3, 124, 127, 254, 0, 0, 2, 249, 255, 254, 0, 0, 12, 243, 255, 255, 0, 0, 31, 244, 127, 255, 128, 0, 127, 240, 127, 255, 192, 0, 255, 248, 255, 255, 192, 3, 255, 255, 255, 255, 192, 15, 255, 255, 255, 255, 224, 31, 231, 255, 224, 255, 224, 63, 223, 255, 222, 255, 240, 127, 191, 255, 191, 127, 240, 127, 127, 254, 119, 191, 248, 127, 127, 249, 247, 191, 252, 63, 255, 231, 239, 191, 254, 95, 254, 31, 31, 191, 255, 103, 241, 249, 31, 191, 255, 56, 15, 232, 63, 191, 255, 31, 255, 225, 127, 63, 255, 14, 254, 65, 254, 239, 255, 4, 212, 11, 253, 87, 255, 0, 212, 15, 250, 171, 255, 0, 96, 159, 245, 85, 255, 0, 117, 255, 202, 170, 255, 0, 63, 255, 5, 85, 95, 0, 31, 252, 2, 170, 175, 0, 7, 192, 1, 85, 87, 0, 0, 0, 0, 170, 171, 0, 0, 0, 0, 21, 85, 0, 0, 0, 0, 10, 170, 0, 0, 0, 0, 5, 85, 0, 0, 0, 0, 2, 170, 0, 0, 0, 0, 1, 85
])

eating3 = bytearray([
    0, 0, 0, 0, 0, 0, 0, 0, 7, 252, 0, 0, 0, 0, 31, 255, 0, 0, 0, 0, 31, 255, 128, 0, 0, 0, 63, 255, 224, 0, 0, 0, 127, 255, 240, 0, 0, 0, 255, 255, 248, 0, 0, 1, 255, 255, 252, 0, 0, 3, 124, 127, 254, 0, 0, 2, 249, 255, 254, 0, 0, 12, 243, 255, 255, 0, 0, 31, 244, 127, 255, 128, 0, 127, 240, 127, 255, 192, 0, 255, 248, 255, 255, 192, 3, 255, 255, 255, 255, 192, 15, 255, 255, 255, 255, 224, 31, 231, 255, 224, 255, 224, 63, 223, 255, 222, 255, 240, 127, 191, 255, 191, 127, 240, 127, 127, 254, 119, 191, 248, 127, 127, 249, 247, 191, 252, 63, 255, 231, 239, 191, 254, 95, 254, 31, 223, 191, 255, 103, 241, 255, 63, 191, 255, 56, 15, 252, 255, 191, 255, 31, 255, 243, 255, 63, 255, 15, 255, 207, 254, 239, 255, 0, 56, 63, 249, 87, 255, 7, 131, 255, 234, 171, 255, 1, 255, 254, 21, 85, 255, 0, 255, 240, 10, 170, 255, 0, 63, 192, 5, 85, 95, 0, 0, 0, 2, 170, 175, 0, 0, 0, 5, 85, 87, 0, 0, 0, 2, 170, 171, 0, 0, 0, 1, 85, 85, 0, 0, 0, 0, 170, 170, 0, 0, 0, 0, 85, 85, 0, 0, 0, 0, 10, 170, 0, 0, 0, 0, 1, 85
])

eating = [eating1, eating2, eating3]

apple = bytearray([
    0, 1, 240, 0, 7, 224, 0, 15, 224, 63, 31, 192, 0, 223, 128, 0, 32, 0, 15, 215, 240, 63, 255, 252, 127, 255, 254, 120, 255, 254, 240, 127, 255, 224, 127, 255, 224, 255, 255, 241, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 127, 255, 254, 127, 255, 254, 63, 255, 252, 31, 255, 248, 15, 255, 240, 7, 195, 224
])

steak = bytearray([
    15, 224, 0, 63, 248, 0, 49, 254, 0, 110, 127, 0, 209, 127, 128, 160, 191, 128, 160, 191, 192, 160, 191, 192, 209, 63, 192, 174, 255, 224, 209, 255, 224, 239, 255, 224, 119, 255, 240, 123, 255, 208, 61, 255, 120, 30, 249, 254, 15, 103, 255, 7, 127, 255, 3, 159, 252, 3, 195, 249, 1, 248, 195, 0, 255, 30, 0, 31, 254, 0, 1, 252
])


# Animation: dinoWalk
dinoWalk_frames = [
    dinoWalk0,
    dinoWalk1,
    dinoWalk2,
    dinoWalk3,
    dinoWalk4,
    dinoWalk5
]
dinoWalk_size = WALKSIZE


## ----


# Menu constants and states
menu_opened = True  # Since we want to always show menu
menu = 0
sub_menu = 1
menu_depth = False
setting = 0
action = 0

# Pet stats
hunger = 100.0
happiness = 100.0
health = 100.0
strength = 100.0
weight = 1.0
age = 0.0

# Animation states
walk_pos = 0
walk_x_pos = 0
walk_anim_reverse = False
walk_right = False
walk_dir_offset = 2

# Environment positions
grass_x_pos = 0
trees_x_pos = -20
clouds_x_pos = 0
sun_radius = 3
sun_or_moon = False
stars = {}
moon_shadow = 2
sun_x_pos = -2 * sun_radius
cloud1_width = 32
cloud1_x_pos = ugfx.width() + cloud1_width

# Game states
sound_enabled = True
action = 0
setting = 0
notification = False
notification_blink = 0
dead = False
sleeping = False
game = False
paused = False
game_over = False
score = 0
hi_score = 0
level = 0
new_hi_score = False
jumping = False
jump_up = True
jump_pos = 0
obstacle1_show = False
obstacle2_show = False
obstacle1_x_pos = 0
obstacle2_x_pos = 0
poopometer = 0.0
poops = [0, 0, 0]

# when it's idle it will update less frequently and turn off backlight
idle_timer = 60

# Menu structure
main_menu = [
    ["food", "apple", "steak", "water", None],
    ["sleep", None],
    ["clean", None],
    ["doctor", None],
    ["train", None],
    ["stats", "hunger", "happiness", "health", "strength", "weight", "age", None],
    ["settings", "sound", None]
]

def draw_bitmap(x, y, bitmap, width, height, color=BLACK):
    """Draw a bitmap on the display at position (x,y)"""
    bytes_per_row = (width + 7) // 8
    
    for row in range(height):
        for col in range(width):
            byte_idx = row * bytes_per_row + (col // 8)
            bit_pos = 7 - (col % 8)  # MSB first
            
            if byte_idx < len(bitmap):
                pixel = (bitmap[byte_idx] >> bit_pos) & 1
                if pixel:
                    ugfx.pixel(x + col, y + row, color)

def count_poops():
    """Count the number of active poops"""
    return sum(1 for poop in poops if poop > 0)

def reset_poops():
    """Reset all poops"""
    global poops
    poops = [0, 0, 0]

def splash():
    # Clear the display
    ugfx.clear()
    
    # Display splash text
    ugfx.string(1, 1, "GaFFel Game Design presents", "roboto_regular12", BLACK)
    
    # Draw splash bitmaps (you'll need to provide the actual bitmap data)
    draw_bitmap(15, 24, splash1, 48, 26, BLACK)
    draw_bitmap(48, 24, splash2, 80, 40, BLACK)
    
    # Update display
    ugfx.flush()
    
    # Delay to match Arduino delay
    time.sleep_ms(2200)

def main_loop():
    """Main game loop for idle state"""
    global dead, poopometer
    
    while not dead:
        # Update game state
        update_pet_stats()
        check_notifications()
        
        # Handle pooping
        if poopometer >= 10:
            poopometer = count_poops()
            poops[round(poopometer)] = random.randint(20, ugfx.width() + 32)
            poopometer = 0
        
        # Update animations
        update_walking_animation()
        
        # Draw everything
        draw_idle_state()
        
        # Small delay to control game speed
        time.sleep_ms(50)
        
def game_step():
    global dead, poopometer
    
    if not dead:
        # Update game state
        update_pet_stats()
        check_notifications()
        
        # Handle pooping
        if poopometer >= 10:
            poopometer = count_poops()
            poops[round(poopometer)] = random.randint(20, ugfx.width() + 32)
            poopometer = 0
    
    redraw()
    return 500

def redraw():
    ugfx.clear()
    # draw the background
    draw_environment()
    
    # Update animations
    update_walking_animation()
    
    
    # Draw everything
    draw_idle_state()

    #
    draw_menu()
    
    # Update display
    ugfx.flush()
    
# game loop stuff
def draw_idle_state():
    """Draw the current idle state"""
    global walk_x_pos, walk_pos, walk_dir_offset, sleeping, walk_right
    global grass_x_pos, trees_x_pos, cloud1_x_pos, poops
    
    # Draw the walking dino
    if not sleeping:
        draw_bitmap(int(walk_x_pos), 26, dinoWalk_frames[walk_pos + walk_dir_offset], 48, 24, BLACK)
    else:
        draw_bitmap(int(walk_x_pos), 29, dinoWalk_frames[walk_pos + walk_dir_offset], 48, 24, BLACK)
        # Draw sleeping Z's
        if walk_right:
            if round(cloud1_x_pos) % 3 == 0:
                ugfx.string(int(walk_x_pos) + 48, 36, "Z", "roboto_regular12", BLACK)
            else:
                ugfx.string(int(walk_x_pos) + 46, 38, "z", "roboto_regular12", BLACK)
        else:
            if round(cloud1_x_pos) % 3 == 0:
                ugfx.string(int(walk_x_pos) - 4, 36, "Z", "roboto_regular12", BLACK)
            else:
                ugfx.string(int(walk_x_pos) - 2, 38, "z", "roboto_regular12", BLACK)
    
    # Draw ground elements
    for i in range(2 * ugfx.width() // 4):
        draw_bitmap(int(-walk_x_pos + i * 8), 50, grass, 8, 6, BLACK)
    
    # Draw poops
    for i in range(3):
        if poops[i] > 0:
            draw_bitmap(int(-walk_x_pos + poops[i]), 44, poop, 16, 6, BLACK)
    
    # Draw front grass
    for i in range(2 * ugfx.width() // 16):
        draw_bitmap(int(-grass_x_pos + i * 32), 56, grass_front, 32, 8, BLACK)
    
    # Draw trees
    draw_bitmap(int(-trees_x_pos), 30, trees, 112, 20, BLACK)

def update_pet_stats():
    """Update all pet statistics based on current state"""
    global hunger, happiness, health, strength, poopometer, age, sleeping
    
    if sleeping:
        # Slower stat decreases while sleeping
        hunger -= 0.00005
        poopometer += 0.00005
        if happiness - 0.0001 > 0:
            happiness -= 0.0001
        health -= 0.00005 + count_poops() * 0.0001
        if strength - 0.0001 > 0:
            strength -= 0.0001
    else:
        # Normal stat decreases while awake
        hunger -= 0.00025
        poopometer += 0.00025
        if happiness - 0.0002 > 0:
            happiness -= 0.0002
        health -= 0.0001 + count_poops() * 0.0001
        if strength - 0.0002 > 0:
            strength -= 0.0002
    
    age += 0.0000025
    
def update_walking_animation():
    """Update the walking animation state"""
    global walk_pos, walk_x_pos, grass_x_pos, trees_x_pos, walk_right, walk_dir_offset
    global walk_anim_reverse, sleeping
    
    if not sleeping:
        if walk_right:
            walk_x_pos += 1
            grass_x_pos += 2
            trees_x_pos += 0.5
            if walk_x_pos > 80:
                walk_right = False
                walk_dir_offset = 3
        else:
            walk_x_pos -= 1
            grass_x_pos -= 2
            trees_x_pos -= 0.5
            if walk_x_pos < 0:
                walk_right = True
                walk_dir_offset = 0
        
        # Update walking animation frame
        if walk_anim_reverse:
            walk_pos -= 1
            if walk_pos == -1:
                walk_pos = 0
                walk_anim_reverse = False
        else:
            walk_pos += 1
            if walk_pos == 3:
                walk_pos = 2
                walk_anim_reverse = True

def check_notifications():
    """Check if any notifications need to be shown"""
    global notification, dead, hunger, happiness, health, notification_blink
    
    # Check for low stats notifications
    if hunger <= 20 or count_poops() > 0 or happiness <= 20 or health <= 20:
        notification = True
        notification_blink += 1
        if notification_blink % 4:
            badge.led(0,255,0,0)
        else:
            badge.led(0,0,0,0)
    else:
        notification = False
        badge.led(0,0,0,0)
    
    # Check for death conditions
    if hunger <= 0 or health <= 0 or happiness <= 0:
        dead = True
        # Death sound would go here


# --- environment ----
def draw_sun_moon():
    global sun_x_pos, sun_or_moon
    
    # Update sun position with bigger steps
    sun_x_pos += 0.5
    if sun_x_pos > ugfx.width() + 2 * sun_radius:
        sun_x_pos = -2 * sun_radius
        sun_or_moon = not sun_or_moon
    if sleeping:
        sun_or_moon = True

    # Draw sun/moon
    if not sun_or_moon:
        ugfx.fill_circle(int(sun_x_pos), 2 * sun_radius, sun_radius, BLACK)
    else:
        ugfx.fill_circle(int(sun_x_pos), 2 * sun_radius, sun_radius, BLACK)
        ugfx.fill_circle(int(sun_x_pos - moon_shadow), 2 * sun_radius, sun_radius, WHITE)

def draw_stars():
    global stars, wind_time
    # Stars - update only every 4 frames
    if wind_time % 4 == 0:
        # Update just one random star
        star_idx = random.randint(0, len(stars) - 1)
        stars[star_idx] = [random.randint(0, ugfx.width()), random.randint(0, 10)]
        
    # Draw all stars
    for i in range(6):
        ugfx.pixel(stars[i][0], stars[i][1], BLACK)

def draw_clouds():
    # Animate clouds with bigger steps
    for cloud in cloud_positions:
        cloud["x"] -= cloud["speed"]
        if cloud["x"] < -cloud1_width:
            cloud["x"] = ugfx.width() + cloud1_width
            cloud["y"] = random.randint(3, 8)
        draw_bitmap(int(cloud["x"]), cloud["y"], cloud2, cloud1_width, 5, BLACK)

def draw_ground():
    if not game:
        # Draw ground grass
        for i in range(2 * ugfx.width() // 4):
            draw_bitmap(int(-walk_x_pos + i * 8), 50, grass, 8, 6, BLACK)
        
        # Draw poops
        for i in range(3):
            if poops[i] > 0:
                draw_bitmap(int(-walk_x_pos + poops[i]), 44, poop, 16, 6, BLACK)
        
        # Draw front grass
        for i in range(2 * ugfx.width() // 16):
            draw_bitmap(int(-grass_x_pos + i * 32), 56, grass_front, 32, 8, BLACK)
        
        # Draw trees
        draw_bitmap(int(-trees_x_pos), 23, trees, 112, 20, BLACK)


def draw_environment():
   global wind_time
   
   draw_sun_moon()
   
   if sun_or_moon:  # night time
       draw_stars()
   
   draw_clouds()
   draw_bitmap(0, 7, mountains, 128, 16, BLACK)  # static mountains
   # draw_ground()  # includes grass, trees, and poops

   # Increment general animation timer
   wind_time += 1
   if wind_time >= 12:
       wind_time = 0
        
def test_animation():
    global wind_time, game, sleeping
    game = False
    sleeping = False
    init_environment()    
    for frame in range(50):
        ugfx.clear()
        draw_environment()
        ugfx.flush()
        time.sleep_ms(100) 
        
        
# ---- MENU stuff ----
def draw_bar(value):
    """Draw a status bar with the given value (0-100)"""
    ugfx.area(72, 19, int(48 * value / 100), 3, BLACK)

MENU_HEIGHT = 15
PADDING=2

def draw_menu():
    global menu, sub_menu, menu_depth, setting
    """Draw the menu interface"""
    if menu_opened:
        # Main menu background 
        ugfx.area(0, 0, ugfx.width(), MENU_HEIGHT, BLACK)
        ugfx.box(0, 0, ugfx.width(), MENU_HEIGHT, WHITE)
        # borders
        #ugfx.area(1, 1, ugfx.width() - 2, 27, 0)
        #ugfx.box(0, 0, ugfx.width(), 14, 0)
        
        if menu_depth and len(main_menu[menu]) > 2:
            draw_submenu()
        else:
            # Forward arrow
            ugfx.area(1, 3, 1, 5, WHITE)
            ugfx.area(2, 4, 1, 3, WHITE)
            ugfx.area(3, 5, 1, 1, WHITE)
        
            if main_menu[menu][0] is not None:
                ugfx.string(8, 0, main_menu[menu][0], "roboto_regular12", WHITE)

def draw_submenu():
    # set background of top to WHITE
    ugfx.area(0, 0, ugfx.width(), MENU_HEIGHT*2, WHITE)
    # write top-menu text in BLACK
    if main_menu[menu][0] is not None:
        ugfx.string(8, -3, main_menu[menu][0], "roboto_regular12", BLACK)
    
    # submenu drawing
    
    # focus arrow
    ugfx.area(1, 18, 1, 5, BLACK)
    ugfx.area(2, 19, 1, 3, BLACK)
    ugfx.area(3, 20, 1, 1, BLACK)
    
    ugfx.string(8, 13, main_menu[menu][sub_menu], "roboto_regular12", BLACK)
    
    # Calculate current setting

    
    # For stat menu items, draw the stat bar as background
    if main_menu[menu][0] == "stats":
        subitem = main_menu[menu][sub_menu]
        if subitem == 'hunger':
            value = hunger
        elif subitem == 'happiness':
            value = happiness
        elif subitem == 'health':
            value = health
        elif subitem == 'strength':
            value = strength
            
        # Show numeric values for weight and age
        if subitem == 'weight':
            ugfx.string(72, 13, str(round(weight, 1)) + " t", "roboto_regular12", BLACK)
        elif subitem == 'age':
            ugfx.string(72, 13, str(round(age, 1)) + " y.", "roboto_regular12", BLACK)
        else:    
            # Draw a progress bar, half the size of the screen which we fill for the value
            ugfx.box(int(ugfx.width()/2+PADDING/2), int(MENU_HEIGHT+PADDING/2), int(ugfx.width()/2-PADDING), int(MENU_HEIGHT-PADDING*2), BLACK)
            # calculate how big % of the progress bar we should fill, based on above
            bar_width = int((ugfx.width()/2) * (value/ 100) - PADDING)
            if bar_width > 0:  # Only draw black part if there's something to draw
                ugfx.area(int(ugfx.width()/2+PADDING), int(MENU_HEIGHT+PADDING/2), bar_width, MENU_HEIGHT-PADDING*2, BLACK) 
        
    
def btn_left_handler(pressed):
    global menu_depth, sub_menu
    if pressed:
        if menu_depth:
            menu_depth = False
        sub_menu = 1
        redraw()
            
def btn_up_handler(pressed):
    global menu, sub_menu, menu_depth
    if pressed and menu_opened:
        if menu_depth:
            # Navigate submenu items
            if main_menu[menu][sub_menu + 1] is None:
                sub_menu = 1
            else:
                sub_menu += 1
        else:
            # Navigate main menu items
            menu = (menu + 1) % len(main_menu)
            if main_menu[menu][1] is not None:
                sub_menu = 1
        redraw()

def btn_right_handler(pressed):
    global menu_depth, action
    if pressed and menu_opened:
        item = main_menu[menu][0]
        # check if we are entering a submenu
        # then take not action just enter and redraw
        if not menu_depth and len(main_menu[menu]) > 2:
            menu_depth = True
            draw_menu()
            ugfx.flush()
        else:
        # otherwise check what we want to do
            subitem = main_menu[menu][sub_menu] if menu_depth else None
        
            if item == "food" and subitem in ["apple", "steak", "water"]:
                feed(subitem)
            elif item == "sleep":
                toggle_sleep()
            elif item == "clean":
                clean_action()
            elif item == "doctor":
                doctor_action()
            elif item == "train":
                train_action()
            elif item == "settings" and subitem == "sound":
                global soundEnabled
                soundEnabled = not soundEnabled

def initialize():
    global menu_opened, menu, sub_menu, menu_depth, setting, action
    global hunger, happiness, health, strength, weight, age
    global walk_pos, walk_x_pos, walk_anim_reverse, walk_right, walk_dir_offset
    global grass_x_pos, trees_x_pos, clouds_x_pos, sun_radius, sun_or_moon, moon_shadow, sun_x_pos, cloud1_width, cloud1_x_pos
    global sound_enabled, action, setting, notification, notification_blink, dead, sleeping, game, paused
    global game_over, score, hi_score, level, new_hi_score, jumping, jump_up, jump_pos
    global obstacle1_show, obstacle2_show, obstacle1_x_pos, obstacle2_x_pos, poopometer, poops
    global cloud_positions, grass_sway, grass_sway_step, wind_time

    # Menu states
    menu_opened = True 
    menu = 0
    sub_menu = 1
    menu_depth = False
    setting = 0
    action = 0

    # Pet stats
    hunger = 100.0
    happiness = 100.0
    health = 100.0
    strength = 10.0
    weight = 1.0
    age = 0.0

    # Animation states
    walk_pos = 0
    walk_x_pos = 0
    walk_anim_reverse = False
    walk_right = False
    walk_dir_offset = 2

    # Environment positions
    grass_x_pos = 0
    trees_x_pos = -20
    clouds_x_pos = 0
    sun_radius = 3
    sun_or_moon = False
    moon_shadow = 2
    sun_x_pos = -2 * sun_radius
    cloud1_width = 32
    cloud1_x_pos = ugfx.width() + cloud1_width

    # Game states
    sound_enabled = True
    action = 0
    setting = 0
    notification = False
    notification_blink = 0
    dead = False 
    sleeping = False
    game = False
    paused = False
    game_over = False
    score = 0
    hi_score = 0
    level = 0
    new_hi_score = False
    jumping = False
    jump_up = True
    jump_pos = 0
    obstacle1_show = False
    obstacle2_show = False
    obstacle1_x_pos = 0
    obstacle2_x_pos = 0
    poopometer = 0.0
    poops = [0, 0, 0]

    # Environment animation states
    cloud_positions = [
        {"x": random.randint(0, ugfx.width()), 
        "y": random.randint(3, 8),
        "speed": 1.5},
        {"x": random.randint(0, ugfx.width()), 
        "y": random.randint(3, 8),
        "speed": 2.0}
    ]
    grass_sway = 0
    grass_sway_step = 0
    wind_time = 0

    ugfx.input_init()
    ugfx.input_attach(ugfx.JOY_UP, btn_up_handler)  
    ugfx.input_attach(ugfx.JOY_RIGHT, btn_right_handler)
    ugfx.input_attach(ugfx.JOY_LEFT, btn_left_handler)
    
    splash()


def feed(food):
    global hunger, weight, health, poopometer
    if not sleeping and random.randint(1, 11 - round(happiness / 10)) == 1:
        animate_eating(food)
        if food == "apple":
            hunger = min(100, hunger + 10)
            health = min(100, health + 1)
            poopometer += 0.02
        elif food == "steak":
            hunger = min(100, hunger + 20)
            weight = min(100, weight + 0.1)
            health = max(0, health - 1)
            poopometer += 0.05
        elif food == "water":
            hunger = min(100, hunger + 5)
            poopometer += 0.01
    else:
        if soundEnabled:
            tone(sound, 500, 200)
            time.sleep_ms(250)

def animate_eating(food):
    ugfx.clear()
    for j in range(3):
        for i in range(3):
            ugfx.clear()
            if food == "apple":
                draw_bitmap(50,40,apple,24,24)
                if j > 0:
                    ugfx.fill_circle(76, 54, 12, ugfx.BLACK)
                if j == 2:
                    ugfx.fill_circle(47, 55, 12, ugfx.BLACK)
            elif food == "steak":
                draw_bitmap(50,40,steak,24,24)
                if j > 0:
                    ugfx.fill_circle(76, 59, 13, ugfx.BLACK)
                if j == 2:
                    ugfx.fill_circle(60, 63, 13, ugfx.BLACK)
            elif food == "water":
                ugfx.circle(80, 55, 1 + i, ugfx.WHITE)
                ugfx.circle(80, 55, 5 + 2 * i, ugfx.WHITE)
                ugfx.circle(80, 55, 10 + 4 * i, ugfx.WHITE)
            draw_bitmap(80,24,eating[i],48,40)
            time.sleep_ms(150)
            ugfx.flush()

def toggle_sleep():
    global sleeping, sun_or_moon, stars
    sleeping = not sleeping
    if sleeping:
        badge.backlight(0)
        sun_or_moon = True
        for i in range(6):
            stars[i] = (random.randint(0, ugfx.width()), random.randint(0, 10))
    else:
        badge.backlight(100)
        sun_or_moon = False
        

def clean_action():
    global poops
    poops = [0, 0, 0]

# 
def doctor_action():
    global health, happiness
    if health < 60:
        health = 100
        for i in range(5):
            ugfx.clear()
            if i % 2 != 0:
                ugfx.area(32, 23, 64, 16, ugfx.WHITE)
                ugfx.area(56, 0, 16, 64, ugfx.WHITE)
            ugfx.flush()
            time.sleep_ms(300)
    else:
        happiness = max(0, happiness - 3)
        error_notice("not sick !")

# training makes it stronger
# there is no point in strength currently
# but training makes it less happy
# TODO: make it so that the training has a chance to fail
# to make life more exciting
def train_action():
    global strength, happiness
    if not sleeping:
        strength = min(100, strength + 12)
        happiness = max(0, happiness - 3)
        time.sleep_ms(150)
        for i in range(5):
            if sound_enabled:
                tone(sound, 200 * i, 100)
            # Draw exclamation marks, showing how it trains.. I guess
            if walk_right:
                ugfx.string(int(walk_x_pos) + 48 + i*4, 36, "!", "roboto_regular18", BLACK)
            else:
                ugfx.string(int(walk_x_pos) - 4 - i*4, 36, "!", "roboto_regular18", BLACK)
            ugfx.flush()
            time.sleep_ms(150)

def error_notice(message):
    # draw a notice in the middle of the screen
    ugfx.area(32,MENU_HEIGHT, int(ugfx.width()/2), 16, WHITE)
    ugfx.box(32, MENU_HEIGHT, int(ugfx.width()/2), 16, BLACK)
    ugfx.string(36, MENU_HEIGHT+2, message, "roboto_regular12", BLACK)
    ugfx.flush()
    time.sleep_ms(200)
    
initialize()
virtualtimers.new(500, game_step)
virtualtimers.activate(500)