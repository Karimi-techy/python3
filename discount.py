def calculate_discount(price, discount_percentage):
    if discount_percentage >= 20:
        discount_amount = price * (discount_percentage / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

input_price = float(input("Enter the price: "))
input_discount = float(input("Enter the discount percentage: "))

final_price = calculate_discount(input_price, input_discount)
print("Final price after discount:", final_price)