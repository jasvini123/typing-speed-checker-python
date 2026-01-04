import tkinter as tk
from time import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing is a useful skill for programmers.",
    "Python is an easy language to learn.",
    "Accuracy is more important than speed.",
    "Practice makes perfect in everything you do."
]

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Tester")
        self.root.geometry("600x300")

        self.text_to_type = random.choice(sentences)
        self.start_time = None

        self.label = tk.Label(root, text=self.text_to_type, wraplength=500, font=('Arial', 12))
        self.label.pack(pady=20)

        self.entry = tk.Entry(root, font=('Arial', 14), width=60)
        self.entry.pack()
        self.entry.bind('<FocusIn>', self.start_timer)
        self.entry.bind('<Return>', self.calculate_results)

        self.result_label = tk.Label(root, text="", font=('Arial', 12))
        self.result_label.pack(pady=20)

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time()

    def calculate_results(self, event):
        end_time = time()
        typed_text = self.entry.get()
        total_time = end_time - self.start_time

        words = len(typed_text.split())
        wpm = round((words / total_time) * 60) if total_time > 0 else 0

        correct_chars = sum(
            1 for i, c in enumerate(typed_text)
            if i < len(self.text_to_type) and c == self.text_to_type[i]
        )

        accuracy = round((correct_chars / len(self.text_to_type)) * 100)

        self.result_label.config(
            text=f"Time: {round(total_time, 2)}s | WPM: {wpm} | Accuracy: {accuracy}%"
        )

        self.entry.config(state='disabled')

root = tk.Tk()
app = TypingSpeedTest(root)
root.mainloop()
