class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_monthly_income(self, x, y):
        return x * y


item1 = Item('RentIncome', 2000, 1)
item1.calculate_total_monthly_income(item1.price, item1.quantity)
# print(item1.calculate_total_monthly_income(item1.price, item1.quantity))

item2 = Item("Laundry", 0, 0)
item2.calculate_total_monthly_income(item2.price, item2.quantity)
# print(item2.calculate_total_monthly_income(item2.price, item2.quantity))

item3 = Item("Storage", 0, 0)
item3.calculate_total_monthly_income(item3.price, item3.quantity)
# print(item3.calculate_total_monthly_income(item3.price, item3.quantity))

item4 = Item("Misc", 0, 0)
item4.calculate_total_monthly_income(item4.price, item4.quantity)
# print(item4.calculate_total_monthly_income(item4.price, item4.quantity))

print(item1.name)
print(item2.name)
print(item3.name)
print(item4.name)
print(item1.price)
print(item2.price)
print(item3.price)
print(item4.price)
print(item1.quantity)
print(item2.quantity)
print(item3.quantity)
print(item4.quantity)


class Expenses:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_monthly_expenses(self, a, b):
        return a * b

    # class Item:
    # def __init__ (self, name, price, quantity):
    #     self.name = name
    #     self.price = price
    #     self.quantity = quantity
    # def calculate_total_monthly_income(self, x, y):
    #     return x * y


expense1 = Expenses('Tax', 150, 1)
expense1.calculate_total_monthly_expenses(expense1.price, expense1.quantity)
# print(item1.calculate_total_monthly_income(item1.price, item1.quantity))

expense2 = Expenses('Insurance', 100, 1)
expense2.calculate_total_monthly_expenses(expense2.price, expense2.quantity)
# print(item2.calculate_total_monthly_income(item2.price, item2.quantity))

expense3 = Expenses('Utilities', 0, 0)
expense3.calculate_total_monthly_expenses(expense3.price, expense3.quantity)
# print(item3.calculate_total_monthly_income(item3.price, item3.quantity))

expense4 = Expenses('HOA', 0, 0)
expense4.calculate_total_monthly_expenses(expense4.price, expense4.quantity)
# print(item4.calculate_total_monthly_income(item4.price, item4.quantity))


expense5 = Expenses('Lawn/Snow', 0, 0)
expense5.calculate_total_monthly_expenses(expense5.price, expense5.quantity)
# print(item5.calculate_total_monthly_income(item5.price, item5.quantity))

expense6 = Expenses('Vacancy', 100, 1)
expense6.calculate_total_monthly_expenses(expense6.price, expense6.quantity)
# print(item6.calculate_total_monthly_income(item6.price, item6.quantity))

expense7 = Expenses('Repairs', 100, 0)
expense7.calculate_total_monthly_expenses(expense7.price, expense7.quantity)
# print(item7.calculate_total_monthly_income(item7.price, item7.quantity))

expense8 = Expenses('CapEx',0 ,0)
expense8.calculate_total_monthly_expenses(expense8.price, expense8.quantity)
# print(item8.calculate_total_monthly_income(item8.price, item8.quantity))

expense9 = Expenses("Property Manager", 200, 0)
expense9.calculate_total_monthly_expenses(expense9.price, expense9.quantity)
# print(item9.calculate_total_monthly_income(item9.price, item9.quantity))

expense10 = Expenses("Mortgage", 860, 1)
expense10.calculate_total_monthly_expenses(expense10.price, expense10.quantity)
# print(item10.calculate_total_monthly_income(item10.price, item10.quantity))

print(expense1.name)
print(expense2.name)
print(expense3.name)
print(expense4.name)
print(expense5.name)
print(expense6.name)
print(expense7.name)
print(expense8.name)
print(expense9.name)
print(expense10.name)

print(expense1.price)
print(expense2.price)
print(expense3.price)
print(expense4.price)
print(expense5.price)
print(expense6.price)
print(expense7.price)
print(expense8.price)
print(expense9.price)
print(expense10.price)

print(expense1.quantity)
print(expense2.quantity)
print(expense3.quantity)
print(expense4.quantity)
print(expense5.quantity)
print(expense6.quantity)
print(expense7.quantity)
print(expense8.quantity)
print(expense9.quantity)
print(expense10.quantity)
