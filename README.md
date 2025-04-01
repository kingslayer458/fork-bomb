# fork-bomb

This is a simple Tkinter-based login system with a fun twist. If the user enters the correct password (`python`), they are granted access. If they enter an incorrect password, the system initiates a countdown and then executes `.bat` files (if available) to simulate a crash effect.

## Features
- Basic authentication with username and password.
- Displays a welcome message if the correct password is entered.
- Initiates a countdown and executes `.bat` files if an incorrect password is entered.
- Simple GUI built with Tkinter.

## Requirements
- Python 3.x
- Tkinter (included with Python standard library)

## How to Use
1. Run the script:
   ```sh
   python sas.py
   python sas2.py
   ```
2. Enter a name and password.
3. If the correct password (`python`) is entered, a welcome message appears.
4. If an incorrect password is entered, a countdown begins before executing `.bat` files (if available).

## File Execution Behavior
- The script searches for `.bat` files in the current directory.
- If two `.bat` files are found, they will be executed using `subprocess.Popen()`.
- If fewer than two `.bat` files are present, a message is displayed in the console.

## Disclaimer
This script is meant for educational and entertainment purposes. Be cautious when running or modifying `.bat` files, as they can execute system commands.

## License
This project is open-source and available under the MIT License.

