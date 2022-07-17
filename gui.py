import tkinter as tk
from ctypes import windll
import os
import tkinter as tk
from tkinter import ttk


def save_pressed(event):
    print("Save button pressed.")


def main():
    window_width = 700
    window_height = 500
    max_width = 1080
    max_height = 1920
    min_width = 100
    min_height = 200
    pixels_from_left = max_height//2-window_width//2
    pixels_from_above = max_width//2-window_height//2

    my_geometry = f'{window_width}x{window_height}+{pixels_from_left}+{pixels_from_above}'

    root = tk.Tk()

    root.title('Alarm App')

    root.geometry(my_geometry)
    root.minsize(min_height, min_width)
    root.maxsize(max_height, max_width)
    ttk.Label(root, text="***ALARM***").pack()
    # root.attributes('-topmost', 1)  ensure that a window is always at the top of the stacking order
    root.iconbitmap(os.path.join("Data", "alarmicon.ico"))

    save_btn = ttk.Button(root, text="SAVE")
    save_btn.bind('<Button>', save_pressed)
    save_btn.bind('<Return>', save_pressed)
    save_btn.focus()
    save_btn.pack(expand=True)
    try:
        from ctypes import windll

        windll.shcore.SetProcessDpiAwareness(1)
    finally:
        root.mainloop()




if __name__ == '__main__':
    main()
