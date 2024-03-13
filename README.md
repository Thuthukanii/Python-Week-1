# Python-Week-1
[![Python Logo](https://www.python.org/static/img/python-logo.png)](https://www.python.org/)

Data Structures in Python
- 1. Lists

      Definition: Ordered, mutable collections of items enclosed within square brackets [].
Properties:
Allow duplicate elements.
Support indexing and slicing.
Methods:
append(): Adds an element to the end of the list.
extend(): Adds elements from another list to the end of the list.
insert(): Inserts an element at a specified position.
remove(): Removes the first occurrence of a specified value.
pop(): Removes and returns the element at a specified index (default is the last element).
index(): Returns the index of the first occurrence of a specified value.
count(): Returns the number of occurrences of a specified value.
sort(): Sorts the list in ascending order.
reverse(): Reverses the order of elements in the list.

- 2. Tuples

     Definition: Immutable collections of items enclosed within parentheses ().
Properties:
Allow duplicate elements.
Support indexing and slicing.
Usage:
Suitable for representing fixed collections of data.
Often used for returning multiple values from a function.
- 3. Dictionaries

     Definition: Unordered collections of key-value pairs enclosed within curly braces {}.
Properties:
Keys must be unique and immutable (strings, numbers, tuples).
Values can be of any data type and mutable.
Methods:
get(): Returns the value associated with a specified key.
keys(): Returns a view of all the keys in the dictionary.
values(): Returns a view of all the values in the dictionary.
items(): Returns a view of all key-value pairs in the dictionary.
update(): Updates the dictionary with key-value pairs from another dictionary.
pop(): Removes and returns the value associated with a specified key.
popitem(): Removes and returns the last inserted key-value pair.
clear(): Removes all key-value pairs from the dictionary.
- 4. Sets

     Definition: Unordered collections of unique elements enclosed within curly braces {}.
Properties:
Do not allow duplicate elements.
Support mathematical set operations like union, intersection, difference. 

     Methods:
add(): Adds an element to the set.
remove(): Removes a specified element from the set.
discard(): Removes a specified element from the set if it is present.
pop(): Removes and returns an arbitrary element from the set.
clear(): Removes all elements from the set.
union(): Returns a new set containing all unique elements from both sets.
intersection(): Returns a new set containing elements that are common to both sets.
difference(): Returns a new set containing elements that are present in the first set but not in the second set.
symmetric_difference(): Returns a new set containing elements that are present in either set, but not in both.
- 5. Strings

     Definition: Sequences of characters enclosed within single quotes '', double quotes "", or triple quotes ''' '''.

     Properties:
Immutable (cannot be changed after creation).
Support indexing and slicing.

     Methods:
capitalize(): Converts the first character to uppercase.
lower(): Converts all characters to lowercase.
upper(): Converts all characters to uppercase.
strip(): Removes leading and trailing whitespace.
split(): Splits the string into a list of substrings based on a specified delimiter.
join(): Joins elements of an iterable into a string using the specified separator.
find(): Returns the index of the first occurrence of a specified substring.
replace(): Replaces occurrences of a specified substring with another substring.

- 6. Arrays

     Definition: Data structures that hold values of the same data type, provided by the array module.

     Properties:More memory-efficient than lists for numerical data.
Support array-specific operations like element-wise arithmetic operations.


- 7. Other Advanced Data Structures

     *Stacks*: Follow Last-In-First-Out (LIFO) principle. Elements are added (pushed) and removed (popped) from the same end.
 
     *Queues*: Follow First-In-First-Out (FIFO) principle. Elements are added (enqueued) at the rear and removed (dequeued) from the front.

     *Linked Lists*: Linear data structures where elements are stored in nodes with references to the next node.

     *Trees*: Hierarchical data structures with a root node and child nodes.

     *Graphs*: Non-linear data structures consisting of nodes and edges that represent connections.