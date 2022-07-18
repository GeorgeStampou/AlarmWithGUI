import tkinter as tk
from ctypes import windll
import os
import tkinter as tk
from tkinter import ttk,font


def save_pressed(year):
    print(f"Save button pressed.{year}")


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
    label = ttk.Label(
        root,
        text="ALARM",
        font=('Small Fonts', 25)
    )
    label.pack()

    # root.attributes('-topmost', 1)  ensure that a window is always at the top of the stacking order
    root.iconbitmap(os.path.join("Data", "alarmicon.ico"))

    date_frame = ttk.Frame(root)
    date_frame.pack(padx=10, pady=10, expand=True)

    year_label = ttk.Label(date_frame, text='Year')
    year_label.pack(expand=True)

    year_text = tk.StringVar()
    year_textbox = ttk.Entry(date_frame, textvariable=year_text)
    year_textbox.pack(expand=True)
    year_textbox.focus()

    save_btn = ttk.Button(root, text="SAVE", command=lambda: save_pressed(year_text.get()))
    save_btn.pack(expand=True)

    try:
        from ctypes import windll

        windll.shcore.SetProcessDpiAwareness(1)
    finally:
        root.mainloop()




if __name__ == '__main__':
    main()
