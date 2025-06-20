import pandas as pd
import numpy as np

data = pd.read_csv("expenses.csv")

data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)

print("\nAll Expenses:\n")
print(data)

total_amount = np.sum(data['Amount'])
print("\nTotal Money Spent:")
print(total_amount)

highest = data.loc[data['Amount'].idxmax()]
print("\nHighest Expense:")
print("Date:", highest['Date'])
print("Category:", highest['Category'])
print("Amount:", highest['Amount'])
print("Description:", highest['Description'])

lowest = data.loc[data['Amount'].idxmin()]
print("\nLowest Expense:")
print("Date:", lowest['Date'])
print("Category:", lowest['Category'])
print("Amount:", lowest['Amount'])
print("Description:", lowest['Description'])

category_total = data.groupby('Category')['Amount'].sum()
category_count = data['Category'].value_counts()
percentage = (category_total / total_amount) * 100

print("\nTotal Spent in Each Category:")
print(category_total)

print("\nNumber of Expenses in Each Category:")
print(category_count)

print("\nPercentage of Spending by Category:")
print(percentage.round(2))