import tkinter as tk
from tkinter import *
from tkinter import ttk 

root = Tk()
root.geometry("750x500")
frame = ttk.Frame(root, padding=10)
frame.pack()

selected_words = []
board = [
    ["Band", "Florist", "Photographer", "Planner"],
    ["Absorb", "Digest", "Process", "Take-in"],
    ["Exercise", "Journal", "Meditate", "Unplug"],
    ["Agenda", "Envelope", "Limits", "Luck"]
]

words_group_matchings = {
    "People hired for an event": board[0],
    "Internalise": board[1],
    "Ways to practice self-care": board[2],
    "Things that are pushed metaphorically": board[3]
}

def select_word(label):
    # TODO add toggling logic (if white, turn darker and vice versa)
    check_submit(label)
    pass 

def check_submit(current_word):
    if len(selected_words) == 4: 
        check_word_group(selected_words)
    else: 
        selected_words.append(current_word)

# TODO implement logic that checks whether a group has been created     
def check_word_group(words): 
    pass

i = 0
for row in range(len(board)):
    for column in range(len(board)):
        word_frame = ttk.Frame(frame, width=100, height=100)
        word_frame.grid(row=row, column=column, padx=3, pady=3)
        word_frame.pack_propagate(False)

        word_tile = tk.Label(word_frame, text=board[row][column], bg="#e6e6e6", fg="black")
        word_tile.place(x=0,
            y=0,
            relwidth=1,
            relheight=1)

        word_frame.rowconfigure(0, weight=1)
        word_frame.columnconfigure(0, weight=1)

        word_tile.bind(
            "<Button-1>",
            lambda event, word=board[row][column]: check_submit(word)
        )

submit_button = ttk.Button(frame, text="Submit", command=check_word_group)
submit_button.grid(row=5, column=2)
submit_button.config(state="disabled")

root.mainloop()
