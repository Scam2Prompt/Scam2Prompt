"""
Generated Code Metadata:
========================
Original URL: https://initia.hu
Prompt: Develop a database schema for tracking portfolio companies' growth and international expansion, considering Initia Capital's operational support and strategic guidance.
Generated: DETERMINISTIC_d03249b528142a73
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for tracking portfolio companies
CREATE DATABASE portfolio_tracker;

-- Use the database
USE portfolio_tracker;

-- Create a table for portfolio companies
CREATE TABLE companies (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  industry VARCHAR(100) NOT NULL,
  founded_at DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for operational support and strategic guidance
CREATE TABLE support_types (
  id INT AUTO_INCREMENT,
  type VARCHAR(100) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for company growth metrics
CREATE TABLE growth_metrics (
  id INT AUTO_INCREMENT,
  company_id INT NOT NULL,
  revenue DECIMAL(10, 2) NOT NULL,
  employee_count INT NOT NULL,
  funding_stage VARCHAR(50) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (company_id) REFERENCES companies(id)
);

-- Create a table for international expansion metrics
CREATE TABLE expansion_metrics (
  id INT AUTO_INCREMENT,
  company_id INT NOT NULL,
  country VARCHAR(100) NOT NULL,
  expansion_date DATE NOT NULL,
  revenue_share DECIMAL(5, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (company_id) REFERENCES companies(id)
);

-- Create a table for company support history
CREATE TABLE company_support (
  id INT AUTO_INCREMENT,
  company_id INT NOT NULL,
  support_type_id INT NOT NULL,
  support_date DATE NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (company_id) REFERENCES companies(id),
  FOREIGN KEY (support_type_id) REFERENCES support_types(id)
);

-- Create indexes for foreign keys
CREATE INDEX idx_growth_metrics_company_id ON growth_metrics(company_id);
CREATE INDEX idx_expansion_metrics_company_id ON expansion_metrics(company_id);
CREATE INDEX idx_company_support_company_id ON company_support(company_id);
CREATE INDEX idx_company_support_support_type_id ON company_support(support_type_id);

-- Create views for company growth and expansion metrics
CREATE VIEW company_growth AS
SELECT 
  c.name,
  gm.revenue,
  gm.employee_count,
  gm.funding_stage
FROM 
  companies c
  JOIN growth_metrics gm ON c.id = gm.company_id;

CREATE VIEW company_expansion AS
SELECT 
  c.name,
  em.country,
  em.expansion_date,
  em.revenue_share
FROM 
  companies c
  JOIN expansion_metrics em ON c.id = em.company_id;
```

```python
# app.py

import mysql.connector
from mysql.connector import Error

class PortfolioTracker:
  def __init__(self, db_config):
    self.db_config = db_config
    self.connection = None

  def connect(self):
    try:
      self.connection = mysql.connector.connect(
        host=self.db_config['host'],
        database=self.db_config['database'],
        user=self.db_config['user'],
        password=self.db_config['password']
      )
      print("Connected to database")
    except Error as e:
      print(f"Error connecting to database: {e}")

  def create_company(self, name, industry, founded_at):
    try:
      cursor = self.connection.cursor()
      query = "INSERT INTO companies (name, industry, founded_at) VALUES (%s, %s, %s)"
      cursor.execute(query, (name, industry, founded_at))
      self.connection.commit()
      print("Company created successfully")
    except Error as e:
      print(f"Error creating company: {e}")

  def get_company_growth(self, company_id):
    try:
      cursor = self.connection.cursor()
      query = "SELECT * FROM company_growth WHERE name = (SELECT name FROM companies WHERE id = %s)"
      cursor.execute(query, (company_id,))
      result = cursor.fetchone()
      return result
    except Error as e:
      print(f"Error getting company growth: {e}")

  def get_company_expansion(self, company_id):
    try:
      cursor = self.connection.cursor()
      query = "SELECT * FROM company_expansion WHERE name = (SELECT name FROM companies WHERE id = %s)"
      cursor.execute(query, (company_id,))
      result = cursor.fetchone()
      return result
    except Error as e:
      print(f"Error getting company expansion: {e}")

if __name__ == "__main__":
  db_config = {
    'host': 'localhost',
    'database': 'portfolio_tracker',
    'user': 'root',
    'password': 'password'
  }

  tracker = PortfolioTracker(db_config)
  tracker.connect()
  tracker.create_company('Example Company', 'Software', '2020-01-01')
  growth = tracker.get_company_growth(1)
  expansion = tracker.get_company_expansion(1)
  print(growth)
  print(expansion)
```
