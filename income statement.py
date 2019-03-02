revenue = int(input("enter revenue here"))
cogs = int(input("enter cost of goods sold here"))
grossprofit = revenue - cogs
print("gross profit is", grossprofit)
sellingexpenses = int(input("enter selling expenses here"))
administrativeexpenses = int(input("enter administrative expenses here"))
totalopexpenses = sellingexpenses + administrativeexpenses
print("total operating expenses are", totalopexpenses)
operatingincome = grossprofit - totalopexpenses
print("operating income is", operatingincome)
interestexpense = int(input("enter interest expense here"))
incomebeforetaxes = operatingincome - interestexpense
print("income before taxes is", incomebeforetaxes)
tax = int(input("enter tax expense here"))
netincomeaftertaxes = incomebeforetaxes - tax
print("net income after taxes is", netincomeaftertaxes)
shares = int(input("enter shares outstanding here"))
eps = netincomeaftertaxes / shares
print("EPS is", eps)