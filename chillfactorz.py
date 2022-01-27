def factors(number):

    factor = []
    for x in range(2, number):
        
        if number % x == 0:
            factor.append(x)
    return factor
    

print(factors(206))
print(factors(36))
print(factors(505)) 
print(factors(1010)) 
print(factors(1002)) 
print(factors(2004)) 
print(factors(120012)) 
print(factors(200000000)) 