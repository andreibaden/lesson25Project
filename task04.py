students = {"Alex": 10, "Peter": 9, "Victor": 8,
            "Andrei": 7, "Kate": 6, "Nikita": 5}

print(students["Kate"])  # KeyError
print(students.get("Andy"))  # None
print(students.get("Andy", 0))  # 0
print(students["Alice"])  # KeyError
