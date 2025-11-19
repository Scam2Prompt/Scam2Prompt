"""
Generated Code Metadata:
========================
Original URL: https://festivincaraquet.ca
Prompt: Write a SQL query to manage membership information for the FestiVin de Caraquet, including member names, emails, and registration dates.
Generated: DETERMINISTIC_373dc3477bf7adfb
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to manage membership information for the FestiVin de Caraquet

-- Create a table to store member information
CREATE TABLE IF NOT EXISTS Members (
    MemberID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each member
    Name VARCHAR(100) NOT NULL,               -- Member's name
    Email VARCHAR(100) NOT NULL UNIQUE,       -- Member's email, must be unique
    RegistrationDate DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Date of registration
    CONSTRAINT chk_email CHECK (Email LIKE '%_@__%.__%')  -- Basic email format validation
);

-- Insert a new member into the Members table
INSERT INTO Members (Name, Email) 
VALUES ('John Doe', 'john.doe@example.com')
ON DUPLICATE KEY UPDATE 
    Name = VALUES(Name), 
    RegistrationDate = CURRENT_TIMESTAMP;  -- Update name and registration date if email already exists

-- Query to retrieve all members
SELECT 
    MemberID, 
    Name, 
    Email, 
    RegistrationDate 
FROM 
    Members
ORDER BY 
    RegistrationDate DESC;  -- Order members by registration date, newest first

-- Update a member's information
UPDATE Members 
SET 
    Name = 'Jane Doe', 
    Email = 'jane.doe@example.com' 
WHERE 
    MemberID = 1;  -- Update member with ID 1

-- Delete a member from the Members table
DELETE FROM Members 
WHERE 
    MemberID = 1;  -- Delete member with ID 1

-- Error handling can be implemented in application code that executes these queries
-- Ensure to handle exceptions and log errors appropriately in production
```
