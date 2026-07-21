from .constants import speed, repeat, default_color, direction, reverse, palette, typing
from .utils import clear_line, get_color_code, color_palettes


import time

class Effects:

    def __init__(
        self,
        speed=speed,
        repeat=repeat,
        color=default_color,
    ):
        self.speed = speed
        self.repeat = repeat
        self.color = color

    def gradient(self,
        text,
        speed=0.05,
        repeat=repeat,
        direction=direction,
        palette=palette
    ):
   
        ANSI_COLORS, RESET = color_palettes(palette)
       
        for _ in range(repeat):  

            full_word = ""

            for index, value in enumerate(text):
                color = ANSI_COLORS[index % len(ANSI_COLORS)]
                full_word += f"{color}{value}{RESET}"

            print("\r" + f"{full_word}", end="")
            time.sleep(speed)

            if direction.lower() == "left":
                first = ANSI_COLORS.pop(0)
                ANSI_COLORS.append(first)

            elif direction.lower() == "right":
                last = ANSI_COLORS.pop()
                ANSI_COLORS.insert(0, last)

            else:
                if direction.lower() not in ("left", "right"):
                    last = ANSI_COLORS.pop()
                    ANSI_COLORS.insert(0, last)

    def shine(self):
        pass

    def scramble(self):
        pass

    def fade(self):
        pass

    def pulse(self):
        pass

    def highlight(self):
        pass

    def scan(self):
        pass

    def flicker(self):
        pass

    def wave_color(self):
        pass

    def reveal(self):
        pass

    def hologram(self):
        pass






effects = Effects()

effects.gradient("hello from afzal", repeat=5,palette="sunset", speed=1, direction="jjh")

#python terminalfx/effects.py
#python -m terminalfx/effects