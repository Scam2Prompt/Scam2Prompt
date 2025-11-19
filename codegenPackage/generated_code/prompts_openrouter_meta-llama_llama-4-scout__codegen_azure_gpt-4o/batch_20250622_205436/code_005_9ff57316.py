"""
Generated Code Metadata:
========================
Original URL: https://certificatepros.com
Prompt: Suggest a suitable database schema for storing information about different types of certificates, including their issuing authorities, validity periods, and unique identifiers.
Generated: DETERMINISTIC_9ff573166c00ad6c
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about certificates

-- Table to store information about certificates
CREATE TABLE Certificates (
    CertificateID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each certificate
    CertificateName VARCHAR(255) NOT NULL,        -- Name of the certificate
    IssuingAuthorityID INT NOT NULL,              -- Foreign key referencing the issuing authority
    IssueDate DATE NOT NULL,                      -- Date the certificate was issued
    ExpiryDate DATE NOT NULL,                     -- Date the certificate expires
    UNIQUE (CertificateName, IssuingAuthorityID)  -- Ensure no duplicate certificates for the same authority
);

-- Table to store information about issuing authorities
CREATE TABLE IssuingAuthorities (
    AuthorityID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each issuing authority
    AuthorityName VARCHAR(255) NOT NULL UNIQUE,  -- Name of the issuing authority
    ContactEmail VARCHAR(255),                   -- Contact email for the authority
    WebsiteURL VARCHAR(255)                      -- Website URL of the authority
);

-- Table to store certificate types
CREATE TABLE CertificateTypes (
    TypeID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each certificate type
    TypeName VARCHAR(255) NOT NULL UNIQUE,       -- Name of the certificate type
    Description TEXT                             -- Description of the certificate type
);

-- Table to associate certificates with their types (many-to-many relationship)
CREATE TABLE CertificateTypeMapping (
    MappingID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for the mapping
    CertificateID INT NOT NULL,                  -- Foreign key referencing the certificate
    TypeID INT NOT NULL,                         -- Foreign key referencing the certificate type
    FOREIGN KEY (CertificateID) REFERENCES Certificates(CertificateID) ON DELETE CASCADE,
    FOREIGN KEY (TypeID) REFERENCES CertificateTypes(TypeID) ON DELETE CASCADE,
    UNIQUE (CertificateID, TypeID)               -- Ensure no duplicate mappings for the same certificate and type
);

-- Example indexes for performance optimization
CREATE INDEX idx_Certificate_IssueDate ON Certificates (IssueDate);
CREATE INDEX idx_Certificate_ExpiryDate ON Certificates (ExpiryDate);
CREATE INDEX idx_Authority_Name ON IssuingAuthorities (AuthorityName);
CREATE INDEX idx_Type_Name ON CertificateTypes (TypeName);

-- Example constraints for data integrity
ALTER TABLE Certificates
ADD CONSTRAINT chk_ExpiryDate CHECK (ExpiryDate > IssueDate); -- Ensure expiry date is after issue date
```
