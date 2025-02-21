import pandas as pd

# Example tax data (income, deductions, tax withheld)
tax_data = {
    'Total_Income': 60000,
    'Deductions': 14200,
    'Tax_Withheld': 8000
}

# Step 1: Calculate taxable income
taxable_income = tax_data['Total_Income'] - tax_data['Deductions']

# Step 2: Define tax brackets (single filer)
brackets = [(0, 11000, 0.10), (11000, 44725, 0.12), (44725, 95375, 0.22)]

# Step 3: Calculate tax owed based on brackets
def calculate_tax(taxable_income, brackets):
    tax_owed = 0
    previous_bracket_upper = 0

    for lower, upper, rate in brackets:
        if taxable_income > upper:
            tax_owed += (upper - lower) * rate
        else:
            tax_owed += (taxable_income - previous_bracket_upper) * rate
            break
        previous_bracket_upper = upper

    return tax_owed

# Calculate tax owed
tax_owed = calculate_tax(taxable_income, brackets)

# Step 4: Calculate tax refund or due
tax_refund_or_due = tax_data['Tax_Withheld'] - tax_owed

#tax_owed, tax_refund_or_due
print ("Predicted tax owned : ", tax_owed)
print ( "Predicted tax refund or due : ", tax_refund_or_due)
