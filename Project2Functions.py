def calculate_total(item_costs):
    #calculates items total from list of item costs.
    return round(sum(item_costs),2)
def calculate_discount(total, promo_code):
    #calculates discount amout based on promotion code and items total
    if promo_code == '123':
        return 1
    elif promo_code == '456':
        return 2
    elif promo_code == '789':
        return 3
    elif promo_code == '0' and total >= 100:
        return round (total * 0.1, 2)
    else:
        return 0
