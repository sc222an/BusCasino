from tkinter import *
from tkinter import ttk


class Profile:
    current_bets = None
    current_balance = None


def get_buses(bus_number):
    # Mock function: Fetch all buses on the specified line with stop names and bus codes
    return [["Victoria Road Jct", "1"], ["Headrow K", "2"], ["Moor Grange", "3"]]


def get_odds(bus_number):
    # Mock function: Return static odds for simplicity
    return "5/1"


def place_bet(bus_number, bus_code, bus_stop_name, odds, profile, balance_label):
    profile.current_balance -= 5
    profile.current_bets.append([bus_number, bus_code, bus_stop_name, odds])
    balance_label.config(text=f"Balance = {profile.current_balance}")


def add_odds_labels(bus_number, profile, balance_label):
    data = get_buses(bus_number)

    # Clear previous data if any
    for widget in results_frame.winfo_children():
        widget.destroy()

    row = 0  # Start placing labels and buttons from the first row
    for line in data:
        bus_stop_name, bus_code = line
        odds = get_odds(bus_number)

        # Create a frame for each bus entry
        bus_frame = Frame(results_frame, bg="#333", pady=5)
        bus_frame.pack(fill="x", pady=2)

        bus_label = Label(bus_frame, text=f"{bus_stop_name} ({bus_number}) | Odds: {odds}", 
                           font=("Arial", 14), fg="white", bg="#333")
        bus_label.pack(side="left", padx=10)

        bet_button = Button(bus_frame, text="Bet on it", bg="#006400", fg="white", 
                             command=lambda b=bus_number, c=bus_code, n=bus_stop_name, o=odds: 
                             place_bet(b, c, n, o, profile, balance_label))
        bet_button.pack(side="right", padx=10)


def show_bets(profile):
    top = Toplevel()
    top.title("Current Bets")
    top.geometry("800x600")
    top.configure(bg="#1a1a1a")

    # Top Frame for the Toplevel window
    top_frame = Frame(top, bg="#222", pady=10)
    top_frame.pack(fill="x")

    header_label = Label(top_frame, text="Current Bets", font=("Arial", 16), fg="white", bg="#222")
    header_label.pack(side="left", padx=10)

    # Content Frame for bets
    bets_frame = Frame(top, bg="#1a1a1a")
    bets_frame.pack(fill="both", expand=True, pady=10)

    row = 0
    for bet in profile.current_bets:
        bet_frame = Frame(bets_frame, bg="#333", pady=5)
        bet_frame.pack(fill="x", pady=2)

        bet_label = Label(bet_frame, text=f"Bus Number: {bet[0]}, Bus Code: {bet[1]}, Stop: {bet[2]}, Odds: {bet[3]}", 
                           font=("Arial", 14), fg="white", bg="#333")
        bet_label.pack(side="left", padx=10)


# Main Application Window
root = Tk()
root.geometry("800x600")
root.title("Goobus")
root.configure(bg="#1a1a1a")

p = Profile()
p.current_balance = 100
p.current_bets = []

# Top Frame for Balance and Search
top_frame = Frame(root, bg="#222", pady=10)
top_frame.pack(fill="x")

# Balance Label
balance_label = Label(top_frame, text=f"Balance = {p.current_balance}", font=("Arial", 16), fg="white", bg="#222")
balance_label.pack(side="left", padx=10)

# Search Bar
search_frame = Frame(top_frame, bg="#222")
search_frame.pack(side="right")

search_label = Label(search_frame, text="Search Bus:", font=("Arial", 14), fg="white", bg="#222")
search_label.pack(side="left", padx=5)

search_entry = Entry(search_frame, font=("Arial", 14))
search_entry.pack(side="left", padx=5)

search_button = Button(search_frame, text="Search", bg="#333", fg="white", 
                        command=lambda: add_odds_labels(search_entry.get(), p, balance_label))
search_button.pack(side="left", padx=5)

# Results Section
results_frame = Frame(root, bg="#1a1a1a")
results_frame.pack(pady=20, fill="x")

# Bets Button
bets_button = Button(root, text="View Bets", bg="#333", fg="white", 
                      command=lambda: show_bets(p))
bets_button.pack(pady=10)

root.mainloop()
