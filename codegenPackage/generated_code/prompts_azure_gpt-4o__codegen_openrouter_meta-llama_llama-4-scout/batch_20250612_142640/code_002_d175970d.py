"""
Generated Code Metadata:
========================
Original URL: https://rhinoassetfinance.com
Prompt: Develop a database schema for tracking asset finance deals across multiple industries, including fields for asset types like amusement rides, commercial mortgages, and plant equipment, as mentioned on Rhino Asset Finance.
Generated: DETERMINISTIC_d175970df52e618f
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for asset finance deals
CREATE DATABASE asset_finance;

-- Use the asset_finance database
USE asset_finance;

-- Create a table for industries
CREATE TABLE industries (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for asset types
CREATE TABLE asset_types (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  industry_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (industry_id) REFERENCES industries(id)
);

-- Create a table for assets
CREATE TABLE assets (
  id INT AUTO_INCREMENT,
  asset_type_id INT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (asset_type_id) REFERENCES asset_types(id)
);

-- Create a table for finance deals
CREATE TABLE finance_deals (
  id INT AUTO_INCREMENT,
  asset_id INT,
  deal_type VARCHAR(255) NOT NULL,
  deal_amount DECIMAL(10, 2) NOT NULL,
  interest_rate DECIMAL(5, 2) NOT NULL,
  term_in_years INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (asset_id) REFERENCES assets(id)
);

-- Create a table for clients
CREATE TABLE clients (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone VARCHAR(20),
  address TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for client finance deals
CREATE TABLE client_finance_deals (
  id INT AUTO_INCREMENT,
  client_id INT,
  finance_deal_id INT,
  deal_status VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (client_id) REFERENCES clients(id),
  FOREIGN KEY (finance_deal_id) REFERENCES finance_deals(id)
);

-- Insert sample data
INSERT INTO industries (name, description)
VALUES
  ('Amusement', 'Amusement park industry'),
  ('Commercial', 'Commercial property industry'),
  ('Plant Equipment', 'Plant equipment industry');

INSERT INTO asset_types (name, description, industry_id)
VALUES
  ('Amusement Rides', 'Amusement rides for parks', 1),
  ('Commercial Mortgages', 'Commercial property mortgages', 2),
  ('Plant Equipment', 'Plant equipment for industries', 3);

INSERT INTO assets (asset_type_id, name, description)
VALUES
  (1, 'Roller Coaster', 'A roller coaster for amusement parks'),
  (2, 'Office Building', 'An office building for commercial use'),
  (3, 'Crane', 'A crane for plant equipment');

INSERT INTO finance_deals (asset_id, deal_type, deal_amount, interest_rate, term_in_years)
VALUES
  (1, 'Lease', 100000.00, 5.00, 5),
  (2, 'Mortgage', 500000.00, 4.00, 10),
  (3, 'Loan', 200000.00, 6.00, 3);

INSERT INTO clients (name, email, phone, address)
VALUES
  ('John Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
  ('Jane Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St');

INSERT INTO client_finance_deals (client_id, finance_deal_id, deal_status)
VALUES
  (1, 1, 'Approved'),
  (2, 2, 'Pending'),
  (1, 3, 'Rejected');
```
