from tkinter import *
import random

root = Tk()
root.title('Random Team Generator')

# Center App on screen
app_width = 500
app_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')


# Default List of Players
global player_list
player_list = ["Justin", "Peter", "Evan", "Ricky", "Jack", "Karuna", "Robin", "Kevin", "Jared", "Danny"]

# Team Labels
team1_label = Label(root, text="Team 1", font=("Helvetica", 12))
team2_label = Label(root, text="Team 2", font=("Helvetica", 12))

team1_label.grid(row=0, column=0, pady=20)
team2_label.grid(row=0, column=1, pady=20)

# Entry boxes
entry0 = Entry(root, font=("Helvetica", 12))
entry1 = Entry(root, font=("Helvetica", 12))
entry2 = Entry(root, font=("Helvetica", 12))
entry3 = Entry(root, font=("Helvetica", 12))
entry4 = Entry(root, font=("Helvetica", 12))
entry5 = Entry(root, font=("Helvetica", 12))
entry6 = Entry(root, font=("Helvetica", 12))
entry7 = Entry(root, font=("Helvetica", 12))
entry8 = Entry(root, font=("Helvetica", 12))
entry9 = Entry(root, font=("Helvetica", 12))

global entry_list
entry_list = [entry0, entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9]

entry0.grid(row=1, column=0, pady=10, padx= 40)
entry1.grid(row=1, column=1, pady=10, padx =20)
entry2.grid(row=2, column=0, pady=10, padx =40)
entry3.grid(row=2, column=1, pady=10, padx =20)
entry4.grid(row=3, column=0, pady=10, padx =40)
entry5.grid(row=3, column=1, pady=10, padx =20)
entry6.grid(row=4, column=0, pady=10, padx =40)
entry7.grid(row=4, column=1, pady=10, padx =20)
entry8.grid(row=5, column=0, pady=10, padx =40)
entry9.grid(row=5, column=1, pady=10, padx =20)

# Shuffle list of players
def shuffle():
    global entry_list, player_list
    player_list.clear()
    # Clear entry boxes
    for entry in entry_list:
        player_list.insert(len(player_list),entry.get())
        entry.delete(0, END)
        
    random.shuffle(player_list)
    count = 0
    for player in player_list:
        entry_list[count].insert('end', player)
        count += 1

# Shuffle Button
randomize_btn = Button(root, text="Shuffle", font=("Helvetica", 12) , command=shuffle)
randomize_btn.grid(row=6, column=0, columnspan=2, pady= 20)



root.mainloop()