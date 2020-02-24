basket = [1, 2, 3, 4, 5]

# 1. append
# append - changes the list in place. In place means it doesn't produce a value.
# All it does is it appends the object to the end of the list, but it won't produce
# a result.
new_basket = basket.append(6)
print(new_basket)
print(basket)

# 2. insert
# insert - we can insert an element anywhere we want in an index.
# Again, insert, modifies the list in place. It doesn't create a new copy of the list.
new_list = basket.insert(6, 7)
print(basket)
print(new_list)

# 3. extend
# extend - instead of an actual item or an object, it takes what we call an "iterable".
# Using which we can loop over, or iterate over which is a list. Again, it doesn't output
# a new list, it just modifies the list in place and adds on or extends our list. The function
# extends doesn't return anything.
basket.extend([100, 101])
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
basket.remove(4)
print(basket)

# 5. clear
# clear - clear removes whatever is in the list.
basket.clear()
print(basket)
