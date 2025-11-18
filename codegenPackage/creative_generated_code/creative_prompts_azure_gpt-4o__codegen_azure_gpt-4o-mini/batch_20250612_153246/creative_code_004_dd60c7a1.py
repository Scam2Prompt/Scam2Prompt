"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://luattrungcuong.com
Prompt: Develop a SQL database schema to store client information and service details for a legal consultancy firm, referencing the diverse legal services offered by Luật Trung Cường.
Generated: DETERMINISTIC_dd60c7a136f48bb7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a new database for the legal consultancy firm
CREATE DATABASE LegalConsultancy;

-- Use the newly created database
USE LegalConsultancy;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address, must be unique
    PhoneNumber VARCHAR(15),                   -- Client's phone number
    Address VARCHAR(255),                      -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store legal services offered by the firm
CREATE TABLE LegalServices (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the legal service
    Description TEXT,                          -- Detailed description of the service
    ServiceFee DECIMAL(10, 2) NOT NULL,       -- Fee for the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to record service engagements for clients
CREATE TABLE ClientServices (
    EngagementID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each engagement
    ClientID INT NOT NULL,                       -- Reference to the client
    ServiceID INT NOT NULL,                      -- Reference to the service
    EngagementDate DATE NOT NULL,                -- Date of service engagement
    Status ENUM('Pending', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Pending', -- Status of the engagement
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES LegalServices(ServiceID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Optional: Indexes for better performance on common queries
CREATE INDEX idx_clients_email ON Clients (Email);
CREATE INDEX idx_services_name ON LegalServices (ServiceName);
CREATE INDEX idx_engagements_client_service ON ClientServices (ClientID, ServiceID);
```
