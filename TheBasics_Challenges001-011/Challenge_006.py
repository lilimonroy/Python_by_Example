# Ask how many slices of pizza the user started with and ask how many slices they have eaten.
# Work out how many slices they have left and display the answer in a user- friendly format.

total_pizza_slices = int(input("How many slices does your pizza have? "))

pizza_slices_eaten = int(input("How many slices of pizza have you eaten? "))

total_pizza_slices = total_pizza_slices - pizza_slices_eaten

print("You have",total_pizza_slices,"slices of pizza left")