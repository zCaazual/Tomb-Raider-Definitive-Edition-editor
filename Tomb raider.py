import tkinter
import struct
import customtkinter
import tkinter as tk
from tkinter import filedialog, messagebox

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

window = customtkinter.CTk()

window.geometry("800x550")

window.resizable(True, True)

window.title("Tomb raider Definitive Edition Tool by zCaazual")

tabs = customtkinter.CTkTabview(window)

notification = tk.StringVar()


singleplayer_frame = tabs.add("Single Player")
singleplayer_label = customtkinter.CTkLabel(singleplayer_frame, text="Single Player tab")
singleplayer_label.grid(row=0, column=0, padx=10, pady=10, sticky="n")

singleplayer_frame.rowconfigure(0, weight=1)
singleplayer_frame.columnconfigure(0, weight=1, minsize=960)

multiplayer_frame = tabs.add("Multiplayer")
multiplayer_label = customtkinter.CTkLabel(multiplayer_frame, text="- Enter a custom value for each option\nButtons are all preset values")
multiplayer_label.grid(row=0, column=0, padx=10, pady=10, sticky="n")

multiplayer_frame.rowconfigure(0, weight=1)
multiplayer_frame.columnconfigure(0, weight=1, minsize=960)

tabs.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

current_file = None
file_name = None

notification_label = customtkinter.CTkLabel(window, textvariable=notification)
notification_label.grid(row=6, column=0, padx=120, pady=10, sticky='s')

def remove_notification():
    notification.set("")
    notification_label.configure(textvariable=notification)

def open_file():
    global current_file, file_name, notification
    file_name = tkinter.filedialog.askopenfilename()
    if not file_name:
        messagebox.showinfo("Error", "File not selected")
        return
    if current_file is not None and current_file == file_name:
        messagebox.showinfo("Error", "File is already opened.")
        return
    current_file = file_name
    try:
        with open(file_name, 'rb') as f:
            file_contents = bytearray(f.read())
    except Exception as e:
        messagebox.showinfo(f"Error: {e}")
        return

    print(file_contents)
    notification.set("File opened successfully.")
    notification_label.configure(textvariable=notification)
    window.after(5000, remove_notification)


def optionmenu_callback_singleplayer(choice):
    print("optionmenu dropdown clicked:", choice)

optionmenu_var = customtkinter.StringVar(value="option 1")

combobox = customtkinter.CTkOptionMenu(master=singleplayer_frame,
                                       values=["option 1", "option 2"],
                                       command=optionmenu_callback_singleplayer,
                                       variable=optionmenu_var,
                                       width=30, height=30,
                                       fg_color=("white", "black"),
                                       button_color=("white", "black"),
                                       dropdown_fg_color=("white", "white"),
                                       dropdown_text_color=("white", "black"),
                                       text_color=("white", "blue"),
                                       font=("Arial", 12),
                                       dropdown_font=("Arial", 12),
                                       hover=True,
                                       state="normal",
                                       dynamic_resizing=True,
                                       anchor="w")
combobox.grid(row=0, column=0, padx=20, pady=10, sticky='nw')
combobox.set("Option 1")

button1 = customtkinter.CTkButton(singleplayer_frame, text="button 1", width=110, height=25, border_width=0, corner_radius=8, hover_color="green", hover=True)
button2 = customtkinter.CTkButton(singleplayer_frame, text="button 2", width=110, height=25, border_width=0, corner_radius=8, hover_color="green", hover=True)
button3 = customtkinter.CTkButton(singleplayer_frame, text="button 3", width=110, height=25, border_width=0, corner_radius=8, hover_color="green", hover=True)
button4 = customtkinter.CTkButton(singleplayer_frame, text="button 4", width=110, height=25, border_width=0, corner_radius=8, hover_color="green", hover=True)
button5 = customtkinter.CTkButton(singleplayer_frame, text="button 5", width=110, height=25, border_width=0, corner_radius=8, hover_color="green", hover=True)

