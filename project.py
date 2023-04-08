import curses
import time
import sys
import random


def start_screen(stdscr):
    '''Intro screen. Prompts user to press any key in order to begin'''

    stdscr.erase()
    stdscr.addstr("Welcome to the Speed Typing test")
    stdscr.addstr("\nPress any key to begin")
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr, target, current, wpm=0):
    '''Function to display user input text on top of target text'''

    stdscr.addstr(target)

    # Display current WPM
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    # Activate 'correct' color pair when character matches
    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)

        # Activate 'incorrect' color pair when character does not match
        if char != correct_char:
            color = curses.color_pair(2)

        stdscr.addstr(0, i, char, color)


def load_text():
    with open("text.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

def wpm_test(stdscr):
    '''Test the users WPM'''

    # The text the user needs to type out
    target_text = load_text()

    # List of what the user has typed so far
    current_text = []

    wpm = 0

    start_time = time.time()

    # Allows WPM to be updated live
    stdscr.nodelay(True)

    while True:
        # calculate time elapsed without dividing by zero
        time_elapsed = max(time.time() - start_time, 1)

        # Calculate WPM (words per minute)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.erase()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        # Break loop when user completes typing the target text
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        # Prevent program from crashing if user doesn't press a key
        try:
            key = stdscr.getkey()
        except:
            continue

        # Exit any time with 'esc' key
        if esc(key) == True:
            sys.exit()

        # Configure 'backspace' to behave as backspace
        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()

        # Do not allow user to type beyond length of target text
        elif len(current_text) < len(target_text):
            current_text.append(key)


def esc(key):
    '''Use esc key to exit program'''
    try:
        if ord(key) == 27:
            return True

    # Exception to prevent TypeError when pressing backspace
    except TypeError:
        return False


def main(stdscr):

    # Initialise font color pairs
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_WHITE)

    start_screen(stdscr)

    while True:
        wpm_test(stdscr)

        # Pause screen when user completes typing test
        stdscr.addstr(2, 0, "You completed the typing test! Press any key to continue...")

        # Press any key except 'esc' to rerun test
        key = stdscr.getkey()

        # If user wishes to, exit with 'esc'
        if esc(key) == True:
            sys.exit()


if __name__ == "__main__":

    # Overlay output screen with curses module
    curses.wrapper(main)