#Elliott Corker
#2/24/25

budget=float(input("Enter your budget: 1200"))
destination=input("Enter your travel destination: Nashville")
gas_expense=float(input("How much do you think you will spend on gas? 250"))
accommodation_expense=float(input("Approximately, how much will you need for accommodation/hotel? 600"))
food_expense=float(input("Last, how much do you need for food? 300"))
total_expenses=gas_expense+accommodation_expense+food_expense
remaining_balance=budget-total_expenses
print("\n-=Travel Expenses=-")
print(f"Location:{destination}")
print(f"Initial Budget:{budget}")
print(f"Fuel:{gas_expense}")
print(f"Accommodation:{accommodation_expense}")
print(f"Food:{food_expense}")
print(f"Remaining Balance:{remaining_balance}")
