import tkinter as tk
from tkinter import *
from tkinter import ttk 

# TODO comment code file into sections

root = Tk()
root.geometry("750x500")
frame = ttk.Frame(root, padding=10)
frame.pack()

selected_words = []
word_labels = {}

# TODO perhaps refactor the board so it's a class, not a list
board = [
    ["Agenda", "Absorb", "Photographer", "Unplug"],
    ["Digest", "Planner", "Envelope", "Meditate"],
    ["Limits", "Process", "Band", "Journal"],
    ["Florist", "Luck", "Take-in", "Exercise"]
]

words_group_matchings = {
    "People hired for an event": ["Band", "Florist", "Photographer", "Planner"],
    "Internalise": ["Absorb", "Digest", "Process", "Take-in"],
    "Ways to practice self-care": ["Exercise", "Journal", "Meditate", "Unplug"],
    "Things that are pushed metaphorically": ["Agenda", "Envelope", "Limits", "Luck"]
}

colour_group_matchings = {
    "Yellow": words_group_matchings["People hired for an event"], 
    "Green": words_group_matchings["Internalise"], 
    "Blue": words_group_matchings["Ways to practice self-care"], 
    "Purple": words_group_matchings["Things that are pushed metaphorically"]
}

# TODO work on implementing logic for wrong groupings 
# - all words should be deselected, and mistakes remaining lives should change colour 
# - if all lives have been used, end of games and the results are shown 
# TODO write out and visualise logic
def select_words(label, word):
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

def deselect_words():
    for word in selected_words:
        word_labels[word].config(bg="white")

    selected_words.clear()

def check_word_group(): 
    ''' Note that connections groups are always listed in alphabetical order, hence why this logic can be used '''
    sorted_words = sorted(selected_words)

    for group in words_group_matchings.values():
        if sorted_words == sorted(group):
            deselect_words()
            create_row(sorted_words)
            return

    print("Incorrect Grouping")
    deselect_words()

# TODO implement correct grouping logic and animation
# - organise into one column 
# - display the title of the group
# NOTE: this may be beyond the abilities of tkinter, may need to move to JavaScript frontend and keep logic in backend
def create_row(sorted_words):
    print(colour_group_matchings.items())
    for colour, groups in colour_group_matchings.items(): 
        if sorted_words == sorted(groups):
            for word in sorted_words:
                print(colour)
                word_labels[word].config(bg=colour)
            
    print("Correct Grouping")

for row in range(len(board)):
    for column in range(len(board)):
        word = board[row][column]
        word_frame = ttk.Frame(frame, width=100, height=100)
        word_frame.grid(row=row, column=column, padx=3, pady=3)
        word_frame.pack_propagate(False)

        word_tile = tk.Label(word_frame, text=board[row][column], bg="white", fg="black")
        word_tile.place(x=0, y=0, relwidth=1, relheight=1)

        word_frame.rowconfigure(0, weight=1)
        word_frame.columnconfigure(0, weight=1)

        word_labels[word] = word_tile

        word_tile.bind(
            "<Button-1>",
            lambda event, label=word_tile, word=board[row][column]: select_words(label, word)
        )

# TODO make the presentation of UI better 
mistakes_remaining_text = tk.Label(frame, text="Mistakes Remaining: ", fg="white")
mistakes_remaining_text.grid(row=5, column=0)

canvas = tk.Canvas(frame, width=140, height=40)
canvas.grid(row=5, column=1)

mistake_circles = []
for i in range(4):
    x1 = 10 + (i * 30)
    y1 = 10
    x2 = x1 + 20
    y2 = y1 + 20

    canvas.create_oval(x1, y1, x2, y2, fill="white", outline="white", width=1)

# TODO add functionality for shuffling words in grid 
shuffle_button = ttk.Button(frame, text="Shuffle")
shuffle_button.grid(row=6, column=1)

deselect_all_button = ttk.Button(frame, text="Deselect All", command=deselect_words)
deselect_all_button.grid(row=6, column=2)

submit_button = ttk.Button(frame, text="Submit", command=check_word_group)
submit_button.grid(row=6, column=3)
submit_button.config(state="disabled")

root.mainloop()
