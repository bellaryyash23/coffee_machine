from data import MENU, resources


def change_calculator(price, qcoin, dcoin, ncoin, pcoin):
    entered_amt = (0.25*qcoin + 0.1*dcoin + 0.05*ncoin + 0.01*pcoin)
    change = round(entered_amt - price, 2)
    if change < 0:
        print("\nSorry that's not enough money. Money refunded.")
        return 0
    else:
        print(f"\nHere is ${change} in change.")
        return 1


def resource_calculator(drink):
    req_water = MENU[drink]["ingredients"]["water"]
    req_milk = MENU[drink]["ingredients"]["milk"]
    req_coffee = MENU[drink]["ingredients"]["coffee"]
    avl_water = resources["water"]
    avl_milk = resources["milk"]
    avl_coffee = resources["coffee"]
    resources["water"] = avl_water - req_water
    resources["milk"] = avl_milk - req_milk
    resources["coffee"] = avl_coffee - req_coffee
    return resources


def resource_check(drink):
    req_water = MENU[drink]["ingredients"]["water"]
    req_milk = MENU[drink]["ingredients"]["milk"]
    req_coffee = MENU[drink]["ingredients"]["coffee"]
    avl_water = resources["water"]
    avl_milk = resources["milk"]
    avl_coffee = resources["coffee"]
    if req_water > avl_water:
        print("Sorry there is not enough water.")
        return 0
    elif req_milk > avl_milk:
        print("Sorry there is not enough milk.")
        return 0
    elif req_coffee > avl_coffee:
        print("Sorry there is not enough coffee.")
        return 0
    else:
        return 1


def coffee_machine():
    machine_on = True
    while machine_on:
        drink_type = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
        if drink_type == "off":
            print("Machine in maintenance mode.")
            machine_on = False
        if drink_type == "report":
            water = resources["water"]
            milk = resources["milk"]
            coffee = resources["coffee"]
            money = resources["money"]
            print(f"Water: {water}ml.")
            print(f"Milk: {milk}ml")
            print(f"Coffee: {coffee}gm")
            print(f"Money: ${money}")
        if drink_type in MENU and resource_check(drink_type):
            drink_amt = float(MENU[drink_type]["cost"])
            print(f"Your drink costs ${drink_amt}, Please insert coins: ")
            qt_coins = int(input("How many quarters: "))
            dm_coins = int(input("How many dimes: "))
            ni_coins = int(input("How many nickles: "))
            pn_coins = int(input("How many pennies: "))
            resource_calculator(drink_type)
            if change_calculator(drink_amt, qt_coins, dm_coins, ni_coins, pn_coins):
                resources["money"] = drink_amt
                print(f"\nHere is your {drink_type} ☕. Enjoy !")
            machine_again = input("\nWant some more beverage? Type 'Y' to continue or 'N' to end: ").lower()
            if machine_again == "y":
                coffee_machine()
            else:
                print("Come again for more beverage!")
                machine_on = False


on = input("Type 'ON' to start the machine: ").lower()
if on == "on":
    coffee_machine()
