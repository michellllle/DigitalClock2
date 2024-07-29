import tkinter as tk
import time

# Function to update the time display
def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)  # Update the time every second

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Create a label to display the time
clock_label = tk.Label(root, font=("Arial", 48), bg="black", fg="white")
clock_label.pack(anchor='center')

# Initialize the time display
update_time()

# Run the Tkinter event loop
root.mainloop()