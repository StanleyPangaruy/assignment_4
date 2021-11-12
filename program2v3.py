# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount is ______.

#Step 1: set the price for apple and orange and get the number of desired apples and oranges.
def setPriceAndGetNumber():
    applePrice_ = 20
    orangePrice_ = 25
    apple_ = int(input('Number of apples (20 pesos each): '))
    orange_ = int(input('Number of oranges (25 pesos each): '))
    return applePrice_, orangePrice_, apple_, orange_

#Step 2: define the function for getting the total and to display it. 
def totalAmount(pApple,pOrange,appleF,orangeF,):
    totalApple = appleF*pApple
    totalOrange = orangeF*pOrange
    _total = totalApple + totalOrange
    if _total == 0:
        print('Come back next time for more fruits')
    elif totalApple == 0:
        print(f'Your total amount is {_total} pesos for {orangeF} orange(s).')
    elif totalOrange == 0:
        print(f'Your total amount is {_total} pesos for {appleF} apple(s).')
    else:
        print(f'Your total amount is {_total} pesos for {appleF} apple(s) and {orangeF} orange(s).')

applePrice,orangePrice,apple,orange = setPriceAndGetNumber()
totalAmount(applePrice,orangePrice,apple,orange)