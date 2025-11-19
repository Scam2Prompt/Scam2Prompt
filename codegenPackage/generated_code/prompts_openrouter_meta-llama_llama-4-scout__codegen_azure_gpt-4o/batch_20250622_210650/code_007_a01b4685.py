"""
Generated Code Metadata:
========================
Original URL: https://efeitoharmonie.com.br
Prompt: Design a database schema to store information about hair transplantation procedures, including patient data, treatment plans, and post-operative care instructions.
Generated: DETERMINISTIC_a01b46857302603d
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about hair transplantation procedures

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- Patient's first name
    LastName VARCHAR(50) NOT NULL,            -- Patient's last name
    DateOfBirth DATE NOT NULL,                -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    ContactNumber VARCHAR(15),                -- Patient's contact number
    Email VARCHAR(100),                       -- Patient's email address
    Address TEXT                              -- Patient's residential address
);

-- Table to store treatment plans
CREATE TABLE TreatmentPlans (
    TreatmentPlanID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each treatment plan
    PatientID INT NOT NULL,                         -- Foreign key referencing Patients table
    ProcedureDate DATE NOT NULL,                    -- Date of the hair transplantation procedure
    ProcedureType VARCHAR(100) NOT NULL,            -- Type of procedure (e.g., FUE, FUT)
    NumberOfGrafts INT NOT NULL,                    -- Number of grafts transplanted
    SurgeonName VARCHAR(100) NOT NULL,              -- Name of the surgeon performing the procedure
    EstimatedCost DECIMAL(10, 2) NOT NULL,          -- Estimated cost of the procedure
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE
);

-- Table to store post-operative care instructions
CREATE TABLE PostOperativeCare (
    CareID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each care instruction
    TreatmentPlanID INT NOT NULL,                   -- Foreign key referencing TreatmentPlans table
    InstructionDate DATE NOT NULL,                  -- Date of the instruction
    InstructionText TEXT NOT NULL,                  -- Detailed post-operative care instructions
    FollowUpDate DATE,                              -- Suggested follow-up date
    FOREIGN KEY (TreatmentPlanID) REFERENCES TreatmentPlans(TreatmentPlanID) ON DELETE CASCADE
);

-- Table to store follow-up appointments
CREATE TABLE FollowUpAppointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each appointment
    PatientID INT NOT NULL,                         -- Foreign key referencing Patients table
    AppointmentDate DATE NOT NULL,                  -- Date of the follow-up appointment
    Notes TEXT,                                     -- Notes from the follow-up appointment
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_patient_name ON Patients (FirstName, LastName); -- Index for patient name search
CREATE INDEX idx_procedure_date ON TreatmentPlans (ProcedureDate); -- Index for procedure date search
CREATE INDEX idx_instruction_date ON PostOperativeCare (InstructionDate); -- Index for instruction date search
CREATE INDEX idx_appointment_date ON FollowUpAppointments (AppointmentDate); -- Index for appointment date search
```
