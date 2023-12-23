from playsound import playsound
import tkinter as tk
import time
from playsound import playsound

class PomodoroTimer:
    def __init__(self):
        self.timer_running = False
        self.window = tk.Tk()
        self.window.title("Tomato Timer")
        self.window.geometry("500x200")
        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        menu_bar = tk.Menu(self.window)
        self.window.config(menu=menu_bar)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Settings", menu=file_menu)
        file_menu.add_separator()
        file_menu.add_command(label="Edit Pomodoro Timer", command="")
        file_menu.add_command(label="What is pomodoro?", command=self.open_what_is_pomodoro)

    def create_widgets(self):
        self.entry = tk.Entry(self.window)
        self.entry.pack()
        self.label = tk.Label(self.window, text="Time remaining:")
        self.label.pack()
        self.text_box = tk.Text(self.window, height=3, width=40)
        self.text_box.insert(tk.END, "You don’t have to be great to start, but you have to start to be great.")
        self.text_box.pack()
        
        self.pomodoro_button = tk.Button(self.window, text="Pomodoro", command=lambda: self.set_timer(25))
        self.pomodoro_button.pack(side="left", padx=5)
        self.short_break_button = tk.Button(self.window, text="Short Break", command=lambda: self.set_timer(5))
        self.short_break_button.pack(side="left", padx=5)
        self.long_break_button = tk.Button(self.window, text="Long Break", command=lambda: self.set_timer(15))
        self.long_break_button.pack(side="left", padx=5)
        self.start_button = tk.Button(self.window, text="Start", command=self.start_timer)
        self.start_button.pack(side="left", padx=5)
        self.stop_button = tk.Button(self.window, text="Stop", command=self.stop_timer)
        self.stop_button.pack(side="left", padx=5)

    def set_timer(self, minutes):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, minutes)

    def start_timer(self):
        minutes = int(self.entry.get())
        seconds = minutes * 60
        self.disable_buttons()
        self.timer_running = True
        
    def open_what_is_pomodoro(self):
        WhatIsPomodoro(self.window)
        
    def open_what_is_pomodoro(self):
        EditPomodoroTimer(self.window)
        
    def start_timer(self):
        minutes = int(self.entry.get())
        seconds = minutes * 60
        self.disable_buttons()
        self.timer_running = True
        
        while seconds >= 0 and self.timer_running:
            self.label.config(text=f"Time remaining: {seconds // 60}:{seconds % 60:02d}")
            self.label.update()
            time.sleep(1)
            seconds -= 1

            if seconds == 0:
                self.enable_buttons()
                self.label.config(text="Time finished!")
                playsound('C:/Users/Richard/Desktop/Github/Pomodoro/audio/notification.mp3')
                break

        self.enable_buttons()

    def stop_timer(self):
        self.enable_buttons()
        self.timer_running = False

    def enable_buttons(self):
        self.pomodoro_button.config(state=tk.NORMAL)
        self.long_break_button.config(state=tk.NORMAL)
        self.short_break_button.config(state=tk.NORMAL)
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.NORMAL)

    def disable_buttons(self):
        self.pomodoro_button.config(state=tk.DISABLED)
        self.long_break_button.config(state=tk.DISABLED)
        self.short_break_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.DISABLED)

    def run(self):
        self.window.mainloop()
 

class WhatIsPomodoro:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("What is Pomodoro?")
        
        # Add content to the new window as needed
        

class EditPomodoroTimer:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Edit Pomodoro Timer")

if __name__ == "__main__":
    timer = PomodoroTimer()
    timer.run()