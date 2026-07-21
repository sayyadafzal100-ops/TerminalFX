from .colors import Colors, Reset
from .constants import default_color
from .palettes import PALETTES

def get_color_code(color=default_color):
    
    if color.lower() not in Colors:
        print(f"Warning: Invalid color '{color}'. Using default color '{default_color}'.")
        color = default_color

    return Colors[color.lower()], Reset

def clear_line(text):
    print("\r" + " " * len(text) + "\r", end="", flush=True)
    

def color_palettes(palettes):
    temp = []
    get_colors = []
    if palettes.lower() in PALETTES:
        temp.append(PALETTES[palettes])

    for i in temp:
      for j in i:
        COLORS, RESET = get_color_code(j)
        get_colors.append(COLORS)
    return get_colors, RESET
       

    








