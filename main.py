"""Creates a Coffee machine functionality"""

from art import LOGO, OFF

def check_resources(order_ingredients):
    """Checks if there are enough resources to make choice coffee"""
    for ingredient in order_ingredients:
        if resources[ingredient] < order_ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False

    return True


def make_coffee(order_ingredients, coffee):
    """Updates the payment of resources left"""
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]
    print(f"Here is your {coffee} ☕. Enjoy!\n")


def calculate_coins(payment, drink_cost):
    """Calculates the monetary value of coins inserted,
    check if its up to the price of coffee and returns change if any"""
    global money
    if payment == drink_cost:
        money += drink_cost
    elif payment > drink_cost:
        change = payment - drink_cost
        money += drink_cost
        print(f"Here is ${round(change, 2)} in change.")
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    return True


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_active = True
print(LOGO)

while is_active:
    for item in MENU:
        print(f"{item.capitalize()}: ${MENU[item]['cost']}")

    choice = input("What would you like? ").strip().casefold()
    if choice == "off":
       is_active = False
    elif choice == "report":
        print(f"\nWater: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}\n")
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            print("\nPlease insert coins.")
            coins = int(input("how many quarters?: ")) * 0.25
            coins += int(input("how many dimes?: ")) * 0.10
            coins += int(input("how many nickels?: ")) * 0.05
            coins += int(input("how many pennies?: ")) * 0.01
            if calculate_coins(coins, drink['cost']):
                make_coffee(drink["ingredients"], choice)

print(OFF)
