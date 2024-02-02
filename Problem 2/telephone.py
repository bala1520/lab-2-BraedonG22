def telephone():
    phone_number = int(input('Write phone number (10-digits, no spaces): '))
    ''' Type your code here. '''
    part1 = phone_number // 10000000
    part2 = phone_number % 10000000 // 10000
    part3 = phone_number % 10000

    print(part1,part2,-part3) 
if __name__ == "__main__":
    telephone()