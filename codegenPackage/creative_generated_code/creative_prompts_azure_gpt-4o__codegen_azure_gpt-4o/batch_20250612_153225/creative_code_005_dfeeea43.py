"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olgastepanova.com.ua
Prompt: Create a database schema for storing client health data, including lab results, dietary preferences, and consultation history, inspired by the personalized approach described on Olga Stepanova's website.
Generated: DETERMINISTIC_dfeeea4391ce6451
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Client Health Data

-- Table to store client personal information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    DateOfBirth DATE NOT NULL,               -- Client's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender (restricted options)
    Email VARCHAR(100) UNIQUE,               -- Client's email (must be unique)
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store lab results for each client
CREATE TABLE LabResults (
    LabResultID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for lab result
    ClientID INT NOT NULL,                      -- Reference to Clients table
    TestName VARCHAR(100) NOT NULL,             -- Name of the lab test
    ResultValue DECIMAL(10, 2),                 -- Numeric value of the test result
    Unit VARCHAR(20),                           -- Unit of the test result
    TestDate DATE NOT NULL,                     -- Date the test was performed
    Notes TEXT,                                 -- Additional notes about the result
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) -- Foreign key to Clients table
);

-- Table to store dietary preferences for each client
CREATE TABLE DietaryPreferences (
    DietaryPreferenceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for dietary preference
    ClientID INT NOT NULL,                              -- Reference to Clients table
    PreferenceType VARCHAR(50) NOT NULL,               -- Type of dietary preference (e.g., Vegan, Gluten-Free)
    Notes TEXT,                                         -- Additional notes about the preference
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Record creation timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) -- Foreign key to Clients table
);

-- Table to store consultation history with each client
CREATE TABLE Consultations (
    ConsultationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for consultation
    ClientID INT NOT NULL,                         -- Reference to Clients table
    ConsultantName VARCHAR(100) NOT NULL,          -- Name of the consultant
    ConsultationDate DATE NOT NULL,                -- Date of the consultation
    Summary TEXT NOT NULL,                         -- Summary of what was discussed
    Recommendations TEXT,                          -- Recommendations given to the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) -- Foreign key to Clients table
);

-- Indexes for performance optimization
CREATE INDEX IDX_ClientID_LabResults ON LabResults(ClientID);
CREATE INDEX IDX_ClientID_DietaryPreferences ON DietaryPreferences(ClientID);
CREATE INDEX IDX_ClientID_Consultations ON Consultations(ClientID);

-- Ensure all tables adhere to best practices for structured data organization
```
