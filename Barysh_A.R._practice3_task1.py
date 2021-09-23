#Блок вводу данних
name = input("Enter the recipient's name: ")
surname = input("Enter the recipient's suname: ")
print("Enter the recipient's phone number: ")
print('you must enter 10 digits')
print('__________')
phone_number = input()
phone_number_1 = int(phone_number)
print
if (phone_number_1 > 0) and (phone_number_1 < 10000000000):
    phone_number = str(phone_number_1)
else:
    print('You entered the wrong data')
street_name = input("Enter the recipient's street name: ")
house_number = input("Enter the recipient's house number")
house_number_1 = int(house_number)
if (house_number_1 > 0):
    house_number = str(house_number_1)
else:
    print('You entered the wrong data')
apartment_number = input("Enter recipient's apartment number: ")
apartment_number_1 = int(apartment_number)
if (apartment_number_1 > 0):
    apartment_number = str(apartment_number_1)
else:
    print('You entered the wrong data')
city = input('Enter the city where the recipient lives: ')
print("Enter the recipient's index: ")
print("you must enter 4 digits")
print('____')
index = input()
index_1 = int(index)
if (index_1 > 0) and (index_1 < 10000) :
    index = str(index_1)
else:
    print('You entered the wrong data')
country = input("Enter the country where the recipient lives: ")
#Блок виводу данних
print()
print(name + ' ' + surname)
print(phone_number)
print('St. ' + street_name + ' ' + house_number + ', ap. ' + apartment_number + ', ' + city)
print(index)
print(country)
print()