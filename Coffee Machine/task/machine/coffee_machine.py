class CoffeeMachine:
    def __init__(self):
        self.money = 550
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9

    def make_espresso(self):
        if self.water > 249:
            if self.beans > 15:
                if self.cups > 0:
                    self.money += 4
                    self.cups -= 1
                    self.water -= 250
                    self.beans -= 16
                    print("I have enough resources, making you a coffee!")
                else:
                    print("Sorry, not enough disposable cups")
            else:
                print("Sorry, not enough coffee beans")
        else:
            print("Sorry, not enough water")
        return

    def make_latte(self):
        if self.water > 349:
            if self.milk > 74:
                if self.beans > 19:
                    if self.cups > 0:
                        self.money += 7
                        self.cups -= 1
                        self.water -= 350
                        self.beans -= 20
                        self.milk -= 75
                        print("I have enough resources, making you a coffee!")
                    else:
                        print("Sorry, not enough disposable cups")
                else:
                    print("Sorry, not enough coffee beans")
            else:
                print("Sorry, not enough milk")
        else:
            print("Sorry, not enough water")
        return

    def make_cappuccino(self):
        if self.water > 199:
            if self.milk > 99:
                if self.beans > 11:
                    if self.cups > 0:
                        self.money += 6
                        self.cups -= 1
                        self.water -= 200
                        self.beans -= 12
                        self.milk -= 100
                        print("I have enough resources, making you a coffee!")
                    else:
                        print("Sorry, not enough disposable cups")
                else:
                    print("Sorry, not enough coffee beans")
            else:
                print("Sorry, not enough milk")
        else:
            print("Sorry, not enough water")
        return

    def buy(self):
        print()
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        choice = (input("> ").strip())
        if choice == "back":
            self.action()
        else:
            choice = int(choice)
            if choice == 1:
                self.make_espresso()
            elif choice == 2:
                self.make_latte()
            elif choice == 3:
                self.make_cappuccino()
        return

    def take(self):
        print()
        print("I gave you $" + str(self.money))
        self.money = 0

    def fill(self):
        print()
        print("Write how many ml of water do you want to add:")
        self.water += int(input("> ").strip())
        print("Write how many ml of milk do you want to add:")
        self.milk += int(input("> ").strip())
        print("Write how many grams of coffee beans do you want to add:")
        self.beans += int(input("> ").strip())
        print("Write how many disposable cups of coffee do you want to add:")
        self.cups += int(input("> ").strip())
        return

    def action(self):
        print()
        print("Write action (buy, fill, take, remaining, exit):")
        choice = input("> ").strip()
        if choice == "buy":
            self.buy()
        elif choice == "fill":
            self.fill()
        elif choice == "take":
            self.take()
        elif choice == "remaining":
            self.machine_status()
        elif choice == "exit":
            exit()
        return

    def machine_status(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.beans, "of coffee beans")
        print(self.cups, "of disposable cups")
        print("$" + str(self.money), "of money")
        return


machine = CoffeeMachine()
while True:
    machine.action()
