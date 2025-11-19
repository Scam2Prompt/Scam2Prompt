"""
Generated Code Metadata:
========================
Original URL: https://trindademota.adv.br
Prompt: "Design a basic database schema for storing and managing legal documents and client information for a full-service law firm like Trindade & Mota Advocacia."
Generated: DETERMINISTIC_2bb452075dc02c2e
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing legal documents and client information
-- Designed for a full-service law firm

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(100) NOT NULL,         -- Client's first name
    LastName VARCHAR(100) NOT NULL,          -- Client's last name
    Email VARCHAR(255) UNIQUE NOT NULL,      -- Client's email address
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT,                            -- Client's physical address
    DateCreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    DateUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store legal documents
CREATE TABLE LegalDocuments (
    DocumentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each document
    ClientID INT NOT NULL,                     -- Foreign key linking to the Clients table
    DocumentTitle VARCHAR(255) NOT NULL,       -- Title of the legal document
    DocumentType VARCHAR(100) NOT NULL,        -- Type of the legal document (e.g., contract, affidavit)
    FilePath VARCHAR(255) NOT NULL,            -- Path to the stored document file
    DateUploaded TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Document upload timestamp
    DateUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Document update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Table to store case information
CREATE TABLE Cases (
    CaseID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each case
    ClientID INT NOT NULL,                     -- Foreign key linking to the Clients table
    CaseTitle VARCHAR(255) NOT NULL,           -- Title of the case
    CaseDescription TEXT,                      -- Detailed description of the case
    CaseStatus ENUM('Open', 'Closed', 'Pending') DEFAULT 'Open', -- Status of the case
    DateCreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Case creation timestamp
    DateUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Case update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Table to store appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    ClientID INT NOT NULL,                        -- Foreign key linking to the Clients table
    CaseID INT,                                   -- Foreign key linking to the Cases table (optional)
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    Notes TEXT,                                   -- Additional notes for the appointment
    DateCreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    DateUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete if client is removed
    FOREIGN KEY (CaseID) REFERENCES Cases(CaseID) ON DELETE SET NULL -- Set to NULL if case is removed
);

-- Table to store user accounts for the law firm staff
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each user
    Username VARCHAR(50) UNIQUE NOT NULL,        -- Username for login
    PasswordHash VARCHAR(255) NOT NULL,          -- Hashed password for security
    Role ENUM('Admin', 'Lawyer', 'Assistant') NOT NULL, -- Role of the user
    FullName VARCHAR(100) NOT NULL,              -- Full name of the user
    Email VARCHAR(255) UNIQUE NOT NULL,          -- Email address of the user
    DateCreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    DateUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to log system activities for auditing purposes
CREATE TABLE ActivityLog (
    LogID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each log entry
    UserID INT NOT NULL,                         -- Foreign key linking to the Users table
    Action VARCHAR(255) NOT NULL,                -- Description of the action performed
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the action
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is removed
);
```
