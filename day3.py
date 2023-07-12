# Write your code here:
def get_yearly_revenue(mRev):
    return mRev*12
def get_yearly_expenses(mExp):
    return mExp*12
def get_tax_amount(pFit):
    if pFit > 100000:
        return pFit*0.25
    else:
        return pFit*0.15
def apply_tax_credits(taxAm, taxCre):
    return taxAm - taxAm*taxCre

# Don't touch anthing below this line 🙅🏻‍♂️🙅🏻‍♀️

monthly_revenue = 5500000
monthly_expenses = 2700000
tax_credits = 0.01

profit = get_yearly_revenue(monthly_revenue) - get_yearly_expenses(monthly_expenses)

tax_amount = get_tax_amount(profit)

final_tax_amount = tax_amount - apply_tax_credits(tax_amount, tax_credits)

print(f"Your tax bill is: ${final_tax_amount}")

