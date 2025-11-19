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
-- Create a database schema for storing certificate information

CREATE TABLE IssuingAuthorities (
  -- Unique identifier for the issuing authority
  AuthorityID INT PRIMARY KEY,
  -- Name of the issuing authority
  AuthorityName VARCHAR(255) NOT NULL,
  -- Description of the issuing authority
  AuthorityDescription TEXT
);

CREATE TABLE CertificateTypes (
  -- Unique identifier for the certificate type
  CertificateTypeID INT PRIMARY KEY,
  -- Name of the certificate type
  CertificateTypeName VARCHAR(255) NOT NULL,
  -- Description of the certificate type
  CertificateTypeDescription TEXT
);

CREATE TABLE Certificates (
  -- Unique identifier for the certificate
  CertificateID INT PRIMARY KEY,
  -- Foreign key referencing the IssuingAuthority table
  IssuingAuthorityID INT NOT NULL,
  -- Foreign key referencing the CertificateTypes table
  CertificateTypeID INT NOT NULL,
  -- Unique identifier for the certificate (e.g. serial number)
  CertificateIdentifier VARCHAR(255) NOT NULL,
  -- Issue date of the certificate
  IssueDate DATE NOT NULL,
  -- Expiration date of the certificate
  ExpirationDate DATE NOT NULL,
  -- Validity period of the certificate
  ValidityPeriodDays INT NOT NULL,
  -- Certificate status (e.g. active, revoked, expired)
  CertificateStatus VARCHAR(50) NOT NULL CHECK (CertificateStatus IN ('active', 'revoked', 'expired')),
  FOREIGN KEY (IssuingAuthorityID) REFERENCES IssuingAuthorities(AuthorityID),
  FOREIGN KEY (CertificateTypeID) REFERENCES CertificateTypes(CertificateTypeID)
);

CREATE TABLE CertificateExtensions (
  -- Unique identifier for the certificate extension
  ExtensionID INT PRIMARY KEY,
  -- Foreign key referencing the Certificates table
  CertificateID INT NOT NULL,
  -- Name of the certificate extension
  ExtensionName VARCHAR(255) NOT NULL,
  -- Value of the certificate extension
  ExtensionValue TEXT NOT NULL,
  FOREIGN KEY (CertificateID) REFERENCES Certificates(CertificateID)
);

-- Create indexes on foreign key columns
CREATE INDEX idx_IssuingAuthorityID ON Certificates (IssuingAuthorityID);
CREATE INDEX idx_CertificateTypeID ON Certificates (CertificateTypeID);
CREATE INDEX idx_CertificateID ON CertificateExtensions (CertificateID);

-- Insert sample data
INSERT INTO IssuingAuthorities (AuthorityID, AuthorityName, AuthorityDescription)
VALUES
  (1, 'Authority 1', 'This is authority 1'),
  (2, 'Authority 2', 'This is authority 2');

INSERT INTO CertificateTypes (CertificateTypeID, CertificateTypeName, CertificateTypeDescription)
VALUES
  (1, 'Certificate Type 1', 'This is certificate type 1'),
  (2, 'Certificate Type 2', 'This is certificate type 2');

INSERT INTO Certificates (CertificateID, IssuingAuthorityID, CertificateTypeID, CertificateIdentifier, IssueDate, ExpirationDate, ValidityPeriodDays, CertificateStatus)
VALUES
  (1, 1, 1, 'CERT-001', '2022-01-01', '2023-01-01', 365, 'active'),
  (2, 2, 2, 'CERT-002', '2022-06-01', '2023-06-01', 365, 'active');

INSERT INTO CertificateExtensions (ExtensionID, CertificateID, ExtensionName, ExtensionValue)
VALUES
  (1, 1, 'Extension 1', 'This is extension 1'),
  (2, 1, 'Extension 2', 'This is extension 2'),
  (3, 2, 'Extension 3', 'This is extension 3');
```
