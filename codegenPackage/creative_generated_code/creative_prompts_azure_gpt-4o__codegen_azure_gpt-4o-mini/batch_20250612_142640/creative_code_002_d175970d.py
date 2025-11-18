"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinoassetfinance.com
Prompt: Develop a database schema for tracking asset finance deals across multiple industries, including fields for asset types like amusement rides, commercial mortgages, and plant equipment, as mentioned on Rhino Asset Finance.
Generated: DETERMINISTIC_d175970df52e618f
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for tracking asset finance deals across multiple industries

CREATE DATABASE AssetFinanceDB;

USE AssetFinanceDB;

-- Table to store information about different asset types
CREATE TABLE AssetTypes (
    AssetTypeID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for asset type
    AssetTypeName VARCHAR(255) NOT NULL,       -- Name of the asset type (e.g., Amusement Ride)
    Description TEXT,                           -- Description of the asset type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about clients
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for client
    ClientName VARCHAR(255) NOT NULL,          -- Name of the client
    ContactEmail VARCHAR(255) UNIQUE,          -- Email of the client for communication
    PhoneNumber VARCHAR(50),                    -- Phone number of the client
    Address VARCHAR(255),                       -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about finance deals
CREATE TABLE FinanceDeals (
    DealID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for finance deal
    ClientID INT NOT NULL,                      -- Foreign key referencing Clients table
    AssetTypeID INT NOT NULL,                   -- Foreign key referencing AssetTypes table
    DealAmount DECIMAL(15, 2) NOT NULL,        -- Amount of the deal
    InterestRate DECIMAL(5, 2),                 -- Interest rate for the finance deal
    DealStartDate DATE NOT NULL,               -- Start date of the finance deal
    DealEndDate DATE NOT NULL,                 -- End date of the finance deal
    Status ENUM('Active', 'Completed', 'Defaulted') NOT NULL DEFAULT 'Active', -- Status of the deal
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,  -- Referential integrity constraint
    FOREIGN KEY (AssetTypeID) REFERENCES AssetTypes(AssetTypeID) ON DELETE CASCADE -- Referential integrity constraint
);

-- Table to store payments related to finance deals
CREATE TABLE Payments (
    PaymentID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for payment
    DealID INT NOT NULL,                        -- Foreign key referencing FinanceDeals table
    PaymentDate DATE NOT NULL,                  -- Date payment was made
    PaymentAmount DECIMAL(15, 2) NOT NULL,     -- Amount of the payment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    FOREIGN KEY (DealID) REFERENCES FinanceDeals(DealID) ON DELETE CASCADE -- Referential integrity constraint
);

-- Insert default asset types for initial setup
INSERT INTO AssetTypes (AssetTypeName, Description) VALUES 
('Amusement Ride', 'Various types of amusement park rides'),
('Commercial Mortgage', 'Financing for commercial property purchases'),
('Plant Equipment', 'Heavy machinery and equipment for industrial use');

-- Insert example clients for initial setup
INSERT INTO Clients (ClientName, ContactEmail, PhoneNumber, Address) VALUES 
('ABC Amusements', 'contact@abc-amusements.com', '555-1234', '123 Fun St, Amusement City'),
('XYZ Real Estate', 'info@xyz-realestate.com', '555-5678', '456 Business Rd, Real Estate Town');

-- Example of handling errors during table creation (if needed in application logic)
BEGIN TRY
    -- Your logic to execute SQL commands goes here
END TRY
BEGIN CATCH
    -- Handle error: Log the error and possibly rethrow or take corrective action
    SELECT ERROR_MESSAGE() AS ErrorMessage;
END CATCH;
```
