#!/usr/bin/env python3
import os
title = "This is a scientfic calculator created by firew shafi"
titlelen = len(title)
def intro():
    '''Displays intro '''
    title = "This is a scientfic calculator created by firew shafi"
    titlelen = len(title)
    print ('*'* titlelen)
    print (title)
    print ('*'* titlelen)
    print(' For the equation in the following format ax2 + bx + c, Enter "abc" without any space\n')
    print('Remember your inputs are case and chatacter sensitive')
    print ('  /\_/\ ')
    print (' ( o.o )    Happy Testing ')
    print ('  > ^ < ')  
    print ('*'* titlelen)
x = 'y'
z = True
while x == 'y' or x == 'Y':
    intro ()
    while z == True:
        equation = input ('Please, input the quadratic equation in the specified format: ')
        if (equation.isdigit()):
            z = False
        else:
            z = True
            print ('  /\_/\ ')
            print (' ( o.o ) {0:^10}'.format('Input Error, Please Enter a value as specified above'))
            print ('  > ^ < ')
    a = int(equation[0])
    b = int(equation[1])
    c = int(equation[2])
    value = ((b * b) - ((4 * a)) * c)
    if value > 0:
        sqrt = value ** (1/2)
        addup = (( -1 * b ) + value)/ (-2 * a)
        subtract = ((-1 * b) - value)/ (-2 * a)
        print ('*'* 10)
        print ('The results are  ' + '{0:3.2F} and {1:3.2F}'.format(addup, subtract))
        print ('*'* 10)
    elif value == 0:
        print ('*'* 10)
        print ('The result is ' + '{0:3.2F}'.format(addup)) 
        print ('*'* 10)
    elif value < 0:
        aa = -1 * b
        print ('The result is a complex number ' + '{0:3.2F} + {1:2.2F}C'.format(aa, value)) 
    else:
        print ('The solution to this equation is COMPLEX number\n ')
        print ('Unfortunatly my program is not yet ready to calculate complex number')
        print ('Please check back soon')
    x = input ('Would you like to perform another operation? Enter "y" for yes or any other key for no: ')
    os.sys('clear')
print ('*'* titlelen)
print (' {0:^53} '.format('Thanks for using my first program'))
print ('*'* titlelen)
