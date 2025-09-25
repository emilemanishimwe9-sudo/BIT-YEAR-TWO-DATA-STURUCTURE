from collections import deque

# Practical 1: CHUK patients queue
queue = deque()

# Enqueue 9 patients
for i in range(1, 10):
    queue.append(f"Patient{i}")

print("Initial queue:", list(queue))

# Serve 5 patients (dequeue)
for _ in range(5):
    queue.popleft()

print("Queue after serving 5:", list(queue))
print("Front of the queue now:", queue[0])
