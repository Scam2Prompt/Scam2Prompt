"""
Generated Code Metadata:
========================
Original URL: https://cbienetre.com
Prompt: "Create a SQL database schema to store information about massage therapy clients, including their medical history and treatment plans."
Generated: DETERMINISTIC_a51bbe8af5745195
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a SQL database schema for storing information about massage therapy clients

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS TreatmentPlans;
DROP TABLE IF EXISTS MedicalHistory;
DROP TABLE IF EXISTS Clients;

-- Create a table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    DateOfBirth DATE NOT NULL,                 -- Client's date of birth
    PhoneNumber VARCHAR(15),                   -- Client's phone number
    Email VARCHAR(100),                        -- Client's email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table to store medical history of clients
CREATE TABLE MedicalHistory (
    HistoryID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each medical history record
    ClientID INT NOT NULL,                      -- Foreign key referencing Clients table
    Condition VARCHAR(255) NOT NULL,           -- Medical condition description
    Treatment VARCHAR(255),                     -- Treatment description
    DateDiagnosed DATE,                        -- Date when the condition was diagnosed
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table to store treatment plans for clients
CREATE TABLE TreatmentPlans (
    PlanID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each treatment plan
    ClientID INT NOT NULL,                      -- Foreign key referencing Clients table
    TreatmentDate DATE NOT NULL,                -- Date of the treatment
    TreatmentType VARCHAR(100) NOT NULL,       -- Type of treatment (e.g., Swedish, Deep Tissue)
    Duration INT NOT NULL,                      -- Duration of the treatment in minutes
    Notes TEXT,                                 -- Additional notes about the treatment
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Insert sample data into Clients table
INSERT INTO Clients (FirstName, LastName, DateOfBirth, PhoneNumber, Email) VALUES
('John', 'Doe', '1985-05-15', '555-1234', 'john.doe@example.com'),
('Jane', 'Smith', '1990-08-22', '555-5678', 'jane.smith@example.com');

-- Insert sample data into MedicalHistory table
INSERT INTO MedicalHistory (ClientID, Condition, Treatment, DateDiagnosed) VALUES
(1, 'Chronic Back Pain', 'Physical Therapy', '2020-01-10'),
(2, 'Tension Headaches', 'Medication', '2021-03-15');

-- Insert sample data into TreatmentPlans table
INSERT INTO TreatmentPlans (ClientID, TreatmentDate, TreatmentType, Duration, Notes) VALUES
(1, '2023-10-01', 'Deep Tissue', 60, 'Focus on lower back'),
(2, '2023-10-02', 'Swedish', 45, 'Relaxation session');
```
