# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format.
# You can buy ___ apples and your change is ___ pesos.

#Step 1: get the user's amount of money then the price of an apple.
def getMoneyAndPrice():
    _money = int(input('Amount of money: '))
    _price = int(input('Price per apple: '))
    return _money, _price

#Step 2: define the function that computes for the max apple and change then display it. 
def maxApple(_money,_price):
    _maxApple = _money//_price
    change = _money-_maxApple*_price
    if _maxApple and change != 0:
        print(f'You can buy {_maxApple} apples and your change is {change} pesos.')
    elif _maxApple > 1 and change == 0:
        print(f'You can buy {_maxApple} apples and you have no change.')
    elif _maxApple == 1 and change == 0:
        print(f'You can buy an apple and you have no change.')
    else:
        print('You have insufficient money.')

money, price = getMoneyAndPrice()
maxApple(money,price)