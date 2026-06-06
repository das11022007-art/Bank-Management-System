print("\n-----Welcome to the Bank Account Management System-----")
name = input("Enter name: ")
balance = int(input("Enter intitial balance:"))
account = {"name": name, "balance": balance}

amount = int(input("Enter amount to deposit:"))
def deposit(account , amount):
    if amount > 0:
        account["balance"] = account["balance"] + amount
        print("Depsit successful . New balance : ", account["balance"])

amount = int(input("Enter maount to withdrawn: "))
def withdraw(account, amount):
    if account["balance"] >=amount:
        account["balance"] = account["balance"] - amount
       # print("Withdrawn successful. New balance: ", account["balance"])
    else:
        print("Insufficient balance. Withdrawal failed.")

def check_balance(account):
    print("current balcne: " , account["balance"])

def exit():
    print("Exsiting the program. Goodbye!")

while True:
    print("\n-----Select operation:-----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter choice (1/2/3/4): "))
    if choice == 1:
        deposit(account, amount)
    elif choice == 2:
        withdraw(account, amount)
    elif choice == 3:
        check_balance(account)
    elif choice == 4:
        exit()
        break
    else:
        print("Invalid choice. Please try again.") 