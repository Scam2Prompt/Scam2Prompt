"""
Generated Code Metadata:
========================
Original URL: https://yourpalmreading.com
Prompt: Create a sample database schema to store client information, palm reading packages, and service orders for a palm reading service website.
Generated: DETERMINISTIC_410686a492e301e1
Batch ID: 20250622_212748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a palm reading service website

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) NOT NULL UNIQUE,      -- Client's email address (must be unique)
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the client record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store palm reading packages
CREATE TABLE Packages (
    PackageID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each package
    PackageName VARCHAR(100) NOT NULL,        -- Name of the palm reading package
    Description TEXT,                         -- Detailed description of the package
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the package
    DurationMinutes INT NOT NULL,             -- Duration of the package in minutes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the package record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store service orders
CREATE TABLE ServiceOrders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each order
    ClientID INT NOT NULL,                   -- Foreign key referencing Clients table
    PackageID INT NOT NULL,                  -- Foreign key referencing Packages table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the order was placed
    Status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    TotalAmount DECIMAL(10, 2) NOT NULL,     -- Total amount for the order
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete if client is removed
    FOREIGN KEY (PackageID) REFERENCES Packages(PackageID) ON DELETE CASCADE -- Cascade delete if package is removed
);

-- Indexes for faster lookups
CREATE INDEX idx_client_email ON Clients(Email); -- Index on email for quick client lookups
CREATE INDEX idx_package_name ON Packages(PackageName); -- Index on package name for quick package lookups
CREATE INDEX idx_order_status ON ServiceOrders(Status); -- Index on order status for quick filtering
```
