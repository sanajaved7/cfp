"""
First line: sum of the first and second number.
Second line: subtracting second number from the first
Third line: product of the first and the second number
Fourth line: the integer division of the first number by the second number, remainder from dividing the first number by the second number
"""

#gets input from user and checks if its valid
num1 = input("Enter your first number: ")

while type(num1) != int or num1 == 0:
    print "That is not a valid number."
    num1 = input("Please enter your first number: ")

num2 = input("Enter your second number: ")

while type(num2) != int or num2 == 0:
    print "That is not a valid number."
    num2 = input("Please enter your second number: ")

#calculates sum
print "The sum of %s and %s is: %s" %(num1, num2, (num1 + num2))

#calculates difference
print "The difference of %s and %s is: %s" %(num1, num2, (num1 - num2))

#multiplies number
print "The product of %s and %s is: %s" %(num1, num2, (num1 * num2))

#divides number with remainder
print "The quotient of %s and %s is: %s with remainder %s" %(num1, num2, (num1/num2), (num1%num2))
