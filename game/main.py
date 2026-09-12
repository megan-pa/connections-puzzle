import tkinter as tk
from tkinter import *
from tkinter import ttk 

root = Tk()
root.geometry("750x500")
frame = ttk.Frame(root, padding=10)
frame.pack()

selected_words = []
# TODO perhaps refactor the board so it's a class, not a list
# TODO change so the words are in a random order on the board
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

def select_words(label, word):
    # TODO add toggling logic (if white, turn darker and vice versa)
    if word not in selected_words:
        label.config(bg="grey")
        selected_words.append(word)
    else:
        label.config(bg="white")
        selected_words.remove(word)
    
    if len(selected_words) == 4: 
        submit_button.config(state="normal")
    else:
        submit_button.config(state="disabled")

# TODO fix below function - will not work since not using label configuration
# can use a dictionary and map each word to a word_tile, making it easier for selection/deselection
'''def deselect_words():
    for word in selected_words:
        word.config(bg="white")

    selected_words.clear()'''

def check_word_group(): 
    ''' Note that connections groups are always '''
    sorted_words = sorted(selected_words)

    for group in words_group_matchings.values():
        if sorted_words == sorted(group):
            create_row(sorted_words)
            return

    print("Incorrect Grouping")
    # deselect_words()

# TODO implement correct grouping logic and animation
# - organise into one column 
# - change the colour of the column 
# - display both the colour of the group and the title
# NOTE: this may be beyond the abilities of tkinter, may need to move to JavaScript frontend and keep logic in backend
def create_row(sorted_words):
    print("Correct Grouping")

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
            lambda event, label=word_tile, word=board[row][column]: select_words(label, word)
        )

# TODO continue adding features to the people tool bar including: 
# - shuffle button: makes the board shuffle around the words 
# - clear button: deselects all buttons 
# - mistakes remaining: taskbar-like UI feature should be added showing the number of lives remaining once an incorrect grouping is submitted
submit_button = ttk.Button(frame, text="Submit", command=check_word_group)
submit_button.grid(row=5, column=2)
submit_button.config(state="disabled")

root.mainloop()
