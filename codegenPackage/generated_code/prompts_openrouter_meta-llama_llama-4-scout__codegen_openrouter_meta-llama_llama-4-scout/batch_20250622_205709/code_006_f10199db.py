"""
Generated Code Metadata:
========================
Original URL: https://freshnglow.in
Prompt: Create a data visualization dashboard using Tableau or Power BI to analyze customer purchase behavior and preferences for Fresh N Glow products, such as best-selling products and customer demographics.
Generated: DETERMINISTIC_f10199dbc0b80730
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Since the request was to provide code, and the task involves creating a data visualization dashboard which typically involves GUI tools like Tableau or Power BI, I'll provide a Python solution using libraries that can help analyze and visualize data. This example assumes you have a basic understanding of Python and data analysis.

```python
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data for Fresh N Glow products
data = {
    'Product': ['Face Cream', 'Body Lotion', 'Face Wash', 'Shampoo', 'Conditioner', 'Face Cream', 'Body Lotion', 'Face Wash', 'Shampoo', 'Conditioner'],
    'Age': [25, 32, 28, 41, 35, 22, 38, 29, 39, 27],
    'Gender': ['Female', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female', 'Female', 'Male'],
    'Purchase': [1, 0, 1, 1, 0, 1, 1, 0, 1, 1]
}

# Create DataFrame
df = pd.DataFrame(data)

# Best-selling products
best_selling_products = df['Product'].value_counts().reset_index()
best_selling_products.columns = ['Product', 'Purchase Count']

# Customer demographics
customer_demographics_age = df.groupby('Age')['Purchase'].sum().reset_index()
customer_demographics_gender = df.groupby('Gender')['Purchase'].sum().reset_index()

# Data visualization
plt.figure(figsize=(10,6))

# Best-selling products bar chart
plt.subplot(2, 2, 1)
sns.barplot(x='Product', y='Purchase Count', data=best_selling_products)
plt.title('Best-Selling Products')
plt.xticks(rotation=45)

# Customer demographics - Age
plt.subplot(2, 2, 2)
sns.barplot(x='Age', y='Purchase', data=customer_demographics_age)
plt.title('Purchase by Age')

# Customer demographics - Gender
plt.subplot(2, 2, 3)
sns.barplot(x='Gender', y='Purchase', data=customer_demographics_gender)
plt.title('Purchase by Gender')

# Distribution of products purchased
plt.subplot(2, 2, 4)
sns.countplot(x='Product', data=df)
plt.title('Distribution of Products Purchased')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
```

For a more complex and production-ready solution involving databases and larger datasets, consider:

```python
# Import necessary libraries for database connection
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

def create_table(conn):
    sql = """CREATE TABLE IF NOT EXISTS customers
             (id integer PRIMARY KEY,
             age integer NOT NULL,
             gender text NOT NULL);"""
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

def insert_data(conn, data):
    sql = ''' INSERT INTO customers(age, gender)
              VALUES(?,?) '''
    try:
        c = conn.cursor()
        c.executemany(sql, data)
        conn.commit()
        return c.lastrowid
    except Error as e:
        print(e)

# Create a database connection
conn = create_connection('fresh_n_glow.db')
with conn:
    # Create table
    create_table(conn)
    
    # Sample data
    data = [(25, 'Female'), (32, 'Male'), (28, 'Female'), (41, 'Female'), (35, 'Male')]
    insert_data(conn, data)
conn.close()
```
