"""
Generated Code Metadata:
========================
Original URL: https://balletcristinavaz.com.br
Prompt: Design a database schema to store information about dance schools, including their locations, programs, and instructors, using the Ballet Cristina Vaz school as an example.
Generated: DETERMINISTIC_8d9032807db0e314
Batch ID: 20250622_210703
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://www.balletcristinavaz.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Dance Schools

-- Create a table to store information about dance schools
CREATE TABLE DanceSchools (
    SchoolID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each school
    Name VARCHAR(255) NOT NULL,              -- Name of the dance school
    Address VARCHAR(255) NOT NULL,           -- Address of the dance school
    City VARCHAR(100) NOT NULL,              -- City where the school is located
    State VARCHAR(100) NOT NULL,             -- State where the school is located
    ZipCode VARCHAR(20),                     -- Zip code of the school location
    PhoneNumber VARCHAR(20),                 -- Contact phone number
    Email VARCHAR(255),                      -- Contact email address
    Website VARCHAR(255)                     -- Website URL of the school
);

-- Create a table to store information about dance programs offered by schools
CREATE TABLE DancePrograms (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each program
    SchoolID INT NOT NULL,                    -- Foreign key referencing DanceSchools
    Name VARCHAR(255) NOT NULL,               -- Name of the dance program
    Description TEXT,                         -- Description of the program
    DurationWeeks INT,                        -- Duration of the program in weeks
    Price DECIMAL(10, 2),                     -- Price of the program
    FOREIGN KEY (SchoolID) REFERENCES DanceSchools(SchoolID) ON DELETE CASCADE
);

-- Create a table to store information about instructors
CREATE TABLE Instructors (
    InstructorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each instructor
    SchoolID INT NOT NULL,                       -- Foreign key referencing DanceSchools
    FirstName VARCHAR(100) NOT NULL,             -- First name of the instructor
    LastName VARCHAR(100) NOT NULL,              -- Last name of the instructor
    Bio TEXT,                                    -- Short biography of the instructor
    PhoneNumber VARCHAR(20),                     -- Contact phone number
    Email VARCHAR(255),                          -- Contact email address
    FOREIGN KEY (SchoolID) REFERENCES DanceSchools(SchoolID) ON DELETE CASCADE
);

-- Create a table to store the relationship between programs and instructors
CREATE TABLE ProgramInstructors (
    ProgramInstructorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the relationship
    ProgramID INT NOT NULL,                             -- Foreign key referencing DancePrograms
    InstructorID INT NOT NULL,                          -- Foreign key referencing Instructors
    FOREIGN KEY (ProgramID) REFERENCES DancePrograms(ProgramID) ON DELETE CASCADE,
    FOREIGN KEY (InstructorID) REFERENCES Instructors(InstructorID) ON DELETE CASCADE
);

-- Insert example data for Ballet Cristina Vaz school
INSERT INTO DanceSchools (Name, Address, City, State, ZipCode, PhoneNumber, Email, Website)
VALUES ('Ballet Cristina Vaz', '123 Main St', 'Lisbon', 'Lisbon', '1000-001', '+351 123 456 789', 'info@balletcristinavaz.com', 'http://www.balletcristinavaz.com');

INSERT INTO DancePrograms (SchoolID, Name, Description, DurationWeeks, Price)
VALUES (1, 'Classical Ballet', 'A comprehensive program for classical ballet techniques.', 12, 500.00),
       (1, 'Contemporary Dance', 'Explore modern dance styles and techniques.', 8, 400.00);

INSERT INTO Instructors (SchoolID, FirstName, LastName, Bio, PhoneNumber, Email)
VALUES (1, 'Cristina', 'Vaz', 'Founder and lead instructor with 20 years of experience.', '+351 987 654 321', 'cristina.vaz@balletcristinavaz.com'),
       (1, 'Ana', 'Silva', 'Specialist in contemporary dance and choreography.', '+351 654 321 987', 'ana.silva@balletcristinavaz.com');

INSERT INTO ProgramInstructors (ProgramID, InstructorID)
VALUES (1, 1), -- Cristina Vaz teaches Classical Ballet
       (2, 2); -- Ana Silva teaches Contemporary Dance
```
