print("Nguyen Van An")
print("Msv:235752021162")
import tkinter as tk

def on_button_click():
    print("Button clicked!")

window = tk.Tk()
window.title("My Window")

button = tk.Button(window, text="Click Me", command=on_button_click, bg="blue", fg="white")
button.pack(pady=20)

window.mainloop()