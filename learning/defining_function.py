# x = int(input("Please enter your number:"))

# def is_check(status):
#     "This function is used to check the condition"
#     if status >= 0:
#         print("thaivodinh")

# is_check(x)

# y = 2
# def change_variable():
#     global y
#     y = 3
#     print(y)
# change_variable()
# print(y)

# def is_verify():
#     print("thaivodinh")

# if is_verify() is None:
#     print("This function returned None")


# def f(a, L=[]):
#     L.append(a)
#     return L

# def f(a, L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L

# print(f(1))
# print(f(2))
# print(f(3))

# def foo(a=10):
#     print(a)
    
# foo()
# foo(2)
# foo(3)

# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print(voltage)
#     print(state)
#     print(action)
#     print(type)
# parrot(voltage=1000, action='thaivodinh')    


# parrot()                     # required argument missing
# parrot(voltage=5.0,action= 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument

# def foo(a, b, /, c=10, d=11):
#     print(a, b, c, d)
# foo(20, 10)

# def foo1(*, a, b):
#     print(a, b)
# foo1(b=1, a=2)
# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])
        
# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")


def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42) # => f(x) = x + 42

print(f(2))