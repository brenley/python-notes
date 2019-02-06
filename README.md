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
    
    # supposedly pretty efficient
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
  # a
  # 2
  # c
  
for i in range(len(alist)):
  print(i,alist[i])
  # (0, 'a')
  # (1, 2)
  # (2, 'c')
  
// searching
if "a" in alist:
  print("We found it!")
```

**Tuples**

Tuples are immutable.

```python
coords = (0, 25, 50)
x, y, z = coords # this is called unloading
print(x) # 0
print(y) # 25
print(z) # 50

x = -10
y = 30
z = 100

# can reassign the new values to the tuple (just can't change inline)
coords = (x, y, z)
```

Can convert a tuple to a list:

```python
mytuple = ("Hello", "world")
mylist = list(mytuple)
print(mylist) 
# ['Hello', 'world']
```

**Dictionaries**

Think maps.

```python
employee = {}
employee{"name"} = "Brenna"
employee{"age"} = 31
print(employee) # looks like JSON
# {'age': 31, 'name': 'Brenna'}

employee2 = {"name": "Brenna", "age": 31}
del employee2["age"]
print(employee2)
# {'name': 'Brenna'}
```

**Functions**

- Unless you use the `global` keyword, variables created inside a function only exist while its active

```python
def whatsMyName(name):
  print(name)
  return "Ludacris"
  
name = whatsMyName("Brenna")
# Brenna

print(name)
# Ludacris
```

`pass` is a valid exit command
```
def doNothing():
  pass
  
var huh = doNothing()
print(huh)
# none
```

You can also do some neat things with parameters, including calling them directly or setting defaults
```
def greet(firstname, job, hobby="do nothing")
  return "greetings {0}, when not at your {1} job, you like to {2}".format(firstname, job, hobby)
  
greet("brenna", "engineer", "snowboard")
# greeting brenna, when not at your engineer job, you like to snowboard
greet(job="engineer", firstname="brenna, hobby="snowboard")
# greeting brenna, when not at your engineer job, you like to snowboard
greet("brenna", "engineer")
# greeting brenna, when not at your engineer job, you like to do nothing

def print_args(* args):
  print("positional argument tuple", args)
  pritn("the third argument", args[2])

print_args(1, 3, 4)
# positional argument tuple (3, 6, 4)
# the third argument 4
  
def create_and_print_dict(** args):
  print("here is the dictionary that was created - hope you didn't think you could pass IN a dictionary", args)
  
create_and_print_dict(name="brenna", age=31)
# {'name': 'brenna', 'age': 31}
```

## Cute Things

- `import this`
- `from __future__ import braces`
