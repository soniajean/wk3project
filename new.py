# Income = 
# RentalIncome =
# Laundry =
# Storage = 
# Misc = 
# TotalMonthlyIncome=
# Expenses =
Tax = 
Insurance =
Utilities = 
Electric=
Water =
Sewer =
Garbage =
Gas =
HOA =
Lawn/Snow=
Vacancy =
Repairs =
CapEx =
PropertyManager
Mortgage
TotalMonthlyExpenses

# CashFlow=
# TotalMonthlyCashflow

# CashonCashROI
# DownPayment
# CLosingCosts
# RehabBudget
# MiscOther
# TotalInvestment
# AnnualCashFlow
# TotalInvestment
# CashonCashROI

# def ROI(Investment, Rent):

Investment = 40000
Rent = 700
Loss = 1000

def ROI(Investment, Rent, Loss):
    NetProfit = Rent * 12 - Loss
    ROI = (NetProfit/Investment) *100
    print(ROI)

ROI(Investment, Rent, Loss)