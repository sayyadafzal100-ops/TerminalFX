from .constants import speed, repeat, default_color, direction, palette, shine_width, shine_color
from .utils import color_palettes, get_color_code, clear_line
from .validators import (
text_validator,
speed_validator,
repeat_validator, 
direction_validator, 
palette_validator,
shine_color_validator,
shine_width_validator)


import time

class Effects:

    # def __init__(
    #     self,
    #     speed=speed,
    #     repeat=repeat,
    #     color=default_color,
    # ):
    #     self.speed = float(speed)
    #     self.repeat = int(repeat)
    #     self.color = color

    def gradient(self,
        text,
        speed=float(0.05),
        repeat=int(repeat),
        direction=str(direction),
        palette=str(palette)
    ):  
        text = text_validator(text)
        speed = speed_validator(speed)
        repeat = repeat_validator(repeat)
        direction = direction_validator(direction)
        palette = palette_validator(palette)

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

    def shine(
        self, 
        text, 
        speed=speed, 
        repeat=repeat, 
        direction=direction, 
        shine_width=shine_width, 
        shine_color=shine_color, 
        color=default_color):

        text = text_validator(text)
        speed = speed_validator(speed)
        repeat = repeat_validator(repeat)
        direction = direction_validator(direction)
        shine_width = shine_width_validator(shine_width)
        shine_color = shine_color_validator(shine_color)
        color, RESET = get_color_code(color)

        
        shine_position = 0

        for _ in range(repeat):
            if direction.lower() == "right":
                start = 0
                step = 1
                end = len(text) + 1

            elif direction.lower() == "left":
                start = len(text) - shine_width
                step = -1
                end= -1
            
            for shine_position in range(start, end, step):
                full_word = ""
                for index, value in enumerate(text):
                    if shine_position <= index < shine_position + shine_width:
                        full_word += f"{shine_color}{value}{RESET}"
                        # shine_position += 1
                    
                    else:
                        full_word += f"{color}{value}{RESET}"
                    
                    
                    
            

                result = '\r' + full_word
                    

                print("\r" + result, end="")
                time.sleep(speed)
                
        clear_line(result + "\r")
                
    # def scramble(self):
    #     pass

    # def fade(self):
    #     pass

    # def pulse(self):
    #     pass

    # def highlight(self):
    #     pass

    # def scan(self):
    #     pass

    # def flicker(self):
    #     pass

    # def wave_color(self):
    #     pass

    # def reveal(self):
    #     pass

    # def hologram(self):
    #     pass
    
    def documents(self):
        documents = """
        from terminalfx import Effects

        effects = Effects()

        effects.gradient("hello from afzal", repeat=5, palette="sunset", speed=1, direction="right")

        effects.shine("hello from afzal", speed=0.1, direction="right", shine_color="black", shine_width=2, color="white")
        """

        print(documents)






