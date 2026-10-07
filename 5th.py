# Loops in Python... 




# 1. While loop... 


# count = 1

# while count <= 5:
#     print(f"{count}. Hello Prafull Rajput")
#     count += 1






# # Ques.   Print the numbers form 1 to 5... 


# i = 1
# while i <= 5 :
#     print(i,"Hello Ji")
#     i += 1






# # Ques Print numbers from 1 to 100... 


# i = 1
# while i <= 100 :
#     print(i)
#     i += 1







# # Ques.   WAP to print the number from 100 to 1... 


# i = 100
# while i >= 1 :
#     print(i)
#     i -= 1









# # Ques.  Print the table of any number... 


# n = int(input("Enter the number which you want to print the table : "))

# i = 1
# while i  <= 10 :
#     print(n, "*", i, "=", n*i)
#     i +=1








# # Ques.   Print the element of the following list using a loop... [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# heros = ["Ram", "Hanuman", "Krishna", "Shiva", "Thor", "Batman", "Ironman"]

# # idx = 0
# # while idx < len(heros) :
# #     print(heros[idx])
# #     idx +=1
    
    
    
# idx = 0
# while idx < len(num) :
#     print(num[idx])
#     idx +=1









# # Ques.   Print the element of the following list using a loop... [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



# i = 1
# while i <= 10 :
#     print(i ** 2)
#     i+=1
    
    






# # Ques.   Search for a number x in this tuple using loop... 



# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 36, 100)

# x = 36

# i = 0
# while i < len(num) :
#     if(num[i] == x) :
#         print("Found at index : ", i)
#     i += 1







# # Break keywords in While loop... 


# i = 1
# while i < 10 :
#     print(i)
#     if(i == 5) :
#         break
#     i += 1






# # continue keyword in while loop... 


# i = 0
# while i <= 10 :
#     if(i == 5) :
#         i+=1
#         continue
#     print(i)
#     i += 1











# # For Loops in Python... 


# num = (1, 5, 8, 9, 6, 3, 4)
# for val in num :
#     print(val)







# str = "ApnaCollege"

# for char in str :
#     print(char)
    
    
    
    
    



# str = "ApnaCollege"

# for char in str :
#     if(char == 'o') :
#         print('o found')
#         break
#     print(char)







# # Ques.   Print the element of the list... 


# num = [1, 5, 8, 9, 7, 6, 2, 5, 9, 4]

# for el in num :
#     print(el)





# # Ques.   Print the idx of the element also witht the searching element... 

# num = [1, 5, 8, 9, 7, 6, 2, 5, 9, 4]
# x = 6
# idx = 0

# for el in num :
#     if(el == x) :
#         print("Found the value at index :", idx)
#         break
#     idx += 1











# Range in for loop... 


# for i in range(10) :
#     print(i)






# for i in range(1, 10, 2) :
#     print(i)









# # Ques.   Print the table of any number ... 


# n = int(input("Enter the number of which you want to print tha table : "))

# for i in range(1,11) :
#     print(i*n)








# Pass Statement... 






# for i in range(5) :
#     pass

# if i > 5:
#     pass

# print("No need of any work")







# # Ques.  WAP to find the sum of first n natural num... 


# n = int(input("Enter the number up to which you want to find the sum : "))

# sum = 0

# for i in range(n+1) :
#     sum += i
#     print("Sum is till", i, "=", sum)






# # Ques.   Same question with the help of while loop... 

# n = int(input("Enter the number up to which you want to find the sum :"))
# sum = 0
# i = 1
# while(i <= n) :
#     sum += i
#     print(sum)
#     i += 1
    
#     print("Total sum = ", sum)

        
        
        





# # Ques. WAP to find the factorial of first n natural numbers... 



# n  = int(input("Enter the number of which you want to print the factorial : " ))  

# fact = 1

# for i in range(1, n+1) :
#     fact *= i
    
    
#     print("Factorial of", i, "=", fact )
        
        
        
    
    
    
         
        
    
# #  Ques ... Same questions with the help pf while loop...    
    

# n = int(input("Enter the number whose you want to print the factorial : "))

# fact = 1
# i = 1
# while(i <= n):
#     fact  = fact * i
#     i += 1
#     print(fact)