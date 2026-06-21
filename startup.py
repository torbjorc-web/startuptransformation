import codecademylib3
from sklearn import preprocessing
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


# load in financial data
financial_data = pd.read_csv('financial_data.csv')


# Task 1
print(financial_data.head())

# Task 2
month = financial_data["Month"]
revenue = financial_data["Revenue"]
expenses = financial_data["Expenses"]

# Task 3 and 4
plt.plot(month, revenue)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Revenue')
plt.show()

# Task 5
plt.clf()
plt.plot(month, expenses)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Expenses')
plt.show()

# Task 6
expense_overview = pd.read_csv('expenses.csv')
print(expense_overview.head(7))

# Task 7
expense_categories = expense_overview["Expense"]
proportions = expense_overview["Proportion"]

# Task 8 and 9
plt.clf()
plt.pie(proportions, labels=expense_categories)
plt.title("Expenses Breakdown")
plt.axis('equal')
plt.tight_layout()
plt.show()

# Task 10
expense_categories_updated = ["Salaries", "Advertising", "Office Rent", "Other"]
other = proportions[proportions < 5].sum()
proportions_updated = [62, 15, 19, other]

plt.clf()
plt.pie(proportions_updated, labels=expense_categories_updated)
plt.title("Expenses Breakdown")
plt.axis('equal')
plt.tight_layout()
plt.show()

# Task 11
expense_cut = "Salaries"

# Task 12
employees = pd.read_csv("employees.csv")
print(employees.head())

# Task 13
sorted_productivity = employees.sort_values(by=["Productivity"])
print(sorted_productivity)

# Task 14
employees_cut = sorted_productivity.head(100)
print(employees_cut)

# Task 15
transformation = "standardization"

# Task 16
commute_times = employees["Commute Time"]

# Task 17
print(commute_times.describe())

# Task 18
plt.clf()
plt.hist(commute_times)
plt.xlabel("Commute Time")
plt.ylabel("Frequency")
plt.title("Commute Times")
plt.show()

# Task 19
commute_times_log = np.log(commute_times)

# Task 20
plt.clf()
plt.hist(commute_times_log)
plt.xlabel("Log of Commute Time")
plt.ylabel("Frequency")
plt.title("Log-Transformed Commute Times")
plt.show()
