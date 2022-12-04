from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_manager = Menu()
coffee_machine = CoffeeMaker()
money_manager = MoneyMachine()


def coffee_machine_program():
    off = False

    while not off:
        selected_item = None

        while selected_item is None or selected_item == "off" or selected_item == "report":
            input_answer = input(f"What would you like? ({menu_manager.get_items()}): ")
            if input_answer.lower() == "off":
                off = True
                break
            if input_answer.lower() == "report":
                coffee_machine.report()
                money_manager.report()
            else:
                selected_item = menu_manager.find_drink(input_answer)

        if coffee_machine.is_resource_sufficient(selected_item):
            if money_manager.make_payment(selected_item.cost):
                coffee_machine.make_coffee(selected_item)


coffee_machine_program()
