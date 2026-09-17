Principal = int(input("How much money will you deposit?"))
Interest_Rate = float(input("Enter Interest Rate: "))
Compound = int(input("Enter Times Compounded: "))
Final_Balance = Principal*(1+Interest_Rate/Compound)**4
Interest = Final_Balance - Principal

print("Interest Rate: ", Interest_Rate,"%")
print("Times Compounded:", Compound)
print("Principle: $", Principal)
print("Interest: $", Interest)
print("Amount in savings: $", Final_Balance)