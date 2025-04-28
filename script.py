def income_tax(net):
    # Initialize variables
    personal_allowance = 12571
    basic_rate_threshold = 50270
    higher_rate_threshold = 100000
    highest_rate = 
    
    # No tax if below personal allowance
    if net <= personal_allowance:
        print("You don't pay any tax")
        return
    
    # Calculate taxable income
    taxable_income = net - personal_allowance
    
    # Calculate for each band
    # Band 1 (Basic rate): 20% on income between £12,571 and £50,270
    if net <= basic_rate_threshold:
        band_1 = taxable_income * 0.2 
        band_2 = 0
    else:
        band_1 = (basic_rate_threshold - personal_allowance) * 0.2
        
        # Band 2 (Higher rate): 40% on income between £50,270 and £100,000
        if net <= higher_rate_threshold:
            band_2 = (net - basic_rate_threshold) * 0.4
        else:
            band_2 = (higher_rate_threshold - basic_rate_threshold) * 0.4
            
    
    # Calculate total tax and take-home pay
    total_tax = band_1 + band_2
    take_home = net - total_tax

   # Display results
    print(f"Net income: £{net}")
    print(f"Taxable income: £{taxable_income}")
    print(f"Basic rate tax (20%): £{band_1:.2f}")
    print(f"Higher rate tax (40%): £{band_2:.2f}")
    print(f"Total tax: £{total_tax:.2f}")
    print(f"Take-home pay: £{take_home:.2f}")




    net = 60000
    taxable_income = net - 12571  
    print("Tax time")
    income_tax(net)



