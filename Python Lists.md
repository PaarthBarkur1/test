1. > # ***Python Lists:***

2. In short, a list is a collection of arbitrary objects, somewhat akin to an array in many other programming languages but more flexible. Lists are defined in Python by enclosing a comma-separated sequence of objects in square brackets ([]), as shown below:

>a = ['foo', 'bar', 'baz', 'qux']

>print(a)
>['foo', 'bar', 'baz', 'qux']
>a
>['foo', 'bar', 'baz', 'qux']

The important characteristics of Python lists are as follows:

Lists are ordered.
Lists can contain any arbitrary objects.
List elements can be accessed by index.
Lists can be nested to arbitrary depth.
Lists are mutable.                                                                                                                 Lists are dynamic.
Each of these features is examined in more detail below.

## **Lists Are Ordered**

A list is not merely a collection of objects. It is an ordered collection of objects. The order in which you specify the elements when you define a list is an innate characteristic of that list and is maintained for that list’s lifetime.

example:

>a = ['foo', 'bar', 'baz', 'qux']
>
>b = ['baz', 'qux', 'bar', 'foo']
>a == b
>
>False

A list can contain any number of objects, from zero to as many as your computer’s memory will allow

Lists can even contain complex objects, like functions, classes, and modules, which you will learn about in upcoming tutorials

You can specify a stride—either positive or negative:

>>> a[0:6:2]
>>> ['foo', 'baz', 'quux']
>>> a[1:6:2]
>>> ['bar', 'qux', 'corge']
>>> a[6:0:-2]
>>> ['corge', 'qux', 'bar']

The syntax for reversing a list works the same way it does for strings:

>>> a[::-1]
>>> ['corge', 'quux', 'qux', 'baz', 'bar', 'foo']

## **Lists Are Mutable**

Most of the data types you have encountered so far have been atomic types. Integer or float objects, for example, are primitive units that can’t be further broken down. These types are immutable, meaning that they can’t be changed once they have been assigned. It doesn’t make much sense to think of changing the value of an integer. If you want a different integer, you just assign a different one.

By contrast, the string type is a composite type. Strings are reducible to smaller parts—the component characters. It might make sense to think of changing the characters in a string. But you can’t. In Python, strings are also immutable.

The list is the first mutable data type you have encountered. Once a list has been created, elements can be added, deleted, shifted, and moved around at will. Python provides a wide range of ways to modify lists.

#### **Modifying Multiple List Values**

What if you want to change several contiguous elements in a list at one time? Python allows this with slice assignment, which has the following syntax:

### Prepending or Appending Items to a List

Additional items can be added to the start or end of a list using the + concatenation operator or the += augmented assignment operator>>> a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

>>> a += ['grault', 'garply']
>>> a
>>> ['foo', 'bar', 'baz', 'qux', 'quux', 'corge', 'grault', 'garply']

### important functions:

1. a.append(<obj>)
2. a.insert(<index>, <obj>)
3. a.remove(<obj>)
4. a.pop()

### Lists Are Dynamic

This tutorial began with a list of six defining characteristics of Python lists. The last one is that lists are dynamic. You have seen many examples of this in the sections above. When items are added to a list, it grows as needed.

