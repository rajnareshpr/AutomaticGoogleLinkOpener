
# Import the webbrowser and time module
import webbrowser
import time

# Taking website to be opened as input
link = [(input("Enter the link to website you want to open ->"))
for i in range(int(input("Enter how many links: ")))]
print(link)

# Taking alarm time from the user
alarm = [(input("Set the website alarm time as (Format:- HH:MM:SS)(24 hour format) ->"))
for i in range(int(input("Enter how many alarms:")))]
print(alarm)

# This is the actual time that we will use to print.
Current_time = time.strftime("%H:%M:%S")

# Printing current time untill alarm time
i = 0
for x in alarm:
    while (Current_time != alarm[i]):
        print("Waiting, the current time is " + Current_time + " :-( ")
        Current_time = time.strftime("%H:%M:%S")
        time.sleep(1)

    # Opening the webpage at alarm time
    if (Current_time == alarm[i]):
        print("WEBSITE IS OPENING :D")
        webbrowser.open(link[i])
    i=i+1
