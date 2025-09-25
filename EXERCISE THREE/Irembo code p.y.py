# Practical 2: Stack Example (Irembo steps)
stack = []

# Push operations
stack.append("Step1")
stack.append("Step2")
stack.append("Step3")

print("Stack after pushes:", stack)

# Pop all
stack.pop()
stack.pop()
stack.pop()

print("Stack after popping all:", stack)
print("Remaining element:", "Empty" if not stack else stack[-1])