button1.grid(row=1, column=0, padx=10, pady=10, sticky="w")
button2.grid(row=2, column=0, padx=10, pady=10, sticky="w")
button3.grid(row=3, column=0, padx=10, pady=10, sticky="w")
button4.grid(row=4, column=0, padx=10, pady=10, sticky="w")
button5.grid(row=5, column=0, padx=10, pady=10, sticky="w")



def Max_XP_write(offset, relative_offset, new_value):
    with open(file_name, "r+b") as f:
        f.seek(offset + relative_offset)
        new_value_packed = struct.pack("<I", int(hex(new_value), 16))
        f.write(new_value_packed)

def on_max_xp_clicked():
    if file_name is None:
        messagebox.showinfo("Error", "No gamesave was opened\nPlease open a gamesave and try again")
    else:
        Max_XP_write(0x00000DB0, 0x8, 999999999)
        notification.set("XP Has been set to 999999999")
        notification_label.configure(textvariable=notification)
        window.after(5000, remove_notification)



def Max_Salvage_write(offset, relative_offset, new_value):
    with open(file_name, "r+b") as f:
        f.seek(offset + relative_offset)
        new_value_packed = struct.pack("<I", int(hex(new_value), 16))
        f.write(new_value_packed)

def on_max_Salvage_clicked():
    if file_name is None:
        messagebox.showinfo("Error", "No gamesave was opened\nPlease open a gamesave and try again")
    else:
        Max_Salvage_write(0x00000DB0, 0x0C, 999999999)
        notification.set("Salvage Has been set to 999999999")
        notification_label.configure(textvariable=notification)
        window.after(5000, remove_notification)


def Max_Salvage_Entry_write(offset, relative_offset, new_value):
    with open(file_name, "r+b") as f:
        f.seek(offset + relative_offset)
        new_value_packed = struct.pack("<B", new_value)
        f.write(new_value_packed)

def Max_Prestige_write(offset, relative_offset, new_value):
    with open(file_name, "r+b") as f:
        f.seek(offset + relative_offset)
        new_value_packed = struct.pack("<B", new_value)
        f.write(new_value_packed)

def on_max_Prestige_clicked():
    if file_name is None:
        messagebox.showinfo("Error", "No gamesave was opened\nPlease open a gamesave and try again")
    else:
        Max_Prestige_write(0x00000DC0, 0, 0x03)
        notification.set("Prestige Has been set to 3")
        notification_label.configure(textvariable=notification)
        window.after(5000, remove_notification)


def Max_survival_feats_write(offset, relative_offset, new_value):
    with open(file_name, "r+b") as f:
        f.seek(offset + relative_offset)
        new_value_packed = struct.pack("<I", int(hex(new_value), 16))
        f.write(new_value_packed)

def on_max_survival_feats_clicked():
    if file_name is None:
        messagebox.showinfo("Error", "No gamesave was opened\nPlease open a gamesave and try again")
    else:
        Max_survival_feats_write(0x00000DF0, 0, 9999999)
        notification.set("Survival Feats Has been set to 9999999")
        notification_label.configure(textvariable=notification)
        window.after(5000, remove_notification)



def Max_wins_write(offset, relative_offset, new_value):
    with open(file_name, "r+b") as f:
        f.seek(offset + relative_offset)
        new_value_packed = struct.pack("<I", int(hex(new_value), 16))
        f.write(new_value_packed)

def on_max_wins_clicked():
    if file_name is None:
        messagebox.showinfo("Error", "No gamesave was opened\nPlease open a gamesave and try again")
    else:
        Max_wins_write(0x00000DF0, 0x4, 9999999)
        notification.set("Game Wins Has been set to 9999999")
        notification_label.configure(textvariable=notification)
        window.after(5000, remove_notification)


def Max_losses_write(offset, relative_offset, new_value):
    with open(file_name, "r+b") as f:
        f.seek(offset + relative_offset)
        new_value_packed = struct.pack("<i", int(hex(new_value), 16))
        f.write(new_value_packed)

