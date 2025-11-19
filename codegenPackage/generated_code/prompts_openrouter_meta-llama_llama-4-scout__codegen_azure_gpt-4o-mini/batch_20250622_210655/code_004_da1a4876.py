"""
Generated Code Metadata:
========================
Original URL: https://scout.kz
Prompt: "Design a database schema to store information about SCOUT equipment, including tractor models, навесное оборудование, and customer details for an agricultural equipment dealership in Kazakhstan."
Generated: DETERMINISTIC_da1a4876b7875d1e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for SCOUT equipment management in an agricultural equipment dealership

-- Create a table to store information about tractor models
CREATE TABLE TractorModels (
    id SERIAL PRIMARY KEY, -- Unique identifier for each tractor model
    model_name VARCHAR(100) NOT NULL, -- Name of the tractor model
    manufacturer VARCHAR(100) NOT NULL, -- Manufacturer of the tractor
    year_of_manufacture INT CHECK (year_of_manufacture > 1900 AND year_of_manufacture <= EXTRACT(YEAR FROM CURRENT_DATE)), -- Year of manufacture
    horsepower INT NOT NULL, -- Horsepower of the tractor
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store information about навесное оборудование (attachments)
CREATE TABLE Attachments (
    id SERIAL PRIMARY KEY, -- Unique identifier for each attachment
    attachment_name VARCHAR(100) NOT NULL, -- Name of the attachment
    type VARCHAR(50) NOT NULL, -- Type of the attachment (e.g., plow, harrow)
    compatible_tractor_id INT REFERENCES TractorModels(id) ON DELETE CASCADE, -- Foreign key referencing compatible tractor model
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store customer details
CREATE TABLE Customers (
    id SERIAL PRIMARY KEY, -- Unique identifier for each customer
    first_name VARCHAR(50) NOT NULL, -- Customer's first name
    last_name VARCHAR(50) NOT NULL, -- Customer's last name
    phone_number VARCHAR(15) NOT NULL UNIQUE, -- Customer's phone number
    email VARCHAR(100) UNIQUE, -- Customer's email address
    address VARCHAR(255), -- Customer's address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store sales transactions
CREATE TABLE Sales (
    id SERIAL PRIMARY KEY, -- Unique identifier for each sale
    customer_id INT REFERENCES Customers(id) ON DELETE CASCADE, -- Foreign key referencing the customer
    tractor_model_id INT REFERENCES TractorModels(id) ON DELETE CASCADE, -- Foreign key referencing the tractor model sold
    attachment_id INT REFERENCES Attachments(id) ON DELETE SET NULL, -- Foreign key referencing the attachment sold (optional)
    sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the sale
    sale_price DECIMAL(10, 2) NOT NULL, -- Sale price of the tractor and/or attachment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Indexes for performance optimization
CREATE INDEX idx_tractor_model_name ON TractorModels(model_name);
CREATE INDEX idx_attachment_name ON Attachments(attachment_name);
CREATE INDEX idx_customer_last_name ON Customers(last_name);
CREATE INDEX idx_sale_date ON Sales(sale_date);
```
