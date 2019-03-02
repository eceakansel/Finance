#Assets
#Current Assets
cash = int(input("enter cash here"))
ar = int(input("enter accounts receivable here"))
inv = int(input("enter inventory here"))
preprent = int(input("enter prepaid rent here"))
totalca = cash + ar + inv + preprent
print("total current assets is", totalca)
#Long term assets
land = int(input("enter land here"))
buildingandimp = int(input("enter building and improvements here"))
furnitureandfixtures = int(input("enter furniture and fixtures here"))
generaleq = int(input("enter general equipment here"))
totalfixedassets = land + buildingandimp + furnitureandfixtures + generaleq
print("total fixed assets is ", totalfixedassets)
totalassets = totalca + totalfixedassets
print("total assets is", totalassets)

#LIABILITIES
#Current Liabilities
ap = int(input("enter accounts payables here"))
tax = int(input("enter taxes payables here"))
salaries = int(input("enter salaries wages payable here"))
interest = int(input("enter interest payable here"))
tcl = ap + tax + salaries + interest
print("total current liabilities is", tcl)
#Lt liabilities
loan = int(input("enter long term liabilities here"))
totalliab = loan + tcl
print("total liabilities is", totalliab)
#owners eq
paidincap = int(input("enter paid in capital here"))
ret = int(input("enter retained earnings here"))
totalownerseq = paidincap + ret
print("total owners equity is", totalownerseq)
totalliabequ = totalownerseq + totalliab
print("total liabilities and owners equity is", totalliabequ, "total assets is", totalassets)