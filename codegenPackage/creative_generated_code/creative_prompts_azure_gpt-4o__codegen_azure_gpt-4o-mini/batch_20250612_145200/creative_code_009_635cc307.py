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
    InquiryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each inquiry
    Name VARCHAR(100) NOT NULL,                -- Customer's name
    Email VARCHAR(100) NOT NULL,               -- Customer's email address
    PhoneNumber VARCHAR(15),                    -- Customer's phone number (optional)
    MessageDetails TEXT NOT NULL,               -- Details of the inquiry
    InquiryDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date and time of the inquiry
    CONSTRAINT chk_email CHECK (Email LIKE '%_@__%.__%')  -- Basic email format validation
);

-- Insert sample data into the CustomerInquiries table
INSERT INTO CustomerInquiries (Name, Email, PhoneNumber, MessageDetails)
VALUES 
    ('John Doe', 'john.doe@example.com', '123-456-7890', 'Inquiry about termopanels.'),
    ('Jane Smith', 'jane.smith@example.com', NULL, 'Looking for aluminum windows options.'),
    ('Mike Johnson', 'mike.j@example.com', '987-654-3210', 'Need information on security blinds.');

-- Query to retrieve all customer inquiries
SELECT 
    InquiryID, 
    Name, 
    Email, 
    PhoneNumber, 
    MessageDetails, 
    InquiryDate 
FROM 
    CustomerInquiries
ORDER BY 
    InquiryDate DESC;  -- Order results by the date of inquiry, most recent first

-- To safely handle exceptions, use a TRY-CATCH block if supported by your SQL dialect
BEGIN TRY
    -- Your SQL statements here
END TRY
BEGIN CATCH
    -- Error handling logic
    SELECT ERROR_MESSAGE() AS ErrorMessage;  -- Return the error message
END CATCH;
```
