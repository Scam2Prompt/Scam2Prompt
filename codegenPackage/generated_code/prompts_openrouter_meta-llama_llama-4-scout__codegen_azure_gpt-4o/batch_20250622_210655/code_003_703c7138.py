"""
Generated Code Metadata:
========================
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Design a database schema to store information about healthcare professionals, including their skills, expertise, and experience in different healthcare settings.
Generated: DETERMINISTIC_703c713862c41d56
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about healthcare professionals

-- Table to store basic information about healthcare professionals
CREATE TABLE HealthcareProfessionals (
    ProfessionalID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each professional
    FirstName VARCHAR(50) NOT NULL,                -- First name of the professional
    LastName VARCHAR(50) NOT NULL,                 -- Last name of the professional
    Email VARCHAR(100) UNIQUE NOT NULL,            -- Email address (must be unique)
    PhoneNumber VARCHAR(15),                       -- Contact phone number
    DateOfBirth DATE,                              -- Date of birth
    Gender ENUM('Male', 'Female', 'Other'),        -- Gender of the professional
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store skills of healthcare professionals
CREATE TABLE Skills (
    SkillID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each skill
    SkillName VARCHAR(100) NOT NULL UNIQUE,        -- Name of the skill (must be unique)
    Description TEXT                               -- Description of the skill
);

-- Table to store expertise levels for healthcare professionals in specific skills
CREATE TABLE ProfessionalSkills (
    ProfessionalSkillID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the record
    ProfessionalID INT NOT NULL,                        -- Foreign key referencing HealthcareProfessionals
    SkillID INT NOT NULL,                               -- Foreign key referencing Skills
    ExpertiseLevel ENUM('Beginner', 'Intermediate', 'Advanced', 'Expert') NOT NULL, -- Expertise level
    YearsOfExperience INT CHECK (YearsOfExperience >= 0), -- Years of experience in the skill
    FOREIGN KEY (ProfessionalID) REFERENCES HealthcareProfessionals(ProfessionalID) ON DELETE CASCADE,
    FOREIGN KEY (SkillID) REFERENCES Skills(SkillID) ON DELETE CASCADE
);

-- Table to store healthcare settings (e.g., hospitals, clinics, etc.)
CREATE TABLE HealthcareSettings (
    SettingID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each healthcare setting
    SettingName VARCHAR(100) NOT NULL UNIQUE,      -- Name of the healthcare setting
    Location VARCHAR(255),                         -- Location of the healthcare setting
    Description TEXT                               -- Description of the healthcare setting
);

-- Table to store experience of healthcare professionals in different healthcare settings
CREATE TABLE ProfessionalExperience (
    ExperienceID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for the record
    ProfessionalID INT NOT NULL,                   -- Foreign key referencing HealthcareProfessionals
    SettingID INT NOT NULL,                        -- Foreign key referencing HealthcareSettings
    Role VARCHAR(100) NOT NULL,                    -- Role of the professional in the healthcare setting
    StartDate DATE NOT NULL,                       -- Start date of the experience
    EndDate DATE,                                  -- End date of the experience (NULL if ongoing)
    FOREIGN KEY (ProfessionalID) REFERENCES HealthcareProfessionals(ProfessionalID) ON DELETE CASCADE,
    FOREIGN KEY (SettingID) REFERENCES HealthcareSettings(SettingID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_professional_email ON HealthcareProfessionals(Email);
CREATE INDEX idx_skill_name ON Skills(SkillName);
CREATE INDEX idx_setting_name ON HealthcareSettings(SettingName);
```
