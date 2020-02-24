# list
amazon_cart = ['notepads', 'laptops']
# print(amazon_cart[0] + '-' + amazon_cart[1])

# IndexError: list index out of range
# print(amazon_cart[2])

# list splicing
flipkart_cart = ['notepads', 'sunglasses', 'toys', 'grapes']
# print(flipkart_cart[0::2])
# lists are mutable unlike strings in Python
# list slicing creates a new copy of a list
flipkart_cart[0] = 'laptops'

# when we modify new_cart, we are changing flipkart_cart directly in the memory.
# modifying list
new_cart = flipkart_cart
new_cart[0] = 'meat'
print(new_cart)
print(flipkart_cart)

# to copy an entire list, we need to use slicing
# copying list
flipkart_cart_copy = ['mint', 'chocolate', 'water', 'fruits']
new_cart_copy = flipkart_cart_copy[:]
new_cart_copy[0] = 'okra'
print(new_cart_copy)
print(flipkart_cart_copy)
