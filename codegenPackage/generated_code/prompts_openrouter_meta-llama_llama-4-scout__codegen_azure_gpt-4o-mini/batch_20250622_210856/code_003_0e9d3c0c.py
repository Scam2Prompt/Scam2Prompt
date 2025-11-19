"""
Generated Code Metadata:
========================
Original URL: https://uniquehomestagingandredesignbydee.com
Prompt: Design a database schema to store information about staged homes, clients, and services offered by a home staging company like Unique Home Staging & Redesign by Dee.
Generated: DETERMINISTIC_0e9d3c0cac30dcea
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Unique Home Staging & Redesign by Dee

-- Create a database for the home staging company
CREATE DATABASE HomeStagingDB;

-- Use the created database
USE HomeStagingDB;

-- Table to store information about clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address (unique)
    Phone VARCHAR(15),                        -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store information about staged homes
CREATE TABLE StagedHomes (
    HomeID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each staged home
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients
    Address VARCHAR(255) NOT NULL,             -- Home address
    City VARCHAR(100) NOT NULL,                -- City where the home is located
    State VARCHAR(50) NOT NULL,                -- State where the home is located
    ZipCode VARCHAR(10) NOT NULL,              -- Zip code for the home
    StagingDate DATE NOT NULL,                 -- Date when staging occurred
    Status ENUM('Staged', 'Available', 'Sold') NOT NULL,  -- Current status of the home
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store information about services offered
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,          -- Name of the service
    Description TEXT,                            -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to link staged homes with services offered
CREATE TABLE HomeServices (
    HomeServiceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each home-service link
    HomeID INT NOT NULL,                           -- Foreign key referencing StagedHomes
    ServiceID INT NOT NULL,                        -- Foreign key referencing Services
    Quantity INT DEFAULT 1,                        -- Quantity of the service used
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (HomeID) REFERENCES StagedHomes(HomeID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_staged_home_status ON StagedHomes(Status);
CREATE INDEX idx_service_name ON Services(ServiceName);
```
