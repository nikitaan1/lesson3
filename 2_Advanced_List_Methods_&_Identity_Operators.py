
#Task 1 
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

sub_att = submitted + attended


submitted = sub_att.count("Alice"), sub_att.count("Bob"), sub_att.count("Charlie"), sub_att.count("David")


print(submitted)

#Task 2

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

print(submitted == attended)

#Task 3

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

attended.remove("Eve")
attended.remove("Frank")
print(attended)