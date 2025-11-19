"""
Generated Code Metadata:
========================
Original URL: https://juridiskklinik.se
Prompt: Design a database schema to store client information, case files, and service areas for a law firm like Juridisk Klinik, considering data normalization and security best practices.
Generated: DETERMINISTIC_57187a58a3878260
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a law firm to store client information, case files, and service areas
-- Following normalization and security best practices

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address (unique for security)
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT,                            -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store case files
CREATE TABLE CaseFiles (
    CaseID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each case
    ClientID INT NOT NULL,                   -- Foreign key referencing Clients table
    CaseTitle VARCHAR(100) NOT NULL,         -- Title of the case
    CaseDescription TEXT,                    -- Detailed description of the case
    Status ENUM('Open', 'Closed', 'Pending') DEFAULT 'Open', -- Status of the case
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete for client cases
);

-- Table to store service areas
CREATE TABLE ServiceAreas (
    ServiceAreaID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service area
    AreaName VARCHAR(100) NOT NULL UNIQUE,        -- Name of the service area (unique for security)
    Description TEXT                              -- Description of the service area
);

-- Junction table to associate cases with service areas (many-to-many relationship)
CREATE TABLE CaseServiceAreas (
    CaseID INT NOT NULL,                          -- Foreign key referencing CaseFiles table
    ServiceAreaID INT NOT NULL,                   -- Foreign key referencing ServiceAreas table
    PRIMARY KEY (CaseID, ServiceAreaID),          -- Composite primary key for many-to-many relationship
    FOREIGN KEY (CaseID) REFERENCES CaseFiles(CaseID) ON DELETE CASCADE, -- Cascade delete for case-service area associations
    FOREIGN KEY (ServiceAreaID) REFERENCES ServiceAreas(ServiceAreaID) ON DELETE CASCADE -- Cascade delete for service area associations
);

-- Table to store user accounts for law firm staff (security best practices)
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each user
    Username VARCHAR(50) UNIQUE NOT NULL,        -- Unique username for the user
    PasswordHash VARCHAR(255) NOT NULL,          -- Hashed password for security
    Role ENUM('Admin', 'Staff') DEFAULT 'Staff', -- Role of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email); -- Index on email for faster lookups
CREATE INDEX idx_case_status ON CaseFiles(Status); -- Index on case status for faster filtering
CREATE INDEX idx_service_area_name ON ServiceAreas(AreaName); -- Index on service area name for faster lookups
```
