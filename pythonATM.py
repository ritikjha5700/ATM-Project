class ATM:
    def __init__(self, pin, balance = 0):
        self.__pin = pin
        self.__balance = balance
    
    def verify_pin(self, entered_pin):
        return self.__pin == entered_pin
    
    def get_balance(self):
        return self.__balance
    
    def deposite(self, amount):
        if(amount <= 0):
            raise ValueError("Amount should be greater than 0")
        
        self.__balance += amount
        return f"₹{amount} deposited successfully"
    
    def withdraw(self, amount):
        if(amount <= 0):
            raise ValueError("Amount should be greater than 0")
        if amount > self.__balance:
            raise ValueError("Insufficient fund")
        
        self.__balance -= amount
        return f"₹{amount} withdrawn successfully"
    
def run_atm():
    print("Welcome to python ATM")
    pin = input("Set your 4 digit pin: ")

    while not pin.isdigit() or len(pin)<4:
        pin = int(input("Invalid. Please enter 4 digit numeric pin"))

    user = ATM(pin)

    try:
        attempts = 3
        while attempts > 0:
            entered_pin = input("Enter your pin: ")
            if user.verify_pin(entered_pin):
                break
            else:
                attempts -= 1
                print(f"Incorrect pin. {attempts} attempt(s) left")

        else:
            print("Too many incorrect attempts. Card blocked")
            return
        
        while True:
            print("\n-- Menu --")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print('4. Exit')

            choice = int(input("Choose an option: "))

            try:

                if choice == 1:
                    print(f"Your balance is ₹{user.get_balance()}")
                elif choice == 2:
                    amt = int(input("Enter deposit amount"))
                    print(user.deposite(amt))
                elif choice == 3:
                    amt = int(input("Enter withdrawl amount"))
                    print(user.withdraw(amt))
                elif choice == 4:
                    print("Thank you for using python ATM")
                else:
                    print("Invalid input")

            except ValueError as ve:
                print(f"Error: {ve}")
            except Exception as e:
                print(f"Unexpected error: {e}")

    except KeyboardInterrupt:
        print("\nSession cancelled.")

run_atm()


        
