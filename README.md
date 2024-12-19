# Anti-AFK Script

This script simulates mouse movements and key presses to prevent your system from going idle. It is designed to be used in situations where you want to avoid being logged out or kicked from a game due to inactivity.

## Features:
- Monitors mouse movement and idle time.
- Moves the mouse and presses random keys when idle for a set threshold.
- Configurable idle time threshold and key actions.
- Supports screen resolutions based on your display size.

## Requirements:
- Python 3.x
- `pydirectinput` library (for simulating mouse and keyboard actions)

## Installation:
1. Install Python 3.x (if not already installed).
2. Install the required library using pip:
   ```bash
   pip install pydirectinput

## Usage:

1. Run the script:
    ```bash
    python anti_afk.py
    ```
    Alternatively, just double-click `start.cmd`

2. The script will monitor your system for idle time. If no mouse movement is detected for a specified period, it will simulate random mouse movements and key presses.

3. Press `Ctrl + C` to stop the script.

## Configuration:

- `afk_threshold`: The time (in seconds) of inactivity before the script triggers actions.
- `keys`: The list of keys that can be randomly pressed (e.g., `['w', 'a', 's', 'd', 'space']`).