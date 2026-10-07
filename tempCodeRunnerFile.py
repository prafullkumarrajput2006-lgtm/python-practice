
n  = int(input("Enter the number of which you want to print the factorial : " ))  

fact = 1

for i in range(1, n+1) :
    fact *= i
    
    
    print("Factorial is : ", fact )