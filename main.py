#Shopping cart Programm

foods = []
prices = []
total = 0


while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the prices of a {food}: $"))
        foods.append(food)
        prices.append(price)


print("-----YOUR CARD-----")

for food in foods:
    print(food)


for price in prices:
    total+= price


print(f"Your total is: ${total}")