from math import sqrt

A = float(input('Enter A: '))
B = float(input('Enter B: '))
C = float(input('Enter C: '))

# Check for negative or zero values
if A <= 0 or B <= 0 or C <= 0:
    print('Wrong parameters: sides must be positive numbers.')
else:
    # Check the triangle inequality theorem
    if (A + B > C) and (A + C > B) and (B + C > A):
        P = A + B + C
        p = P / 2
        S = sqrt(p * (p - A) * (p - B) * (p - C))
        print(f'Perimeter = {P}')
        print(f'Area = {S}')
    else:
        print('Such a triangle does not exist.')
