# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format.
# You can buy ___ apples and your change is ___ pesos.

#Step 1: get the user's amount of money then the price of an apple.
def getMoneyAndPrice():
    _money = int(input('Amount of money: '))
    _price = int(input('Price per apple: '))
    return _money, _price

money, price = getMoneyAndPrice()