def on_max_losses_clicked():
    if file_name is None:
        messagebox.showinfo("Error", "No gamesave was opened\nPlease open a gamesave and try again")
    else:
        Max_losses_write(0x00000DF0, 0x8, -9999999)
        notification.set("Game Losses Has been set to -9999999")
        notification_label.configure(textvariable=notification)
        window.after(5000, remove_notification)


def Max_kills_write(offset, relative_offset, new_value):
    with open(file_name, "r+b") as f:
        f.seek(offset + relative_offset)
        new_value_packed = struct.pack("<I", int(hex(new_value), 16))
        f.write(new_value_packed)

def on_max_kills_clicked():
    if file_name is None:
        messagebox.showinfo("Error", "No gamesave was opened\nPlease open a gamesave and try again")
    else:
        Max_kills_write(0x00000DF0, 0x0C, 9999999)
        notification.set("kills Has been set to 9999999")
        notification_label.configure(textvariable=notification)
        window.after(5000, remove_notification)

def Max_deaths_write(offset, relative_offset, new_value):
    with open(file_name, "r+b") as f:
        f.seek(offset + relative_offset)
        new_value_packed = struct.pack("<i", int(hex(new_value), 16))
        f.write(new_value_packed)

def on_max_deaths_clicked():
    if file_name is None:
        messagebox.showinfo("Error", "No gamesave was opened\nPlease open a gamesave and try again")
    else:
        Max_deaths_write(0x00000E00, 0, -9999999)
        notification.set("Deaths Has been set to -9999999")
        notification_label.configure(textvariable=notification)
        window.after(5000, remove_notification)


def Max_matches_quit_write(offset, relative_offset, new_value):
    with open(file_name, "r+b") as f:
        f.seek(offset + relative_offset)
        new_value_packed = struct.pack("<i", int(hex(new_value), 16))
        f.write(new_value_packed)

def on_max_matches_quit_clicked():
    if file_name is None:
        messagebox.showinfo("Error", "No gamesave was opened\nPlease open a gamesave and try again")
    else:
        Max_matches_quit_write(0x00000E00, 0x4, -9999999)
        notification.set("matches played Has been set to -9999999")
        notification_label.configure(textvariable=notification)
        window.after(5000, remove_notification)



def Max_salvage_gathered_write(offset, relative_offset, new_value):
    with open(file_name, "r+b") as f:
        f.seek(offset + relative_offset)
        new_value_packed = struct.pack("<I", int(hex(new_value), 16))
        f.write(new_value_packed)

def on_max_salvage_gathered_clicked():
    if file_name is None:
        messagebox.showinfo("Error", "No gamesave was opened\nPlease open a gamesave and try again")
    else:
        Max_salvage_gathered_write(0x00000E30, 0x0C, 9999999)
        notification.set("Salvage Gathered Has been set to 9999999")
        notification_label.configure(textvariable=notification)
        window.after(5000, remove_notification)

def Max_Prestige_Entry_write(offset, relative_offset, new_value):
    with open(file_name, "r+b") as f:
        f.seek(offset + relative_offset)
        new_value_packed = struct.pack("<B", new_value)
        f.write(new_value_packed)

Max_XP = customtkinter.CTkButton(multiplayer_frame, text="Max XP", width=120, height=25, border_width=0, corner_radius=8, hover_color="green", hover=True, command=on_max_xp_clicked)
Max_XP.grid(row=1, column=0, padx=10, pady=20, sticky="w")

Max_XP_textbox = customtkinter.CTkTextbox(multiplayer_frame, width=70, height=3, font=("Arial", 12))
Max_XP_textbox.grid(row=1, column=0, padx=140, pady=5, sticky="w")

Max_Salvage = customtkinter.CTkButton(multiplayer_frame, text="Max Salvage", width=120, height=25, border_width=0, corner_radius=8, hover_color="green", hover=True, command=on_max_Salvage_clicked)
Max_Salvage.grid(row=2, column=0, padx=10, pady=20, sticky="w")

