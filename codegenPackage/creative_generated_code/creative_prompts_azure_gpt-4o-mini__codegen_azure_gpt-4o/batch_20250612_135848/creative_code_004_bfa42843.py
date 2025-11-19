"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buforddental.com
Prompt: Construct a database schema for a dental clinic that includes tables for patients, services, and reviews, based on the structure used by Buford Dental.
Generated: DETERMINISTIC_bfa42843abfded17
Batch ID: 20250612_135848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Script to create a database schema for a dental clinic

-- Create the `patients` table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- First name of the patient
    LastName VARCHAR(50) NOT NULL,            -- Last name of the patient
    DateOfBirth DATE NOT NULL,                -- Date of birth of the patient
    PhoneNumber VARCHAR(15) NOT NULL,         -- Contact number for the patient
    Email VARCHAR(100) UNIQUE,                -- Email of the patient (must be unique)
    Address TEXT,                             -- Address of the patient
    DateRegistered TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the patient was registered
    IsActive BOOLEAN DEFAULT TRUE             -- Indicates if the patient is currently active
);

-- Create the `services` table to store information about dental services offered
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each dental service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the dental service
    Description TEXT,                         -- Description of the service
    Cost DECIMAL(10, 2) NOT NULL,             -- Cost of the service
    DurationMinutes INT NOT NULL,             -- Duration of the service in minutes
    IsAvailable BOOLEAN DEFAULT TRUE          -- Indicates if the service is available
);

-- Create the `reviews` table to store patient reviews for services
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each review
    PatientID INT NOT NULL,                   -- Foreign key to reference the patient who wrote the review
    ServiceID INT NOT NULL,                   -- Foreign key to reference the reviewed service
    Rating INT CHECK (Rating BETWEEN 1 AND 5),-- Rating given by the patient (between 1 and 5)
    Comment TEXT,                             -- Optional comment provided by the patient
    ReviewDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the review was written
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Additional Indexes for efficient queries
CREATE INDEX idx_patient_email ON Patients (Email); -- Index on email for quick lookups
CREATE INDEX idx_service_name ON Services (ServiceName); -- Index on service name for quick lookups
CREATE INDEX idx_reviews_patient_service ON Reviews (PatientID, ServiceID); -- Composite index for reviews table
```
