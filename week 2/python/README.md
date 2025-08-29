# Python List Operations Assignment

## ✨ Introduction
This project is a simple Python exercise that demonstrates how to perform basic operations on **lists**.  
Lists are an important data structure in Python because they allow us to store and manage multiple items in a single variable.

---

## 📝 Task Breakdown
The assignment requires the following steps:

1. **Create an empty list** called `my_list`.
2. **Append** the elements `10, 20, 30, 40` to the list.
3. **Insert** the value `15` at the second position.
4. **Extend** the list with another list: `[50, 60, 70]`.
5. **Remove** the last element from the list.
6. **Sort** the list in ascending order.
7. **Find and print** the index of the value `30`.

---

## 📂 Code Implementation

```python
# Step 1: Create an empty list
my_list = []

# Step 2: Append elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Step 3: Insert 15 at the second position (index 1)
my_list.insert(1, 15)

# Step 4: Extend with [50, 60, 70]
my_list.extend([50, 60, 70])

# Step 5: Remove the last element
my_list.pop()

# Step 6: Sort in ascending order
my_list.sort()

# Step 7: Find and print index of 30
index_of_30 = my_list.index(30)
print("Final list:", my_list)
print("Index of 30:", index_of_30)
