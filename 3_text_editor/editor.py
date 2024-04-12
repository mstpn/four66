'''
lil_chirp: 140 character editor

Todo:
    File list
    Load file and edit
    File preview
'''
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
def main(stdscr: curses.window):
    stdscr.clear()
    stdscr.addstr(0, 2, "lil chirp: 140 char text editor")
    win = curses.newwin(4, 35, 2, 2)
    rectangle(stdscr, 1, 1, 6, 37)
    box = Textbox(win)
    save_win = curses.newwin(3, 50, 2, 40)
    cmd_win = curses.newwin(3, 25, 8, 2)
    rectangle(stdscr, 7, 1, 11, 27)
    stdscr.refresh()
    cmd_win.clear()
    cmd_win.addstr(0, 0, "Control-D: Delete")
    cmd_win.addstr(1, 0, "Control-H: Backspace")
    cmd_win.addstr(2, 0, "Control-G: Stop editing")
    cmd_win.refresh()

    def text_edit() -> str:
        box.edit()
        text = box.gather().strip()
        return text

    def save_file(text: str):
        save_win.clear()
        save_win.addstr("Do you want to save your file (y/n)?\n")
        choice = save_win.getkey()
        if choice.lower() != 'y':
            return
        save_win.addstr("Enter a filename:\n")
        curses.echo()
        fname = ""
        key = ""
        while key != "\n":
            key = save_win.getkey()
            if key.isalpha():
                fname += key
        curses.noecho()
        fname += ".txt"
        with open(fname, mode="wt") as f:
            f.write(text)

    def handler():
        while True:
            text = text_edit()
            save_file(text)
            save_win.clear()
            win.clear()
            save_win.addstr("Would you like to edit another file (y/n)?\n")
            choice = save_win.getkey()
            if choice.lower() != 'y':
                break

    handler()
    
if __name__ == '__main__':
    wrapper(main)
