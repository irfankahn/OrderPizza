# In this program we will print out the final bill for a pizza ordered

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
# write your code below

# Declaring constants
Small_pizza = 15
Medium_pizza = 20
Large_pizza = 25
Pepperoni_Spizza = 2
Pepperoni_Mpizza = 3
Pepperoni_Lpizza = 3
Extra_Cheese = 1

# (1) For small Pizza with extra cheese and pepperoni
if size == "S" and add_pepperoni == "Y" and extra_cheese == "Y":
    print(f"Your final bill is ${Small_pizza + Pepperoni_Spizza + Extra_Cheese }")

# (2) For small pizza with No extra cheese and no pepperoni
elif size == "S" and add_pepperoni == "N" and extra_cheese == "N":
    print(f"Your total bill is ${Small_pizza}")

# (3) For small pizza with extra pepperoni but No extra cheese
elif size == "S" and add_pepperoni == "Y" and extra_cheese == "N":
    print(f"Your total bill is ${Small_pizza + Pepperoni_Spizza}")

# (4) For small pizza with No pepperoni but Extra Cheese
elif size == "S" and add_pepperoni == "N" and extra_cheese == "Y":
    print(f"Your total bill is ${Small_pizza + Extra_Cheese}")

# (1) For Medium pizza with extra cheese and pepperoni
elif size == "M" and add_pepperoni == "Y" and extra_cheese == "Y":
    print(f"Your final bill is ${Medium_pizza + Pepperoni_Mpizza + Extra_Cheese }")

# (2) For Medium pizza with extra pepperoni but No extra cheese
elif size == "M" and add_pepperoni == "Y" and extra_cheese == "N":
    print(f"Your final bill is ${Medium_pizza + Pepperoni_Mpizza}")

# (3) For Medium pizza with no pepperoni and extra cheese
elif size == "M" and add_pepperoni == "N" and extra_cheese == "Y":
    print(f"Your total bill is ${Medium_pizza + Extra_Cheese}")

# (4) For medium pizza with no pepperoni and no extra cheese
elif size == "M" and add_pepperoni == "N" and extra_cheese == "N":
    print(f"Your total bill is ${Medium_pizza}")

# (1) For Large pizza with pepperoni and extra cheese
elif size == "L" and add_pepperoni == "Y" and extra_cheese == "Y":
    print(f"Your total bill is ${Large_pizza + Pepperoni_Lpizza + Extra_Cheese}")

# (2) For Large pizza with No pepperoni and No extra cheese
elif size == "L" and add_pepperoni == "N" and extra_cheese == "N":
    print(f"Your total bill is ${Large_pizza}")

# (3) For Large pizza with pepperoni but no extra cheese
elif size == "L" and add_pepperoni == "Y" and extra_cheese == "N":
    print(f"Your total bill is ${Large_pizza + Pepperoni_Lpizza}")

# (4) For Large pizza with No pepperoni but extra cheese
elif size == "L" and add_pepperoni == "N" and extra_cheese == "Y":
    print(f"Your total bill is ${Large_pizza + Extra_Cheese}")

else:
    print("Invalid Entry! Please select from the given optioins")







