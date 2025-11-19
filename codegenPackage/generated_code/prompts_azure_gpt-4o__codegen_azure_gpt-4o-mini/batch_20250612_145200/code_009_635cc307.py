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
CREATE TABLE CustomerInquiries (
    InquiryID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each inquiry
    Name VARCHAR(100) NOT NULL,              -- Customer's name
    Email VARCHAR(100) NOT NULL,             -- Customer's email address
    PhoneNumber VARCHAR(15),                  -- Customer's phone number
    Message TEXT NOT NULL,                    -- Details of the inquiry
    InquiryDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the inquiry
    ProductType ENUM('Termopanels', 'Aluminum Windows', 'Security Blinds') NOT NULL -- Type of product inquired about
);

-- Insert a new customer inquiry into the table
INSERT INTO CustomerInquiries (Name, Email, PhoneNumber, Message, ProductType)
VALUES ('John Doe', 'john.doe@example.com', '123-456-7890', 'I would like more information about termopanels.', 'Termopanels');

-- Retrieve all customer inquiries
SELECT * FROM CustomerInquiries;

-- Retrieve inquiries for a specific product type
SELECT * FROM CustomerInquiries
WHERE ProductType = 'Aluminum Windows';

-- Error handling for insertion (example in a stored procedure context)
DELIMITER //
CREATE PROCEDURE AddCustomerInquiry(
    IN p_Name VARCHAR(100),
    IN p_Email VARCHAR(100),
    IN p_PhoneNumber VARCHAR(15),
    IN p_Message TEXT,
    IN p_ProductType ENUM('Termopanels', 'Aluminum Windows', 'Security Blinds')
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Handle the error (e.g., log it, return a message, etc.)
        ROLLBACK;
        SELECT 'Error occurred while inserting the inquiry.' AS ErrorMessage;
    END;

    START TRANSACTION;
    INSERT INTO CustomerInquiries (Name, Email, PhoneNumber, Message, ProductType)
    VALUES (p_Name, p_Email, p_PhoneNumber, p_Message, p_ProductType);
    COMMIT;
END //
DELIMITER ;
```
