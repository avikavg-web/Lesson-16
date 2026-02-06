def total_calc(bill, perc):
    total = bill*(1 + 0.01*perc)
    total = round(total,2)
    print("Your total is", total)

total_calc(150,20)
    