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
-- Create a database for customer inquiries
CREATE DATABASE CustomerInquiries;

-- Use the CustomerInquiries database
USE CustomerInquiries;

-- Create a table for storing customer inquiries
CREATE TABLE Inquiries (
    InquiryID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    PhoneNumber VARCHAR(20) NOT NULL,
    ProductOfInterest ENUM('Termopanels', 'Aluminum Windows', 'Security Blinds') NOT NULL,
    MessageDetails TEXT NOT NULL,
    InquiryDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (InquiryID)
);

-- Create a trigger to ensure email and phone number are valid
DELIMITER $$
CREATE TRIGGER ValidateInquiry
BEFORE INSERT ON Inquiries
FOR EACH ROW
BEGIN
    IF NEW.Email NOT REGEXP '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid email address';
    END IF;
    
    IF NEW.PhoneNumber NOT REGEXP '^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid phone number';
    END IF;
END$$
DELIMITER ;

-- Insert a new customer inquiry
DELIMITER $$
CREATE PROCEDURE InsertInquiry(
    IN p_Name VARCHAR(255),
    IN p_Email VARCHAR(255),
    IN p_PhoneNumber VARCHAR(20),
    IN p_ProductOfInterest ENUM('Termopanels', 'Aluminum Windows', 'Security Blinds'),
    IN p_MessageDetails TEXT
)
BEGIN
    INSERT INTO Inquiries (Name, Email, PhoneNumber, ProductOfInterest, MessageDetails)
    VALUES (p_Name, p_Email, p_PhoneNumber, p_ProductOfInterest, p_MessageDetails);
END$$
DELIMITER ;

-- Retrieve all customer inquiries
DELIMITER $$
CREATE PROCEDURE GetAllInquiries()
BEGIN
    SELECT * FROM Inquiries;
END$$
DELIMITER ;

-- Retrieve a customer inquiry by ID
DELIMITER $$
CREATE PROCEDURE GetInquiryByID(
    IN p_InquiryID INT
)
BEGIN
    SELECT * FROM Inquiries
    WHERE InquiryID = p_InquiryID;
END$$
DELIMITER ;

-- Example usage:
CALL InsertInquiry('John Doe', 'john@example.com', '+1 123-456-7890', 'Termopanels', 'This is a sample inquiry');

CALL GetAllInquiries();

CALL GetInquiryByID(1);
```
