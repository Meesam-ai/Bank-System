 import os

def create_account(name, initial_balance=0.0):
   
    account = {"name": name,"balance": initial_balance,"transactions": []}
    save_transactions(account)
    print(f"Account for {name} created with balance ${initial_balance:.2f}.")
    return account

def deposit(account, amount):
    
    if amount <= 0:
        print("Please Enter a Valid amount.")
        return account
    
    account["balance"] += amount
    account["transactions"].append(("Deposit", amount))
    save_transactions(account)
    print(f"Deposited ${amount:.2f}. New balance: ${account['balance']:.2f}.")
    return account

def withdraw(account, amount):
   
    if amount <= 0:
        print("Please Enter a Valid amount.")
        return account

    if amount > account["balance"]:
        print("Insufficient balance. Transaction declined.")
        return account

    account["balance"] -= amount
    account["transactions"].append(("Withdrawal", amount))
    save_transactions(account)
    print(f"Withdrew ${amount:.2f}. New balance: ${account['balance']:.2f}.")
    return account

def check_balance(account):
   
    print(f"Current balance: ${account['balance']:.2f}.")
    return account["balance"]

def print_statement(account):
   
    print(f"Account statement for {account['name']}:\n")
    if not account["transactions"]:
        print("No transactions available.")
    else:
        for txn_type, amount in account["transactions"]:
            print(f"- {txn_type}: ${amount:.2f}")
    print(f"Final Balance: ${account['balance']:.2f}")

def save_transactions(account):
   
    filename = f"{account['name'].replace(' ', '_').lower()}_transactions.txt"
    with open(filename, "w") as file:
        file.write(f"Account Holder: {account['name']}\n")
        file.write(f"Balance: ${account['balance']:.2f}\n")
        file.write("Transactions:\n")
        for txn_type, amount in account["transactions"]:
            file.write(f"- {txn_type}: ${amount:.2f}\n")

def load_transactions(name):
   
    filename = f"{name.replace(' ', '_').lower()}_transactions.txt"
    if not os.path.exists(filename):
        print("Account not Availaible.")
        return create_account(name)

    with open(filename, "r") as file:
        lines = file.readlines()
        balance = float(lines[1].split(": $")[1].strip())
        transactions = []
        for line in lines[3:]:
            txn_type, amount = line.strip("- ").split(": $")
            transactions.append((txn_type, float(amount)))

    account = {
        "name": name,
        "balance": balance,
        "transactions": transactions
    }
    print(f"Loaded account for {name} with balance ${balance:.2f}.")
    return account

def main():
    
    account = None
    while True:
        print("\nBanking System Menu:")
        print("1. Create an Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Print Transaction Statement")
        print("6. Exit")
        choice = input("Please Select an option: ")

        if choice == "1":
            name = input("Enter your name Here: ")
            initial_balance = 0
            account = create_account(name, initial_balance)

        elif choice == "2":
            if account:
                amount = float(input("How much amount you want to deposit: "))
                account = deposit(account, amount)
            else:
                print("Please create an account by selecting option 1.")

        elif choice == "3":
            if account:
                amount = float(input("How much amount you want to withdraw: "))
                account = withdraw(account, amount)
            else:
                print("Please create an account by selecting option 1.")

        elif choice == "4":
            if account:
                check_balance(account)
            else:
                print("Please create an account by selecting option 1.")

        elif choice == "5":
            if account:
                print_statement(account)
            else:
                print("Please create an account by selecting option 1.")

        elif choice == "6":
            print("Thank You for Giving us your time. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
