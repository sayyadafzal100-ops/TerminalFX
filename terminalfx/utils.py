from .colors import Colors, Reset
from .constants import default_color
from .palettes import PALETTES

def get_color_code(color=default_color):
    try:
        if color.lower() not in Colors:
            print(f"Warning: Invalid color '{color}'. Using default color '{default_color}'.")
            color = default_color

        return Colors[color.lower()], Reset
    except TypeError:
        print(f"Error: Invalid color '{color}'.")
        return default_color, Reset


def clear_line(text):
    print("\r" + " " * len(text) + "\r", end="", flush=True)
    

def color_palettes(palettes):
    temp = []
    get_colors = []
    try:
        if palettes.lower() in PALETTES:
            temp.append(PALETTES[palettes])
    except ValueError as e:
        print(f"error: {e}")

    for i in temp:
      for j in i:
        COLORS, RESET = get_color_code(j)
        get_colors.append(COLORS)
    return get_colors, RESET
       

def color_handling(color):
    try:
        # Getting colors codes
        COLOR, RESET = get_color_code(color)
    except TypeError:
        print(f"Error: Invalid color '{color}'.")
        COLOR, RESET = get_color_code(default_color)

    return COLOR, RESET

