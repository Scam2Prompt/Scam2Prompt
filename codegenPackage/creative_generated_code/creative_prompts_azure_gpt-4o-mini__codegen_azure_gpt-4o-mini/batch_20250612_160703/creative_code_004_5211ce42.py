"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stars-ksa.com
Prompt: Design a database schema for managing customer inquiries and service requests for a cleaning company, inspired by the contact methods used by Star Cleaning Services.
Generated: DETERMINISTIC_5211ce42a09ac979
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Managing Customer Inquiries and Service Requests for a Cleaning Company

-- Create a table to store customer information
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY, -- Unique identifier for each customer
    first_name VARCHAR(50) NOT NULL, -- Customer's first name
    last_name VARCHAR(50) NOT NULL,  -- Customer's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Customer's email address
    phone VARCHAR(15), -- Customer's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create a table to store service requests
CREATE TABLE service_requests (
    request_id SERIAL PRIMARY KEY, -- Unique identifier for each service request
    customer_id INT REFERENCES customers(customer_id) ON DELETE CASCADE, -- Foreign key linking to customers
    service_type VARCHAR(100) NOT NULL, -- Type of cleaning service requested
    request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the request
    status VARCHAR(20) DEFAULT 'Pending', -- Status of the service request (e.g., Pending, In Progress, Completed)
    notes TEXT, -- Additional notes by the customer or staff
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record last updated timestamp
);

-- Create a table to store customer inquiries
CREATE TABLE customer_inquiries (
    inquiry_id SERIAL PRIMARY KEY, -- Unique identifier for each inquiry
    customer_id INT REFERENCES customers(customer_id) ON DELETE SET NULL, -- Foreign key linking to customers
    inquiry_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the inquiry
    inquiry_type VARCHAR(50) NOT NULL, -- Type of inquiry (e.g., General, Pricing, Availability)
    inquiry_message TEXT NOT NULL, -- Customer's inquiry message
    response TEXT, -- Response from the service team
    response_date TIMESTAMP -- Date and time the response was sent
);

-- Create a table to store all contact methods used by the cleaning company
CREATE TABLE contact_methods (
    contact_id SERIAL PRIMARY KEY, -- Unique identifier for each contact method
    method_name VARCHAR(50) NOT NULL, -- Name of the contact method (e.g., Phone, Email, Website)
    is_active BOOLEAN DEFAULT TRUE -- Indicates if the contact method is currently active
);

-- Create a linking table to associate service requests and contact methods
CREATE TABLE service_request_contact_methods (
    request_id INT REFERENCES service_requests(request_id) ON DELETE CASCADE, -- Foreign key linking to service requests
    contact_id INT REFERENCES contact_methods(contact_id) ON DELETE CASCADE, -- Foreign key linking to contact methods
    PRIMARY KEY (request_id, contact_id) -- Composite primary key
);

-- Example of inserting contact methods
INSERT INTO contact_methods (method_name) VALUES
('Phone'),
('Email'),
('Website Form');

-- Note: Make sure to handle any potential errors during insertion, updates, or deletions
-- by implementing appropriate error handling in your application code.
```
