# Python Tuples:

### Defining and Using Tuples

Tuples are identical to lists in all respects, except for the following properties:

1. Tuples are defined by enclosing the elements in parentheses (()) instead of square brackets ([]).
2. Tuples are immutable.

>>> t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
>>> t
>>> ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')

>>> t[0]
>>> 'foo'
>>> t[-1]
>>> 'corge'
>>> t[1::2]

### Tuple reversal :

Its the same as 

code:

t[::-1]

## Why use a tuple instead of a list?

1. Program execution is faster when manipulating a tuple than it is for the equivalent list. (This is probably not going to be noticeable when the list or tuple is small.)

2. Sometimes you don’t want data to be modified. If the values in the collection are meant to remain constant for the life of the program, using a tuple instead of a list guards against accidental modification.

3. There is another Python data type that you will encounter shortly called a dictionary, which requires as one of its components a value that is of an immutable type. A tuple can be used for this purpose, whereas a list can’t be

## Fact:

### In a Python REPL session, you can display the values of several objects simultaneously by entering them directly at the 

>>> prompt, separated by commas.

>>> a = 'foo'
>>> b = 42
>>> a, 3.14159, b
>>> ('foo', 3.14159, 42)

### When you define a empty tuple it interprets it as tuple :

ex: t=()

type(t)

output: tuple

### but when u define a single element as a tuple it gets an error and misinterprets its type:

 >>> t = (2)
 >>> type(t)
 >>> <class 'int'>

but to create a single element tuple we have to follow the following code:

### **Tuple Assignment, Packing, and Unpacking:**

(s1,s2,s3,s4)=t = ('foo', 'bar', 'baz', 'qux')

print(s1)

'>>>foo'

### In Python, the swap can be done with a single tuple assignment

>>> a = 'foo'
>>> b = 'bar'
>>> a, b
>>> ('foo', 'bar')

>>># Magic time!
>>>a, b = b, a

>>> a, b
>>> ('bar', 'foo')