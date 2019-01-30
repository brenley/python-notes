## Control Structures

Things will look pretty familiar here, with the absence of a switch statement.

**If**

```

```

**While**

**For**

## Data Structures

**Lists**

Python calls these lists, not arrays! As any sane language, indexing starts at 0.

- `alist.append(value)`
- `alist.extend(other_list)`
- `alist.insert(i, value)`
- `alist.remove(value)` - remove the first instance of value
- `del alist[value]`
- `alist.pop()` - remove item from end of list and return it
- `alist.sort()` - sorts the actual list (does not return a copy)
- `alist.len()` or `len(list)`
- `alist[2:]` - returns index 2 to the end
- `alist[1:3]` - returns from index 1 to 3
- `newlist = oldlist` - copies a list by reference
  - `newlist[0] = 3` also mutates `oldlist`!
  - To copy a list by value:
    ```python
    from copy import deepcopy
    
    // supposedly pretty efficient
    newlist = deepcopy(oldlist)
    ```
 - `alist.split(".")`

```python
newlist = ["Hello", 23, "some string", 3.14, 223355]
print(newlist)

newlist2 = []
newlist2.append("banana")
newlist2.extend(["literal", 3.14])
print(newlist2)
```

There is also some cool list comprehension functionality

```python
alist = ["a", 2, "c"]

for item in alist:
  print(item)
  // a
  // 2
  // c
  
for i in range(len(alist)):
  print(i,alist[i])
  // (0, 'a')
  // (1, 2)
  // (2, 'c')
  
// searching
if "a" in alist:
  print("We found it!")
```

**Tuples**

Tuples are immutable.

```python
coords = (0, 25, 50)
x, y, z = coords // this is called unloading
print(x) // 0
print(y) // 25
print(z) // 50

x = -10
y = 30
z = 100

// can reassign the new values to the tuple (just can't change inline)
coords = (x, y, z)
```

Can convert a tuple to a list:

```python
mytuple = ("Hello", "world")
mylist = list(mytuple)
print(mylist) 
// ['Hello', 'world']
```

## Cute Things

- `import this`
