selfish = '01234567'
# TypeError: 'str' object does not support item assignment
# selfish[0] = '8'

# completely valid
selfish = selfish + '8'
print(selfish)
