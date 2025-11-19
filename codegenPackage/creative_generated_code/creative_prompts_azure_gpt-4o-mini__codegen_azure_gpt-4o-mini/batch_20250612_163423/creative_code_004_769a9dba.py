"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://johnbarrybaker.com
Prompt: Design a database schema for storing client information and accident details for a personal injury law firm, ensuring it includes fields for various accident types and client contact methods.
Generated: DETERMINISTIC_769a9dba55fc72dc
Batch ID: 20250612_163423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Personal Injury Law Firm

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,         -- Client's first name
    LastName VARCHAR(50) NOT NULL,          -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,     -- Client's email address, must be unique
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address VARCHAR(255),                     -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Table to store different types of accidents
CREATE TABLE AccidentTypes (
    AccidentTypeID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each accident type
    TypeName VARCHAR(100) NOT NULL UNIQUE,         -- Name of the accident type
    Description TEXT                               -- Description of the accident type
);

-- Table to store accident details associated with clients
CREATE TABLE Accidents (
    AccidentID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each accident
    ClientID INT NOT NULL,                         -- Foreign key referencing Clients table
    AccidentTypeID INT NOT NULL,                   -- Foreign key referencing AccidentTypes table
    AccidentDate DATE NOT NULL,                    -- Date of the accident
    Description TEXT,                              -- Detailed description of the accident
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last updated timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Handle client deletion
    FOREIGN KEY (AccidentTypeID) REFERENCES AccidentTypes(AccidentTypeID) ON DELETE CASCADE -- Handle accident type deletion
);

-- Example of inserting an accident type
INSERT INTO AccidentTypes (TypeName, Description) VALUES 
('Car Accident', 'Involves vehicles colliding on roadways.'),
('Slip and Fall', 'Involves injuries due to falls on someone else’s property.'),
('Medical Malpractice', 'Involves injuries caused by healthcare professionals.');

-- Ensure that all necessary indexes are created for performance
CREATE INDEX idx_clients_email ON Clients(Email);
CREATE INDEX idx_accidents_clientid ON Accidents(ClientID);
CREATE INDEX idx_accidents_typeid ON Accidents(AccidentTypeID);
```
