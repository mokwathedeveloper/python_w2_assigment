
# Step 1: Create an empty list called my_list.
my_list = []
print(f"Step 1: Created an empty list: {my_list}")

# Step 2: Append the following elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"Step 2: Appended 10, 20, 30, 40: {my_list}")

# Step 3: Insert the value 15 at the second position in the list.
my_list.insert(1, 15)
print(f"Step 3: Inserted 15 at the second position: {my_list}")

# Step 4: Extend my_list with another list: [50, 60, 70].
my_list.extend([50, 60, 70])
print(f"Step 4: Extended with [50, 60, 70]: {my_list}")

# Step 5: Remove the last element from my_list.
my_list.pop()
print(f"Step 5: Removed the last element: {my_list}")

# Step 6: Sort my_list in ascending order.
my_list.sort()
print(f"Step 6: Sorted the list in ascending order: {my_list}")

# Step 7: Find and print the index of the value 30 in my_list.
index_of_30 = my_list.index(30)
print(f"Step 7: The index of 30 is: {index_of_30}")
