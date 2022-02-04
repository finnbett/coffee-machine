from menu import MENU
import operator

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,

}
money = 0
# set the machine to "on".
machine_on = True
while machine_on:
    request = input("what coffee would you like (espresso/latte/cappuccino)")
    if request == "off":
        machine_on = False
    if request == "resource":
        print(resources)
    coffee = MENU[request]
    coffee_cost = coffee["cost"]
    # check resource
    coffee_ingredients = coffee["ingredients"]
    ingredients_list = coffee_ingredients.values()
    resources_list = resources.values()
    print(f"first rousrources list{resources_list}")
    # subtracts two lists
    difference = list(map(int.__sub__, resources_list, ingredients_list))
    print(difference)
    # checks each ingredient
    has_resource = all(i >= 0 for i in difference)
    if has_resource:
        print(f"{request} is ${coffee_cost}, coins accepted: 50c, $1, $2.")
        ## TODO: count coins
        coin_total = 0
        remaining = coffee_cost
        fivety_cent = int(input("enter number of 50c coins"))
        fivety_cent_total = fivety_cent * 0.5
        coin_total += fivety_cent_total
        one_dollar = int(input("enter number one dollar coins"))
        one_dollar_total = one_dollar
        coin_total += one_dollar_total
        two_dollar = int(input("enter number of two dollar coins"))
        two_dollar_total = two_dollar * 2
        coin_total += two_dollar_total
        print(f"you have given {coin_total}")
        change = coin_total - coffee_cost
        # if coin_total == coffee_cost:
        #     ## TODO: make the coffee
    else:
        print("sorry not enough resources")

    # print (f"resources list and ingredients list{resources_list}, {ingredients_list}")

    if coffee == MENU["espresso"]:
        # check resources:

        # if coffee_ingredients["water"] > resources["water"] or
        print(coffee_ingredients)
    if coffee == MENU["latte"]:
        print(coffee)
    if coffee == MENU["cappuccino"]:
        print(coffee)
# TODO: 1. Print a report of all the coffee machine resources
# TODO: 2. create an off prompt to stop execution.
# TODO: 3. make prompt show once a coffee has been dispensed
# TODO: 4. handle the resources.
# TODO: 4.1 subtract the ingredients from the resources
# TODO: 4.2 handle the change
