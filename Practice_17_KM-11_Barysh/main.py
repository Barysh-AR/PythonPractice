
from factorial.factorial import fact
from exp_root.root import root2, root3
from exp_root.exponentiation import exp2, exp3
from logarithm.logarithm import log, ln, lg

def main():
    def number_input(word):

        if word == 'fact':
            while True:
                try: 
                    n = int(input('enter the number: '))
                    if n > 0: break
                    else: print('the number must be greater than 0')
                except: print('it must be an integer')

        elif word == 'exp2' or word == 'exp3':
            while True:
                try: 
                    n = float(input('enter the number: '))
                except: print('it should be a number')
                else: break

        elif word == 'root2' or word == 'root3':
            while True:
                try:
                    n = float(input('enter the number: '))
                    if n >= 0: break
                    else: print('the number must be at least 0')
                except: print('it should be a number')

        elif word == 'ln' or word == 'lg' :
            while True:
                try:
                    n = float(input('enter the number: '))
                    if n > 0: break
                    else: print('the number must be greater than 0')
                except: print('it should be a number')

        elif word == 'log':
            n =[]
            while True:
                try:
                    a = float(input('enter the base of the logarithm: '))
                    if a > 0 and n != 0 : break
                    else: print('number must be greater than 0\nand not equal to 1')
                except: print('it should be a number')
            while True:
                try:
                    b = float(input('enter the number: '))
                    if b > 0: break
                    else: print('the number must be greater than 0')
                except: print('it should be a number')
            n += [b]
            n += [a]

        return n

    lis = '''
Name   Function
fact   factorial
root2  square root
root3  cube root
exp2   number in 2nd power
exp3   number in 3rd power
log    logarithm
ln     natural logarithm
lg     common logarithm'''
    w = True
    while w:
        print('\nEnter the name of the function you want to calculate\nif you want to know the names of the functions, enter "functions"')
        word = input()
        if word == 'functions':
            print(lis)
        else:
            w = False
            if word == 'fact': result = fact(number_input(word))
            elif word == 'root2': result = root2(number_input(word))  
            elif word == 'root3': result = root3(number_input(word))
            elif word == 'exp2': result = exp2(number_input(word))
            elif word == 'exp3': result = exp3(number_input(word))
            elif word == 'log':
                n = number_input(word)
                result = log(n[1], n[0])
            elif word == 'ln': result = ln(number_input(word))
            elif word == 'lg': result = lg(number_input(word))
            else: 
                print('you entered incorrect data')
                w = True
    print('Result of function {} = {}'.format(word ,result))

main()
