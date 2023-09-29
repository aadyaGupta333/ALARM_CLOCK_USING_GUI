from tkinter import *
import datetime
import time
from pydub import AudioSegment
from pydub.playback import play

def alarm(set_alarm_timer):
    while True:
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:", date)
        print("Current Time is:", now)
        if now == set_alarm_timer:
            print("Set Alarm For:", set_alarm_timer)
            sound_file = r"C:\Users\KIIT\Downloads\Alarm Kebakaran ! Alarm.mp3"  # Adjust the filename and path as needed
            song=AudioSegment.from_mp3(sound_file)
            play(song)
            break
        time.sleep(1)

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)
    
clock = Tk()

clock.title("Alarm Clock")
clock.geometry("400x200")
time_format = Label(clock, text="Enter time in 24-hour format.", fg="white", bg="purple", font="Arial")
time_format.place(x=60, y=120)

addTime = Label(clock, text="Hour  Min   Sec", font=60)
addTime.place(x=110)

setYourAlarm = Label(clock, text="Set Alarm for", fg="blue", relief="solid", font=("Helvetica", 7, "bold"))
setYourAlarm.place(x=15, y=29)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime = Entry(clock, textvariable=hour, bg="skyblue", width=15)
hourTime.place(x=110, y=30)
minTime = Entry(clock, textvariable=min, bg="skyblue", width=15)
minTime.place(x=150, y=30)
secTime = Entry(clock, textvariable=sec, bg="skyblue", width=15)
secTime.place(x=200, y=30)

submit = Button(clock, text="Set Alarm", fg="red", width=10, command=actual_time)
submit.place(x=110, y=70)

clock.mainloop()