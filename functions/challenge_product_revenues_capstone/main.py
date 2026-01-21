# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

def calculate_revenue(prices, quantities_sold):
    revenue_list = []
    for idx in range(len(prices)):
        revenue = prices[idx] * quantities_sold[idx]
        revenue_list.append(revenue)
    return revenue_list

revenue = calculate_revenue(prices, quantities_sold)
revenue_per_product = list(zip(products, revenue))

def formatted_output(revenue_per_product):
    sorted_revenue_per_product = sorted(revenue_per_product)
    for elem in sorted_revenue_per_product:
        print(f"{elem[0]} has total revenue of ${elem[1]}")

final_values = formatted_output(revenue_per_product)
    

# revenue_per_product = list(zip(products, revenue))
# sorted_revenue_per_product = sorted(revenue_per_product)
# print(sorted_revenue_per_product)
# for elem in sorted_revenue_per_product:
#     print(f"{elem[0]} has total revenue of ${elem[1]}")

# Example of expected output line (do not remove):
# print(f"{revenue[0]} has total revenue of ${revenue[1]}")