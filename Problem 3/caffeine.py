
def caffeine():
    caffeine_intake = ('Please record how much caffeine you just consumed (in mg): ')
    print(caffeine_intake)
    caffeine_mg = float(input())
    ''' Type your code here. '''
    sixhrs = (caffeine_mg / 2)
    twelvehrs = (caffeine_mg / 4)
    twentyfourhrs = (caffeine_mg / 16)

    print('Caffeine in body after 6 hours' + ' ' + f'{sixhrs:.2f}'+ ' ' + 'mg')
    print('Caffeine in body after 12 hours' + ' ' + f'{twelvehrs:.2f}'+ ' ' + 'mg')
    print('Caffeine in body after 24 hours' + ' ' + f'{twentyfourhrs:.2f}' + ' ' + 'mg')
if __name__ == "__main__":
    caffeine() 