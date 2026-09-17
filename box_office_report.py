Movie_Name = input("What movie do you want to watch?")
Adult_Tickets_Sold = int(input("Enter number of adults"))
Child_Tickets_Sold = int(input("Enter number of children"))
Adult_Ticket = 10
Child_Ticket = 6
Gross_Box_Office_Profit = Adult_Tickets_Sold*10 + Child_Tickets_Sold*6
Net_Box_Office_Profit = Gross_Box_Office_Profit*.2
Amount_Paid_to_Distributor = Gross_Box_Office_Profit - Net_Box_Office_Profit
print("Movie Name: ", Movie_Name)
print("Adult Tickets Sold: ", Adult_Tickets_Sold)
print("Child Tickets Sold: ", Child_Tickets_Sold)
print("Gross Box Oficce Profit: $",Gross_Box_Office_Profit)
print("Net Box Office Profit: $",Net_Box_Office_Profit)
print("Amount Paid to Distributor: $",Amount_Paid_to_Distributor )