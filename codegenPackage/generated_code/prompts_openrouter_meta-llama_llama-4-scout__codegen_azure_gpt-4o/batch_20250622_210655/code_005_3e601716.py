"""
Generated Code Metadata:
========================
Original URL: https://velemeny.moriczdental.hu
Prompt: Create a SQL database schema for storing patient reviews and ratings for a dental clinic, inspired by the types of evaluations collected on the Móricz Dental website.
Generated: DETERMINISTIC_3e6017169932faeb
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for storing patient reviews and ratings for a dental clinic

-- Create a table to store information about patients
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- Patient's first name
    LastName VARCHAR(50) NOT NULL,            -- Patient's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Patient's email address (unique for identification)
    PhoneNumber VARCHAR(15),                  -- Patient's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the patient record was created
);

-- Create a table to store reviews and ratings
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each review
    PatientID INT NOT NULL,                   -- Foreign key linking to the Patients table
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the patient (1 to 5 scale)
    ReviewText TEXT,                          -- Textual review provided by the patient
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store responses from the clinic to patient reviews
CREATE TABLE ClinicResponses (
    ResponseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each response
    ReviewID INT NOT NULL,                      -- Foreign key linking to the Reviews table
    ResponseText TEXT NOT NULL,                 -- Textual response from the clinic
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the response was created
    FOREIGN KEY (ReviewID) REFERENCES Reviews(ReviewID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create indexes for faster querying
CREATE INDEX idx_patient_email ON Patients(Email); -- Index on email for quick lookup
CREATE INDEX idx_review_rating ON Reviews(Rating); -- Index on rating for filtering reviews

-- Error handling and constraints
-- Ensure that email addresses are unique and properly formatted
ALTER TABLE Patients ADD CONSTRAINT chk_email_format CHECK (Email LIKE '%_@__%.__%');

-- Ensure that reviews cannot be empty if submitted
ALTER TABLE Reviews ADD CONSTRAINT chk_review_text CHECK (ReviewText IS NOT NULL AND LENGTH(ReviewText) > 0);

-- Ensure that clinic responses cannot be empty
ALTER TABLE ClinicResponses ADD CONSTRAINT chk_response_text CHECK (ResponseText IS NOT NULL AND LENGTH(ResponseText) > 0);
```
