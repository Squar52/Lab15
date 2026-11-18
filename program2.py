import os
import tkinter as tk
FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "text.txt")
if not os.path.exists(FILE):
    with open(FILE, "w", encoding="utf-8") as f:
        f.write("Python3 is 1 great language since 1991, version 3.12!\n")
def remove_digits():
    "Зчитує рядок із файлу, видаляє з нього всі цифри і виводить результат в Entry."
    with open(FILE, "r", encoding="utf-8") as f:
        line = f.readline().strip()
    result = "".join(ch for ch in line if not ch.isdigit())
    label_source.config(text="Рядок із файлу: " + line)
    entry.delete(0, tk.END)
    entry.insert(0, result)
win = tk.Tk()
win.title("Видалення цифр із рядка")
label_title = tk.Label(win, text="Результат (рядок без цифр):")
label_source = tk.Label(win, text="Натисніть кнопку, щоб зчитати рядок із файлу text.txt")
frame = tk.Frame(win, relief=tk.GROOVE, borderwidth=3)
entry = tk.Entry(frame, width=60)
button = tk.Button(frame, text="Зчитати файл і видалити цифри", command=remove_digits)
label_source.pack(pady=5)
label_title.pack()
frame.pack(padx=10, pady=10)
entry.pack(padx=5, pady=5)
button.pack(pady=5)
win.mainloop()