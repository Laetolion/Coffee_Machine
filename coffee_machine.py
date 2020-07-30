# Write your code here
water_status = 400
milk_status = 540
coffee_status = 120
cups_status = 9
money_status = 550
State = True
def current_status(water_status, milk_status, coffee_status, cups_status, money_status):
    print("The coffee machine has:")
    print(water_status, "of water")
    print(milk_status, "of milk")
    print(coffee_status, "of coffee beans")
    print(cups_status, "of disposable cups")
    print(money_status, "of money")

def action_inputter():
    print("Write action (buy, fill, take, remaining, exit):")
    action_recieved = input()
    return action_recieved

def buy_menu():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappucino, back - to main menu:")
    coffee_type = input()
    return coffee_type

def espresso():
    global water_status
    water_status -= 250
    global coffee_status
    coffee_status -= 16
    global cups_status
    cups_status -= 1
    global money_status
    money_status += 4
    return

def latte():
    global water_status
    water_status -= 350
    global milk_status
    milk_status -= 75
    global coffee_status
    coffee_status -= 20
    global cups_status
    cups_status -= 1
    global money_status
    money_status += 7
    return

def cappuccino():
    global water_status
    water_status -= 200
    global milk_status
    milk_status -= 100
    global coffee_status
    coffee_status -= 12
    global cups_status
    cups_status -= 1
    global money_status
    money_status += 6
    return

def fill_menu():
    water_added = int(input("Write how many ml of water do you want to add:"))
    milk_added = int(input("Write how many ml of milk do you want to add:"))
    coffee_added = int(input("Write how many grams of coffee beans do you want to add:"))
    cups_added = int(input("Write how many disposable cups of coffee do you want to add:"))
    global water_status
    water_status += water_added
    global milk_status
    milk_status += milk_added
    global coffee_status
    coffee_status += coffee_added
    global cups_status
    cups_status += cups_added
    return

def take_menu():
    global money_status
    print("I gave you", money_status)
    money_status = 0
    return

def main():
    global State
    while State:
        while True:
                action_to_do = action_inputter()
                if action_to_do == "buy":
                    coffee_type = buy_menu()
                    if coffee_type == "2":
                        if coffee_status >= 20 and water_status >= 350 and cups_status >= 1 and milk_status >= 75:
                            latte()
                            print("I have enough resources, making you a coffee!")
                        elif coffee_status < 20:
                            print("Sorry, not enough coffee!")
                        elif water_status < 350:
                            print("Sorry, not enough water!")
                        elif cups_status < 1:
                            print("Sorry, not enough cups")
                        else:
                            print("Sorry, not enough milk")
                    elif coffee_type == "1":
                         if coffee_status >= 16 and water_status >= 250 and cups_status >= 1:
                            espresso()
                            print("I have enough resources, making you a coffee!")
                         elif coffee_status < 16:
                            print("Sorry, not enough coffee!")
                         elif water_status < 250:
                            print("Sorry, not enough water!")
                         else:
                            print("Sorry, not enough cups")
                    elif coffee_type == "3":
                        if coffee_status >= 12 and water_status >= 200 and cups_status >= 1 and milk_status >= 200:
                            cappuccino()
                            print("I have enough resources, making you a coffee!")
                        elif coffee_status < 12:
                            print("Sorry, not enough coffee!")
                        elif water_status < 200:
                            print("Sorry, not enough water!")
                        elif cups_status < 1:
                            print("Sorry, not enough cups")
                        else:
                            print("Sorry, not enough milk")
                    else:
                        break
                elif action_to_do == "fill":
                    fill_menu()
                elif action_to_do == "remaining":
                    current_status(water_status, milk_status, coffee_status, cups_status, money_status)
                elif action_to_do == "take":
                    take_menu()
                else:
                    State = False
                    break
main()
