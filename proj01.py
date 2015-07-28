""" Program takes in debt number and currency bill. Returns height in miles of bill denomination equal to debt number and distance in miles translated to distance to moon."""

thickness = 0.0043
distance_to_moon = 238857

#Gets amount of debt and currency from user
debt = int(raw_input("Enter the amount of debt: "))
currency = int(raw_input("Enter the denomination of currency: "))

#Calculates number of bills based on denomination
num_of_bills = debt / currency

#Calculate miles of bills
miles_of_currency = (num_of_bills * thickness) * (1.0/63360)

#Calculate distance to moon
distance_in_bills = miles_of_currency / distance_to_moon

print "The debt %s has a height in miles of %s 's, %s" %(debt, currency, miles_of_currency)

print "That is %s times the average distance from the Earth to the moon." %(distance_in_bills)
