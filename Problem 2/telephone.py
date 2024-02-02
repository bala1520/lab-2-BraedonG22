def telephone():
    phone_number = int(input('Write phone number (10-digits, no spaces): '))
    ''' Type your code here. '''
    area_code = ([phone_number // 10000000])
    prefix = (phone_number % 10000000 // 10000)
    line_number = (phone_number % 10000)*-1
    
    print(area_code,prefix,line_number)
if __name__ == "__main__":
    telephone()