Max_Salvage_textbox = customtkinter.CTkTextbox(multiplayer_frame, width=70, height=3, font=("Arial", 12))
Max_Salvage_textbox.grid(row=2, column=0, padx=140, pady=5, sticky="w")


Survival_feats = customtkinter.CTkButton(multiplayer_frame, text="Survival feats", width=120, height=25, border_width=0, corner_radius=8, hover_color="green", hover=True, command=on_max_survival_feats_clicked)
Survival_feats.grid(row=4, column=0, padx=10, pady=20, sticky="w")

Survival_feats_textbox = customtkinter.CTkTextbox(multiplayer_frame, width=70, height=3, font=("Arial", 12))
Survival_feats_textbox.grid(row=4, column=0, padx=140, pady=5, sticky="w")

Wins = customtkinter.CTkButton(multiplayer_frame, text="Wins", width=120, height=25, border_width=0, corner_radius=8, hover_color="green", hover=True, command=on_max_wins_clicked)
Wins.grid(row=5, column=0, padx=10, pady=20, sticky="w")

Wins_textbox = customtkinter.CTkTextbox(multiplayer_frame, width=70, height=3, font=("Arial", 12))
Wins_textbox.grid(row=5, column=0, padx=140, pady=5, sticky="w")

Losses = customtkinter.CTkButton(multiplayer_frame, text="Losses", width=120, height=25, border_width=0, corner_radius=8, hover_color="green", hover=True, command=on_max_losses_clicked)
Losses.grid(row=1, column=0, padx=220, pady=20, sticky="w")

Losses_textbox = customtkinter.CTkTextbox(multiplayer_frame, width=70, height=3, font=("Arial", 12))
Losses_textbox.grid(row=1, column=0, padx=350, pady=5, sticky="w")

Kills = customtkinter.CTkButton(multiplayer_frame, text="Kills", width=120, height=25, border_width=0, corner_radius=8, hover_color="green", hover=True, command=on_max_kills_clicked)
Kills.grid(row=2, column=0, padx=220, pady=20, sticky="w")

Kills_textbox = customtkinter.CTkTextbox(multiplayer_frame, width=70, height=3, font=("Arial", 12))
Kills_textbox.grid(row=2, column=0, padx=350, pady=5, sticky="w")

Deaths = customtkinter.CTkButton(multiplayer_frame, text="Deaths", width=120, height=25, border_width=0, corner_radius=8, hover_color="green", hover=True, command=on_max_deaths_clicked)
Deaths.grid(row=5, column=0, padx=220, pady=20, sticky="w")

Deaths_textbox = customtkinter.CTkTextbox(multiplayer_frame, width=70, height=3, font=("Arial", 12))
Deaths_textbox.grid(row=5, column=0, padx=350, pady=5, sticky="w")

Matches_quit = customtkinter.CTkButton(multiplayer_frame, text="Matches quit", width=120, height=25, border_width=0, corner_radius=8, hover_color="green", hover=True, command=on_max_matches_quit_clicked)
Matches_quit.grid(row=3, column=0, padx=220, pady=20, sticky="w")

Matches_quit_textbox = customtkinter.CTkTextbox(multiplayer_frame, width=70, height=3, font=("Arial", 12))
Matches_quit_textbox.grid(row=3, column=0, padx=350, pady=5, sticky="w")

downs = customtkinter.CTkButton(multiplayer_frame, text="Number of downs", width=120, height=25, border_width=0, corner_radius=8, hover_color="green", hover=True)
downs.grid(row=4, column=0, padx=220, pady=20, sticky="w")

downs_textbox = customtkinter.CTkTextbox(multiplayer_frame, width=70, height=3, font=("Arial", 12))
downs_textbox.grid(row=4, column=0, padx=350, pady=5, sticky="w")

Max_Prestige = customtkinter.CTkButton(multiplayer_frame, text="Max Prestige", width=120, height=25, border_width=0, corner_radius=8, hover_color="green", hover=True, command=on_max_Prestige_clicked)
Max_Prestige.grid(row=3, column=0, padx=10, pady=20, sticky="w")

