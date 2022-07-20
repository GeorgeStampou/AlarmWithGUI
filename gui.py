import datetime
import os
import tkinter as tk
from tkinter import ttk
from alarm import func_alarm


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


def exit_pressed(root):
    root.destroy()


def convert_month(month):
    datetime_obj = datetime.datetime.strptime(month, '%B')
    return datetime_obj.month


def create_button(root, text, command, row, column, **kwargs):
    button = ttk.Button(root, text=text, command=command)
    button.grid(row=row, column=column)
    return button


def create_frame(root, row, column, **kwargs):
    frame = ttk.Frame(root)
    colspan = kwargs['columnspan'] if 'columnspan' in kwargs else None
    frame.grid(row=row, column=column, columnspan=colspan)
    return frame


def create_label(root, text, row, column, **kwargs):
    f = kwargs['font'] if 'font' in kwargs else None
    s = kwargs['sticky'] if 'sticky' in kwargs else None
    colspan = kwargs['columnspan'] if 'columnspan' in kwargs else None
    label = ttk.Label(root, text=text, font=f)
    label.grid(row=row, column=column, columnspan=colspan, sticky=s)
    return label


def create_textbox(frame, text, row, column, **kwargs):
    textbox = ttk.Entry(frame, textvariable=text)
    textbox.grid(row=row, column=column)
    return textbox


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

    root.columnconfigure(0, weight=1)
    root.rowconfigure(3, weight=1)

    label = create_label(root, 'ALARM', 0, 0, font=('Small Fonts', 25), columnspan=3, sticky='n')

    # root.attributes('-topmost', 1)  ensure that a window is always at the top of the stacking order
    root.iconbitmap(os.path.join("Data", "alarmicon.ico"))

    # year frame
    year_frame = create_frame(root, 1, 2)

    year_label = create_label(year_frame, 'Year', 1, 2, font=('Small Fonts', 15))

    year_text = tk.StringVar()
    year_textbox = create_textbox(year_frame, year_text, 2, 2)

    # month frame
    month_frame = create_frame(root, 1, 1)

    month_label = create_label(month_frame, 'Month', 1, 1, font=('Small Fonts', 15))

    month_options = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                     'September', 'October', 'November', 'December']

    month_text = tk.StringVar()
    month_text.set("January")
    month_drop = ttk.OptionMenu(month_frame, month_text, *month_options)
    month_drop.grid(row=2, column=1)

    # day frame
    day_frame = create_frame(root, 1, 0)

    day_label = create_label(day_frame, 'Day', 1, 0, font=('Small Fonts', 15))

    day_options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                   '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                   '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    day_text = tk.StringVar()
    day_text.set("1")
    day_drop = ttk.OptionMenu(day_frame, day_text, *day_options)
    day_drop.grid(row=2, column=0)

    # hour frame
    hour_frame = create_frame(root, 2, 0)

    hour_label = create_label(hour_frame, 'Hour', 1, 0, font=('Small Fonts', 15))

    hour_option = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13',
                   '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
    hour_text = tk.StringVar()
    hour_text.set("00")
    hour_drop = ttk.OptionMenu(hour_frame, hour_text, *hour_option)
    hour_drop.grid(row=2, column=0)

    # minute frame
    minute_frame = create_frame(root, 2, 1)

    minute_label = create_label(minute_frame, 'Minute', 1, 1, font=('Small Fonts', 15))

    minute_text = tk.StringVar()
    minute_textbox = create_textbox(minute_frame, minute_text, 2, 1)

    # second frame
    second_frame = create_frame(root, 2, 2)

    second_label = create_label(second_frame, 'Second', 1, 0, font=('Small Fonts', 15))

    second_text = tk.StringVar()
    second_textbox = create_textbox(second_frame, second_text, 2, 0)

    # saved alarms
    saved_alarms_frame = create_frame(root, 4, 0, columnspan=3)

    saved_alarms_label = create_label(saved_alarms_frame, '', 0, 0, font=('Small Fonts', 15))

    # save button
    save_btn = create_button(root, 'Save',
                             lambda: alarms == save_pressed(day_text.get(), str(convert_month(month_text.get())),
                                                            year_text.get(), hour_text.get(), minute_text.get(),
                                                            second_text.get(), saved_alarms_label, alarms), 3, 0)

    # submit button
    submit_btn = create_button(root, 'Submit', lambda: submit_pressed(alarms), 3, 1)

    # exit button
    exit_btn = create_button(root, 'Exit', lambda: exit_pressed(root), 3, 2)

    try:
        from ctypes import windll

        windll.shcore.SetProcessDpiAwareness(1)
    finally:
        root.mainloop()


if __name__ == '__main__':
    main()
