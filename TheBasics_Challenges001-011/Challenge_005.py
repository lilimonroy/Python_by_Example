# ****** PYTHON BY EXAMPLE ******
# Challenge 005
# Solution by Lili Monroy
#
# Ask the user to enter three numbers. Add together the first two numbers and then multiply this total by the third. 
# Display the answer as The answer is [answer].

first_number = int(input("Please enter the first number: "))
second_number = int(input("Please enter the second number: "))
third_number = int(input("Please enter the last number: "))

total = (first_number + second_number) * third_number

print("The answer is", total)