number=int(input('Enter a number:'))
for i in range(2,int(number/2)+1) :
    if number % i ==0 :
        print('The number IS NOT PRIME')
        break
else :
    print('The number IS PRIME')