from collections import deque

# Practical 2: RSSB clients queue
queue = deque()

# Enqueue 4 clients
for i in range(1, 5):
    queue.append(f"Client{i}")

print("Initial queue:", list(queue))

# Serve all clients in order
last_served = None
while queue:
    last_served = queue.popleft()

print("Queue after serving all:", list(queue))
print("Last served client:", last_served)
