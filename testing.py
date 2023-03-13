class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity 

    def calculate_total_item_total(self, v, w):
        return v * w
       
item1 = Item('Rent Income', 2000, 0)
item1.calculate_total_item_total(item1.price, item1.quantity)
# print(item1.calculate_total_monthly_income(item1.price, item1.quantity))

item2 = Item("Laundry", 0, 0)
item2.calculate_total_item_total(item2.price, item2.quantity)
# print(item2.calculate_total_monthly_income(item2.price, item2.quantity))

item3 = Item("Storage", 0, 0)
item3.calculate_total_item_total(item3.price, item3.quantity)
# print(item3.calculate_total_monthly_income(item3.price, item3.quantity))

item4 = Item("Misc", 0, 0)
item4.calculate_total_item_total(item4.price, item4.quantity)
# print(item4.calculate_total_monthly_income(item4.price, item4.quantity))

class Expenses:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_monthly_expenses(self, a, b):
        return a * b

expense1 = Expenses('Tax', 150, 1)
expense1.calculate_total_monthly_expenses(expense1.price, expense1.quantity)
# # print(item1.calculate_total_monthly_income(item1.price, item1.quantity))

expense2 = Expenses('Insurance', 100, 1)
expense2.calculate_total_monthly_expenses(expense2.price, expense2.quantity)
# # print(item2.calculate_total_monthly_income(item2.price, item2.quantity))

expense3 = Expenses('Utilities', 0, 0)
expense3.calculate_total_monthly_expenses(expense3.price, expense3.quantity)
# # print(item3.calculate_total_monthly_income(item3.price, item3.quantity))

expense4 = Expenses('HOA', 0, 0)
expense4.calculate_total_monthly_expenses(expense4.price, expense4.quantity)
# # print(item4.calculate_total_monthly_income(item4.price, item4.quantity))

expense5 = Expenses('Lawn', 0, 0)
expense5.calculate_total_monthly_expenses(expense5.price, expense5.quantity)
# # print(item5.calculate_total_monthly_income(item5.price, item5.quantity))

expense6 = Expenses('Vacancy', 100, 1)
expense6.calculate_total_monthly_expenses(expense6.price, expense6.quantity)
# # print(item6.calculate_total_monthly_income(item6.price, item6.quantity))

expense7 = Expenses('Repairs', 100, 0)
expense7.calculate_total_monthly_expenses(expense7.price, expense7.quantity)
# # print(item7.calculate_total_monthly_income(item7.price, item7.quantity))

expense8 = Expenses('CapEx',0 ,0)
expense8.calculate_total_monthly_expenses(expense8.price, expense8.quantity)
# # print(item8.calculate_total_monthly_income(item8.price, item8.quantity))

expense9 = Expenses("Property Manager", 200, 0)
expense9.calculate_total_monthly_expenses(expense9.price, expense9.quantity)
# # print(item9.calculate_total_monthly_income(item9.price, item9.quantity))

expense10 = Expenses("Mortgage", 860, 1)
expense10.calculate_total_monthly_expenses(expense10.price, expense10.quantity)
# # print(item10.calculate_total_monthly_income(item10.price, item10.quantity))

def __add__ (self, name, total):
        return self.name + self.price * self.quantity
print(item1.name, item1.price)
def __add__ (self, name, total):
        return self.name + self.price * self.quantity
print(item2.name, item2.price)
def __add__ (self, name, total):
        return self.name + self.price * self.quantity
print(item3.name, item3.price)
def __add__ (self, name, total):
        return self.name + self.price * self.quantity
print(item4.name, item4.price)

def __add__ (self, name, total):
        return self.name + self.price * self.quantity
print(expense1.name, expense1.price)
def __add__ (self, name, total):
        return self.name + self.price * self.quantity
print(expense2.name, expense2.price)
def __add__ (self, name, total):
        return self.name + self.price * self.quantity
print(expense3.name, expense3.price)
def __add__ (self, name, total):
        return self.name + self.price * self.quantity
print(expense4.name, expense4.price)
def __add__ (self, name, total):
        return self.name + self.price * self.quantity
print(expense5.name, expense5.price)
def __add__ (self, name, total):
        return self.name + self.price * self.quantity
print(expense6.name, expense6.price)
def __add__ (self, name, total):
        return self.name + self.price * self.quantity
print(expense7.name, expense7.price)
def __add__ (self, name, total):
        return self.name + self.price * self.quantity
print(expense8.name, expense8.price)
def __add__ (self, name, total):
        return self.name + self.price * self.quantity
print(expense9.name, expense9.price)
def __add__ (self, name, total):
        return self.name + self.price * self.quantity
print(expense10.name, expense10.price)

DownPayment = 40000
ClosingCosts = 3000
RehabBudget = 7000
MiscOther = 0


def CashonCashROI(DownPayment, ClosingCosts, RehabBudget, MiscOther):
    CashonCashROI = (DownPayment+ClosingCosts+RehabBudget+MiscOther) 
    print("Cash on Cash ROI = " ,CashonCashROI)

CashonCashROI(DownPayment, ClosingCosts, RehabBudget, MiscOther)

Income = 2000 #pull from the math above
Expenses = 1610 #pull from the math above
AnnualCashFlow = 4680
Investment = 50000
Tax = 150
Insurance = 100
Utilities = 0
Electric= 0
Water = 0
Sewer = 0
Garbage = 0
Gas = 0
HOA = 0
Lawn= 0
Vacancy = 100
Repairs = 100
CapEx = 100
PropertyManager = 200
Mortgage = 860
TotalMonthlyExpenses = 1610
Tax = 150
Insurance = 100
Utilities = 0
Electric= 0
Water = 0
Sewer = 0
Garbage = 0
Gas = 0
HOA = 0
Lawn= 0
Vacancy = 100
Repairs = 100
CapEx = 100
PropertyManager = 200
Mortgage = 860
RentalIncome = 2000
Laundry = 0
Storage = 0
Misc = 0

def MonthlyCashFlow(Income, Expenses):
    MonthlyCashFlow = (Income-Expenses)
    print( "Monthly Cash Flow = " ,MonthlyCashFlow)

MonthlyCashFlow(Income,Expenses)


def CashonCashROIPercentage(AnnualCashFlow, Investment):
    CashonCashROIPercentage = (AnnualCashFlow/Investment)*100
    print("Cash on Cash ROI % = " ,CashonCashROIPercentage)

CashonCashROIPercentage(AnnualCashFlow, Investment)



def UtilitiesExpense(Electric, Water, Sewer, Garbage, Gas):
    UtilitiesExpense = (Electric+Water+Sewer+Garbage+Gas)
    print("Total Expenses = " ,UtilitiesExpense)

UtilitiesExpense(Electric, Water, Sewer, Garbage, Gas)




def MonthlyExpenses(Tax, Insurance, Utilities, HOA, Lawn, Vacancy, Repairs, CapEx, PropertyManager, Mortgage):
    MonthlyExpenses = (Tax+Insurance+Utilities+HOA+Lawn+Vacancy+Repairs+CapEx+PropertyManager+Mortgage)
    print("Monthly Expenses = " ,MonthlyExpenses)

MonthlyExpenses(Tax, Insurance, Utilities, HOA, Lawn, Vacancy, Repairs, CapEx, PropertyManager, Mortgage)



def MonthlyIncome(RentalIncome, Laundry, Storage, Misc):
    MonthlyIncome = (RentalIncome+Laundry+Storage+Misc)
    print("Monthly Income = " ,MonthlyIncome)

MonthlyIncome(RentalIncome, Laundry, Storage, Misc)