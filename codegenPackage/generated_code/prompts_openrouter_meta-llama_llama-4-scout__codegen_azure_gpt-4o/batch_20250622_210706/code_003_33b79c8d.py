"""
Generated Code Metadata:
========================
Original URL: https://ai-rex.xyz
Prompt: Design a simple database schema using SQL for a website that manages domain names and their hosting status, like the one seemingly planned for ai-rex.xyz on Porkbun.com.
Generated: DETERMINISTIC_33b79c8d1bc76d9d
Batch ID: 20250622_210706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing domain names and their hosting status

-- Create a table to store information about domains
CREATE TABLE Domains (
    DomainID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each domain
    DomainName VARCHAR(255) NOT NULL UNIQUE, -- Fully qualified domain name (e.g., ai-rex.xyz)
    RegistrationDate DATE NOT NULL,          -- Date the domain was registered
    ExpirationDate DATE NOT NULL,            -- Date the domain will expire
    HostingStatus ENUM('Active', 'Inactive', 'Pending') NOT NULL, -- Hosting status of the domain
    Registrar VARCHAR(255) NOT NULL,         -- Name of the registrar (e.g., Porkbun.com)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Create a table to store hosting details for domains
CREATE TABLE HostingDetails (
    HostingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for hosting details
    DomainID INT NOT NULL,                    -- Foreign key referencing Domains table
    HostingProvider VARCHAR(255) NOT NULL,    -- Name of the hosting provider
    HostingPlan VARCHAR(255),                 -- Hosting plan details (e.g., shared, VPS, dedicated)
    IPAddress VARCHAR(45),                    -- IP address of the hosting server
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (DomainID) REFERENCES Domains(DomainID) ON DELETE CASCADE -- Cascade delete if domain is removed
);

-- Create a table to store DNS records for domains
CREATE TABLE DNSRecords (
    DNSRecordID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for DNS record
    DomainID INT NOT NULL,                      -- Foreign key referencing Domains table
    RecordType ENUM('A', 'AAAA', 'CNAME', 'MX', 'TXT', 'NS') NOT NULL, -- Type of DNS record
    RecordValue VARCHAR(255) NOT NULL,          -- Value of the DNS record (e.g., IP address, CNAME target)
    TTL INT DEFAULT 3600,                       -- Time-to-live for the DNS record (default: 3600 seconds)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (DomainID) REFERENCES Domains(DomainID) ON DELETE CASCADE -- Cascade delete if domain is removed
);

-- Create a table to store user information (optional, for managing domain ownership)
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FullName VARCHAR(255) NOT NULL,        -- Full name of the user
    Email VARCHAR(255) NOT NULL UNIQUE,    -- Email address of the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for authentication
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Create a table to associate domains with users (many-to-many relationship)
CREATE TABLE UserDomains (
    UserDomainID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the association
    UserID INT NOT NULL,                         -- Foreign key referencing Users table
    DomainID INT NOT NULL,                       -- Foreign key referencing Domains table
    Role ENUM('Owner', 'Admin', 'Viewer') NOT NULL, -- Role of the user for the domain
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is removed
    FOREIGN KEY (DomainID) REFERENCES Domains(DomainID) ON DELETE CASCADE -- Cascade delete if domain is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_domain_name ON Domains(DomainName);
CREATE INDEX idx_user_email ON Users(Email);
CREATE INDEX idx_dns_record_type ON DNSRecords(RecordType);
```
