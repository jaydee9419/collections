# # Example1: creating tuple
# my_tuple = ("Apple", "Orange", "Banana")
#
# print(my_tuple)


# # Example2: access tuple item by using index number
# my_tuple = ("Apple", "Orange", "Banana")
#
# print(my_tuple[1])
# print(my_tuple[-1])


# # Example3: access tuple item by using index number with range function
# my_tuple = ("Apple", "Orange", "Banana")
#
# print(my_tuple[0:2])
# print(my_tuple[-3:-1])


# # Example4: change tuple item
# my_tuple = ("Apple", "Orange", "Banana")
#
# # Note: change item from tuple is not possible bcz this is immutable
# #     we can not modify exiting value
# #     we can not append new value
# #     we can not insert a new value
# #     we can not remove a value


# # Example5: convert tuple in to list and do modifications and reconvert in to tuple
# my_tuple = ("Apple", "Orange", "Banana")
# print(my_tuple)
#
# my_list = list(my_tuple)
# my_list.append("Mango")
# print(my_list)
# my_list.pop(0)
# print(my_list)
#
# my_tuple = tuple(my_list)
# print(my_tuple)


# # Example6: Check the item is present in the tuple or not
# my_tuple = ("Apple", "Orange", "Banana")
#
# if "Apple" in my_tuple:
#     print("Yes. Apple is exist in tuple")
# else:
#     print("No. Apple is not exit in tuple")


# # Example7: copy tuple
# my_tuple1 = ("Apple", "Orange", "Banana")
# my_tuple2 = my_tuple1
#
# print(my_tuple2)


# # Example8: combine/join tuple
# my_tuple1 = ("Apple", "Orange", "Banana")
# my_tuple2 = (1, 2, 3)
#
# my_tuple3 = my_tuple1+my_tuple2
# print(my_tuple3)


# Example9: combine/join tuple
my_tuple1 = ("Apple", "Orange", "Banana")
my_tuple2 = ("Apple", "Orange", "Banana")
my_tuple3 = (1, 2, 3)

if my_tuple1 == my_tuple2:
    print("tuples are equal")
else:
    print("tuples are not equal")

if my_tuple1 == my_tuple3:
    print("tuples are equal")
else:
    print("tuples are not equal")
