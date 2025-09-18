# Table of Contents

- [Table of Contents](#table-of-contents)
- [About Python](#about-python)
- [Using the Python Interpreter](#using-the-python-interpreter)
- [Control Flows](#control-flows)
  - [if statement](#if-statement)
  - [for statement](#for-statement)
  - [range() function](#range-function)
  - [break, continue](#break-continue)
  - [else on loops](#else-on-loops)
  - [pass statement](#pass-statement)
  - [match statment](#match-statment)
- [Defining Function](#defining-function)
- [Data Structures](#data-structures)
  - [List](#list)
  - [Stack](#stack)
  - [Queue](#queue)
  - [List Comprehensions](#list-comprehensions)
  - [Nested List Comprehensions](#nested-list-comprehensions)
  - [del statement](#del-statement)
  - [Tuples and Sequences](#tuples-and-sequences)
  - [Sets](#sets)
  - [Dictionaries](#dictionaries)
  - [Looping Techniques](#looping-techniques)
  - [More on Condition](#more-on-condition)
  - [Comparing Sequences](#comparing-sequences)

# About Python
Phân biệt giữa Compiled và Interpreted Programming Languages:

> Compiled languages are fully translated into machine-readable machine code before execution, resulting in faster run times but requiring a separate compilation step for each platform. 
> 
> Interpreted languages are translated and executed line-by-line at runtime by an interpreter, which offers greater flexibility and portability but can lead to slower performance.

Tại sao lại cần nhiều programming languages:
- Mỗi cái sinh ra để giải quyết một nhu cầu khác nhau
  - C/C++: Gần vời phần cứng, chạy nhanh, thích hợp viết hệ điều hành, driver, ...
  - Python: Cú pháp dễ hiểu, thư viện mạnh -> phân tích dữ liệu, AI, tự động hóa, ...
  - Javascript: Web
  - SQL: Database
- Performance và Resources
- Sự tiến hóa theo thời gian
------

Python là một ngôn ngữ:
- High-level programming language
    - Low-level - tức là ngôn ngữ gần gủi với máy tính và phần cứng hơn, thường phải làm việc trực - tiếp với bộ nhớ, thanh ghi, địa chỉ, commands, …
    
    - High-level - gần với human language, ít quan tâm đến chi tiết phần cứng, cú pháp dễ hiểu, …
    
- Ngắn gọn
- Interpreter
- Dễ dàng collaborate với nhiều programming languages

# Using the Python Interpreter
Bản chất trong mỗi OS, python interpreter sẽ được store in a specific directory
- Linux:
- Window: 

# Control Flows
## if statement
Trong python sử dụng "if, elif, else".
```python
x = int(input("Enter your number:"))
def is_check(status):
    if x > 0:
        print("This is a position number")
    elif x == 0:
        print("This is zero")
    else:
        print("This is a nagative number")
is_check(x)
```

## for statement
Việc modify (appen, delete) trên origin list có thể lỗi -> nên sử dụng một bản copy.
```python
words = ['thai', 'quoc', 'khue', 'soa']
for item in words:
    print(item)

users = {'Hans': 'active', 'Eleonore': 'inactive', '景太郎': 'active'}
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

for item in users:
    print(item)

for item in active_users:
    print(item)
```

## range() function
Tạo một arithmetic progressions (cấp số cộng) → tức một dãy số nằm trong range.
```python
for i in range(4):
    print(i)

words = list(range(3, 10, 3))
for i in words:
    print(i)

# can combine range() with len()
subwords = ['Mary', 'had', 'a', 'little', 'cat']
for i in range(len(subwords)):
    print(subwords[i])

# can enumerate() function instead
sessons = ['Spring', 'Summer', 'Fall', 'Winter']
listitems = list(enumerate(sessons, start=2))
for i, e in listitems:
    print(i, e)
```
## break, continue
Nó hoạt động như trong C/C++

## else on loops
Trong loops như for or while thì else có thể được execute nếu không break, return, throw exceptions (sử dụng try catch)
```python
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
```

## pass statement
Nghĩa là do nothing, thông báo cho interpreter là chỗ đó chưa implement, nên bỏ qua, sau này sẽ implement.

Trong trường hợp define a function, thì **pass** có thể thay thể bằng **"..."** để biểu thỉ function đó chưa được implement.

## match statment


# Defining Function
Trong python dùng **"def"** để define một function. Body function được interpreter recognize by indentations.

Line đầu tiên trong function có thể là note describe cho function

Khi gọi để execute một function thì mỗi function sẽ có một local table riêng (bất kể cả function này gọi function khác or recursive) -> suy ra các biến sử dụng trong function là k liên quan đến nhau.
- khi access một variable nó sẽ search trong các table từ trong ra ngoài - the local symbol tables of enclosing function → the global symbol table → the built-in table.
- dùng “global, local, nonlocal” để specify the type of variable

Mỗi function nó được xem là object gắn với a name -> ta có thể assign function for another name.

Mỗi function trong python đều implicitly return một giá trị là None

```python
x = int(input("Please enter your number:"))

def is_check(status):
    "This function is used to check the condition"
    if status >= 0:
        print("thaivodinh")

is_check(x)

y = 2
def change_variable():
    global y
    y = 3
    print(y)
change_variable()
print(y)

def is_verify():
    print("thaivodinh")

if is_verify() is None:
    print("This function returned None")
```
1. Default Arguments

Default argument trong function chỉ được evaluated một lần, sau đó nó có thể tái sử dụng.
```python
def f(a, L=[]):
    L.append(a)
    return L

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
```

2. Keyword Arguments

Keyword Argument: kwarg=value -> cú pháp trong lúc gọi hàm

Ta có thể chỉ định một argument trong function với một giá trị cụ thể -> nhưng bắt buộc tên phải match.
```python
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print(voltage)
    print(state)
    print(action)
    print(type)
parrot(voltage=1000, action='thaivodinh') 
```

3. Special Parameters

Việc pass arguments trong python chia làm 2 loại:
- theo position
- theo keyword

Thì nó dùng "/" và "*" để phân tách các type argument trong một function.

4. Lambda Functions
```python
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42) # => f(x) = x + 42

print(f(2))
```

# Data Structures
## List
Support append(), extend(), insert, remove(), sort(), reverse(), ....

List is mutable
## Stack
Follow principle LAST-IN, FIRST-OUT. Thằng cuối vào chính là thằng phải ra đầu tiên
## Queue
FIRST-IN, FIRST-OUT
## List Comprehensions
Cung cấp một cách để tạo một cái list nhanh chóng.
```python
squares1 = list(map(lambda x: x**2, range(10)))
for i in squares1:
    print(i)
    
squares2 = [x**2 for x in range(10)] # List Comprehensions
for i in squares2:
    print(i)
    
squares3 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
for i in squares3:
    print(i)
    
#====> the same
temp_squares3 = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            temp_squares3.append((x, y))
```
## Nested List Comprehensions
## del statement
To remove a item
## Tuples and Sequences

Một tuple chứa các giá trị khác nhau  

Tuple is immutable
```python
tuple_item1 = () # empty
tuple_item2 = 'thaivodinh', # one item (comma symbol at the end)

# Cannot change value by index
tuple_item2[0] = 'quocvodinh'

# But can a sign new objects to the tuple
tuple_item2 = 'khue', 56, 'nghean'

# Can upack to assign other variable respectively
tuple_item = 2, 'thaivodinh', 1234,
x, y, z = tuple_item
print(x, y, z)
```
## Sets
- It is unordered collection with no duplicate elements
- A set can create by curply braces or set() function
- A empty set only create by set() function, not {}
- Create set via list comprehension
```python
a = {x for x in 'aracaraaacra' if x not in 'abc'}
print(a)
```
## Dictionaries
Similar to std::map in C++ with pairs of key and value.
```python
dict_items = dict([('thai', 26), ('quoc', 22), ('khue', 57)])
# dict_items = {'thai': 26, 'quoc': 22}
```

## Looping Techniques
Using items() function to access to keys and their associated values.
```python
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
```
> Sometime you try to change the value while you're iterating over it -> you should create a new list for simpler and safer.

## More on Condition
- in, not in: to check a value is in (or not in) a container
- is, not is: to compare two objects are really the same
- and, or, not to compare

## Comparing Sequences
Các chuỗi object có thể compare với nhau.
