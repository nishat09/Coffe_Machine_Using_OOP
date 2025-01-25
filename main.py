from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


#Menu Items+Cost+Making Process
menu=Menu()

#Coffee_Machine

coffee_machine=CoffeeMaker()

#MoneyMachine
money_handler=MoneyMachine()





while True:
    user_input=input(f"What would you like? ({menu.get_items()}):")
    if user_input=='report':
        coffee_machine.report()

    elif user_input=='off':
        break


    else:
        item_availibility=menu.find_drink(user_input)

        if item_availibility==None:
            continue
        else:
            resource_check=coffee_machine.is_resource_sufficient(item_availibility)
            if resource_check==False:
                continue
            else:
                transaction=money_handler.make_payment(item_availibility.cost)
                if transaction==True:
                    coffee_machine.make_coffee(item_availibility)

                else:
                    continue

















