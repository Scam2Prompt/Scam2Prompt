"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jaraesconstruction.com
Prompt: Create a database schema for tracking roof inspections, storm damage assessments, and insurance claims, based on the services offered by JaraEs Construction LLC.
Generated: DETERMINISTIC_b7df8f7622136ab8
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for JaraEs Construction LLC's Roof Inspections, Storm Damage Assessments, and Insurance Claims

-- Create a table for users (homeowners, inspectors, etc.)
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FirstName VARCHAR(50) NOT NULL,        -- First name of the user
    LastName VARCHAR(50) NOT NULL,         -- Last name of the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Email address (must be unique)
    PhoneNumber VARCHAR(15),               -- Contact phone number
    Role ENUM('Homeowner', 'Inspector', 'Admin') NOT NULL, -- Role of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table for properties (homes being inspected)
CREATE TABLE Properties (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each property
    UserID INT NOT NULL,                       -- Foreign key referencing the property owner
    Address VARCHAR(255) NOT NULL,             -- Full address of the property
    City VARCHAR(100) NOT NULL,                -- City where the property is located
    State VARCHAR(50) NOT NULL,                -- State where the property is located
    ZipCode VARCHAR(10) NOT NULL,              -- Zip code of the property
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

-- Create a table for roof inspections
CREATE TABLE RoofInspections (
    InspectionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each roof inspection
    PropertyID INT NOT NULL,                     -- Foreign key referencing the property being inspected
    InspectorID INT NOT NULL,                    -- Foreign key referencing the user conducting the inspection
    InspectionDate DATE NOT NULL,                -- Date of the inspection
    InspectionReport TEXT NOT NULL,              -- Detailed inspection report
    Findings ENUM('No Issues', 'Minor Damage', 'Major Damage') NOT NULL, -- Type of findings from the inspection
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE,
    FOREIGN KEY (InspectorID) REFERENCES Users(UserID) ON DELETE SET NULL
);

-- Create a table for storm damage assessments
CREATE TABLE StormDamageAssessments (
    AssessmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each damage assessment
    PropertyID INT NOT NULL,                     -- Foreign key referencing the affected property
    AssessorID INT NOT NULL,                     -- Foreign key referencing the user conducting the assessment
    AssessmentDate DATE NOT NULL,                -- Date of the storm damage assessment
    DamageReport TEXT NOT NULL,                  -- Detailed damage report
    Severity ENUM('Low', 'Medium', 'High') NOT NULL, -- Severity of the storm damage
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE,
    FOREIGN KEY (AssessorID) REFERENCES Users(UserID) ON DELETE SET NULL
);

-- Create a table for insurance claims
CREATE TABLE InsuranceClaims (
    ClaimID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each insurance claim
    PropertyID INT NOT NULL,                    -- Foreign key referencing the insured property
    ClaimantID INT NOT NULL,                    -- Foreign key referencing the user submitting the claim
    ClaimDate DATE NOT NULL,                    -- Date the claim was submitted
    InsuranceProvider VARCHAR(100) NOT NULL,    -- Name of the insurance provider
    ClaimStatus ENUM('Pending', 'Approved', 'Rejected') NOT NULL, -- Current status of the claim
    ClaimAmount DECIMAL(10, 2) NOT NULL,        -- Amount being claimed
    Notes TEXT,                                 -- Additional notes about the claim
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE,
    FOREIGN KEY (ClaimantID) REFERENCES Users(UserID) ON DELETE SET NULL
);
```
