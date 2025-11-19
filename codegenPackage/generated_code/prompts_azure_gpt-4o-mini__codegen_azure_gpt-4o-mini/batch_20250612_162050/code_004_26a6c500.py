"""
Generated Code Metadata:
========================
Original URL: https://fachriahyani.com
Prompt: Design a database schema for storing information about legal consultations and cases, inspired by the practices of Fachri Ahyani as an advocate.
Generated: DETERMINISTIC_26a6c5000aaeab9b
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about legal consultations and cases

CREATE DATABASE LegalConsultationDB;

USE LegalConsultationDB;

-- Table to store information about clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address
    Phone VARCHAR(15),                        -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store information about legal consultations
CREATE TABLE Consultations (
    ConsultationID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each consultation
    ClientID INT NOT NULL,                          -- Foreign key referencing Clients
    ConsultationDate DATETIME NOT NULL,             -- Date and time of the consultation
    Notes TEXT,                                     -- Notes taken during the consultation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store information about legal cases
CREATE TABLE Cases (
    CaseID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each case
    ClientID INT NOT NULL,                          -- Foreign key referencing Clients
    CaseTitle VARCHAR(255) NOT NULL,               -- Title of the case
    CaseDescription TEXT,                           -- Description of the case
    Status ENUM('Open', 'Closed', 'Pending') NOT NULL,  -- Current status of the case
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store case-related documents
CREATE TABLE CaseDocuments (
    DocumentID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each document
    CaseID INT NOT NULL,                            -- Foreign key referencing Cases
    DocumentName VARCHAR(255) NOT NULL,            -- Name of the document
    DocumentPath VARCHAR(255) NOT NULL,            -- Path to the document file
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (CaseID) REFERENCES Cases(CaseID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store billing information for consultations and cases
CREATE TABLE Billing (
    BillingID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each billing record
    ClientID INT NOT NULL,                          -- Foreign key referencing Clients
    Amount DECIMAL(10, 2) NOT NULL,                -- Amount billed
    BillingDate DATETIME NOT NULL,                  -- Date of billing
    PaymentStatus ENUM('Paid', 'Unpaid', 'Pending') NOT NULL,  -- Payment status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_case_status ON Cases(Status);
CREATE INDEX idx_billing_status ON Billing(PaymentStatus);
```
