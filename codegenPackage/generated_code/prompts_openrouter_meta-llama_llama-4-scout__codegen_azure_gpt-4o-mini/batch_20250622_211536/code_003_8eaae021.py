"""
Generated Code Metadata:
========================
Original URL: https://cohencues.com
Prompt: "Design a database schema to store information about custom cue sticks, including customer details, cue specifications, and repair services offered by Cohen Cues."
Generated: DETERMINISTIC_8eaae021890084ee
Batch ID: 20250622_211536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about custom cue sticks, customer details, and repair services offered by Cohen Cues

-- Create a table to store customer details
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,             -- Customer's first name
    LastName VARCHAR(50) NOT NULL,               -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Customer's email address (unique)
    Phone VARCHAR(15),                           -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer was added
);

-- Create a table to store cue specifications
CREATE TABLE Cues (
    CueID INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for each cue
    CustomerID INT NOT NULL,                      -- Foreign key referencing the customer
    CueType VARCHAR(50) NOT NULL,                 -- Type of cue (e.g., break, jump, etc.)
    Material VARCHAR(50) NOT NULL,                -- Material of the cue (e.g., wood, fiberglass)
    Length DECIMAL(4,2) NOT NULL,                 -- Length of the cue in inches
    Weight DECIMAL(4,2) NOT NULL,                 -- Weight of the cue in ounces
    TipSize DECIMAL(3,2) NOT NULL,                -- Size of the tip in inches
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the cue was added
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Establishing foreign key relationship
);

-- Create a table to store repair services offered
CREATE TABLE RepairServices (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each repair service
    CueID INT NOT NULL,                            -- Foreign key referencing the cue
    ServiceDescription VARCHAR(255) NOT NULL,     -- Description of the repair service
    ServiceCost DECIMAL(10,2) NOT NULL,           -- Cost of the repair service
    ServiceDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the service was performed
    FOREIGN KEY (CueID) REFERENCES Cues(CueID)   -- Establishing foreign key relationship
);

-- Create an index on the Customers table for faster lookups by email
CREATE INDEX idx_email ON Customers(Email);

-- Create an index on the Cues table for faster lookups by customer ID
CREATE INDEX idx_customer_id ON Cues(CustomerID);

-- Create an index on the RepairServices table for faster lookups by cue ID
CREATE INDEX idx_cue_id ON RepairServices(CueID);
```
