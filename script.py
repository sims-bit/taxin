net = 15000

def ni_tax(net):
    taxable_income = net - 12570
    print(f"Your taxable income is: £{taxable_income}")



if net < 12570:
    print("You don't pay any tax")
else:
    print("Tax time")
    ni_tax(net)