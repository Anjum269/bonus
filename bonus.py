import sys

# Take salary from command line
salary = float(sys.argv[1])

# Calculate 10% bonus
bonus = salary * 0.10
total = salary + bonus

# Display results
print("----- Salary Bonus Calculator -----")
print("Salary:", salary)
print("Bonus (10%):", bonus)
print("Total Salary after Bonus:", total)
