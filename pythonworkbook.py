#34 

num = int(input("Pick a number, any number: "))
 
if (num % 2) == 0:
   print("{0} is Even".format(num))

else:
   print("{0} is Odd".format(num))

#39 python workbook - decibels ranking programme

decibels = int(input("Enter your decibel level: "))

if decibels < 40:
    print("more silent then a quiet room")
elif decibels == 40:
    print("quiet room")
elif decibels < 70:
    print("higher than a Quiet room, but lower than an alarm clock")
elif decibels == 70:
    print("alarm clock")
elif decibels < 106:
    print("louder than an Alarm clock, but not as bad as a pesky Gas lawnmower")
elif decibels == 106:
    print("a gas lawnmower")
elif decibels < 130:
    print("above a Gas lawnmower, less in your face - or ears -than a jackhammer")
elif decibels == 130:
    print("Jackhammer, baby")
else:
    print("louder than war")

#43 Faces on Money

note=int(input("What\'s your bank note: "))
if note ==1:
    print ("George Washington")
elif note ==2:
    print("Thomas Jefferson")
elif note ==5:
    print("Abraham Lincoln")
elif note ==10:
    print("Alexander Hamilton - The Musical")
elif note ==20:
    print("Andrew Jackson")
elif note ==50:
    print("Ulysses S. Grant - the General")
elif note ==100:
    print("Benjamin Franklin - he who loved a good bath")
else:
    print("We aint got your dollar. Good day, Good Sir")






