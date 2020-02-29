# Lists get really powerful when it comes to methods. Instead of a built in functions,
# remember, a method is a new action that is owned by something and it is specific to
# let's say, to a data type.

# Python has a few list methods that we can use:
# append(), clear(), copy(), count(), extend(),
# index(), insert(), pop(), remove(), reverse(),
# sort()
#
# The way we use these methods is, remember, we just add a dot after a list.

basket = ['a', 'b', 'c', 'd', 'e']

# 1. append
# append - changes the list in place. "In place" means it doesn't produce a value.
# It does not create a new copy of the list.
# All it does is it appends the object to the end of the list, but it won't produce
# a result.
new_basket = basket.append('f')
print(new_basket)
print(basket)

# 2. insert
# insert - we can insert an element anywhere we want in an index.
# Again, insert, modifies the list in place. It doesn't create a new copy of the list.
new_list = basket.insert(6, 'g')
print(new_list)
print(basket)

# 3. extend
# extend - instead of an actual item or an object, it takes what we call an "iterable".
# Using which we can loop over, or iterate over which is a list. Again, it doesn't output
# a new list, it just modifies the list in place and adds on or extends our list. The function
# extends doesn't return anything.
basket.extend(['y', 'z'])
print(basket)

# 4. remove
# remove - there are a few ways to remove an item from a list.
# a. pop() - pop removes what ever is at the end of the list.
basket.pop()
basket.pop()
print(basket)

# We give the index that we want to remove from a particular position.
basket.pop(0)
print(basket)

# Another important distinction of pop() is that it removes and returns an item at the specified index.
# pop returns whatever you have just removed.
new_basket = basket.pop(4)
print(new_basket)

# b. remove() - We give the value that we want to remove. Again, remove()
# doesn't return any value, but changes whatever list you give it.
# Since it doesn't return anything it returns "None".
basket.remove('d')
print(basket)

# 5. clear
# clear - clear removes whatever is in the list.
# basket.clear()
# print(basket)


# 6. index
# index - index gives us the index number of the specified element.
print(basket.index('g'))
# we can provide the index where to start and where to end.
print(basket.index('e', 0, 3))

# Errors are not good in our programs. Ideally we don't want to get errors.
# How to avoid this? What if we are looking for something and we are not sure
# if it is in the list or not?
# There is another nifty way of looking for things in a list and this involves
# what we call a Python keyword. A keyword is something that we use in Python that
# already has some meaning.

# 7. in
# in - Used to look for something in the list. Returns a boolean True if found
# else returns False.
print('g' in basket)
print('x' in basket)
# can be used with a string to find a character or a sequence of character.
print('am' in 'Hi my name is Nithin')

# 8 - count
# count - we can count how many times an item occurs.
print(basket.count('e'))
print('hi my name is Nithin'.count('hi'))

# 9. sort
# sort - sorts the list in place. It will not return anything.
unsorted_basket = ['b', 'c', 'a', 'e', 'd', 'd']
unsorted_basket.sort()
print(unsorted_basket)

# 10. sorted() -
# This is a built-in function and not a method.
# Since it is a built-in function we do not use the dot operator.
# Just like type built-in function we can use
# this inside of our sorted function as shown below.
# This will produce a new array.
basket_to_sort = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
print(sorted(basket_to_sort))
# Here the basket_to_sort will be unchanged.
# So sorted() "doesn't modify" the basket_to_sort in place. Instead
# it creates a new copy of the basket and sorts it.
# This is equivalent of doing:
#   new_sorted_basket = basket_to_sort[:]
#   new_sorted_basket.sort()
# which is list slicing.
print(basket_to_sort)

# 11. copy() -
# There is also a .copy() method that copies the list for us and returns
# for us a new list.
new_basket = ['a', 'z', 'b', 'c', 'f', 'e', 'd', 'g']
new_basket_copy = new_basket.copy()
new_basket_copy.sort()
print(new_basket_copy)
print(new_basket)

# 12. reverse() -
# simply switches all the indexes into opposite sides.
basket_to_reverse = ['a', 'z', 'b', 'c', 'f', 'e', 'd', 'g']
basket_to_reverse.reverse()
print(basket_to_reverse)

# COMMON LIST PATTERNS:
# List slicing can be used to reverse a list.
# List slicing [::-1] creates a new list or used may be when you
# need to make a copy of the list ([:]) or may be when you need a portion
# of the list.
basket_to_reverse.sort()
print(basket_to_reverse[::-1])

# If we want to generate a list real quick, let's say, 1 to 100 then we can do something like
print(range(1, 100))    # we get "range(1, 100)".
# When we wrap this in a list then it will create a new list for us.
# This will generate a range of number from 1 to 99. The two parameters are start and a stop.
# So before it hits 100 it is going to stop.
print(list(range(1, 100)))

# If we remove the start index 1
# we get a list starting from 0 all the way till 99.
# this is a great way to generate a numbered list really quickly.
print(list(range(100)))

# Finally, the last common thing that you will see a lot is this
# idea of .join(). join is something that works on strings. It is a string method.
sentence = ' '
sentence = sentence.join(['hi', 'my', 'name', 'is', 'Nithin'])
print(sentence)
# join() takes what we call an iterable (a list, for now) inside which we can have any
# string. join() returns us a new string. join() joins these little iterable items by whatever
# is in front of it. What we are doing is combining lists into a string which is a common pattern.

# List Unpacking
# what if we wanted to assign a variable to each item?
# We can do something like this.
a, b, c = [1, 2, 3]
print(a)
print(b)
print(c)

# but this is where list unpacking gets really useful.
# a, b, c = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# what if we wanted to unpack 1, 2, and 3, but keep
# everything else still in the list? With list unpacking we can.
# all we need to do is to add a star and give it a variable name
# whatever we like.
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(other)
print(d)
