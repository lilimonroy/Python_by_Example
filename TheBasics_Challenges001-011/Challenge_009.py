
# ****** PYTHON BY EXAMPLE ******
# Challenge 009
# Solution by Lili Monroy
# Write a program that will ask for a number of days and then will show how many hours, minutes and seconds are in that number of days.

days = int(input("Please enter the number of days: "))

hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print("In",days,"days are\n",hours,"hours\n",minutes,"minutes\n",seconds,"seconds." ) 