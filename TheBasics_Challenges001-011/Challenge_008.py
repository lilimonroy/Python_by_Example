# ****** PYTHON BY EXAMPLE ******
# Challenge 008
# Solution by Lili Monroy
#
# Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by the number of diners and show how much each person must pay.

total_bill = int(input("How much was the total bill? "))

total_dinners = int(input("How many dinners were there? "))

total_each_person = total_bill/total_dinners

print("Each person must pay",total_each_person)
