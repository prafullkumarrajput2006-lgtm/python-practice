# Methods... 


# Print all the keys... 


info = {
    "Name" : "Prafull Rajput",
    "CGPA" : 9,
    "AGE" : 21,
    "College Name" : "AKGEC",
    "Package" : "50 LPA"
}

print(info.keys())

print(info.values())

dict_values = list(info.values())
print(dict_values)

print(info.items())


info.update ( {
    "City" : "Ghaziabad"
})
print(info)