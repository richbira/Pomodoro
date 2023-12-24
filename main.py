from playsound import playsound
import tkinter as tk
import time
from playsound import playsound

class PomodoroTimer:
    def __init__(self):
        self.timer_running = False
        self.window = tk.Tk()
        self.window.title("Tomato Timer")
        self.window.geometry("500x250+660+300")
        self.window.iconbitmap('./images/logo.ico')
        self.window.resizable(False, False)
        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        menu_bar = tk.Menu(self.window)
        self.window.config(menu=menu_bar)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Settings", menu=file_menu)
        file_menu.add_separator()
        file_menu.add_command(label="Edit Pomodoro Timer", command=self.open_edit_pomodoro)
        file_menu.add_command(label="What is pomodoro?", command=self.open_what_is_pomodoro)
        file_menu.add_command(label="How to use pomodoro timer", command=self.open_how_pomodoro)


    def create_widgets(self):
        self.entry = tk.Entry(self.window)
        self.entry.pack()
          
        frame_mode_buttons = tk.Frame(self.window,padx=10, pady=10)
        frame_mode_buttons.pack()
        
        self.pomodoro_button = tk.Button(frame_mode_buttons, text="Pomodoro", command=lambda: self.set_timer(25))
        self.pomodoro_button.pack(side="left", padx=5)
        self.short_break_button = tk.Button(frame_mode_buttons, text="Short Break", command=lambda: self.set_timer(5))
        self.short_break_button.pack(side="left", padx=5)
        self.long_break_button = tk.Button(frame_mode_buttons, text="Long Break", command=lambda: self.set_timer(15))
        self.long_break_button.pack(side="left", padx=5)
        
        self.label = tk.Label(self.window, text="Time remaining:",font=("Helvetica", 14))
        self.label.pack()
        self.text_box = tk.Text(self.window, height=3, width=40)
        self.text_box.insert(tk.END, "You don’t have to be great to start, but you have to start to be great.")
        self.text_box.pack()
        
        play_photo = tk.PhotoImage(file = "./images/play.png")
        pause_photo = tk.PhotoImage(file = "./images/pause.png")
        
        self.play_photo_ref = play_photo
        self.stop_photo_ref = pause_photo
                
        frame_buttons_time = tk.Frame(self.window,padx=10, pady=10, height=100, width=100)
        frame_buttons_time.pack()
        self.start_button = tk.Button(frame_buttons_time, text="Start", command=self.start_timer,image=play_photo)
        self.start_button.pack(side="left", padx=5)
        self.stop_button = tk.Button(frame_buttons_time, text="Stop", command=self.stop_timer,image=pause_photo)
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
        
    def open_edit_pomodoro(self):
        EditPomodoroTimer(self.window)
        
    def open_how_pomodoro(self):
        HowToPomodoro(self.window)
        
    def start_timer(self):
        minutes = int(self.entry.get())
        seconds = minutes * 60
        self.disable_buttons()
        self.timer_running = True
        
        while seconds >= 0 and self.timer_running:
            self.label.config(text=f"Time remaining: {seconds // 60}:{seconds % 60:02d}", font=("Helvetica", 14))
            self.label.update()
            time.sleep(1)
            seconds -= 1

            if seconds == 0:
                self.enable_buttons()
                self.label.config(text="Time finished!")
                playsound('./audio/notification.mp3')
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
        self.window.iconbitmap('./images/logo.ico')
        # Add content to the new window as needed
        self.text_box = tk.Text(self.window, height=10, width=50)
        self.text_box.insert(tk.END, "The Pomodoro Technique is a time management method that uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks. It is named after the tomato-shaped kitchen timer that was used by the creator of this technique. The technique aims to improve productivity by reducing distractions and promoting focus and concentration.")
        self.text_box.pack()
        
class EditPomodoroTimer:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.iconbitmap('./images/logo.ico')
        self.window.title("Edit Pomodoro Timer")
        self.window.geometry("500x200+460+350")
        
        # Initialize StringVar with default values
        self.pomodoro_time = tk.StringVar(value="25")
        self.short_break_time = tk.StringVar(value="5")
        self.long_break_time = tk.StringVar(value="15")
        
        self.create_widgets(parent)
        
    def create_widgets(self, parent):
        pomodoro_label = tk.Label(self.window, text="Pomodoro", font=("Helvetica", 12))
        pomodoro_label.pack()
        
        pomodoro_time = tk.StringVar()
        pomodoro_time = 25
        pomodoro_entry = tk.Entry(self.window,textvariable=pomodoro_time)
        pomodoro_entry.insert(0, pomodoro_time)
        pomodoro_entry.pack(padx=5, pady=5)
        pomodoro_entry.focus()
        
        short_break_label = tk.Label(self.window, text="Short Break", font=("Helvetica", 12))
        short_break_label.pack()
        
        short_break_time = tk.StringVar()
        short_break_time = 5
        short_break_entry = tk.Entry(self.window,textvariable=short_break_time)
        short_break_entry.insert(0, short_break_time)
        short_break_entry.pack(padx=5, pady=5)
        
        long_break_label = tk.Label(self.window, text="Long Break", font=("Helvetica", 12))
        long_break_label.pack()
        
        long_break_time = tk.StringVar()
        long_break_entry = tk.Entry(self.window,textvariable=long_break_time)
        long_break_time = 15
        long_break_entry.insert(0, long_break_time)
        long_break_entry.pack(padx=5, pady=5)
        
       #save_button = tk.Button(self.window, text="Save", command=lambda: self.save_values(parent))
        save_button = tk.Button(self.window, text="Save", command=self.save_values)
        save_button.pack()

    def close_window(self, parent):
        parent.deiconify()  # Show the main window
        self.window.destroy()  # Close the Toplevel window
    
    
    def save_values(self):
        # Retrieve the entered values
        pomodoro_value = int(self.pomodoro_time.get())
        short_break_value = int(self.short_break_time.get())
        long_break_value = int(self.long_break_time.get())

        # You can use these values as needed (e.g., save to a file or update settings)
        print("Pomodoro:", pomodoro_value)
        print("Short Break:", short_break_value)
        print("Long Break:", long_break_value)

        # Close the Toplevel window
        self.window.deiconify()
        self.window.destroy()
        
class HowToPomodoro:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Edit Pomodoro Timer")
        self.window.iconbitmap('./images/logo.ico')
        self.text_box = tk.Text(self.window, height=10, width=50)
        text = """
        - Decide task to be done set timers to 25 minutes for one "Pomodoro" \n
        - Work on task until timer is complete \n
        - Take a 5 minutes short break \n
        - After four "Pomodoro" take a long break \n
        - Repeat to step 1 \n
         
        Final Result: You have worked for 100 minutes and took 15 minutes break"""
        self.text_box.insert(tk.END, text)
        self.text_box.pack()

if __name__ == "__main__":
    timer = PomodoroTimer()
    timer.run()
    
    