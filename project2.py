import Project2Functions
while True:
    print('Department Store Sales Tax and Grand Total Application\n')
#Get cost of items
    item_costs=[]
    while True:
        cost= float(input('Cost of item: '))
        if cost == 0:
            break
    item_costs.append(cost)
    #calculate item total
    total = Project2Functions.calculate_total(item_costs)
    print(f'All items total: ${total: .2f}')
    #Get sales tax rate
    while True:
        tax_rate=float(input('Sales tax rate (%):'))
        if 6 <=tax_rate <=10:
            break
        else:
            print('Tax rate should be from 6 to 10')
        #Get promo code
            while True:
                promo_code = input('Promotion code: ')
                if promo_code in['123', '456','789', '0']:
                    break
                else:
                    print('Invalid promotion code. Try again')
                    #calculate discount amount
                    discount_amount=Project2Functions.calculate_discount(total, promo_code)
                    print(f'Discount amount: ${discount_amount: .2f}')
                    #calculate subtotal, sales tax amount, and grand total
                    subtotal = total - discount_amount
                    sales_tax = subtotal * (tax_rate/100)
                    grand_total = subtotal + sales_tax
                    
                    #print results
                    print(f'Subtotal: ${subtotal: .2f}')
                    print(f'Sales tax amount: ${sales_tax: .2f}')
                    print(f'Grand total: ${grand_total: .2f}')
                    
                    #check if continuing
                    choice = input('\nContinue? y/Y/n/N: ')
                    if choice.lower() == 'n':
                        break
                    print('\nProgram is terminated')
        
                    