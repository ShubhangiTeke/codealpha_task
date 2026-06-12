stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400,
    "AMZN": 150
}

total_investment = 0

print("Available Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

n = int(input("\nHow many stocks do you own? "))

portfolio = {}

for i in range(n):
    stock_name = input("Enter stock name (e.g., AAPL): ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        portfolio[stock_name] = quantity
    else:
        print("Stock not found! Skipping.")

for stock, quantity in portfolio.items():
    investment = stock_prices[stock] * quantity
    total_investment += investment

print("\nPortfolio Summary:")
for stock, quantity in portfolio.items():
    print(f"{stock} - {quantity} shares × ${stock_prices[stock]} = ${stock_prices[stock] * quantity}")

print(f"\nTotal Investment Value: ${total_investment}")

with open("portfolio_summary.txt", "w") as file:
    file.write("Portfolio Summary\n")
    file.write("-----------------\n")

    for stock, quantity in portfolio.items():
        file.write(
            f"{stock} - {quantity} shares × ${stock_prices[stock]} = ${stock_prices[stock] * quantity}\n"
        )

    file.write(f"\nTotal Investment Value: ${total_investment}")

print("\nPortfolio details saved to 'portfolio_summary.txt'")