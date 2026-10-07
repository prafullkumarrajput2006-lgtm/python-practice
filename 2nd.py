# # For changing the line...


# str1 = "This is a string.\nWe are creating in the Python"
# str2 = "Apna College"

# print(str1)









# # Concatination... Adding two or more string in a single string 



# str1 = "My name is Prafull Rajput. "
# str2 = "I'm from Rajput family"

# final_str = str1 + str2

# print(final_str)
# print(len(final_str))







# # Indexing...For gettig the specific index


# str = "Prafull Rajput"

# ch = str[0]

# print(ch)






# # Slicing... For getting the specing portion of the string or part of the string  


# str = "My name is Prafull Rajput"

# print(str[3:])
# print(str[0:7])
# print(str[-6:-2])









# String Functions 


# # 1. endwith function... 

# str = "I'm Studying Python with from Apna College"

# print(str.endswith("eged"))
# print(str.endswith("ege"))




# # 2.  capitalize function... 


# str = "i'm Studying Python with from Apna College" 

# print(str.capitalize())





# # 3. replace function... 


# str = "I'm Studying Python with from Apna College"

# # print(str.replace("o", "a"))
# print(str.replace("Python", "Java"))






# # 4.  Find function... give the starting index



# str = "I'm Studying Python with from Apna College"

# print(str.find("Python"))
# print(str.find("Java"))






# # 5. Count function...



# str = "I'm Studying Python with from Apna College"

# print(str.count("o"))







# # Ques.   WAP to input user first name and print its lenght...


# name = input("Enter the first name : ")
# print("Your name is : " + name)
# print(len(name))







# # Conditional Statement ... 


# age = int(input("Enter your age : "))

# if(age >= 18):
#    print("You can vote and drive")

# else:
#       print("You can't vote and drive")








# # Ques.  take the input from the user of the color of the traffic light and perform operation ont he basis of conditional statement... 


# color = input("Enter the color of the traffic light : ")

# if (color == "red"):
#     print("Stop")
    
# elif(color == "yellow"):
#     print("Wait")
    
# elif(color == green):
#     print("Go")

# else :
#     print("Wrong Choice")









# # Conditional Statement... 



# marks = int(input("Enter the marks of the student : "))

# if (marks >= 90):
#     print("Grade A")

# elif(marks >= 80 and marks < 90):
#     print("Grade B")

# elif(marks >= 70 and marks <80):
#     print("Grade C")

# elif(marks >= 60 and marks < 70):
#     print("Grade D")

# elif(marks >= 50 and marks < 60):
#     print("Grade E")

# else :
#     print("Fail")








# # Nesting... 

# age = int(input("Enter the age : "))

# if(age >= 18):
#     if(age >= 80):
#         print("Can't drive")
#     else:
#      print("Can drive")

# else:
#     print("Can't drive")








# # Ques.  WAP to check the given number is even or odd... 


# n = int(input("Enter the number : "))

# if (n % 2 == 0):
#     print(n, "is a even number.")

# else:
#     print(n, "is odd number")










# # Ques. WAP to find the greatest number among 3 numbers... 


# a = int(input("Enter the first number : "))
# b = int(input("Enter the second number :"))
# c = int(input("Enter the third number :"))

# if(a>b and a>c):
#     print(a, "is the greatest number, which is the value of a.")

# elif(b>a and b>c):
#     print(b, "is greatest number, which is the value of b.")

# else:
#     print(c, " is greates number, which is the value of c.")









# # Ques.  WAp to check the number is multiple of 7 or not... 


# n = int(input("Enter the number : "))  

# if(n % 7 == 0):
#     print(n, "is the multiple of 7")

# else:
#     print(n, "is not the multiple of 7")
