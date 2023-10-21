class Bank_Account:
    accounts = {}

    def __init__(self,account_number , balance =0):
        self.account_number = account_number
        self.balance = balance
        Bank_Account.accounts[account_number] = self

    def deposit(self,amount):
        if amount >0:
            self.balance += amount
            print(f"Deposited :${amount} , Net balance :${self.balance}")
        else:
            print(f"invalid amount for depositing")

    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ${amount}, Net balance :${self.balance}")
        else:
            print(f"insufficient balance to withdraw or invalid amount")

    def get_balance_display(self):
        return self.balance

def create_account():
    while True:
        account_number = input("Enter a new account number:")
        if account_number in Bank_Account.accounts:
            print("Account already existing , try with different number")
        elif not account_number.isdigit():
            print(f"Invalid account number , give a valid account in digits")
        else:
            balance = input("initial amount :$")
            if not balance.replace(",", "", 1).isdigit():
                print(f"Enter a valid number , invalid balance")
            else:
                balance = float(balance)
                account = Bank_Account(account_number, balance)
                print(f"account {account_number} , is created with ${balance} initial balance")
                break


def main():
    bank_name = input("Enter bank name:")
    #bank = Bank_Account(bank_name)
    print(f"Welcome to {bank_name} bank")
    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Select an option: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            account_number = input("Enter your account number:")
            if account_number in Bank_Account.accounts:
                account = Bank_Account.accounts[account_number]
                amount = input("Enter amount to deposit:$")
                if not amount.replace(",","",1).isdigit():
                    print("invalid amount, enter a amount in digits")
                else:
                    amount = float(amount)
                    account.deposit(amount)
            else:
                print("Account not found")
        elif choice == "3":
            account_number = input("Enter your account number:")
            if account_number in Bank_Account.accounts:
                account = Bank_Account.accounts[account_number]
                amount = input("Enter amount to deposit:$")
                if not amount.replace(",", "", 1).isdigit():
                    print("invalid amount, enter a amount in digits")
                else:
                    amount = float(amount)
                    account.withdraw(amount)
            else:
                print("Account not found")

        elif choice == "4":
            break
        else:
            print("invalid option , try agian")

if __name__ == "__main__":
    main()