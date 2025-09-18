# squares1 = list(map(lambda x: x**2, range(10)))
# for i in squares1:
#     print(i)
    
# squares2 = [x**2 for x in range(10)] # List Comprehensions
# for i in squares2:
#     print(i)
    
# squares3 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# for i in squares3:
#     print(i)
    
# #====> the same
# temp_squares3 = []
# for x in [1, 2, 3]:
#     for y in [3, 1, 4]:
#         if x != y:
#             temp_squares3.append((x, y))

# tuple_item1 = () # empty
# tuple_item2 = 'thaivodinh', # one item (comma symbol at the end)

# # Cannot change value by index
# tuple_item2[0] = 'quocvodinh'

# # But can a sign new objects to the tuple
# tuple_item2 = 'khue', 56, 'nghean'

# # Can upack to assign other variable respectively
# tuple_item = 2, 'thaivodinh', 1234,
# x, y, z = tuple_item
# print(x, y, z)

a = {x for x in 'aracaraaacra' if x not in 'abc'}
print(a)

dict_items = dict([('thai', 26), ('quoc', 22), ('khue', 57)])
# dict_items = {'thai': 26, 'quoc': 22}

# Using items() to access values
for k, v in dict_items.items():
    print(k, v)
    
# Using enumerate() function to retrieve the index
for i, v in enumerate(dict_items):
    print(i, v)
    
# To loop over two or more sequences at the same time -> use zip() function
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
    
# To loop over a sequence in reverse -> use reversed() function
for i in reversed(range(1, 10, 2)):
    print(i)
    
# To loop over a sequence in sorted order -> use sorted() function
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)
    
# To loop over on a sequence with no duplicate elements -> use sorted() and set() function combination
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