Max_Prestige_textbox = customtkinter.CTkTextbox(multiplayer_frame, width=70, height=3, font=("Arial", 12))
Max_Prestige_textbox.grid(row=3, column=0, padx=140, pady=5, sticky="w")


Max_salvage_gathered = customtkinter.CTkButton(multiplayer_frame, text="Max Prestige", width=120, height=25, border_width=0, corner_radius=8, hover_color="green", hover=True, command=on_max_Prestige_clicked)
Max_salvage_gathered.grid(row=1, column=0, padx=440, pady=20, sticky="w")

Max_salvage_textbox = customtkinter.CTkTextbox(multiplayer_frame, width=70, height=3, font=("Arial", 12))
Max_salvage_textbox.grid(row=1, column=0, padx=570, pady=5, sticky="w")

def write_value_to_file(value):
    print(f"Selected value: {value}")

def optionmenu_callback_multiplayer(choice):
    write_value_to_file(choice)

# Create the dropdown menu
optionmenu_var = customtkinter.StringVar(value="Survivor Bow")
combobox = customtkinter.CTkOptionMenu(master=multiplayer_frame,
                                       values=["Survivor Bow", "Hitman shotgun", "Solarii Compound Bow", "Solarii "
                                                                                                         "Crossbow",
                                               "Solarii Double Barrel", "Solarii Marksman rifle",
                                               "Hitman silverballer", "Hitman JAG-D", "Survivor sawn off",
                                               "Solarii Magnum", "Grenade Launcher", "Smoke launcher", "Mines",
                                               "Flare gun", "Flash grenade"],
                                       command=optionmenu_callback_multiplayer,
                                       variable=optionmenu_var,
                                       width=30, height=30,
                                       fg_color=("white", "black"),
                                       button_color=("white", "black"),
                                       dropdown_fg_color=("white", "white"),
                                       dropdown_text_color=("white", "black"),
                                       text_color=("white", "blue"),
                                       font=("Arial", 12),
                                       dropdown_font=("Arial", 12),
                                       hover=True,
                                       state="normal",
                                       dynamic_resizing=True,
                                       anchor="w")
combobox.grid(row=0, column=0, padx=0, pady=10, sticky='nw')

option_values = {
    "Survivor Bow": "17 86 AE D6",
    "Hitman shotgun": "6D 7F EC AF",
    "Solarii Compound Bow": "BE CB 72 D7",
    "Solarii Crossbow": "63 D5 26 CA",
    "Solarii Double Barrel": "F4 26 42 A7",
    "Solarii Marksman rifle": "B1 87 65 AD",
    "Hitman silverballer": "2C FA 17 FF",
    "Hitman JAG-D": "2B FA 17 FF",
    "Survivor sawn off": "1B C2 5F 62",
    "Solarii Magnum": "5F 7C 1E 1B",
    "Grenade Launcher": "AF A0 D8 B6",
    "Smoke launcher": "B7 5B 01 E3",
    "Mines": "2A 05 16 DC",
    "Napalm Launcher": "C1 B1 05 07",
    "Flare gun": "B5 E7 26 75",
    "Flash grenade": "13 53 49 6B",
}
def optionmenu_callback_multiplayer(choice):
    hex_value = option_values.get(choice)
    write_value_to_file(hex_value)

def write_to_file():
    selected_value = optionmenu_var.get()
    write_value_to_file(selected_value)

write_button = customtkinter.CTkButton(master=multiplayer_frame, text="Swap weapon", width=110, height=25, border_width=0, corner_radius=8, hover_color="green", hover=True, command=write_to_file)
write_button.grid(row=0, column=0, padx=190, pady=12, sticky='nw')


menu_bar = tk.Menu(window)

menu_bar.configure(bg="#26242f")

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open Save", command=open_file)
menu_bar.add_cascade(label="Open File", menu=file_menu)

file_menu.add_command(label="Close Application", command=window.destroy)

window.config(menu=menu_bar)

if __name__ == "__main__":
     window.mainloop()
