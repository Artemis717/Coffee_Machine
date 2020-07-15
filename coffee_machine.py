# Coffee Machine program that will let you buy, fill, take money out, as well
# as give you options to see the remaining resources and exit the program.

water = 400
milk = 540
beans = 120
cups = 9
money = 550


def buy_coffee():
      drink = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, "
                        "3 - cappuccino, back - to main menu:\n")
      if drink == "1":
            make_espresso()
      elif drink == "2":
            make_latte()
      elif drink == "3":
            make_cappuccino()
      elif drink == "back":
            return
      else:
            print("invalid entry")


def make_espresso():
      global water, beans, cups, money

      if water < 250:
            print("Sorry, not enough water!")
      elif beans < 16:
            print("Sorry, not enough coffee beans!")
      elif cups < 1:
            print("Sorry, not enough disposable cups!")
      else:
            print("I have enough resources, making you a coffee!")

            water -= 250
            beans -= 16
            cups -= 1
            money += 4

      return


def make_latte():
      global water, milk, beans, cups, money

      if water < 350:
            print("Sorry, not enough water!")
      elif milk < 75:
            print("Sorry, not enough milk!")
      elif beans < 20:
            print("Sorry, not enough coffee beans!")
      elif cups < 1:
            print("Sorry, not enough disposable cups!")
      else:
            print("I have enough resources, making you a coffee!")

            water -= 350
            milk-= 75
            beans -= 20
            cups -= 1
            money += 7

      return


def make_cappuccino():
      global water, milk, beans, cups, money

      if water < 200:
            print("Sorry, not enough water!")
      elif milk < 100:
            print("Sorry, not enough milk!")
      elif beans < 12:
            print("Sorry, not enough coffee beans!")
      elif cups < 1:
            print("Sorry, not enough disposable cups!")
      else:
            print("I have enough resources, making you a coffee!")

            water -= 200
            milk -= 100
            beans -= 12
            cups -= 1
            money += 6

      return


def fill_machine():
      global water, milk, beans, cups

      fill_water = int(input("\nWrite how many ml of water do you want to add:\n"))
      fill_milk = int(input("Write how many ml of milk do you want to add:\n"))
      fill_beans = int(input("Write how many grams of coffee beans do you want to add:\n"))
      fill_cups = int(input("Write how many disposable cups of coffee do you want to add:\n"))

      water += fill_water
      milk += fill_milk
      beans += fill_beans
      cups += fill_cups

      return


def take_money():
      global money
      print(f"I gave you ${money}\n")
      money = 0
      return


def remaining():
      print(f"\nThe coffee machine has:\n"
            f"{water} of water\n"
            f"{milk} of milk\n"
            f"{beans} of coffee beans\n"
            f"{cups} of disposable cups\n"
            f"{money} of money")
      return


while True:
      action = input("\nWrite action (buy, fill, take, remaining, exit):\n")

      if action == "buy":
            buy_coffee()
      elif action == "fill":
            fill_machine()
      elif action == "take":
            take_money()
      elif action == "remaining":
            remaining()
      elif action == "exit":
            break
      else:
            print("invalid entry, try again")

