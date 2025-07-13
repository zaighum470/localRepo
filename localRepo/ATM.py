class ATM():
    def __init__(self,balance=0):
        self.balance=balance
    def check_balance(self):
        print(f"your current balance is $:{self.balance}")
    def deposit(self,amount):
        if amount<=0:
            print("please deposit amount should be greater than 0!")
        else:
            self.balance +=amount
            print(f"${amount} has been deposited successfully!")
   
        self.check_balance()
    def withdraw(self,amount):
        if amount <=0:
            print("your withdraw amount must be greater than 0!")
        elif amount > self.balance:
            print("insufficient balance!")
        else:
            self.balance -=amount
            print(f"${amount} has been successfully withdrawn!")
        self.check_balance()
    
def main():
    atm = ATM(1000)    
    while True:
        print("\n ======ATM MENU======")
        print("1.CHECK BALANCE")    
        print("2.DEPOSIT AMOUNT")  
        print("3.WITHDRAW AMOUNT")   
        print("4.EXIT!")  
        choice =input("choose an option (1-4):")
        if choice <"1" or choice >"4":
           print("please choose an option between (1-4)")
        if choice == "1":
         atm.check_balance()
        elif choice == "2":
         amount =  float(input("enter the amount you wants to deposit:"))
         atm.deposit(amount)
         print("Thanks for using the ATM!")
        elif choice == "3":
          amount = float(input("enter the amount you wants to withdraw:"))
          atm.withdraw(amount)
          print("Thanks for using the ATM!")
        elif choice =="4":
          print("Thanks for using the ATM!")
        else:
         print("invalid optons ,please try again later!")

if __name__=="__main__":
    main()
