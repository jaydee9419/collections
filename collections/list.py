# # Example1: How to create list
# mylist_num = [10, 20, 30, 40, 50]
# mylist_string = ["Rajesh", "Satya", "John", "Scoot", "Mike"]
# mylist_combo = [10, "Rajesh", 30, "John", 50]
#
# print(mylist_num)
# print(mylist_string)
# print(mylist_combo)


# # Example2: How to access items form the list by using index value
# mylist_num = [10, 20, 30, 40, 50]
# mylist_string = ["Rajesh", "Satya", "John", "Scoot", "Mike"]
# mylist_combo = [10, "Rajesh", 30, "John", 50]
#
# # positive index
# print(mylist_num[0])
# print(mylist_string[1])
# print(mylist_combo[2])
#
# # Negative index
# print(mylist_string[-1])
# print(mylist_combo[-2])


# # Example3: How to access items form the list by using range
# mylist_num = [10, 20, 30, 40, 50]
# mylist_string = ["Rajesh", "Satya", "John", "Scoot", "Mike"]
# mylist_combo = [10, "Rajesh", 30, "John", 50]
#
# print(mylist_num[0:2])  # get from 1st to 3rd value
# print(mylist_string[2:4])  # get from 2nd to 4th value
# print(mylist_string[-4:-1])
# print(mylist_string[::-1])  # Accessing list in reverse


# # Example4: How to change the item value from the list
# mylist_num = [10, 20, 30, 40, 50]
# mylist_string = ["Rajesh", "Satya", "John", "Scoot", "Mike"]
# mylist_combo = [10, "Rajesh", 30, "John", 50]
#
# print(mylist_string)
#
# # want to change the 1st item
# mylist_string[0] = "Rahul"
#
# print(mylist_string)


# # Example5: Reading items by using loop statement
# mylist_num = [10, 20, 30, 40, 50]
# mylist_string = ["Rajesh", "Satya", "John", "Scoot", "Mike"]
# mylist_combo = [10, "Rajesh", 30, "John", 50]
#
# for item in mylist_string:
#     print(item)


# # Example6: check if item is existed or not
# mylist_num = [10, 20, 30, 40, 50]
# mylist_string = ["Rajesh", "Satya", "John", "Scoot", "Mike"]
# mylist_combo = [10, "Rajesh", 30, "John", 50]
#
# if "Rajesh" in mylist_string:
#     print("Yes. Rajesh is exit in the list")
# else:
#     print("No. Rajesh is not exit in the list")


# # Example7: check total no of items in the list
# mylist_num = [10, 20, 30, 40, 50]
# mylist_string = ["Rajesh", "Satya", "John", "Scoot", "Mike"]
# mylist_combo = [10, "Rajesh", 30, "John", 50]
#
# print(len(mylist_string))


# # Example8: add new item to the list append(), insert()
# mylist_num = [10, 20, 30, 40, 50]
# mylist_string = ["Rajesh", "Satya", "John", "Scoot", "Mike"]
# mylist_combo = [10, "Rajesh", 30, "John", 50]
#
# mylist_string.append("Krish")  # Item will be added at the end
# print(mylist_string)
#
# mylist_string.insert(2, "Ramu")  # insert value along with index value means where we need to insert
# print(mylist_string)


# # Example9: Remove items from the list
# # pop()
# mylist_string = ["Rajesh", "Satya", "John", "Scoot", "Mike"]
#
# mylist_string.pop(1)  # by using index value
# print(mylist_string)
#
# # del
# del mylist_string[1]  # del uses to remove single item based on index value
# print(mylist_string)
#
# # clear()
# mylist_string.clear()
# print(mylist_string)


# # Example10: copy list
# mylist_string1 = ["Rajesh", "Satya", "John", "Scoot", "Mike"]
# mylist_string2 = list(mylist_string1)
#
# print(mylist_string1)
# print(mylist_string2)
#
# # copy()
# mylist_string1 = ["Rajesh", "Satya", "John", "Scoot", "Mike"]
# mylist_string2 = mylist_string1.copy()
#
# print(mylist_string1)
# print(mylist_string2)


# Example11: combine/join list
mylist1 = [1, 2, 3]
mylist2 = ["John", "Scoot", "Mike"]

mylist3 = mylist1+mylist2
print(mylist3)

# using looping statement
for item in mylist1:
    mylist2.append(item)

print(mylist2)
