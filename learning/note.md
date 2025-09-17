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

Đầu function có thể có một “string literal” như một doc describe for functions
- Mỗi function sẽ có một local symbol table to store all local variables trong function
    - global variable cũng là by a value
    - khi access một variable nó sẽ search trong các table từ trong ra ngoài - the local symbol tables of enclosing function → the global symbol table → the built-in table
    - dùng “global, local, nonlocal” để specify the type of variable
- Mỗi function name sẽ được associated với một function object được store trong local table → Ta có thể assign một existing function cho other function names.
- Function trong python luôn return “None”.
```python
words = ['thai', 'quoc', 'khue', 'soa']
for i in words:
    ... # pass
    
def http_error(var):
    'this function is used to interate over items in var'
    for item in var:
        print(item)
        
http_error(words)
```