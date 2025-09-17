# Table of Contents

- [Table of Contents](#table-of-contents)
- [About Python](#about-python)
- [Control Flows](#control-flows)
  - [if statement](#if-statement)
  - [for statement](#for-statement)
  - [range() function](#range-function)
  - [Defining Function](#defining-function)

# About Python
Python là một ngôn ngữ:
- high-level programming language
    - low-level - tức là ngôn ngữ gần gủi với máy tính và phần cứng hơn, thường phải làm việc trực - tiếp với bộ nhớ, thanh ghi, địa chỉ, commands, …
    
    - high-level - gần với human language, ít quan tâm đến chi tiết phần cứng, cú pháp dễ hiểu, …
    
- ngắn gọn
- interpreter
- dễ dàng collaborate với nhiều programming languages

# Control Flows
## if statement
Trong python sử dụng "if, elif, else" 

## for statement
```python
# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

```

## range() function
Tạo một arithmetic progressions (cấp số cộng) → tức một dãy số nằm trong range.
```python
list(range(5, 10))
list(range(0, 10, 3))
list(range(-10, -100, -30))
```

## Defining Function
- Dùng "def" keyword to create functions, body function is recognized by indentation
- Đầu function có thể có một “string literal” như một doc describe for functions
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