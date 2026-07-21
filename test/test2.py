from terminalfx import Text

text = Text()

text.typewriter("afzal", repeat=5, color="blue", speed=0.1)

text.blink("hello welcome", repeat=5, color="magenta", speed=1)

text.dots("hello welcome", repeat=5, speed=1, color="blue")

text.reverse_typewriter("hello welcome", repeat=5, speed=1, color="blue")

text.wave("hello welcome", speed=1, color="blue", repeat=5)

text.bounce("hello welcome", speed=0.1, color="blue", repeat=5, width=20)

text.scroll_left("hello welcome", speed=0.1, color="blue", repeat=1, width=20)

text.scroll_right("hello welcome", speed=0.1, color="blue", repeat=1, width=20)
