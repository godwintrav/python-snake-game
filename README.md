# Blitz Snake Game 🐍

A classic Snake game built in Python using the built-in [`turtle`](https://docs.python.org/3/library/turtle.html) graphics module. Guide the snake to eat food, grow longer, and rack up points — your best run is saved between sessions as a persistent high score.

## Features

- 🎮 Smooth arrow-key controls with reverse-direction protection
- 🍎 Randomly spawning food that grows the snake on each catch
- 💥 Collision detection for both walls and the snake's own tail
- 🏆 Persistent high score saved to `data.txt` across game sessions
- 🔁 Automatic reset on collision — keep playing without restarting

## Demo

▶️ [Watch the demo](https://drive.google.com/file/d/17KWgWWDA_fGw0VvHnh1hDjyDGhHcrnnf/view?usp=drive_link)

## Controls

| Key       | Action          |
| --------- | --------------- |
| `↑` Up    | Move up         |
| `↓` Down  | Move down       |
| `←` Left  | Move left       |
| `→` Right | Move right      |

Eat the blue food to grow and increase your score. The game resets your current score (and updates the high score if you beat it) whenever the snake hits a wall or its own tail.

## Requirements

- Python 3.9+ (uses `list[Turtle]` type hints)
- `turtle` module — included in the Python standard library (requires Tk/Tkinter, which ships with most Python installations)

No third-party packages are required.

## Installation & Running

```bash
# Clone the repository
git clone https://github.com/godwintrav/python-snake-game.git
cd python-snake-game

# (Optional) create and activate a virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

# Run the game
python main.py
```

A game window titled **"Blitz Snake Game"** will open. Click anywhere in the window to exit after a game ends.

## Project Structure

| File            | Description                                                                 |
| --------------- | --------------------------------------------------------------------------- |
| `main.py`       | Entry point — sets up the screen, game loop, input bindings, and collisions |
| `snake.py`      | `Snake` class — body segments, movement, growth, direction, and reset logic |
| `food.py`       | `Food` class — spawns food at a random position and refreshes when eaten    |
| `scoreboard.py` | `ScoreBoard` class — tracks current/high score and reads/writes `data.txt`  |
| `data.txt`      | Stores the persistent high score                                            |

## How It Works

- **`main.py`** runs the main loop: it updates the screen, moves the snake every 0.1s, and checks for collisions with food, walls, and the snake's own body.
- **`snake.py`** manages the snake as a list of turtle segments. Movement is handled by shifting each segment to the position of the one ahead, then moving the head forward. Reversing directly into itself is prevented.
- **`food.py`** repositions the food to a random `(x, y)` within the play area each time it's eaten.
- **`scoreboard.py`** displays the score, persists the high score to `data.txt`, and updates it whenever the current score beats the saved best.

## Notes

`snake.py` includes an unused `set_snake_within_screen()` method that, if enabled, would let the snake wrap around the screen edges (exiting one side and reappearing on the opposite side) instead of dying on wall contact.
