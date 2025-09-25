import array

# ------------------ Integers ------------------
usage_counts = [25, 30, 28, 32, 27, 35, 29]
total_usage = sum(usage_counts)
average_usage = total_usage / len(usage_counts)
min_usage = min(usage_counts)
max_usage = max(usage_counts)

# ------------------ Strings ------------------
report = f"Computer Lab Usage Report\n" \
         f"Total Usage: {total_usage}\n" \
         f"Average Usage: {average_usage:.2f}\n" \
         f"Minimum Usage: {min_usage}\n" \
         f"Maximum Usage: {max_usage}\n"
print(report)

# ------------------ Booleans ------------------
threshold = 28
if average_usage > threshold and max_usage > 30:
    print("Status: Above Standard")
else:
    print("Status: Below Standard")

# ------------------ Lists ------------------
lab_users = ["Alice", "Bob", "Charlie", "Diana"]
print("Before modifications:", lab_users)

# Add new element
lab_users.append("Ethan")
# Remove one element based on a condition
if "Bob" in lab_users:
    lab_users.remove("Bob")
# Sort list
lab_users.sort()
print("After modifications:", lab_users)

# ------------------ Arrays ------------------
usage_array = array.array('i', [25, 30, 28, 32])
array_sum = sum(usage_array)
list_sum = sum(usage_counts[:4])
print(f"Array sum: {array_sum}, List sum: {list_sum}")

# ------------------ Dictionaries ------------------
lab_records = [
    {"id": 1, "name": "Alice", "value": 25},
    {"id": 2, "name": "Bob", "value": 30},
    {"id": 3, "name": "Charlie", "value": 28},
]

# Update one record
lab_records[0]["value"] = 26
# Delete another
lab_records = [record for record in lab_records if record["name"] != "Bob"]
# Compute total
records_total = sum(record["value"] for record in lab_records)
print("Updated Lab Records:", lab_records)
print("Total of values in records:", records_total)
