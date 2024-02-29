# # Example1: creating dictionary
# my_dictionary = {
#     "brand": "Apple",
#     "model": "iphone 15 Pro",
#     "year": "2023",
#     "price": "99,000/-"
# }
#
# print(my_dictionary)


# # Example2: Access items from the dictionary
# my_dictionary = {
#     "brand": "Apple",
#     "model": "iphone 15 Pro",
#     "year": "2023",
#     "price": "99,000/-"
# }
#
# print("Brand:", my_dictionary["brand"])  # we can use this direct or get() function
# print("Model:", my_dictionary["model"])
# print("Price:", my_dictionary.get("price"))  # we can use this direct or get() function


# # Example3: change values from the dictionary
# my_dictionary = {
#     "brand": "Apple",
#     "model": "iphone 15 Pro",
#     "year": "2023",
#     "price": "99,000/-"
# }
#
# my_dictionary["model"] = "iphone 14 Pro Max"
# print(my_dictionary)


# # Example4: how to get only values from dictionary
# my_dictionary = {
#     "brand": "Apple",
#     "model": "iphone 15 Pro",
#     "year": "2023",
#     "price": "99,000/-"
# }
#
# for keys in my_dictionary:
#     print(keys)  # This will print only keys
#
# for values in my_dictionary:
#     print(my_dictionary[values])  # This will print only values
#
# # or
#
# for values in my_dictionary.values():
#     print(values)  # This will print only values
#
# # to get key and value at a time
# for key, value in my_dictionary.items():
#     print(key, ":", value)


# # Example5: check key is exit in dictionary or not
# my_dictionary = {
#     "brand": "Apple",
#     "model": "iphone 15 Pro",
#     "year": "2023",
#     "price": "99,000/-"
# }
#
# if "brand" in my_dictionary:
#     print("Yes. Brand key is exit in dictionary")
# else:
#     print("No. Brand is not exist in dictionary")
#
# # or
#
# print("brand" in my_dictionary)


# # Example6: find no of items in dictionary
# my_dictionary = {
#     "brand": "Apple",
#     "model": "iphone 15 Pro",
#     "year": "2023",
#     "price": "99,000/-"
# }
#
# print(len(my_dictionary))


# # Example6: add items to the dictionary
# my_dictionary = {
#     "brand": "Apple",
#     "model": "iphone 15 Pro",
#     "year": "2023"
# }
#
# my_dictionary["price"] = "99,000/-"
# print(my_dictionary)


# # Example6: remove item from the dictionary
# my_dictionary = {
#     "brand": "Apple",
#     "model": "iphone 15 Pro",
#     "year": "2023"
# }
#
# my_dictionary.pop("year")  # remove individual item
# print(my_dictionary)
#
# del my_dictionary["model"]  # remove individual item
# print(my_dictionary)
#
# del my_dictionary["brand"]  # remove individual item
# print(my_dictionary)
#
# del my_dictionary  # remove complete dictionary along with variable
# print(my_dictionary)


# Example6: copy the dictionary
my_dictionary1 = {
    "brand": "Apple",
    "model": "iphone 15 Pro",
    "year": "2023"
}

my_dictionary2 = my_dictionary1
print(my_dictionary2)
