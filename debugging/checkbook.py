#!/usr/bin/python3
class Checkbook:
    """
    Function Description:
    Represents a simple checkbook system that allows deposits,
    withdrawals, and balance inquiries.

    Parameters:
    None

    Returns:
    None
    """

    def __init__(self):
        """
        Function Description:
        Initializes a Checkbook instance with a starting balance of zero.

        Parameters:
        None

        Returns:
        None
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Function Description:
        Adds a specified amount to the current balance.

        Parameters:
        amount (float): The amount of money to deposit.

        Returns:
        None
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Function Description:
        Withdraws a specified amount from the balance if sufficient funds exist.

        Parameters:
        amount (float): The amount of money to withdraw.

        Returns:
        None
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Function Description:
        Displays the current account balance.

        Parameters:
        None

        Returns:
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Function Description:
    Runs the main program loop, allowing the user to interact
    with the checkbook through text-based commands.

    Parameters:
    None

    Returns:
    None
    """
    cb = Checkbook()

    while True:
        action = input(
            "What would you like to do? (deposit, withdraw, balance, exit): "
        ).lower()

        if action == 'exit':
            break

        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif action == 'balance':
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
