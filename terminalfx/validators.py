from terminalfx.utils import get_color_code
from .palettes import PALETTES



def text_validator(text):
    if not isinstance(text, str):
        raise TypeError("Text must be a string")
    return text

def speed_validator(speed):
    if not isinstance(speed, (int, float)):
        raise TypeError("Speed must be a float")
    if speed < 0:
        raise ValueError("Speed cannot be negative")
    return float(speed)

def repeat_validator(repeat):
    if not isinstance(repeat, int):
        raise TypeError("Repeat must be an integer")
    if repeat < 1:
        raise ValueError("Repeat must be greater than 0")
    return repeat

def width_validator(width):
    if not isinstance(width, int):
        raise TypeError("Width must be an integer")
    if width < 0:
        raise ValueError("Width cannot be negative")
    return width

def palette_validator(palette):
    if not isinstance(palette, str):
        raise TypeError("Palette must be a string")
    if palette not in PALETTES:
        raise ValueError("Invalid palette")
    return palette

def direction_validator(direction):
    if not isinstance(direction, str):
        raise TypeError("direction must be a string")
    if direction not in ["left", "right"]:
        raise ValueError("Invalid direction")
    return direction

def shine_color_validator(shine_color):
    if not isinstance(shine_color, str):
        raise TypeError("Shine color must be a string")
    COLOR, RESET = get_color_code(shine_color)
    if not COLOR:
        raise ValueError("Invalid shine color")
    return COLOR
    

def shine_width_validator(shine_width):
    if not isinstance(shine_width, int):
        raise TypeError("Shine width must be an integer")
    if shine_width < 1:
        raise ValueError("Shine width cannot be negative")
    return shine_width



