stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 170
}

total_investment = 0

print("Available stocks:", stock_prices)
print("Type 'done' when you have finished.\n")

while True:
    stock_name = input("Enter stock name: ").upper().strip()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        stock_value = stock_prices[stock_name] * quantity
        total_investment = total_investment + stock_value

        print("Value of", stock_name, "=", stock_value)
    else:
        print("Stock not found. Please choose from the available stocks.")

print("\nTotal investment value = $", total_investment)