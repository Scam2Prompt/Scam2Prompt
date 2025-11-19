"""
Generated Code Metadata:
========================
Original URL: https://colegiodepsicologosoruro.org
Prompt: Design a database schema for a system to manage certifications and memberships for a professional organization like the Colegio de Psicologos de Oruro.
Generated: DETERMINISTIC_90466b5e2699b054
Batch ID: 20250622_212724
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing certifications and memberships
-- for a professional organization like the Colegio de Psicologos de Oruro.

-- Table to store information about members
CREATE TABLE Members (
    MemberID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each member
    FirstName VARCHAR(100) NOT NULL,         -- Member's first name
    LastName VARCHAR(100) NOT NULL,          -- Member's last name
    Email VARCHAR(150) UNIQUE NOT NULL,      -- Member's email address (must be unique)
    PhoneNumber VARCHAR(15),                 -- Member's phone number
    Address TEXT,                            -- Member's address
    DateOfBirth DATE,                        -- Member's date of birth
    JoinDate DATE NOT NULL,                  -- Date the member joined the organization
    Status ENUM('Active', 'Inactive') DEFAULT 'Active', -- Membership status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about certifications
CREATE TABLE Certifications (
    CertificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each certification
    Name VARCHAR(150) NOT NULL,                     -- Name of the certification
    Description TEXT,                               -- Description of the certification
    IssuedBy VARCHAR(150) NOT NULL,                -- Organization or entity that issued the certification
    ValidityPeriod INT,                             -- Validity period in months (NULL if no expiration)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store the relationship between members and certifications
CREATE TABLE MemberCertifications (
    MemberCertificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the relationship
    MemberID INT NOT NULL,                                -- Foreign key referencing Members table
    CertificationID INT NOT NULL,                         -- Foreign key referencing Certifications table
    IssueDate DATE NOT NULL,                              -- Date the certification was issued
    ExpiryDate DATE,                                      -- Expiry date of the certification (NULL if no expiration)
    Status ENUM('Valid', 'Expired') DEFAULT 'Valid',      -- Status of the certification
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,        -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (CertificationID) REFERENCES Certifications(CertificationID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store information about memberships
CREATE TABLE Memberships (
    MembershipID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each membership
    MemberID INT NOT NULL,                       -- Foreign key referencing Members table
    MembershipType ENUM('Standard', 'Premium', 'Lifetime') NOT NULL, -- Type of membership
    StartDate DATE NOT NULL,                     -- Start date of the membership
    EndDate DATE,                                -- End date of the membership (NULL for lifetime memberships)
    Status ENUM('Active', 'Expired') DEFAULT 'Active', -- Status of the membership
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store payment records for memberships
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each payment
    MemberID INT NOT NULL,                    -- Foreign key referencing Members table
    Amount DECIMAL(10, 2) NOT NULL,           -- Payment amount
    PaymentDate DATE NOT NULL,                -- Date the payment was made
    PaymentMethod ENUM('Credit Card', 'Bank Transfer', 'Cash') NOT NULL, -- Payment method
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for optimizing queries
CREATE INDEX idx_member_email ON Members(Email); -- Index for quick lookup by email
CREATE INDEX idx_certification_name ON Certifications(Name); -- Index for quick lookup by certification name
CREATE INDEX idx_membership_status ON Memberships(Status); -- Index for quick lookup by membership status
CREATE INDEX idx_payment_date ON Payments(PaymentDate); -- Index for quick lookup by payment date
```
