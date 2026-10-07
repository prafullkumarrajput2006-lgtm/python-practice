# # Dictionary in Python... 

 
# info = {
#     "name " : "Prafull Rajput",
#     "Age" : 20,
#     "clg " : "AKGEC",
   
# }
# print(info)










# # Student_info dictionary...



# student = {
    
#     "name" : "Prafull Rajput",
#     "age" : 20,
#     "subjects" : {
#         "phy" : 95,
#         "chem" : 97,
#         "math" : 94,
#     }
    
# }
# print(student )
# print("Dictionary inside the List : " , list(student.values()))






# Dictionary Method... 


# 1. myDict.keys() ... returns all key
# 2. myDict.value()... return all values
# 3. myDict.item()... returns all (key, val) pair as tuples
# 4. myDict.get("key")... return the key according to value 
# 5. myDict.update(newDict)... inserts the specified items to the dictionary 









# # Sets in Python... 1. Collection of the unordered items
#                   # 2. each element in the set must be unique & immutable 




# nums = {1, 5, 8, 9, "Hello World", 8, 4, 7}

# print(nums)
# print(type(nums))









# # Set Methods... 


# 1. set.add(el)... adds an element 
# 2. set.remove(el)...remove the element 
# 3. set.clear()... empties the set                
# 4. set.pop()...remove a random vaule on the basis of index
# 5. set.union(set2)... combines the set
# 6. set.intersection(set2)...combines comman value 





# collection = set()

# collection.add(1)
# collection.add(5)
# collection.add(9)
# collection.add(8)
# collection.remove(9)

# print(collection)
# print(type(collection))









# # Ques.   WAP to enter of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. USer subject name as key & mark as value... 


# marks = {}

# x = int(input("Enter the marks of Physics : "))
# marks.update({"Physics" : x})

# y = int(input("Enter the marks of Chemistry : "))
# marks.update({"Chemistry" : y})

# z = int(input("Enter the marks of Math : "))
# marks.update({"Math" : z})

# print(marks)



 
