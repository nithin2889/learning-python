basket = ['a', 'b', 'c', 'd', 'e']

# 1. append
# append - changes the list in place. In place means it doesn't produce a value.
# All it does is it appends the object to the end of the list, but it won't produce
# a result.
new_basket = basket.append('f')
print(new_basket)
print(basket)

# 2. insert
# insert - we can insert an element anywhere we want in an index.
# Again, insert, modifies the list in place. It doesn't create a new copy of the list.
new_list = basket.insert(6, 'g')
print(basket)
print(new_list)

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
# We can use index to remove an item from a particular position.
basket.pop()
basket.pop()
print(basket)

basket.pop(0)
print(basket)

# Another important distinction of pop() is that it removes and returns an item
# at the specified index.
new_basket = basket.pop(4)
print(new_basket)

# b. remove() - here we need to give a value that we want to remove. Again, remove()
# doesn't return any value, but changes whatever list you give it.
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
basket.sort()
print(basket)

# 10. sorted() - built in function
# sorted() - produces a new array.
print(sorted(basket))
print(basket)

# Here, the basket hasn't been modified. It will still be the same.
# sorted(), on the other hand, doesn't modify the basket in place.
# Instead it creates a new copy of the basket and sorts it.
# Here, sorted() is nothing but list slicing and performing sort function
# on the object.
# Example:
# new_basket = basket[:]
# new_basket.sort()
# print(new_basket)
