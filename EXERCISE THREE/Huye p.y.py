stack = []

# Step 1: Push 1, 2, 3
stack.append("1")
stack.append("2")
stack.append("3")
print("After pushes:", stack)

# Step 2: Pop two
stack.pop()
stack.pop()
print("After popping 2:", stack)

# Step 3: Push 4
stack.append("4")
print("After pushing 4:", stack)

# Step 4: Show top
print("Top of stack:", stack[-1])
