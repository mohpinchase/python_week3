def calculate_discount(price, discount_percent):
    """Calculates the final price after applying a discount if it's 20% or higher."""
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price  # No discount applied

def display_price_message(original_price, discount_percentage):
    final_price = calculate_discount(original_price, discount_percentage)

    if final_price < original_price:
        print(f"A discount of {discount_percentage}% was applied.")
        print(f"The final price after discount is: ${final_price:.2f}")
    else:
        print("No discount was applied. The price remains:")
        print(f"${original_price:.2f}")

# Prompt user for input for bboth the price and discount
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Each user is given the appropriate message showing if discount was applie or not
display_price_message(original_price, discount_percentage)
