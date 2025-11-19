"""
Generated Code Metadata:
========================
Original URL: https://amandiorodrigues.com
Prompt: Create a simple database schema to store technician contact information and provide a SQL script to populate it with sample data.
Generated: DETERMINISTIC_5e2ef6faf46f7cf2
Batch ID: 20250622_211852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for storing technician contact information

-- Drop the table if it already exists to avoid conflicts during creation
DROP TABLE IF EXISTS Technicians;

-- Create the Technicians table
CREATE TABLE Technicians (
    TechnicianID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each technician
    FirstName VARCHAR(50) NOT NULL,             -- Technician's first name
    LastName VARCHAR(50) NOT NULL,               -- Technician's last name
    PhoneNumber VARCHAR(15) NOT NULL,            -- Technician's phone number
    Email VARCHAR(100) NOT NULL UNIQUE,          -- Technician's email address (must be unique)
    HireDate DATE NOT NULL,                       -- Date when the technician was hired
    Specialty VARCHAR(100)                        -- Technician's area of expertise
);

-- Insert sample data into the Technicians table
INSERT INTO Technicians (FirstName, LastName, PhoneNumber, Email, HireDate, Specialty) VALUES
('John', 'Doe', '555-1234', 'john.doe@example.com', '2022-01-15', 'Electrical'),
('Jane', 'Smith', '555-5678', 'jane.smith@example.com', '2021-06-20', 'Plumbing'),
('Alice', 'Johnson', '555-8765', 'alice.johnson@example.com', '2023-03-10', 'HVAC'),
('Bob', 'Brown', '555-4321', 'bob.brown@example.com', '2020-11-05', 'Carpentry'),
('Charlie', 'Davis', '555-2468', 'charlie.davis@example.com', '2022-09-30', 'General Maintenance');

-- Query to verify the inserted data
SELECT * FROM Technicians;
```
