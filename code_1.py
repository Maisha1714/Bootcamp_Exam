def withdraw(balance,amount):
         if amount > balance:
              return print("Insufficient balance")
         return balance - amount

try:
      balance = float(input("Enter the balance: "))
      amount = float(input("Enter the amount: "))
      updated_balance = withdraw(balance, amount)
      print(f"Updated balance: {updated_balance}")
except ValueError:
      print("Please enter a valid amount.")
