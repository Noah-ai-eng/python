MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("The amount must be greater than zero!!")
        else:
            print("Please enter a number...")
    return amount
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-"+ str(MAX_LINES) +")? : ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid line!!")
        else:
            print("Please enter a number...")
    return lines
def get_bet():
    while True:
        bet = input("Enter your bet (min. " + str(MIN_BET) + ", max. " + str(MAX_BET) + ")? : ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print("Enter a valid bet!!")
        else:
            print("Please enter a number...")
    return bet

def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = bet * lines

    print(f"You have this much balance: ${balance}.")
    print(f"You are betting ${bet} on {lines} lines.Your total winning amount is {total_bet}.")
    
main()
