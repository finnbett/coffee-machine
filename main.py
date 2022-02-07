from menu import MENU
import operator

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,

}
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
    # subtracts two lists
    difference = list(map(int.__sub__, resources_list, ingredients_list))
    # checks each ingredient
    has_resource = all(i >= 0 for i in difference)
    if has_resource:
        print(f"{request} is ${coffee_cost}, coins accepted: 50c, $1, $2.")
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
        print(f"you have given ${coin_total}")
        change = coin_total - coffee_cost
        if change:
            print(f"{change} change")


        if coffee == MENU["espresso"]:
            resources["water"] = difference[0]
            resources["coffee"] = difference[1]
            resources["milk"] = resources["milk"]
        else:
            resources["water"] = difference[0]
            resources["milk"] = difference[1]
            resources["coffee"] = difference[2]
        #print(resources)
        print(f"enjoy your {request}")

    else:
        print("sorry not enough resources")



