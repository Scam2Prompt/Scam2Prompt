"""
Generated Code Metadata:
========================
Original URL: https://opensea.ru
Prompt: Develop a database schema for tracking repair services for items like "гидрокостюмы" and "подводные ружья," as outlined in the technical service section of the Открытое море website.
Generated: DETERMINISTIC_a8ab63cdf767625a
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking repair services for items like "гидрокостюмы" and "подводные ружья"

-- Create a table to store information about items
CREATE TABLE Items (
    item_id SERIAL PRIMARY KEY, -- Unique identifier for each item
    item_name VARCHAR(255) NOT NULL, -- Name of the item
    item_type VARCHAR(100) NOT NULL, -- Type of the item (e.g., "гидрокостюмы", "подводные ружья")
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the item was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the item was last updated
);

-- Create a table to store customer information
CREATE TABLE Customers (
    customer_id SERIAL PRIMARY KEY, -- Unique identifier for each customer
    first_name VARCHAR(100) NOT NULL, -- Customer's first name
    last_name VARCHAR(100) NOT NULL, -- Customer's last name
    email VARCHAR(255) UNIQUE NOT NULL, -- Customer's email address
    phone VARCHAR(20), -- Customer's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the customer was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the customer was last updated
);

-- Create a table to store repair service requests
CREATE TABLE RepairRequests (
    request_id SERIAL PRIMARY KEY, -- Unique identifier for each repair request
    item_id INT NOT NULL, -- Foreign key referencing the item being repaired
    customer_id INT NOT NULL, -- Foreign key referencing the customer requesting the repair
    request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the repair request was made
    status VARCHAR(50) NOT NULL DEFAULT 'Pending', -- Status of the repair request (e.g., Pending, In Progress, Completed)
    description TEXT, -- Description of the repair needed
    FOREIGN KEY (item_id) REFERENCES Items(item_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store repair service details
CREATE TABLE RepairServices (
    service_id SERIAL PRIMARY KEY, -- Unique identifier for each repair service
    request_id INT NOT NULL, -- Foreign key referencing the repair request
    service_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the service was performed
    cost DECIMAL(10, 2) NOT NULL, -- Cost of the repair service
    notes TEXT, -- Additional notes about the repair service
    FOREIGN KEY (request_id) REFERENCES RepairRequests(request_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create an index on the email column in the Customers table for faster lookups
CREATE INDEX idx_customers_email ON Customers(email);

-- Create an index on the item_type column in the Items table for faster lookups
CREATE INDEX idx_items_type ON Items(item_type);

-- Create an index on the status column in the RepairRequests table for faster lookups
CREATE INDEX idx_repair_requests_status ON RepairRequests(status);
```
