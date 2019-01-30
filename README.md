## Control Structures

Things will look pretty familiar here, with the absence of a switch statement.

**If**

```

```

**While**

**For**

## Data Structures

**List**

Python calls these lists, not arrays! As any sane language, indexing starts at 0.

- `list.append(value)`
- `list.extend(other_list)`
- `list.insert(i, value)`
- `list.remove(value)` - remove the first instance of value
- `list.pop()` - remove item from end of list and return it
- `list.sort()` - sorts the actual list (does not return a copy)
- `list.len()` or `len(list)`

```python
newlist = ["Hello", 23, "some string", 3.14, 223355]
print(newlist)

newlist2 = []
newlist2.append("banana")
newlist2.extend(["literal", 3.14])
print(newlist2)
```

## Cute Things

- `import this`
