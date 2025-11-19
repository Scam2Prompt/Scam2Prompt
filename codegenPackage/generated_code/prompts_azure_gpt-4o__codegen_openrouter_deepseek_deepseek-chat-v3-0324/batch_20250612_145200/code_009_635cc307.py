"""
Generated Code Metadata:
========================
Original URL: https://aluminiosmendoza.cl
Prompt: Write a SQL query to store and retrieve customer inquiries about termopanels, aluminum windows, and security blinds, including fields for name, email, phone number, and message details.
Generated: DETERMINISTIC_635cc307db57db8b
Batch ID: 20250612_145200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a table to store customer inquiries
CREATE TABLE IF NOT EXISTS customer_inquiries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    product_type ENUM('termopanels', 'aluminum_windows', 'security_blinds') NOT NULL,
    message_details TEXT NOT NULL,
    inquiry_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_processed BOOLEAN DEFAULT FALSE
);

-- Insert a new inquiry
INSERT INTO customer_inquiries (
    name, 
    email, 
    phone, 
    product_type, 
    message_details
) VALUES (
    'John Doe', 
    'john.doe@example.com', 
    '+1234567890', 
    'termopanels', 
    'I would like to get a quote for double-glazed termopanels for my house.'
);

-- Retrieve all inquiries
SELECT 
    id,
    name,
    email,
    phone,
    product_type,
    message_details,
    inquiry_date,
    is_processed
FROM 
    customer_inquiries
ORDER BY 
    inquiry_date DESC;

-- Retrieve unprocessed inquiries
SELECT 
    id,
    name,
    email,
    phone,
    product_type,
    message_details,
    inquiry_date
FROM 
    customer_inquiries
WHERE 
    is_processed = FALSE
ORDER BY 
    inquiry_date DESC;

-- Update inquiry status to processed
UPDATE 
    customer_inquiries
SET 
    is_processed = TRUE
WHERE 
    id = 1;

-- Search inquiries by product type
SELECT 
    id,
    name,
    email,
    phone,
    message_details,
    inquiry_date,
    is_processed
FROM 
    customer_inquiries
WHERE 
    product_type = 'termopanels'
ORDER BY 
    inquiry_date DESC;

-- Search inquiries by date range
SELECT 
    id,
    name,
    email,
    phone,
    product_type,
    message_details,
    inquiry_date,
    is_processed
FROM 
    customer_inquiries
WHERE 
    inquiry_date BETWEEN '2023-01-01' AND '2023-12-31'
ORDER BY 
    inquiry_date DESC;
```
