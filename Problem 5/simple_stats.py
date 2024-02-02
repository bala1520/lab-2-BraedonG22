
def simple_stats():
    Instructions = ('Provide 4 relatively small numbers. One at a time: ')
    print(Instructions)
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    ''' Type your code here. '''
    prod= num1*num2*num3*num4
    avg= (num1+num2+num3+num4)/4
    print('The product is ' f'{prod:.0f}' + ' ' + 'and the average is ' f'{avg:.0f}')
    print('The product is ' f'{prod:.3f}' + ' ' + 'and the average is ' f'{avg:.3f}')
if __name__ == "__main__":
    simple_stats()