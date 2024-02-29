# # Example1: creating set
# my_set = {"Rakesh", "Satya", "John", "Peter", "Scoot"}
#
# print(my_set)


# # Example2: Accessing set
# my_set = {"Rakesh", "Satya", "John", "Peter", "Scoot"}
#
# for names in my_set:
#     print(names)


# # Example3: Value is exist or not
# my_set = {"Rakesh", "Satya", "John", "Peter", "Scoot"}
#
# if "Satya" in my_set:
#     print("Yes. Satya is exist in the set")
# else:
#     print("No. Satya is not exist in the set")
#
# # or
#
# print("Satya" in my_set)


# # Example4: add item to the set
# my_set = {"Rakesh", "Satya", "John", "Peter"}
# # add() single item at a time
# my_set.add("Scoot")
# print(my_set)
#
# # update() add multiple items at a time
# my_set.update({"Krish", "Ramu"})
# print(my_set)


# # Example5: find no of items in a set
# my_set = {"Rakesh", "Satya", "John", "Peter"}
#
# print(len(my_set))


# # Example6: remove items from set
# my_set = {"Rakesh", "Satya", "John", "Peter"}
# # remove()
# my_set.remove("Rakesh")
# print(my_set)
# # my_set.remove("abc")  # if we are removing non-existing item then the remove function will through you an error
# # print(my_set)
#
# # discard()
# my_set.discard("John")
# print(my_set)
# my_set.discard("abc")  # if we are removing non-existing item then this discard() function wil not through any error
# print(my_set)


# # Example7: clear all items from set
# my_set = {"Rakesh", "Satya", "John", "Peter"}
#
# my_set.clear()  # just clear the values but set variable exit
# print(my_set)
# my_set.add("Satya")
# print(my_set)
#
# del my_set  # delete completely along with set variable
# print(my_set)


# # Example8: join/combine sets
# # union()
# my_set1 = {"Rakesh", "Satya", "John", "Peter"}
# my_set2 = {1, 2, 3, 4}
#
# my_set3 = my_set1.union(my_set2)
# print(my_set3)

# # update()
# my_set1 = {"Rakesh", "Satya", "John", "Peter"}
# my_set2 = {1, 2, 3, 4}

# my_set1.update(my_set2)
# print(my_set1)


