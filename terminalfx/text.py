
from .constants import speed, repeat, text, default_color, width
from .utils import clear_line, color_handling
from .validators import (
text_validator, 
speed_validator, 
repeat_validator, 
width_validator)
import time


class Text:

    

    # def __init__(self, text=text, speed=speed, repeat=repeat, color=default_color, width=width):
    #     self.text = text
    #     self.speed = speed
    #     self.repeat = repeat
    #     self.color = color
    #     self.width = width

    def typewriter(self, text, speed=speed, repeat=repeat, color=default_color):
        """
        typewriter: typing effect
        description:
        -----This function prints the text in a typewriter effect.
        examples:
        ----- text.typewriter("hello world", repeat=5, color="blue", speed=0.1)
            
        """
        
        text = text_validator(text)
        speed = speed_validator(speed)
        repeat = repeat_validator(repeat)
        COLOR, RESET = color_handling(color)

        # Typewriter effect
        for _ in range(repeat):
            for char in text:
                print(f"{COLOR}{char}{RESET}", end='', flush=True)
                time.sleep(speed)
        print()
        
        
            

    def blink(self, text, speed=speed, repeat=repeat, color=default_color):
        """
        blink: blink effect
        description:
        ----- This function prints the text in a blink effect.
        examples:
        ----- text.blink("hello world", repeat=5, color="blue", speed=0.1)

        """
        text = text_validator(text)
        speed = speed_validator(speed)
        repeat = repeat_validator(repeat)
        COLOR, RESET = color_handling(color)

        for _ in range(repeat):
            print(f"{COLOR}{text}{RESET}", end="", flush=True)
            time.sleep(speed)
            clear_line(text)
            time.sleep(speed)
            

    def dots(self, text, speed=speed, repeat=repeat, color=default_color):
        """
        dots: dots effect
        description:
        ----- This function prints the text in a dots effect.
        examples:
        ----- text.dots("hello world", repeat=5, color="blue", speed=0.1)

        """
        text = text_validator(text)
        speed = speed_validator(speed)
        repeat = repeat_validator(repeat)
        
        COLOR, RESET = color_handling(color)
        dots = [".", "..", "..."]

        for _ in range(repeat):
            for dot in dots:
                print(f"{COLOR}{text}{dot}{RESET}", end="", flush=True)
                time.sleep(speed)
                clear_line(text+dot)
                



    def reverse_typewriter(self, text, speed=speed, repeat=repeat, color=default_color):

        """
        reverse_typewriter:reverse typewriter effect
        description:
        ----- This function prints the text in a reverse typewriter effect.
        examples:
        ----- text.reverse_typewriter("hello world", repeat=5, color="blue", speed=0.1)

        """
        text = text_validator(text)
        speed = speed_validator(speed)
        repeat = repeat_validator(repeat)
        
        COLOR, RESET = color_handling(color)

        for _ in range(repeat):
            print(f"{COLOR}{text}{RESET}", end="", flush=True)
            time.sleep(speed)
            for i in range(len(text)):
                clear_line(text)
                print(f"{COLOR}{text[:-i-1]}{RESET}", end="", flush=True)
                time.sleep(speed)
                data = text[:-i-1]

            clear_line(data)
   


    def wave(self, text, speed=speed, repeat=repeat, color=default_color):
        """
        wave: wave effect
        description:
        ----- This function prints the text in a wave effect.
        examples:
        ----- text.wave("hello world", repeat=5, color="blue", speed=0.1)

        """
        text = text_validator(text)
        speed = speed_validator(speed)
        repeat = repeat_validator(repeat)

        COLOR, RESET = color_handling(color)
        temp = list(text)

        for _ in range(repeat):
            for i in range(len(text)):
                

                temp[i] = temp[i].upper()
                data = "".join(temp)
                clear_line(data)
                print(f"{COLOR}{data}{RESET}", end="", flush=True)
                time.sleep(speed)
                temp[i] = temp[i].lower()
                

    def bounce(self, text, speed=speed, repeat=repeat, color=default_color, width=width):
        """
        bounce: bounce effect
        description:
        ----- This function prints the text in a bounce effect.
        examples:
        ----- text.bounce("hello world", repeat=5, color="blue", speed=0.1, width=20)
        
        """
        text = text_validator(text)
        speed = speed_validator(speed)
        repeat = repeat_validator(repeat)
        width = width_validator(width)

        COLOR, RESET = color_handling(color)
        
        for _ in range(repeat):
            for i in range(width + 1):
               
                print(" " * i + f"{COLOR}{text}{RESET}", end="", flush=True)
            
                time.sleep(speed)
                data = " " * i + text
                clear_line(data)
                
            for i in range(width -1, -1, -1):
                   
                print(" " * i + f"{COLOR}{text}{RESET}", end="", flush=True)

                time.sleep(speed)
                data = " " * i + text
                clear_line(data)
        clear_line(text)


    def scroll_left(self, text, speed=speed, repeat=repeat, color=default_color, width=width):
        """
        scroll_left: scroll left effect
        description:
        ----- This function prints the text in a scroll left effect.
        examples:
        ----- text.scroll_left("hello world", repeat=5, color="blue", speed=0.1, width=20)

        """
        text = text_validator(text)
        speed = speed_validator(speed)
        repeat = repeat_validator(repeat)
        width = width_validator(width)

        COLOR, RESET = color_handling(color)

        for _ in range(repeat):
            for i in range(width, -1, -1):
                print(" " * i + f"{COLOR}{text}{RESET}", end="", flush=True)
                time.sleep(speed)
                data = " " * i + f"{text}"
                
                clear_line(data)
            for i in range(1, len(text) + 1):
                print("\r" + f"{COLOR}{text[i:]}{RESET}", end="", flush=True)
                time.sleep(speed)
                clear_line(text[i:])
                
    
    

    def scroll_right(self, text, speed=speed, repeat=repeat, color=default_color, width=width):
        """
        scroll_right: scroll right effect
        description:
        ----- This function prints the text in a scroll right effect.
        examples:
        ----- text.scroll_right("hello world", repeat=5, color="blue", speed=0.1, width=20)
        
        """
        text = text_validator(text)
        speed = speed_validator(speed)
        repeat = repeat_validator(repeat)
        width = width_validator(width)
        
        COLOR, RESET = color_handling(color)

        
        for _ in range(repeat):
            for i in range(width + 1):
                print(" " * i + f"{COLOR}{text}{RESET}", end="", flush=True)
                time.sleep(speed)
                data = " " * i + f"{text}"
                
                clear_line(data)
            for i in range(1, len(text) + 1):
                print(" " * width +f"{COLOR}{text[:-i]}{RESET}", end="", flush=True)
                time.sleep(speed)
                data = " " * width + text[:-i]
                clear_line(data)
        
    def documents(self):
        documents = """

from terminalfx.text import Text

text = Text()

text.typewriter("afzal", repeat=5, color="blue", speed=0.1)

text.blink("hello welcome", repeat=5, color="magenta", speed=1)

text.dots("hello welcome", repeat=5, speed=1, color="blue")

text.reverse_typewriter("hello welcome", repeat=5, speed=1, color="blue")

text.wave("hello welcome", speed=1, color="blue", repeat=5)

text.bounce("hello welcome", speed=0.1, color="blue", repeat=5, width=20)

text.scroll_left("hello welcome", speed=0.1, color="blue", repeat=1, width=20)

text.scroll_right("hello welcome", speed=0.1, color="blue", repeat=1, width=20)


"""
        print(documents)


