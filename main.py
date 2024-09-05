from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

# Get random words
random_index = 0
random_word = ""


def get_random():
    global random_index, random_word
    try:
        data = pd.read_csv("./data/words_to_learn.csv")
    except FileNotFoundError:
        data = pd.read_csv("./data/list_words.csv")
    index_list = data.index.tolist()
    random_index = random.choice(index_list)
    random_word = data.loc[random_index]["Arabic"]
    canvas.itemconfig(card, image=card_front)
    canvas.itemconfig(title, text="Arabic")
    canvas.itemconfig(word, text=random_word)
    print(random_word)
    print(len(data))
    window.after(3000, flip_card)


# Flip the card
def flip_card():
    try:
        data = pd.read_csv("./data/words_to_learn.csv")
    except FileNotFoundError:
        data = pd.read_csv("data/list_words.csv")
    translated_word = data.loc[random_index]["English"]
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(word, text=translated_word)


# Delete a word to avoid repeating
def delete_word():
    try:
        data_to_update = pd.read_csv("./data/words_to_learn.csv")
    except FileNotFoundError:
        data_to_update = pd.read_csv("data/list_words.csv")
    data_updated = data_to_update[data_to_update["Arabic"] != random_word]
    data_updated.to_csv('./data/words_to_learn.csv', index=False)
    get_random()


# Load window
window = Tk()
window.title("Flash Card App")
window.configure(background=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526)

# Load pictures
card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")

# Create buttons
Button_right = Button(window, image=right, highlightthickness=0, command=delete_word)
Button_left = Button(window, image=wrong, highlightthickness=0, command=get_random)

# Place picture and texts
card = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text="Language", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 50, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Place buttons
Button_left.grid(row=1, column=0)
Button_right.grid(row=1, column=1)
get_random()
window.mainloop()
