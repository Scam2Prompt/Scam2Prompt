"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aluminiosmendoza.cl
Prompt: Write a SQL query to store and retrieve customer inquiries about termopanels, aluminum windows, and security blinds, including fields for name, email, phone number, and message details.
Generated: DETERMINISTIC_635cc307db57db8b
Batch ID: 20250612_145200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a table to store customer inquiries
CREATE TABLE CustomerInquiries (
    InquiryID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each inquiry
    Name VARCHAR(100) NOT NULL,                     -- Customer's name (required)
    Email VARCHAR(100) NOT NULL,                    -- Customer's email (required)
    PhoneNumber VARCHAR(15),                        -- Customer's phone number (optional)
    MessageDetails TEXT NOT NULL,                   -- Details of the inquiry (required)
    InquiryCategory ENUM('Termopanels', 'Aluminum Windows', 'Security Blinds') NOT NULL, -- Inquiry category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Timestamp for when the inquiry was created
);

-- Insert a new customer inquiry into the table
INSERT INTO CustomerInquiries (Name, Email, PhoneNumber, MessageDetails, InquiryCategory)
VALUES 
    ('John Doe', 'john.doe@example.com', '123-456-7890', 'I would like more details about termopanels.', 'Termopanels');

-- Retrieve all customer inquiries from the table
SELECT 
    InquiryID, 
    Name, 
    Email, 
    PhoneNumber, 
    MessageDetails, 
    InquiryCategory, 
    CreatedAt 
FROM 
    CustomerInquiries
ORDER BY CreatedAt DESC; -- Order inquiries by creation date (latest first)

-- Error handling considerations:
-- 1. Ensure proper validation and sanitization of inputs at the application level to prevent SQL injection.
-- 2. Use prepared statements in the application code for inserting data into the table.
-- 3. Set appropriate constraints (e.g., NOT NULL) to enforce data integrity.
```
