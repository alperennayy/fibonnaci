

a = int(input("fibonnaci kaçıncı terime kadar yazalım : "))
number_1 = 1
number_2 = 1

number_3 = number_1 + number_2

i = 2

print(number_1)
print(number_2)

while i<a : 
    
    number_3 = number_1 + number_2
    
    
    i=i+1
    number_1 = number_2
    number_2 = number_3
    
    print(number_3)
    
    
    
    

