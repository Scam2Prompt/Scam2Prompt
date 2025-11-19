"""
Generated Code Metadata:
========================
Original URL: https://aaronrojo.com
Prompt: "Design a database schema to store client information and financial plans for a World Financial Group agent, including fields for insurance products and retirement income strategies."
Generated: DETERMINISTIC_2924ca8f86c4f692
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for World Financial Group agent

-- Create database
CREATE DATABASE world_financial_group;

-- Use database
USE world_financial_group;

-- Create table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  date_of_birth DATE NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create table for financial plans
CREATE TABLE financial_plans (
  plan_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  plan_name VARCHAR(255) NOT NULL,
  plan_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (plan_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create table for insurance products
CREATE TABLE insurance_products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  premium DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id)
);

-- Create table for client insurance products
CREATE TABLE client_insurance_products (
  client_id INT NOT NULL,
  product_id INT NOT NULL,
  policy_number VARCHAR(255) NOT NULL,
  coverage_amount DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id, product_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
  FOREIGN KEY (product_id) REFERENCES insurance_products(product_id) ON DELETE CASCADE
);

-- Create table for retirement income strategies
CREATE TABLE retirement_income_strategies (
  strategy_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  strategy_name VARCHAR(255) NOT NULL,
  strategy_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (strategy_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create table for client meetings
CREATE TABLE client_meetings (
  meeting_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  meeting_date DATE NOT NULL,
  meeting_notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (meeting_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create indexes on foreign keys
CREATE INDEX idx_financial_plans_client_id ON financial_plans(client_id);
CREATE INDEX idx_client_insurance_products_client_id ON client_insurance_products(client_id);
CREATE INDEX idx_client_insurance_products_product_id ON client_insurance_products(product_id);
CREATE INDEX idx_retirement_income_strategies_client_id ON retirement_income_strategies(client_id);
CREATE INDEX idx_client_meetings_client_id ON client_meetings(client_id);
```

```sql
-- Example insert statements

INSERT INTO clients (first_name, last_name, date_of_birth, email, phone_number, address)
VALUES ('John', 'Doe', '1990-01-01', 'john.doe@example.com', '123-456-7890', '123 Main St');

INSERT INTO financial_plans (client_id, plan_name, plan_description)
VALUES (1, 'Retirement Plan', 'Plan for retirement savings');

INSERT INTO insurance_products (product_name, product_description, premium)
VALUES ('Life Insurance', 'Life insurance policy', 100.00);

INSERT INTO client_insurance_products (client_id, product_id, policy_number, coverage_amount)
VALUES (1, 1, 'POL12345', 500000.00);

INSERT INTO retirement_income_strategies (client_id, strategy_name, strategy_description)
VALUES (1, 'Annuity Strategy', 'Strategy for retirement income');

INSERT INTO client_meetings (client_id, meeting_date, meeting_notes)
VALUES (1, '2022-01-01', 'Initial meeting with client');
```
