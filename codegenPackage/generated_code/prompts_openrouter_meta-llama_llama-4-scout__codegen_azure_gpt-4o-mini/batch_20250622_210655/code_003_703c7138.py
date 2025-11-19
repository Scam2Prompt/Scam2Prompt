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

CREATE TABLE HealthcareProfessionals (
    id SERIAL PRIMARY KEY, -- Unique identifier for each healthcare professional
    first_name VARCHAR(50) NOT NULL, -- First name of the healthcare professional
    last_name VARCHAR(50) NOT NULL, -- Last name of the healthcare professional
    email VARCHAR(100) UNIQUE NOT NULL, -- Email address, must be unique
    phone_number VARCHAR(15), -- Phone number of the healthcare professional
    date_of_birth DATE NOT NULL, -- Date of birth
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

CREATE TABLE Skills (
    id SERIAL PRIMARY KEY, -- Unique identifier for each skill
    skill_name VARCHAR(100) NOT NULL UNIQUE -- Name of the skill, must be unique
);

CREATE TABLE Expertise (
    id SERIAL PRIMARY KEY, -- Unique identifier for each area of expertise
    expertise_name VARCHAR(100) NOT NULL UNIQUE -- Name of the area of expertise, must be unique
);

CREATE TABLE Experience (
    id SERIAL PRIMARY KEY, -- Unique identifier for each experience record
    professional_id INT NOT NULL, -- Foreign key referencing HealthcareProfessionals
    setting VARCHAR(100) NOT NULL, -- Name of the healthcare setting (e.g., hospital, clinic)
    role VARCHAR(100) NOT NULL, -- Role held in the healthcare setting
    start_date DATE NOT NULL, -- Start date of the experience
    end_date DATE, -- End date of the experience (nullable for current roles)
    FOREIGN KEY (professional_id) REFERENCES HealthcareProfessionals(id) ON DELETE CASCADE -- Ensures referential integrity
);

CREATE TABLE ProfessionalSkills (
    professional_id INT NOT NULL, -- Foreign key referencing HealthcareProfessionals
    skill_id INT NOT NULL, -- Foreign key referencing Skills
    PRIMARY KEY (professional_id, skill_id), -- Composite primary key
    FOREIGN KEY (professional_id) REFERENCES HealthcareProfessionals(id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (skill_id) REFERENCES Skills(id) ON DELETE CASCADE -- Ensures referential integrity
);

CREATE TABLE ProfessionalExpertise (
    professional_id INT NOT NULL, -- Foreign key referencing HealthcareProfessionals
    expertise_id INT NOT NULL, -- Foreign key referencing Expertise
    PRIMARY KEY (professional_id, expertise_id), -- Composite primary key
    FOREIGN KEY (professional_id) REFERENCES HealthcareProfessionals(id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (expertise_id) REFERENCES Expertise(id) ON DELETE CASCADE -- Ensures referential integrity
);
```
