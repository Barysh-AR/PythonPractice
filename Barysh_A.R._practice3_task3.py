age = float(input('Enter the age of the dog in calendar years: '))
if (age > 0) and (age <= 2):
    dog_age = age * 10.5
    print('The dog is ' + str(dog_age) +' years old, by dog ​​standards')
elif (age > 2):
    dog_age = 21 + (age - 2) * 4
    print('The dog is ' + str(dog_age) +' years old, by dog ​​standards')
else:
    print('You entered the wrong data')