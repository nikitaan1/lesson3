
#Task 1 
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

if submitted[0] in attended:
    print("Alice")
if submitted[1] in attended: 
    print("Bob")
if submitted[2] in attended: 
    print("Charlie")
if submitted[3] in attended:
    print("David")

#Task 2

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

if "Alice" in attended and "Bob" in attended and  "Charlie" in attended and  "David" in attended:
    print("Lists Are The Same")
else:
    print("Listis Are Different")

#Task 3

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

attended.remove("Eve")
attended.remove("Frank")
print(attended)