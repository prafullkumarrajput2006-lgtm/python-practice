# File Input/Output in Pythonn... 


# f = open("demo.txt", "r")

# # data = f.read(10)
# line1 = f.readline()
# print(line1)
# print(type(line1))
# f.close()









# # For print the data line wise... 



# f = open("demo.txt", "r")

# f.readline()      # skip first line
# line2 = f.readline()
# print(line2)

# line3 = f.readline()
# print(line3)
# f.close()







# For read and write both operations... by using this method ABC overwrite on "This" word...


f = open("demo.txt", "r+")

f.write("ABC")
print(f.read)
f.close()


