import menü
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            return False
    return True


def process_coins():
    print("please insert coins")
    total = int(input("how money quarters?"))*0.25
    total += int(input("how money dimes?")) * 0.1
    total += int(input("how money nickles?")) * 0.05
    total += int(input("how money pennies?")) * 0.01

    return total

def trans_successful(custom_money, drink_cost):
    if custom_money >= drink_cost:
        giveback = round((custom_money) - (drink_cost),2)
        print(f"here is change {giveback} dollars.")
        global profit
        profit += drink_cost
        return True

    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffe(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f"Here is your {drink_name} . Enjoy!")


coffee_machine_on= True

while coffee_machine_on:
    choice=input("what would you like? (espresso/latte/cappuccino) ")
    if choice=="off":
        coffee_machine_on=False

    elif choice=="report":
        print(f"water: {resources['water']} ml")
        print(f"milk: {resources['milk']} ml")
        print(f"coffee: {resources['coffee']} g")
        print(f"coffee: {resources['coffee']} g")
        print(f"Money: $ {profit}")

    else:
        drink = MENU[choice]
        if resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if trans_successful(payment, drink["cost"]):
                make_coffe(choice, drink["ingredients"])








