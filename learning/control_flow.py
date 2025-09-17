# #### if statment
# x = int(input("Enter your number:"))
# def is_check(status):
#     if x > 0:
#         print("This is a position number")
#     elif x == 0:
#         print("This is zero")
#     else:
#         print("This is a nagative number")
# is_check(x)


# #### for statment
# words = ['thai', 'quoc', 'khue', 'soa']
# for item in words:
#     print(item)

# users = {'Hans': 'active', 'Eleonore': 'inactive', '景太郎': 'active'}
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]

# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status


# for item in users:
#     print(item)

# for item in active_users:
#     print(item)

# #### range() function
# for i in range(4):
#     print(i)

# words = list(range(3, 10, 3))
# for i in words:
#     print(i)

# # can combine range() with len()
# subwords = ['Mary', 'had', 'a', 'little', 'cat']
# for i in range(len(subwords)):
#     print(subwords[i])

# # can enumerate() function instead
# sessons = ['Spring', 'Summer', 'Fall', 'Winter']
# listitems = list(enumerate(sessons, start=2))
# for i, e in listitems:
#     print(i, e)

#### else on loops
# for statement
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

# while statement
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("done")