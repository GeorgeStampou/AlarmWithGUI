import time
from datetime import datetime
from pygame import mixer
import os

mixer.init()

# funtion which plays the song from Data folder
def sound_playing(a):
    mixer.Sound.play(a)
    duration = mixer.Sound.get_length(a)
    time.sleep(duration)


#function to check date and time from user, all inputs must be filled
def validate_time(t):
    time_obj = "WRONG TIME"
    correct = False
    try:
        time_obj = datetime.strptime(t, '%d/%m/%Y %H:%M:%S')
        correct = True
    except ValueError:
        print("This is incorrect date/time format. It should be DD-MM-YYYY hh:mm:ss")
    return [time_obj, correct]


#function to check the time has come so the alarm has to ring
def check_time(time_obj, sound):

    current_time = datetime.now().isoformat(' ', 'seconds')
    if current_time > str(time_obj):
        print(f"Date is in the past ({str(time_obj)}). Live in present.")
        return False
    else:
        while True:
            current_time = datetime.now().isoformat(' ', 'seconds')

            if current_time == str(time_obj):  # elegxos an sympimptoyn oi wres kai meres alliws ksanatrexei
                sound_playing(sound)
                return True
           
            #else: time.sleep(1) 
            

def func_alarm(alarms):

    a = mixer.Sound(os.path.join("Data", "alarm.mp3"))
    print("***ALARM***")
    checked_alarms = []
    for alarm in alarms:
        time_validated = validate_time(alarm)
        if time_validated[1]:
            checked_alarms.append(time_validated[0])
        else:
            print("Wrong time. Try again.")
            continue
    for alarm in checked_alarms:
        check_time(alarm, a)

