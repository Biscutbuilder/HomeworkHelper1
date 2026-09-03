import tkinter as tk
import asyncio
import webbrowser
import subprocess 
from subprocess import call
from desktop_notifier import DesktopNotifier, DEFAULT_SOUND
def open_site():
    webbrowser.open("https://www.merriam-webster.com")
def open_py_files():
    call(["python", "calculator.py"])

def submit():
    answer = entry.get()
    print(answer)

    async def main2():
        notifier = DesktopNotifier()
        await asyncio.sleep(1800)
        await notifier.send(
            title="Homework Helper",
            message="Do " + answer,
            sound=DEFAULT_SOUND
        )

    asyncio.run(main2())


window = tk.Tk()
window.title("Homework Helper")
window.geometry("300x250")
window.resizable(False, False)
text = tk.Label(window, text="Welcome to Homework Helper!")
text.pack()
text2 = tk.Label(window, text="Below, type what you need a reminder for in 30 minutes")
text2.pack()


entry = tk.Entry(window)
entry.config(font=("Ink Free", 30))
entry.config(bg="Beige")
entry.config(fg="Dark grey")
entry.config(width=11)
entry.pack()

submit_button = tk.Button(
    window,
    text="Turn On Reminder",
    command=submit
)
submit_button.pack()
button_calc = tk.Button(
    window,
    text = "Open Calculator",
    command=open_py_files
)

button_calc.pack(side=tk.LEFT)
button_dic = tk.Button(window, text="Dictonary",command=open_site)
button_dic.pack(side=tk.LEFT)


window.mainloop()
