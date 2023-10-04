import random

# Initialize
options = ["D", "W", "Q"]
current_balance = float(random.randint(-1000, 10000))

while True:
    # Display interface
    print(f"{'*' * 39}")
    print(f"{'PIXELL RIVER FINANCIAL':>30}")
    print(f"{'ATM Simulator':>30}")
    print(f"Your current balance is: ${current_balance:,.2f}")
    print(f"{'Deposit: D':>30}")
    print(f"{'Withdraw: W':>30}")
    print(f"{'To Quit: Q':>30}")
    print(f"{'*' * 39}")

    # Take user input
    user_input = input("Enter your selection: ").upper()

    if user_input in options:
        if user_input == "D":
            amount = float(input("Enter amount of transaction: "))
            current_balance += amount
        elif user_input == "W":
            amount = float(input("Enter amount of transaction: "))
            if amount > current_balance:
                print("INSUFFICIENT FUNDS")
            else:
                current_balance -= amount
        elif user_input == "Q":
            break
    else:
        print("INVALID SELECTION")
