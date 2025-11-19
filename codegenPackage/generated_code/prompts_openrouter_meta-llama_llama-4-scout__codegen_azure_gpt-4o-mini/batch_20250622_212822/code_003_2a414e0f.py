"""
Generated Code Metadata:
========================
Original URL: https://www-magiceden-marketplace-ar5-f.blogspot.com
Prompt: "Design a simple database schema for storing information about automotive services, including tire renovation and parts distribution, and write SQL to query services offered by a specific provider."
Generated: DETERMINISTIC_2a414e0f141a7908
Batch ID: 20250622_212822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for automotive services
CREATE DATABASE AutomotiveServices;

-- Use the created database
USE AutomotiveServices;

-- Table to store information about service providers
CREATE TABLE ServiceProviders (
    ProviderID INT AUTO_INCREMENT PRIMARY KEY,
    ProviderName VARCHAR(100) NOT NULL,
    ContactInfo VARCHAR(255),
    Address VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store information about services offered
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,
    ServiceName VARCHAR(100) NOT NULL,
    Description TEXT,
    ProviderID INT,
    Price DECIMAL(10, 2),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ProviderID) REFERENCES ServiceProviders(ProviderID) ON DELETE CASCADE
);

-- Table to store information about tire renovations
CREATE TABLE TireRenovations (
    RenovationID INT AUTO_INCREMENT PRIMARY KEY,
    ServiceID INT,
    TireType VARCHAR(50),
    RenovationDate DATE,
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE
);

-- Table to store information about parts distribution
CREATE TABLE PartsDistribution (
    PartID INT AUTO_INCREMENT PRIMARY KEY,
    ServiceID INT,
    PartName VARCHAR(100),
    Quantity INT,
    DistributionDate DATE,
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE
);

-- Query to retrieve services offered by a specific provider
-- Replace 'provider_name' with the actual provider name you want to query
SELECT 
    s.ServiceID,
    s.ServiceName,
    s.Description,
    s.Price
FROM 
    Services s
JOIN 
    ServiceProviders sp ON s.ProviderID = sp.ProviderID
WHERE 
    sp.ProviderName = 'provider_name';
```
