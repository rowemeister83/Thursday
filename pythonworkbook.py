#34 

num = int(input("Pick a number, any number: "))
 
if (num % 2) == 0:
   print("{0} is Even".format(num))

else:
   print("{0} is Odd".format(num))

#39 python workbook - decibels ranking programme

decibels = int(input('Enter number of decibels: '))

if decibels < 40:
    print('even less than a quiet room')
elif decibels == 40:
    print('quiet room')
elif decibels < 70:
    print('higher than a Quiet room, but lower than an alarm clock')
elif decibels == 70:
    print('alarm clock')
elif decibels < 106:
    print('louder than an Alarm clock, less than a Gas lawnmower')
elif decibels == 106:
    print('a gas lawnmower')
elif decibels < 130:
    print('above a Gas lawnmower, quieter than a jackhammer')
elif decibels == 130:
    print('Jackhammer')
else:
    print('even louder than a jackhammer')



