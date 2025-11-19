"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spanglerroofingllc.com
Prompt: Design a database schema using SQL for storing customer reviews and service requests for a roofing company, focusing on fields like customer name, service type, and satisfaction rating.
Generated: DETERMINISTIC_bb34b21a6b88fed9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for a roofing company to store customer reviews and service requests

-- Create table for Customers
CREATE TABLE Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each customer
    customer_name VARCHAR(100) NOT NULL,         -- Name of the customer
    customer_email VARCHAR(100) UNIQUE,          -- Email of the customer, must be unique
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer record was created
);

-- Create table for ServiceTypes
CREATE TABLE ServiceTypes (
    service_type_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service type
    service_name VARCHAR(100) NOT NULL,              -- Name of the service (e.g., roof repair, installation)
    description TEXT                                  -- Description of the service
);

-- Create table for Reviews
CREATE TABLE Reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each review
    customer_id INT NOT NULL,                        -- Identifier for the customer who left the review
    service_type_id INT NOT NULL,                    -- Identifier for the service related to the review
    satisfaction_rating INT CHECK (satisfaction_rating BETWEEN 1 AND 5), -- Rating from 1 to 5
    review_text TEXT,                                -- Text of the review
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE, -- Link to Customers table
    FOREIGN KEY (service_type_id) REFERENCES ServiceTypes(service_type_id) ON DELETE CASCADE -- Link to ServiceTypes table
);

-- Create table for ServiceRequests
CREATE TABLE ServiceRequests (
    request_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each service request
    customer_id INT NOT NULL,                        -- Identifier for the customer making the request
    service_type_id INT NOT NULL,                    -- Identifier for the requested service type
    request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the service request was made
    status VARCHAR(20) CHECK (status IN ('Pending', 'In Progress', 'Completed', 'Cancelled')), -- Status of the service request
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE, -- Link to Customers table
    FOREIGN KEY (service_type_id) REFERENCES ServiceTypes(service_type_id) ON DELETE CASCADE -- Link to ServiceTypes table
);
```
