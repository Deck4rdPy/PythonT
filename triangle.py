from math import sqrt

A = float(input('Enter A '))
B = float(input('Enter B '))
C = float(input('Enter C '))

if A < 0 or B < 0 or C < 0 and (A + B > C) and (A + C > B) and (B + C > A):
    print('Wrong parameters ')
    # Check the triangle inequality theorem

else:

    P = A + B + C
    p = P / 2
 #   S = (p * (p - A) * (p - B) * (p - C)) ** 0.5
    S = sqrt((p * (p - A) * (p - B) * (p - C)))

    print(f'Perimeter = {P} \nArea = {S}')
