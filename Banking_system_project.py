class BankAccount:
    accounts = {}  # A class-level dictionary to store bank accounts
    user_credentials = {}  # A dictionary to store user authentication data

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        BankAccount.accounts[account_number] = self  # Store the account in the dictionary

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount for withdrawal.")

    def get_balance(self):
        return self.balance


def create_account():
    while True:
        account_number = input("Enter a new account number: ")
        if account_number in BankAccount.accounts:
            print("Account number already exists. Please choose a different number.")
        elif not account_number.isdigit():
            print("Invalid account number. Please use only digits.")
        else:
            balance = input("Initial balance: $")
            if not balance.replace(".", "", 1).isdigit():
                print("Invalid balance. Please enter a valid number.")
            else:
                balance = float(balance)
                account = BankAccount(account_number, balance)
                print(f"Account {account_number} created with a balance of ${balance}.")
                break

BankAccount.user_credentials = {
    "user1": "password1",
    "user2": "password2",
}
def login():
    global logged_in
    if logged_in:
        print("You are already logged in.")
        return

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in BankAccount.user_credentials and BankAccount.user_credentials[username] == password:
        print("Login successful!")
        logged_in = True
    else:
        print("Login failed. Please check your credentials.")


def logout():
    global logged_in
    logged_in = False
    print("Logged out successfully.")


def main():
    bank_name = input("Enter bank name:")
    # bank = Bank_Account(bank_name)
    print(f"Welcome to {bank_name} bank")
    print("please select from the option (1/2/3/4/5) to proceed ")
    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        if logged_in:
            print("5. Log out")
        else:
            print("5. Log in")
        choice = input("Select an option: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            if not logged_in:
                print("You must log in to perform this operation.")
            else:
                account_number = input("Enter account number for deposit: ")
                if account_number in BankAccount.accounts:
                    account = BankAccount.accounts[account_number]
                    amount = input("Enter the deposit amount: $")
                    if not amount.replace(".", "", 1).isdigit():
                        print("Invalid amount. Please enter a valid number.")
                    else:
                        amount = float(amount)
                        account.deposit(amount)
                else:
                    print("Account not found.")
        elif choice == "3":
            if not logged_in:
                print("You must log in to perform this operation.")
            else:
                account_number = input("Enter account number for withdrawal: ")
                if account_number in BankAccount.accounts:
                    account = BankAccount.accounts[account_number]
                    amount = input("Enter the withdrawal amount: $")
                    if not amount.replace(".", "", 1).isdigit():
                        print("Invalid amount. Please enter a valid number.")
                    else:
                        amount = float(amount)
                        account.withdraw(amount)
                else:
                    print("Account not found.")
        elif choice == "4":
            break
        elif choice == "5":
            if logged_in:
                logout()
            else:
                login()
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    logged_in = False
    main()
