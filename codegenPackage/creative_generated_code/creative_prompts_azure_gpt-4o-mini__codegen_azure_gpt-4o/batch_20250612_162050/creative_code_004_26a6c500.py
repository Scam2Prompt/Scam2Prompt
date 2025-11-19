"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fachriahyani.com
Prompt: Design a database schema for storing information about legal consultations and cases, inspired by the practices of Fachri Ahyani as an advocate.
Generated: DETERMINISTIC_26a6c5000aaeab9b
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing information about legal consultations and cases.

-- Create a table for users who are interacting with the system.
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FullName VARCHAR(255) NOT NULL,        -- Full name of the user
    Email VARCHAR(255) UNIQUE NOT NULL,   -- Email address, must be unique
    PhoneNumber VARCHAR(15),              -- Contact number of the user
    Role ENUM('Advocate', 'Client') NOT NULL, -- Role of the user in the system
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the user was last updated
);

-- Create a table for cases.
CREATE TABLE Cases (
    CaseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each case
    CaseTitle VARCHAR(255) NOT NULL,       -- Title of the case
    CaseDescription TEXT,                  -- Detailed description of the case
    CaseType ENUM('Civil', 'Criminal', 'Family', 'Corporate', 'Other') NOT NULL, -- Type of the case
    ClientID INT NOT NULL,                 -- Foreign key referencing the user (client)
    AdvocateID INT NOT NULL,               -- Foreign key referencing the user (advocate)
    Status ENUM('Open', 'Closed', 'In Progress', 'On Hold') DEFAULT 'Open', -- Current status of the case
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the case was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the case was last updated
    FOREIGN KEY (ClientID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if client is removed
    FOREIGN KEY (AdvocateID) REFERENCES Users(UserID) ON DELETE SET NULL -- Set null if advocate is removed
);

-- Create a table for legal consultations.
CREATE TABLE LegalConsultations (
    ConsultationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each consultation
    CaseID INT NOT NULL,                           -- Foreign key referencing the case
    AdvocateID INT NOT NULL,                       -- Foreign key referencing the user (advocate)
    ClientID INT NOT NULL,                         -- Foreign key referencing the user (client)
    StartTime DATETIME NOT NULL,                   -- Start time of the consultation
    EndTime DATETIME NOT NULL,                     -- End time of the consultation
    Notes TEXT,                                    -- Notes taken during the consultation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the consultation was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the consultation was last updated
    FOREIGN KEY (CaseID) REFERENCES Cases(CaseID) ON DELETE CASCADE, -- Cascade delete if case is removed
    FOREIGN KEY (AdvocateID) REFERENCES Users(UserID) ON DELETE SET NULL, -- Set null if advocate is removed
    FOREIGN KEY (ClientID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Create a table for tracking payments related to consultations and cases.
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each payment
    ConsultationID INT,                       -- Foreign key referencing the consultation
    CaseID INT,                               -- Foreign key referencing the case (optional, for case-related payments)
    Amount DECIMAL(10, 2) NOT NULL,           -- Payment amount
    PaymentDate DATE NOT NULL,                -- Date of payment
    PaymentStatus ENUM('Pending', 'Completed', 'Failed') DEFAULT 'Pending', -- Status of the payment
    PaymentMethod ENUM('Cash', 'Card', 'Bank Transfer', 'Other') NOT NULL, -- Method of payment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the payment was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the payment was last updated
    FOREIGN KEY (ConsultationID) REFERENCES LegalConsultations(ConsultationID) ON DELETE SET NULL, -- Nullable if consultation is removed
    FOREIGN KEY (CaseID) REFERENCES Cases(CaseID) ON DELETE SET NULL -- Nullable if case is removed
);

-- Create indexes for optimizing queries.
CREATE INDEX idx_user_email ON Users (Email);
CREATE INDEX idx_case_status ON Cases (Status);
CREATE INDEX idx_consultation_time ON LegalConsultations (StartTime, EndTime);
CREATE INDEX idx_payment_status ON Payments (PaymentStatus);
```
