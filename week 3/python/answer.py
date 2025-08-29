# Function to calculate discounted price
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # Apply discount only if 20% or higher
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price  # No discount applied


# Prompt user for input, to take in a float value
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Call function
    final_price = calculate_discount(original_price, discount_percent)

    # Output result
    if discount_percent >= 20:
        print(f"Discount applied! Final price: {final_price:.2f}")
    else:
        print(f"No discount applied. Price remains: {final_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values.")
