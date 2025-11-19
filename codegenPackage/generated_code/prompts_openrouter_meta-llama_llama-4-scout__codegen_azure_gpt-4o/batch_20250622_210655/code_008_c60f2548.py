"""
Generated Code Metadata:
========================
Original URL: https://lexuscertifications.com
Prompt: "Design a simple database schema for tracking and managing ISO certifications and audits."
Generated: DETERMINISTIC_c60f25483c6b5cfd
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking and managing ISO certifications and audits

-- Table to store information about ISO certifications
CREATE TABLE Certifications (
    CertificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each certification
    CertificationName VARCHAR(255) NOT NULL,        -- Name of the ISO certification (e.g., ISO 9001)
    Description TEXT,                               -- Description of the certification
    IssuedDate DATE NOT NULL,                       -- Date when the certification was issued
    ExpiryDate DATE NOT NULL,                       -- Date when the certification expires
    OrganizationName VARCHAR(255) NOT NULL,         -- Name of the organization holding the certification
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Table to store information about audits related to certifications
CREATE TABLE Audits (
    AuditID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each audit
    CertificationID INT NOT NULL,                   -- Foreign key referencing the Certifications table
    AuditDate DATE NOT NULL,                        -- Date when the audit was conducted
    AuditorName VARCHAR(255) NOT NULL,              -- Name of the auditor conducting the audit
    AuditResult ENUM('Pass', 'Fail', 'Pending') NOT NULL, -- Result of the audit
    Notes TEXT,                                     -- Additional notes or observations from the audit
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (CertificationID) REFERENCES Certifications(CertificationID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store corrective actions for failed audits
CREATE TABLE CorrectiveActions (
    ActionID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each corrective action
    AuditID INT NOT NULL,                           -- Foreign key referencing the Audits table
    ActionDescription TEXT NOT NULL,                -- Description of the corrective action
    AssignedTo VARCHAR(255) NOT NULL,               -- Name of the person responsible for the action
    DueDate DATE NOT NULL,                          -- Deadline for completing the corrective action
    Status ENUM('Open', 'In Progress', 'Completed') DEFAULT 'Open', -- Status of the corrective action
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (AuditID) REFERENCES Audits(AuditID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_certification_expiry ON Certifications (ExpiryDate); -- Index for querying certifications by expiry date
CREATE INDEX idx_audit_date ON Audits (AuditDate);                    -- Index for querying audits by date
CREATE INDEX idx_corrective_due_date ON CorrectiveActions (DueDate);  -- Index for querying corrective actions by due date
```
