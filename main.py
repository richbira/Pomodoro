from logging import root
import tkinter as tk
import time
from winsound import PlaySound
from playsound import playsound


# Define a global variable to track the timer state
global timer_running

def start_timer():
    
    # Get the time in minutes from the user
    minutes = int(entry.get())
    seconds = minutes * 60

    # Disable the start button
    disable_buttons()
    
    # Set the timer state to running
    timer_running = True

    # Start the timer
    while seconds >= 0 and timer_running:
        # Update the label with the remaining time
        label.config(text=f"Time remaining: {seconds // 60}:{seconds % 60:02d}")
        label.update()

        # Wait for 1 second
        time.sleep(1)

        # Decrease the remaining time
        seconds -= 1

        # Check if the timer has reached 0
        if seconds == 0:
                enable_buttons()
                label.config(text=f"Time finished!")
                playsound('C:/Users/Richard/Desktop/Github/Pomodoro/audio/notification.mp3')
                break
    
    # Enable the start button after the timer ends or is stopped
    enable_buttons()
    
def stop_timer():
    enable_buttons()
    # Set the timer state to not running
    timer_running = False

def enable_buttons():
    pomodoro.config(state=tk.NORMAL)
    long_break_button.config(state=tk.NORMAL)
    short_break_button.config(state=tk.NORMAL)
    start_button.config(state=tk.NORMAL)

def disable_buttons():
    pomodoro.config(state=tk.DISABLED)
    long_break_button.config(state=tk.DISABLED)
    short_break_button.config(state=tk.DISABLED)
    start_button.config(state=tk.DISABLED)

def set_timer(option):
    if option == "pomodoro":
        entry.delete(0, tk.END) 
        entry.insert(0, 25)
    elif option == "short_break":
        entry.delete(0, tk.END) 
        entry.insert(0, 5)
    elif option == "long_break":
        entry.delete(0, tk.END) 
        entry.insert(0, 15)

# Create the main window

window = tk.Tk()
window.title("Tomato Timer")
window.geometry("500x200")

# Create a menu bar
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# Create a File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Settings", menu=file_menu)
file_menu.add_separator()
file_menu.add_command(label="Edit Pomodoro Timer", command="")
file_menu.add_command(label="What is pomodoro?", command="")

# Create an entry field for the user to input the time in minutes
entry = tk.Entry(window)
entry.pack()

# Create a label to display the remaining time
label = tk.Label(window, text="Time remaining:")
label.pack()

# Create a text box for additional notes
text_box = tk.Text(window, height=3, width=40)
default_value = "You don’t have to be great to start, but you have to start to be great."
text_box.insert("1.0", default_value) 
text_box.pack()

# Update the pomodoro command to call set_timer with "pomodoro" option
pomodoro = tk.Button(window, text="Pomodoro", command=lambda: set_timer("pomodoro"))
pomodoro.pack(side="left", padx=5)

# Create a short break button
short_break_button = tk.Button(window, text="Short Break", command=lambda: set_timer("short_break"))
short_break_button.pack(side="left", padx=5)

# Create a long break button
long_break_button = tk.Button(window, text="Long Break", command=lambda: set_timer("long_break"))
long_break_button.pack(side="left", padx=5)


# Button to Start
start_button = tk.Button(window, text="Start", command=start_timer)
start_button.pack(side="left", padx=5)

# Button to Stop
stop_button = tk.Button(window, text="Stop", command=stop_timer)
stop_button.pack(side="left", padx=5)

# Start the main event loop
window.mainloop()
