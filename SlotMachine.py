import random

#constant value which is not going to change
MAX_BET=5000
MIN_BET=10
MAX_LINES=4
ROWS=4
COLOUMNS=4

#Symbol count for slott
symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8,
    "E":10
}
#the more the symbol is the higher the reward is
symbol_value={
    "A":6,
    "B":5,
    "C":4,
    "D":3,
    "E":2
}

def check_winning(columns,lines,values,bet):
    winning=0
    winnnig_lines=[] #line represents index
    for line in range(lines): #lines represents lines 
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol !=symbol_to_check:
                break
        else:
            winning+=values[symbol]*bet
            winnnig_lines.append(line+1)
    return winning,winnnig_lines





def get_slot_spin(rows,clmns,symbols):
    all_symbols=[]
#it gives both symbol and value associated with it
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
#usually list when implemented in this way represent rows but here we use to represent columns
#start by defining columns list
    columns=[]
    for _ in range(clmns):
        column=[]
        #we used [:] here because we want copy of all_symbol not reference
        current_symbol=all_symbols[:]

        for _ in range(rows):
            value=random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for rows in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!=len(columns)-1:
                print(column[rows],end=" | ")
            else:
                print(column[rows],end="")
        print()


def deposit():
    while True:
        amount=input("Enter the deposit amount:")
        if amount.isdigit():
            amount=int(amount)

            if amount>0:
                break;
            else:
                print("amount must be greater than zero")
        else:
            print("Enter a number")

    return amount
    

def get_no_of_lines():
    while True:
        lines=input("Enter the no. of lines to bet on(1-"+str(MAX_LINES)+"): ")
        if lines.isdigit():
            lines=int(lines)

            if 1<=lines<=MAX_LINES:
                break;
            else:
                print("Give a valid line number")
        else:
            print("Enter a number")

    return lines
    
def get_bet():
    while True:
        bet_amount=input("How much would you like to bet: ")
        if bet_amount.isdigit():
            bet_amount=int(bet_amount)

            if MIN_BET<=bet_amount<=MAX_BET:
                break; 
            else:
                print(f"Amount must be between {MIN_BET}₹ TO {MAX_BET}₹")
        else:
            print("Enter betting amount")
    return bet_amount


def game_spin(balance):
    betlines=get_no_of_lines()
    while True:
            betting=get_bet()
            total_bet=betting*betlines
            if total_bet>balance:
                    print(f"Insufficient Balance.Your current balance is {balance}₹")
            else:
                break
    print(f"Your betting amount is {betting}₹ on {betlines} lines.Your Total bet is equal to {total_bet}")
    print(balance,betlines)


    slots=get_slot_spin(ROWS,COLOUMNS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines= check_winning(slots, betlines, symbol_value, betting)
    print(f"You Won {winnings}₹.")
    print(f"You Won on lines",*winning_lines)
    return winnings-total_bet


def main():
    balance=deposit()
    while True:
        print(f"current Balance is {balance}₹ ")
        spin=input("Press Enter To Play(q to quit).")
        if spin=="q":
            break
        balance+=game_spin(balance)
    print(f"You left with {balance}₹. THANK YOU FOR PLAYING")

main()



  