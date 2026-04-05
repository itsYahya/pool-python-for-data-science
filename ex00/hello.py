ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# Modifying the data structures

# Lists are mutable, so we can change their elements
ft_list[1] = "World!"

# Tuples are immutable, so we cannot change their elements directly. 
# We need to convert the tuple to a list, modify it, and then convert it back to a tuple.
temp_tuple = list(ft_tuple)
temp_tuple[1] = "Morocco!"
ft_tuple = tuple(temp_tuple)

# Sets are mutable, but they do not support indexing. 
# We can convert the set to a list, modify it, and then convert it back to a set.
temp_set = list(ft_set)
temp_set[1] = "Khouribga!"
ft_set = set(temp_set)

# Dictionaries are mutable, so we can change their values by using their keys
ft_dict["Hello"] = "1337!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
