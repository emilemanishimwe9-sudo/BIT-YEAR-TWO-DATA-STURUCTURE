# Practical 1: Stack Example (UR quizzes)
stack = []  

# Push operations
stack.append("Quiz1")
stack.append("Quiz2")
stack.append("Quiz3")

print("Stack after pushes:", stack)

# Undo one (pop)
stack.pop()

print("Stack after undo:", stack)
print("Top of stack:", stack[-1] if stack else "Empty")
