# Functions in Python... 




# # Ques.   Create a function for sum two number...



# def calc_sum(a, b) :
#     sum = a+b
#     print(sum)
#     # return(sum)


# calc_sum(2,85)
# calc_sum(58, 19)









# # Ques.  WAF for print the hello world... 


# def print_hello():
#     print("Hello Prafull")
    
# print_hello()    










# # Ques.   WAF to calculate the average of 3 numbers... 


# def calc_avg(a, b, c):
    
#     sum = a+b+c
#     avg = sum/3
#     print(avg)
        
# calc_avg(257,864,489)        
# calc_avg(7,47,4)        
# calc_avg(25527,84864,44789)        
# calc_avg(25,84,48)        










# Types of function in python... 

# 1.  Built-in function (print, len, type, range)
# 2. User define Function 







# # Ques.   WAF for print the two command in the same line... 


# print("ApnaCollege", end=" ")
# print("Prafull Rajput")









# # Default Parameter... 


# def calc_prod(b, a = 45):         #  we give the default parameter then we start from the last 
#     prod = a*b
#     print(prod)
    
# calc_prod(5)   










# # WAF to print the lenght of a list... list is a parameter... 


# cities = ["Meerut", "Noida", "Delhi", "Bijnor", "Ghaziabad"]  
# heros = ["Ram", "Krishna", "Hanuman", "Shiva"]

# def print_len(list):
#     print(len(list))
  
  
# print_len(cities)    
# print_len(heros)









# # Ques. WAF to print the elemens of a list in a single line...



# cities = ["Meerut", "Noida", "Delhi", "Bijnor", "Ghaziabad"]


# print(cities[2], end = " ")
# print(cities[4])


# def print_len(list):
#     print(len(list))

# print_len(cities) 










# WAF to find the factorial of n... 


# n = int(input("Enter the number whose you want to print the factorial : ")) 

# fact = 1

# for i in range (1, n+1) :
    
#     fact = fact * i
#     print("Factorial of ", i, " =", fact)
      
      
      

# # factorial with the help of function... 


# def calc_fact(n):
#     fact = 1
#     for i in range (1, n+1):
#         fact = fact*i
#         print("Factorial of ", i, " =", fact)
        
# calc_fact(6)        
# calc_fact(7)        
# calc_fact(8)        
# calc_fact(9)        











# # Ques. WAF to convert USD to INR... 


# def converter(usd_val) :
#     inr_val = usd_val * 90.56
    
#     print(usd_val, "USD = ", inr_val, "INR")
    
# converter(75)    








# # Recursion... When a function calls itself repeatedly...


# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
    

# show(150)    
# print("END")









# # Ques. Factorial using recurion... 


# def fact(n):
#     if(n == 0 or n == 1):
#         return 1
#     else :
#         return n * fact(n-1)
    
# print(fact(5))









# # Ques.   Write a recursive function to calculate the sum of first n natural numbers... 


# def sum(n):
#      sum = 0
#      for i in range(n+1):
#          if(n == 0):
#              return 
#          else:
#              sum = sum + i
#              print("Total sum of until ",i, " =", sum)
             
# sum(9)        
         












# # Ques.  Write a recursive function to print all element in a list...



# list = ["Ghaziabad", "Meerut", "Noida", "Delhi", "Bijnor"]

# def print_list(list, idx = 0):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx+1)

# fruits = ["Mango", "Litchi", "Apple", "Banana"]    

# print_list(fruits)
















