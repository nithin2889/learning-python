user = {
  'basket': [1, 2, 3],
  'greet': 'Hello',
  'age': 20
}
# Remember errors in our programs are not good. They're going to stop
# the program as soon as the python interpreters enters. It is going to
# completely ignore what's underneath it.
# Another good way to access a key and to see if it even exists is to use
# a `.get()` method and this is a method on the object or the dictionary.
# If the key doesn't exist then we get "None". So my program doesn't error.
print(user.get('age'))

# Let's say there is no age property but you want to have a default value.
# You can do something like this.
print(user.get('age', 30))  # prints the default value, 30, for age property

# Another way to create a dictionary which is not very common. Most of the
# time we would use something as shown above. Just so we are aware of it.
# Here's another way.
new_user = dict(name='NithinNithin', place='Bangalore')
print(new_user)  # OUTPUT: {'name': 'NithinNithin', 'place': 'Bangalore'}

# There is actually one more way that we have actually seen in lists how to
# look for an item in a dictionary. Remember how in lists we used the keyword
# `in`?
print('in' in new_user['name'])

# Here is where it gets really interesting. This is another dictionary
# method that we can use.
# 1. keys()
# keys() simply checks for the keys
print('name' in new_user.keys())

# 2. values()
# values() simply checks for the values
print('NithinNithin' in new_user.values())

# 3. items()
# items() is special because we have seen keys and values, but
# items actually grabs the entire item.
print(new_user.items())
# OUTPUT: dict_items([('name', 'NithinNithin'), ('place', 'Bangalore')])
# The weird syntax inside the parentheses is called "Tuple".

# 4. clear()
# clear() actually doesn't return anything. It just in place removes whatever
# the dictionary has.
# user.clear()
# print(user)

# 5. copy()
# copy() allows us to copy an object
user_copy = user.copy()
print(user)
print(user_copy)
# If we use clear() method, only `user` would be cleared, but because I have
# copied another user it still has the old information.

# 6. pop()
# pop() removes a key and a value from the dictionary. pop() returns the
# value of whatever got removed.
print(user.pop('age'))

# 7. popitem()
# popitem() randomly pops off something, one of the keys and the values.
# Remember, a dictionary is unordered. If this was a massive dictionary
# that, well, doesn't have any order to it sometimes it removes some pair
# of key and value. So we have to be careful with this one. It doesn't
# necessarily remove the last thing that you entered, but it might be
# useful on some occasion (useful to destructively iterate over a dictionary).
print(user.popitem())

# 8. update()
# update() simply updates, as the name suggests, a key value.
user.update({'age': 10})
print(user)
# if this key was a key that doesn't exist then it still would update with a
# new key item.
user.update({'job': 'IT'})
print(user)
