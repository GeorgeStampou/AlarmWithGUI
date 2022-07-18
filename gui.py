import datetime
import tkinter as tk
from ctypes import windll
import os
import tkinter as tk
from tkinter import ttk, font
from alarm2 import func_alarm


def save_pressed(day, month, year, hour, minute, second, label, alarms):
    date_time = day + '/' + month + '/' + year + ' ' + hour + ':' + minute + ':' + second
    print(f"Save button pressed.{date_time}")
    # label['text'] = label['text'] + date_time + " is saved.\n"   an thelw na vgainoyn ola ta ksipnitira
    label['text'] = date_time + " is saved.\n"
    label.update()
    alarms.append(date_time)
    print(alarms)
    return alarms


def submit_pressed(alarms):
    func_alarm(alarms)


def convert_month(month):
    datetime_obj = datetime.datetime.strptime(month, '%B')
    return datetime_obj.month


def main():

    alarms = []

    window_width = 350
    window_height = 250
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

    root.columnconfigure(1, weight=1)
    root.rowconfigure(3, weight=1)

    label = ttk.Label(
        root,
        text="ALARM",
        font=('Small Fonts', 25)
    )
    label.grid(row=0, column=0, columnspan=3, sticky='n')

    # root.attributes('-topmost', 1)  ensure that a window is always at the top of the stacking order
    root.iconbitmap(os.path.join("Data", "alarmicon.ico"))

    # year frame
    year_frame = ttk.Frame(root)
    year_frame.grid(row=1, column=2)

    year_label = ttk.Label(year_frame, text='Year', font=('Small Fonts', 15))
    year_label.grid(row=1, column=2)

    year_text = tk.StringVar()
    year_textbox = ttk.Entry(year_frame, textvariable=year_text)
    year_textbox.grid(row=2, column=2)

    # month frame
    month_frame = ttk.Frame(root)
    month_frame.grid(row=1, column=1)

    month_label = ttk.Label(month_frame, text='Month', font=('Small Fonts', 15))
    month_label.grid(row=1, column=1)

    month_options = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                     'September', 'October', 'November', 'December']

    month_text = tk.StringVar()
    month_text.set("January")
    month_drop = ttk.OptionMenu(month_frame, month_text, *month_options)
    month_drop.grid(row=2, column=1)

    # day frame
    day_frame = ttk.Frame(root)
    day_frame.grid(row=1, column=0)

    day_label = ttk.Label(day_frame, text='Day', font=('Small Fonts', 15))
    day_label.grid(row=1, column=0)

    day_options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                   '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                   '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    day_text = tk.StringVar()
    day_text.set("1")
    day_drop = ttk.OptionMenu(day_frame, day_text, *day_options)
    day_drop.grid(row=2, column=0)

    # hour frame
    hour_frame = ttk.Frame(root)
    hour_frame.grid(row=2, column=0)

    hour_label = ttk.Label(hour_frame, text='Hour', font=('Small Fonts', 15))
    hour_label.grid(row=1, column=0)

    hour_option = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13',
                   '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
    hour_text = tk.StringVar()
    hour_text.set("00")
    hour_drop = ttk.OptionMenu(hour_frame, hour_text, *hour_option)
    hour_drop.grid(row=2, column=0)

    # minute frame
    minute_frame = ttk.Frame(root)
    minute_frame.grid(row=2, column=1)

    minute_label = ttk.Label(minute_frame, text='Minute', font=('Small Fonts', 15))
    minute_label.grid(row=1, column=1)

    minute_text = tk.StringVar()
    minute_textbox = ttk.Entry(minute_frame, textvariable=minute_text)
    minute_textbox.grid(row=2, column=1)

    # second frame
    second_frame = ttk.Frame(root)
    second_frame.grid(row=2, column=2)

    second_label = ttk.Label(second_frame, text="Seconds", font=('Small Fonts', 15))
    second_label.grid(row=1, column=0)

    second_text = tk.StringVar()
    second_textbox = ttk.Entry(second_frame, textvariable=second_text)
    second_textbox.grid(row=2, column=0)

    # saved alarms
    saved_alarms_frame = ttk.Frame(root)
    saved_alarms_frame.grid(row=4, column=0, columnspan=3)

    saved_alarms_label = ttk.Label(saved_alarms_frame, text=" ", font=('Small Fonts', 15))
    saved_alarms_label.grid(row=0, column=0)

    # save button
    save_btn = ttk.Button(root, text="SAVE",
                          command=lambda: alarms == save_pressed(day_text.get(),
                                                                 str(convert_month(month_text.get())), year_text.get(),
                                                                 hour_text.get(), minute_text.get(), second_text.get(),
                                                                 saved_alarms_label, alarms))
    save_btn.grid(row=3, column=0)

    # submit button
    submit_btn = ttk.Button(root, text="SUBMIT", command=lambda: submit_pressed(alarms))
    submit_btn.grid(row=3, column=1)

    try:
        from ctypes import windll

        windll.shcore.SetProcessDpiAwareness(1)
    finally:
        root.mainloop()


if __name__ == '__main__':
    main()
