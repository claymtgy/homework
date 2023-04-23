'''
Promp user to ask what would you like
Turn off the coffee machine by entering off to the prompt
print report when user enters report
Check if resources are sufficient
process coins
check if transaction is successful
Make coffee
make it still work even if dictionary doesn't contain milk

'''

from data import MENU

# Global Variables
cont = True
water = 300 
milk = 200 
coffee = 100 
money = 0

def user_prompt():
    global cont
    user_sel = input("What would you like? (espresso/latte/cappuccino):\n")
    if user_sel.lower() == "report":
        report()
    elif user_sel.lower() == "espresso" or user_sel.lower() == "latte" or user_sel.lower() == "cappuccino":
        if res_check(user_sel):
            print("Success.")
            charge(user_sel)
    elif user_sel.lower() == "off":
        print("Device Powering Off")
        cont = False
        return
    else:
        pass

def charge(brew):
    global money
    brew_dict = MENU[brew]
    cost = brew_dict["cost"]
    print(cost)
    quarter = int(input("How many quarters?\n"))
    dime = int(input("How many dimes?\n"))
    nickel = int(input("How many nickels?\n"))
    pennies = int(input("How many pennies?\n"))
    total_charge = (quarter * .25) + (dime * .10) + (nickel * .5) + (pennies * .01)
    if total_charge > cost:
        total_change = total_charge - cost
        money += cost 
        print(f"Your change is {total_change} cents.")
        print(f"Here is your {brew}. Enjoy!")
    elif total_charge == cost:
        money += cost
        print(f"Here is your {brew}. Enjoy!")
    else:
        print("Sorry, that's not enough money. Money refunded.")

def report():
    global water
    global milk
    global coffee
    global money
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")

def res_check(brew):
    #print(MENU[brew])
    global water
    global milk
    global coffee
    global money
    brew_dict = MENU[brew]
    ingredients = brew_dict["ingredients"]
    #print(ingredients["water"])
    water1 = ingredients["water"]

    if "milk" in ingredients:
        milk1 = ingredients["milk"]
    coffee1 = ingredients["coffee"]

    if water >= water1:
        print("Enough water")
        water -= water1
        return True
    else:
        print(f"Not enough water, {water}.")
        return
    if milk >= milk1:
        print("Enough water")
        print(milk)
        print(milk1)
        milk -= milk1
        return True
    else:
        print(f"Not enough milk.")
        return
    if coffee >= coffee1:
        print("Enough coffee")
        milk -= milk1
        return True
    else:
        print(f"Not enough coffee.")
        return
    return


while cont:
    user_prompt()
