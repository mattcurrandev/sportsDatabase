import tkinter
from tkinter import ttk
from tkinter import messagebox

#function for enter data button
def enter_data():
    #terms and conditions accept
    accepted = accept_var.get()

    if accepted == "Accepted":

        #player info
        firstName = firstNameEntry.get()
        lastName = lastNameEntry.get()
        position = positionCombobox.get()
        if firstName and lastName and position:
            age = ageSpinbox.get()
            nationality = nationalityEntry.get()
        
            #player team and stats
            team = teamNameEntry.get()
            season = yearPlayedEntry.get()
            gp = gamesPlayedSpinbox.get()
            goals = goalsScoredEntry.get()
            assists = assistsScoredEntry.get()
            pims = pimsRecordedEntry.get()
            wins = winsRecordedEntry.get()
            losses = lossesRecordedEntry.get()
            savePercentage = savePercentageEntry.get()

            #salary Info
            baseSalary = baseSalaryEntry.get()
            totalSalary = totalSalaryEntry.get()
            aav = aavEntry.get()

            print("First Name: ", firstName, "Last Name: ", lastName)
            print("Position: ", position, "Age: ", age, "Nationality: ", nationality)
            print("Team: ", team, "Season: ", season, "Games Played: ", gp)
            print("Goals Scored: ", goals, "Assists scored: ", assists, "Penalties in Minutes: ", pims)
            print("Wins Recorded: ", wins, "Losses Recorded: ", losses, "Save Percentage: ", savePercentage)
            print('Base Salary: ', baseSalary, "Total Salary: ", totalSalary, "AAV: ", aav)
            #added a seperator for terminal print out
            print("-------------------------------------------------------------------------")
        else:
            tkinter.messagebox.showwarning(title = "Error", message = "First name, Last Name and Position are required.")
    else:
        tkinter.messagebox.showwarning(title = "Error", message = "Terms and conditions not accepted.")


#create window
window = tkinter.Tk()
window.title('Sports Data Entry Form')

frame = tkinter.Frame(window)
frame.pack()

playerInfoFrame = tkinter.LabelFrame(frame, text='Player Information')
playerInfoFrame.grid(row=0, column=0, padx=20, pady=10)

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

#saving team info/stats 
teamFrame = tkinter.LabelFrame(frame)
teamFrame.grid(row=1, column=0, sticky='news', padx=20, pady=10)

teamNameLabel = tkinter.Label(teamFrame, text='Team Name')
teamNameEntry = tkinter.Entry(teamFrame)

teamNameLabel.grid(row=0, column=0)
teamNameEntry.grid(row=1, column=0)

yearPlayedLabel = tkinter.Label(teamFrame, text='Season Played')
yearPlayedEntry = tkinter.Entry(teamFrame)

yearPlayedLabel.grid(row=0, column=1)
yearPlayedEntry.grid(row=1, column=1)

gamesPlayedLabel =tkinter.Label(teamFrame, text='Games Palyed')
gamesPlayedSpinbox = tkinter.Spinbox(teamFrame, from_=0, to=100)

gamesPlayedLabel.grid(row=0, column=2)
gamesPlayedSpinbox.grid(row=1, column=2)

goalsScoredLabel = tkinter.Label(teamFrame, text='Goals Scored')
goalsScoredEntry = tkinter.Entry(teamFrame)

goalsScoredLabel.grid(row=2, column=0)
goalsScoredEntry.grid(row=3, column=0)

assistsScoredLabel = tkinter.Label(teamFrame, text='Assists Scored')
assistsScoredEntry = tkinter.Entry(teamFrame)

assistsScoredLabel.grid(row=2, column=1)
assistsScoredEntry.grid(row=3, column=1)

pimsRecordedLabel = tkinter.Label(teamFrame, text='Penalties in Minutes')
pimsRecordedEntry = tkinter.Entry(teamFrame)

pimsRecordedLabel.grid(row=2, column=2)
pimsRecordedEntry.grid(row=3, column=2)

winsRecordedLabel = tkinter.Label(teamFrame, text='Wins Recorded')
winsRecordedEntry = tkinter.Entry(teamFrame)

winsRecordedLabel.grid(row=4, column=0)
winsRecordedEntry.grid(row=5, column=0)

lossesRecordedLabel = tkinter.Label(teamFrame, text='Losses Recorded')
lossesRecordedEntry = tkinter.Entry(teamFrame)

lossesRecordedLabel.grid(row=4, column=1)
lossesRecordedEntry.grid(row=5, column=1)

savePercentageLabel = tkinter.Label(teamFrame, text='Save Percentage')
savePercentageEntry = tkinter.Entry(teamFrame)

savePercentageLabel.grid(row=4, column=2)
savePercentageEntry.grid(row=5, column=2)

#add padding to widgets
for widget in teamFrame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#saving salary info
salaryInfoFrame = tkinter.LabelFrame(frame, text='Salary Information')
salaryInfoFrame.grid(row=2, column=0, sticky='news', padx=20, pady=10)

baseSalaryLabel = tkinter.Label(salaryInfoFrame, text='Base Salary')
baseSalaryEntry = tkinter.Entry(salaryInfoFrame)

baseSalaryLabel.grid(row=0, column=0)
baseSalaryEntry.grid(row=1, column=0)

totalSalaryLabel = tkinter.Label(salaryInfoFrame, text='Total Salary')
totalSalaryEntry = tkinter.Entry(salaryInfoFrame)

totalSalaryLabel.grid(row=0, column=1)
totalSalaryEntry.grid(row=1, column=1)

aavLabel = tkinter.Label(salaryInfoFrame, text='Annual Average Salary')
aavEntry = tkinter.Entry(salaryInfoFrame)

aavLabel.grid(row=0, column=2)
aavEntry.grid(row=1, column=2)

#terms and conditions
termsFrame = tkinter.LabelFrame(frame, text='Terms and Conditions')
termsFrame.grid(row=3, column=0, sticky='news', padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
termsCheck = tkinter.Checkbutton(termsFrame, text='I accept the terms and conditions.',
                                 variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
termsCheck.grid(row=0, column=0)

#enter data button
button = tkinter.Button(frame, text='Enter Data', command= enter_data)
button.grid(row=4, column=0, sticky='news', padx=20, pady=10)

#main loop to run the window when the window is closed the loop stops
window.mainloop()