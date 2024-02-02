'''
Name: Braedon Gehring
Lab Time: Friday, 3:00
'''

def right_arrow():
    base_char = input("Character for arrow base: ")
    head_char = input("Character for arrow head: ")

    row1 = base_char + head_char
    row2 = base_char + base_char + head_char
    row3 = base_char + base_char + base_char + head_char


    print(row1)
    print(row2)
    print(row3)
    print(row2)
    print(row1)

if __name__ == "__main__":
    right_arrow()