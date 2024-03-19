import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

def timer_loop():
    while True:
        try:
            duration = int(input("Enter the countdown duration in seconds (0 to exit): "))
            if duration == 0:
                break
            countdown_timer(duration)
        except ValueError:
            print("Invalid input. Please enter a valid number of seconds.")

if __name__ == "__main__":
    timer_loop()
