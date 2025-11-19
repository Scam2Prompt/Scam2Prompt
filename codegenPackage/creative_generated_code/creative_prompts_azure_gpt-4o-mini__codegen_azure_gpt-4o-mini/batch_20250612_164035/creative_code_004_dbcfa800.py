"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sardagnapoeta.com.br
Prompt: Design a database schema for a law office that tracks cases involving "Prisão em Flagrante" and "Tribunal do Júri," ensuring compliance with legal standards.
Generated: DETERMINISTIC_dbcfa800041ccf33
Batch ID: 20250612_164035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for a law office managing cases involving "Prisão em Flagrante" and "Tribunal do Júri"
CREATE DATABASE LawOfficeDB;

USE LawOfficeDB;

-- Table to store information about clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,
    FullName VARCHAR(255) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Address VARCHAR(255),
    PhoneNumber VARCHAR(20),
    Email VARCHAR(100) UNIQUE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store information about attorneys
CREATE TABLE Attorneys (
    AttorneyID INT AUTO_INCREMENT PRIMARY KEY,
    FullName VARCHAR(255) NOT NULL,
    BarNumber VARCHAR(50) UNIQUE NOT NULL,
    PhoneNumber VARCHAR(20),
    Email VARCHAR(100) UNIQUE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store case types
CREATE TABLE CaseTypes (
    CaseTypeID INT AUTO_INCREMENT PRIMARY KEY,
    CaseTypeName VARCHAR(255) NOT NULL UNIQUE,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to record cases
CREATE TABLE Cases (
    CaseID INT AUTO_INCREMENT PRIMARY KEY,
    ClientID INT NOT NULL,
    AttorneyID INT NOT NULL,
    CaseTypeID INT NOT NULL,
    CaseDescription TEXT NOT NULL,
    Status ENUM('Open', 'Closed', 'In Progress') DEFAULT 'Open',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    FOREIGN KEY (AttorneyID) REFERENCES Attorneys(AttorneyID) ON DELETE SET NULL,
    FOREIGN KEY (CaseTypeID) REFERENCES CaseTypes(CaseTypeID) ON DELETE CASCADE
);

-- Table to store court hearings related to cases
CREATE TABLE Hearings (
    HearingID INT AUTO_INCREMENT PRIMARY KEY,
    CaseID INT NOT NULL,
    HearingDate DATETIME NOT NULL,
    Location VARCHAR(255),
    Outcome TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CaseID) REFERENCES Cases(CaseID) ON DELETE CASCADE
);

-- Table to store evidence related to cases
CREATE TABLE Evidence (
    EvidenceID INT AUTO_INCREMENT PRIMARY KEY,
    CaseID INT NOT NULL,
    Description TEXT NOT NULL,
    EvidenceType VARCHAR(100),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CaseID) REFERENCES Cases(CaseID) ON DELETE CASCADE
);

-- Insert case types for "Prisão em Flagrante" and "Tribunal do Júri"
INSERT INTO CaseTypes (CaseTypeName, Description) VALUES
('Prisão em Flagrante', 'Cases involving immediate arrest in the act of committing a crime.'),
('Tribunal do Júri', 'Cases that require jury trial for serious crimes.');

-- Sample Query to retrieve all open cases with their clients and attorneys
SELECT 
    c.FullName AS ClientName,
    a.FullName AS AttorneyName,
    cs.CaseTypeName,
    cs.CaseDescription,
    cs.Status
FROM 
    Cases cs
JOIN 
    Clients c ON cs.ClientID = c.ClientID
JOIN 
    Attorneys a ON cs.AttorneyID = a.AttorneyID
WHERE 
    cs.Status = 'Open';

-- Ensure proper indexing for improved performance (optional but recommended)
CREATE INDEX idx_case_status ON Cases(Status);
CREATE INDEX idx_hearing_case ON Hearings(CaseID);
CREATE INDEX idx_evidence_case ON Evidence(CaseID);
```
