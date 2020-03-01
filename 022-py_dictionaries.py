# Dictionary is a data structure in Python.
# In other languages it might be called the hash table, or an hash map
# or an object. In Python, we have this idea called dictionary or as Python
# likes to call it "dict".

# Dictionary is a data type in Python but it is also a data structure.
# Dictionary will contain a key and a value.
dictionary = {
    'a': 1,
    'b': 2
}
# A key is a string in order for us to grab/access the value.
print(dictionary['b'])

# When we give the key to search for a value it is going to go into the memory
# or into the machine's memory, it is going to find where the key is stored in
# our memory and grab the value.

# If we try to find something that is not present in the dictionary, then we are
# going to get an error.
# This is what a dictionary is. A dictionary is an unordered key-value pair.
# Unordered means that they are not right next to each other in memory unlike in lists.
# Dictionary on the other hand are all over the place. Although we have put the keys
# a and b here they might be at different spots in memory.

# Also, if we had a really really large dictionary I might not have them in order in the
# way they would be inserted. The value can be anything in a dictionary. It can be a list,
# or a string or a boolean value. It is all valid.
dictionary = {
    'a': [1, 2, 3],
    'b': 'Hello!',
    'x': True
}
print(dictionary['a'][1])

# this is the same with lists.
my_list = [{
    'a': [1, 2, 3],
    'b': 'Hello!',
    'x': True
}, {
    'c': [4, 5, 6],
    'd': 'Bye!',
    'y': False
}]
print(my_list[0]['a'][2])
print(my_list[1]['d'])
print(my_list[1]['y'])

# When to use a dictionary and when to use a list?
# A dictionary is not sorted. A list has order, but a dictionary has no order.
# A dictionary can hold more information than a list because lists only have that
# single value. Deep down, a list is simply an index in some sort of value versus
# a dictionary that holds a lot more information.

# A dictionary can hold any sort of data type. But what about the keys?
# Up until now, we have only used strings to denote a key, but could I
# use something other than a string?
dictionary = {
    123: [1, 2, 3],  # works fine!
    True: 'Hello!'  # works fine!
    # [100]: True      # doesn't work.
}
# print(dictionary[100]) # We get an error saying "unhashable type: list"

# Dictionary keys need to have a special property. A key need to be immutable.
# That means a key cannot change, but in this example the list is a mutable data type.
# So, a dictionary key always has to be immutable. 95% of the time a key for a
# dictionary is usually something descriptive like a string.

# What if we have duplicate keys?
dictionary = {
    '123': [1, 2, 3],
    '123': 'Hello!'
}
print(dictionary['123'])    # prints "Hello!"
# A key in a dictionary has to be unique because there can only be one key
# because that key is going to represent a bookshelf in that memory space.
# Any time we do the same key and may be add a value it is going to overwrite.

