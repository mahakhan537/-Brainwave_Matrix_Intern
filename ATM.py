class ATM:
    def __init__(self):
        self.balance = 1000  # Initial balance
        self.pin = "1234"    # Default PIN

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"You have successfully deposited ${amount}.")
            self.check_balance()
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"You have successfully withdrawn ${amount}.")
            self.check_balance()

    def change_pin(self, new_pin):
        self.pin = new_pin
        print("Your PIN has been changed successfully.")

def main():
    atm = ATM()
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        entered_pin = input("Please enter your PIN: ")
        if entered_pin == atm.pin:
            print("Access granted.")
            break
        else:
            print("Incorrect PIN. Please try again.")
            attempts += 1

    if attempts == max_attempts:
        print("Too many incorrect attempts. Access denied.")
        return

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == '4':
            new_pin = input("Enter new PIN: ")
            atm.change_pin(new_pin)
        elif choice == '5':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
    class ATM:
     def __init__(self):
        self.balance = 1000  # Initial balance
        self.pin = "1234"    # Default PIN

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"You have successfully deposited ${amount}.")
            self.check_balance()
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"You have successfully withdrawn ${amount}.")
            self.check_balance()

    def change_pin(self, new_pin):
        self.pin = new_pin
        print("Your PIN has been changed successfully.")

def main():
    atm = ATM()
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        entered_pin = input("Please enter your PIN: ")
        if entered_pin == atm.pin:
            print("Access granted.")
            break
        else:
            print("Incorrect PIN. Please try again.")
            attempts += 1

    if attempts == max_attempts:
        print("Too many incorrect attempts. Access denied.")
        return

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == '4':
            new_pin = input("Enter new PIN: ")
            atm.change_pin(new_pin)
        elif choice == '5':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()