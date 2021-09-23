print()
magnitude = float(input('Enter the magnitude value: '))
if magnitude > 0 :
    print()
    if magnitude < 2:
        print("It's Micro earthquake")
    elif magnitude < 3:
        print("It's Very minor earthquake")
    elif magnitude < 4:
        print("It's Minor earthquake")
    elif magnitude < 5:
        print("It's Light earthquake")
    elif magnitude < 6:
        print("It's Moderate earthquake")
    elif magnitude < 7:
        print("It's Strong earthquake")
    elif magnitude < 8:
        print("It's Major earthquake")
    elif magnitude < 10:
        print("It's Great earthquake")
    else:
        print("It's Meteoric earthquake")
    print()
else:
    print('You entered the wrong data')