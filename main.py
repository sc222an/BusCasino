from tkinter import *
class profile:
    currentBets = None
    currentBalance = None
def getBuses(busNumber):
    #get all buses on specified line with the name of the next stop and the bus code
    return [["Stabbing Hill", "1"], ["Knife Crime Close", "2"], ["Accrington", "3"]]

def getOdds(busNumber):
    #calculate odds based on previous data for that line
    return "5/1"

def placeBet(busNumber, busCode, busStopName, odds, p, balanceLabel):
    p.currentBalance -= 5
    p.currentBets.append([busNumber, busCode, busStopName, odds])
    balanceLabel.config(text="Balance = " + str(p.currentBalance))


def addOddsLabels(busNumber, p, balanceLabel):
    data = getBuses(busNumber)
    row = 2  # Start placing labels and buttons from row 2
    for line in data:
        bus_stop_name, busCode = line
        odds = getOdds(busNumber)
        label = Label(root, text=f"{bus_stop_name} {busNumber} {odds}")
        label.grid(row=row, column=0, padx=10, pady=5)
        button = Button(root, text="Bet on it", command=lambda: placeBet(busNumber, busCode, bus_stop_name, odds, p, balanceLabel))
        button.grid(row=row, column=1, padx=10, pady=5)
        row += 1

def showBets(p):
    top = Toplevel()
    top.title("Current Bets")
    top.geometry("400x300")
    
    row = 0
    for bet in p.currentBets:
        bet_label = Label(top, text=f"Bus Number: {bet[0]}, Bus Code: {bet[1]}, Bus Stop: {bet[2]}, Odds: {bet[3]}")
        bet_label.grid(row=row, column=0, padx=10, pady=5)
        row += 1

root = Tk()
root.geometry("800x600")
p = profile()
p.currentBalance = 100
p.currentBets = []
balanceLabel = Label(root, text="Balance = "+str(p.currentBalance))
balanceLabel.grid(row=0, column=0, padx=10, pady=10)

search_label = Label(root, text="Search")
search_label.grid(row=1, column=0, padx=10, pady=10)

search = Entry(root)
search.grid(row=1, column=1, padx=10, pady=10)

search_button = Button(root, text="Search", command=lambda: addOddsLabels(search.get(), p, balanceLabel))
search_button.grid(row=1, column=2, padx=10, pady=10)

betsButton = Button(root, text="View bets", command=lambda: showBets(p))
betsButton.grid(row=2, column=2, padx=10, pady=10, sticky="e")

root.mainloop()