import csv
stock_prices = {
    "AAPL": 180.25,
    "GOOG": 2750.50,
    "MSFT": 330.75,
    "TSLA": 250.60,
    "AMZN": 140.10
}
investment=[]

print("welcome to Simple Stock Tracker!")

while True:
    print("Available stocks :",",".join(stock_prices.keys()))
    stock_name=input("Enter stock name to buy (or 'done' to finish): ").upper()
    if stock_name=='DONE':
        break
    if stock_name not in stock_prices:
        print("Stock not available. Please choose from the available stocks.")
        continue
    try:
        quantity=int(input(f"Enter quantity of {stock_name} shares: "))
    except ValueError:
        print("Invalid quantity. Please enter a number.")
        continue
    price = stock_prices[stock_name]
    total_cost = price * quantity
    investment.append((stock_name, quantity, price, total_cost))
    print(f"Added {quantity} shares of {stock_name} worth ${total_cost:.2f}")

total_investment=0

print("\nYour Investment Summary:")

for stock,qty,price,total in investment:
    print(f"{stock}: {qty} shares x price ${price} = total_cost amzn${total:.2f}")
    total_investment+=total 

print(f"\nTotal portfolio value: ${total_investment:.2f}")

if investment:
    with open("stock_investment.csv",mode="a",newline='')as file:
        write=csv.writer(file)
        write.writerow(["stock","Quantity","Price","Total Cost"])
        write.writerows(investment)
        write.writerow([])#blank row
        write.writerow(["Total Portfolio value","","",total_investment])
    print("Investment details saved to stock_investment.csv")
else:
    print("No investments made.")