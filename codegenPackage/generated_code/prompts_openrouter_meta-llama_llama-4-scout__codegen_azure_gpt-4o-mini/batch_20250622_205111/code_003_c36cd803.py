"""
Generated Code Metadata:
========================
Original URL: https://yexinerangel.com
Prompt: "Design a database schema to store insurance claims (siniestros) and client information for a company like Yexine Rangel Asesores de Seguros Ltda, including tables for clients, policies, and claims."
Generated: DETERMINISTIC_c36cd803ccc6317f
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing insurance claims and client information

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Claims;
DROP TABLE IF EXISTS Policies;
DROP TABLE IF EXISTS Clients;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address (unique)
    Phone VARCHAR(15),                        -- Client's phone number
    Address VARCHAR(255),                      -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store insurance policies
CREATE TABLE Policies (
    PolicyID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each policy
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients
    PolicyNumber VARCHAR(50) UNIQUE NOT NULL,  -- Unique policy number
    PolicyType VARCHAR(50) NOT NULL,           -- Type of insurance policy
    StartDate DATE NOT NULL,                   -- Policy start date
    EndDate DATE NOT NULL,                     -- Policy end date
    Premium DECIMAL(10, 2) NOT NULL,          -- Policy premium amount
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store insurance claims
CREATE TABLE Claims (
    ClaimID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each claim
    PolicyID INT NOT NULL,                      -- Foreign key referencing Policies
    ClaimNumber VARCHAR(50) UNIQUE NOT NULL,   -- Unique claim number
    ClaimDate DATE NOT NULL,                    -- Date of the claim
    ClaimAmount DECIMAL(10, 2) NOT NULL,       -- Amount claimed
    Status ENUM('Pending', 'Approved', 'Denied') NOT NULL DEFAULT 'Pending',  -- Status of the claim
    Description TEXT,                           -- Description of the claim
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (PolicyID) REFERENCES Policies(PolicyID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Sample data insertion (for testing purposes)
INSERT INTO Clients (FirstName, LastName, Email, Phone, Address) VALUES
('John', 'Doe', 'john.doe@example.com', '1234567890', '123 Elm St, Springfield'),
('Jane', 'Smith', 'jane.smith@example.com', '0987654321', '456 Oak St, Springfield');

INSERT INTO Policies (ClientID, PolicyNumber, PolicyType, StartDate, EndDate, Premium) VALUES
(1, 'POL123456', 'Health', '2023-01-01', '2024-01-01', 500.00),
(2, 'POL654321', 'Auto', '2023-02-01', '2024-02-01', 300.00);

INSERT INTO Claims (PolicyID, ClaimNumber, ClaimDate, ClaimAmount, Status, Description) VALUES
(1, 'CLAIM001', '2023-03-01', 1500.00, 'Pending', 'Medical expenses for treatment.'),
(2, 'CLAIM002', '2023-04-01', 2000.00, 'Approved', 'Accident repair costs.');
```
