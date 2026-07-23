# TerminalFX

A modern Python library for beautiful terminal text animations and effects.


TerminalFX is a Python library that makes terminal output more fun and beautiful.

Instead of printing plain text, you can create smooth animations and colorful effects with just a few lines of Python.

Whether you're building a CLI application, a game, a script, or just experimenting in the terminal, TerminalFX helps bring your text to life.

---

## ✨ Current Features

### 📝 Text Animations

- Typewriter
- Blink
- Loading Dots
- Reverse Typewriter
- Wave
- Bounce
- Scroll Left
- Scroll Right

### 🎨 Text Effects

- Gradient Animation

More effects are coming in future updates.

- shine Animation

more effects arecoming in future updates.

---

## 📦 Installation

```bash
pip install terminalfx
```

Or if you're working on the project locally:

```bash
pip install -e .
```

---

# 🚀 Quick Example

## Typewriter

```python
from terminalfx import Text

text = Text()

text.typewriter(
    "Welcome to TerminalFX!",
    speed=0.05,
    color="cyan"
)
```

---

## Gradient

```python
from terminalfx import Effects

effects = Effects()

effects.gradient(
    "Hello from TerminalFX",
    palette="ocean",
    direction="left",
    speed=0.05,
    repeat=20
)
```

---

# 📚 Available Classes

## Text

The `Text` class contains different terminal text animations.

Currently available:

- typewriter()
- blink()
- dots()
- reverse_typewriter()
- wave()
- bounce()
- scroll_left()
- scroll_right()


---

## Effects

The `Effects` class contains visual text effects.

Currently available:

- gradient()
- shine()

More effects will be added over time.

---

# 🎨 Colors

The following ANSI colors are currently supported:

- black
- red
- green
- yellow
- blue
- magenta
- cyan
- white

---

# 🌈 Palettes

Current gradient palettes:

- ocean

More palettes will be added in future releases.

---

# ⚙️ Common Parameters

| Parameter | Description |
|-----------|-------------|
| text | Text to animate |
| speed | Animation speed |
| repeat | Number of repetitions |
| color | Text color |
| palette | Gradient palette |
| direction | left / right |
| width | Used in scrolling and bounce animations |

---

# 💻 Requirements

- Python 3.9+
- Windows
- Linux
- macOS

---

# 📁 Project Structure

```
terminalfx/
│
├── terminalfx/
│   ├── text.py
│   ├── effects.py
│   ├── palettes.py
│   ├── colors.py
│   ├── constants.py
│   ├── utils.py
│   └── __init__.py
│
├── examples/
├── tests/
├── README.md
├── LICENSE
└── pyproject.toml
```

---

# 🚀 Roadmap

### Version 0.2

- ✅ Text animations
- ✅ Gradient effect

### Next Updates

- Rainbow effect
- Pulse effect
- Shine effect
- Fire effect
- Matrix effect
- Glitch effect
- Progress bars
- Spinners

---

# 🤝 Contributing

If you'd like to improve TerminalFX, fix bugs, or suggest new features, feel free to open an issue or submit a pull request.

Every contribution is appreciated.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Made with ❤️ by **Afzal Sayyad**

GitHub:
https://github.com/sayyadafzal100-ops/TerminalFX

Email:
sayyadafzal100@gmail.com

---

If you find this project useful, consider giving it a ⭐ on GitHub.
It really helps and motivates me to keep improving TerminalFX.