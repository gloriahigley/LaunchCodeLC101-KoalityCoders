print("STUDIO 2\n")
#Print the welcome message.
print('''Welcome to the Loop Hole!
Today's Manager's Special is:
Existential Crisis: A hard, crunchy husk of a donut with absolutely no filling or substance whatsoever,
mirroring the absence of life in the consumer.''')
#Ask for how many they would like. Since they can ask for fractional quantities, use a float.
donut_quantity=float(input("How many would you like? "))

#Ask how much they are willing to pay. Since they can provide fractional prices, use a float.
donut_price=float(input("How much would you like to pay per donut (suggested price is $0.10)? "))

#Multiply the quantity by the price.
donut_preTax_total=donut_quantity*donut_price

#Print out the amount they owe after tax.
print("Okay, let me prepare that for you....")
print("After tax, your total is: $" + str(float(donut_preTax_total + (donut_preTax_total*.05))))
print("Thank you for snacking! Loop back around here soon!")
