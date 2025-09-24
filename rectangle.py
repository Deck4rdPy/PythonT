L = int(input('Enter Length '))
W = int(input('Enter Width '))
if L < 0 or W < 0:
    print('Wrong parameters ')
else:
    P = 2 * (L + W)
    S = L * W

# print('Perimeter = ', P,'\nArea = ', S)
    print(f'Perimeter = {P} \nArea = {S}')
