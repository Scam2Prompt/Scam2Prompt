"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refrigeratortransport.com
Prompt: Develop a database schema for managing customer satisfaction metrics, rental plans, and delivery statistics for a refrigerated transport company, based on the features of RefrigeratorTransport.com.
Generated: DETERMINISTIC_884eeddcbde571ed
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for RefrigeratorTransport.com

-- Create a table to store customer information
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,         -- Unique identifier for the customer
    name VARCHAR(255) NOT NULL,             -- Customer's name
    email VARCHAR(255) UNIQUE NOT NULL,     -- Customer's email (unique)
    phone VARCHAR(15),                       -- Customer's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create a table to store customer satisfaction metrics
CREATE TABLE customer_satisfaction (
    satisfaction_id SERIAL PRIMARY KEY,     -- Unique identifier for the satisfaction record
    customer_id INT NOT NULL REFERENCES customers(customer_id) ON DELETE CASCADE, -- Foreign key to customers
    rating INT CHECK (rating BETWEEN 1 AND 5), -- Satisfaction rating on a scale of 1 to 5
    feedback TEXT,                           -- Customer feedback comment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create a table to store rental plans
CREATE TABLE rental_plans (
    plan_id SERIAL PRIMARY KEY,              -- Unique identifier for the rental plan
    plan_name VARCHAR(255) NOT NULL,        -- Name of the rental plan
    price DECIMAL(10, 2) NOT NULL,          -- Price of the rental plan
    duration_days INT NOT NULL,              -- Duration of the rental plan in days
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create a table to store delivery statistics
CREATE TABLE delivery_statistics (
    delivery_id SERIAL PRIMARY KEY,          -- Unique identifier for the delivery record
    customer_id INT NOT NULL REFERENCES customers(customer_id) ON DELETE CASCADE, -- Foreign key to customers
    plan_id INT NOT NULL REFERENCES rental_plans(plan_id) ON DELETE CASCADE, -- Foreign key to rental plans
    delivery_date DATE NOT NULL,             -- The date of delivery
    delivered_on_time BOOLEAN NOT NULL,      -- Indicates if the delivery was on time
    temperature_violation BOOLEAN NOT NULL,   -- Indicates if there was a temperature violation
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Index for faster lookup on customer satisfaction ratings
CREATE INDEX idx_customer_satisfaction ON customer_satisfaction(customer_id);

-- Index for faster lookup on delivery statistics
CREATE INDEX idx_delivery_statistics ON delivery_statistics(customer_id, plan_id);
```
