num=int(input("enter a Number:"))

factor=1

if (num < 0):
    print("this no is not valid")

elif (num == 0):
    print("this num fac is 1")

else:

   for i in range(1,num + 1):
    factor = factor*i
   print("the factor of",num,"is",factor) 


    
