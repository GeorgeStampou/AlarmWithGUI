import time
from datetime import datetime
from pygame import mixer
import os

mixer.init()

# synarthsh poy paizei to tragoydi poy exoyme apothikeysi ston fakelo Data
def sound_playing(a):
    mixer.Sound.play(a)
    duration = mixer.Sound.get_length(a)
    time.sleep(duration)


# synarthsh poy elegxei thn hmeromhnia kai wra poy dinei o xrhsths
def validate_time(t):
    time_obj = "WRONG TIME"
    correct = False
    try:
        time_obj = datetime.strptime(t, '%d-%m-%Y %H:%M:%S')
        correct = True
    except ValueError:
        print("This is incorrect date/time format. It should be DD-MM-YYYY hh:mm:ss")
    return [time_obj, correct]


def main():
    a = mixer.Sound(os.path.join("Data", "alarm.mp3"))
    print("***ALARM***")
    time_str = input("What time do you want the alarm to ring?(Date-Month-Year hours:minutes:seconds(24 hour format): ")
    while True:
        time_obj = validate_time(time_str)
        if time_obj[1]:
            while True:
                current_time = datetime.now().isoformat(' ', 'seconds')
                if current_time == str(time_obj[0]):  # elegxos an sympimptoyn oi wres kai meres alliws ksanatrexei
                    sound_playing(a)
                    exit()
        else:
            time_str = input(
                "What time you want the alarm to ring? (Date-Month-Year hours:minutes:seconds (24 hour format): ")




if __name__ == '__main__':
    main()

