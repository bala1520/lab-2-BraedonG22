
def real_estate():
    current_price = int(input('Current price of house: '))
    last_month_price = int(input('Price of house last month: '))
    # Your code goes here
    changeval = (current_price - last_month_price)
    mortgage = (current_price * 0.051) / 12
    print('This house is $' f'{current_price:.2f}' + '.' + ' ' + 'The change is $' f'{changeval:.2f}' + ' ' + 'since last month.')
    print('The estimated monthly mortgae is $' f'{mortgage:.2f}' + '.')
if __name__ == "__main__":
    real_estate()