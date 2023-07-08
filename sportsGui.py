import tkinter
from tkinter import ttk

#create window
window = tkinter.Tk()
window.title('Sports Data Entry Form')

frame = tkinter.Frame(window)
frame.pack()

playerInfoFrame = tkinter.LabelFrame(frame, text='Player Information')
playerInfoFrame.grid(row=0, column=0, padx=20, pady=20)

firstNameLabel = tkinter.Label(playerInfoFrame, text="Player's First Name")
firstNameLabel.grid(row=0, column=0)

lastNameLabel = tkinter.Label(playerInfoFrame, text="Player's Last Name")
lastNameLabel.grid(row=0, column=1)

firstNameEntry = tkinter.Entry(playerInfoFrame)
lastNameEntry = tkinter.Entry(playerInfoFrame)
firstNameEntry.grid(row=1, column=0)
lastNameEntry.grid(row=1, column=1)

positionLabel = tkinter.Label(playerInfoFrame, text='Position')
positionCombobox = ttk.Combobox(playerInfoFrame, values=['Center', 'Left Wing', 'Right Wing', 
                                                         'Right Defender', 'Left Defender', 'Goalie'])
positionLabel.grid(row=0, column=2)
positionCombobox.grid(row=1, column=2)

ageLabel = tkinter.Label(playerInfoFrame, text='Players Age')
ageSpinbox = tkinter.Spinbox(playerInfoFrame, from_=15, to=100)
ageLabel.grid(row=2, column=0)
ageSpinbox.grid(row=3, column=0)

nationalityLabel = tkinter.Label(playerInfoFrame, text='Players Nationality')
nationalityEntry = tkinter.Entry(playerInfoFrame)
nationalityLabel.grid(row=2, column=1)
nationalityEntry.grid(row=3, column=1)

#add padding to widgets
for widget in playerInfoFrame.winfo_children():
    widget.grid_configure(padx=10, pady=5)




#main loop to run the window when the window is closed the loop stops
window.mainloop()