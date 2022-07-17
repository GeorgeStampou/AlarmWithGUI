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


# synarthsh pou elegxei an ftasame sthn wra wste na xtyphsei to ksipnititri
def check_time(time_obj, sound):

    while True:
        current_time = datetime.now().isoformat(' ', 'seconds')
        if current_time == str(time_obj):  # elegxos an sympimptoyn oi wres kai meres alliws ksanatrexei
            sound_playing(sound)
            return True


# erwthsh an theloume na valoyme kai allo ksipnitiri
def play_again():
    while True:
        again_input = input("Do you want to add another alarm? ('Y', 'y' = yes, 'N', 'n' = no): ").lower()

        if again_input == 'y':
            return '0'
        elif again_input == 'n':
            print("exit")
            return '1'
        else:
            print("You should give 'y' for yes and 'n' for no.")


def main():
    alarms = []
    a = mixer.Sound(os.path.join("Data", "alarm.mp3"))
    print("***ALARM***")
    while True:
        time_str = input("What time do you want the alarm to ring?(Date-Month-Year hours:minutes:seconds(24 hour format)): ")
        time_validated = validate_time(time_str)
        if time_validated[1]:
            alarms.append(time_validated[0])
        answer = play_again()
        if answer == '0':
            continue
        elif answer == '1':
            break
    # print(alarms)
    for alarm in alarms:
        if check_time(alarm, a):
            continue

    print(alarms)


if __name__ == '__main__':
    main()

