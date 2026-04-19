from itertools import zip_longest

def zip_longest_list(list1, list2):
    return list(zip_longest(list1, list2))

list1 = [1, 2, 3]
list2 = ['a', 'b']

print(zip_longest_list(list1, list2))
```

```python
from itertools import zip_longest

def zip_longest_list(list1, list2):
    return list(zip_longest(list1, list2))

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd']

print(zip_longest_list(list1, list2))
