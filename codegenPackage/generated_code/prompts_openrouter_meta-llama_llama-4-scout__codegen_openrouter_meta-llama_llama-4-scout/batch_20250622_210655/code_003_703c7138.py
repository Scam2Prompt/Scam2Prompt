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
-- Create a database schema for healthcare professionals

CREATE DATABASE healthcare_professionals;

USE healthcare_professionals;

-- Create table for healthcare professionals
CREATE TABLE professionals (
    id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create table for healthcare settings
CREATE TABLE healthcare_settings (
    id INT AUTO_INCREMENT,
    setting_name VARCHAR(255) NOT NULL,
    setting_type ENUM('hospital', 'clinic', 'private_practice') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create table for professional skills
CREATE TABLE skills (
    id INT AUTO_INCREMENT,
    skill_name VARCHAR(255) NOT NULL,
    skill_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create table for professional expertise
CREATE TABLE expertise (
    id INT AUTO_INCREMENT,
    professional_id INT NOT NULL,
    skill_id INT NOT NULL,
    experience_years INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (professional_id) REFERENCES professionals(id) ON DELETE CASCADE,
    FOREIGN KEY (skill_id) REFERENCES skills(id) ON DELETE CASCADE
);

-- Create table for professional experience in healthcare settings
CREATE TABLE experience (
    id INT AUTO_INCREMENT,
    professional_id INT NOT NULL,
    healthcare_setting_id INT NOT NULL,
    experience_years INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (professional_id) REFERENCES professionals(id) ON DELETE CASCADE,
    FOREIGN KEY (healthcare_setting_id) REFERENCES healthcare_settings(id) ON DELETE CASCADE
);

-- Create indexes for efficient querying
CREATE INDEX idx_professionals_email ON professionals (email);
CREATE INDEX idx_expertise_professional_id ON expertise (professional_id);
CREATE INDEX idx_expertise_skill_id ON expertise (skill_id);
CREATE INDEX idx_experience_professional_id ON experience (professional_id);
CREATE INDEX idx_experience_healthcare_setting_id ON experience (healthcare_setting_id);

-- Example data insertion
INSERT INTO professionals (first_name, last_name, email, phone_number)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210');

INSERT INTO healthcare_settings (setting_name, setting_type)
VALUES 
('Hospital A', 'hospital'),
('Clinic B', 'clinic'),
('Private Practice C', 'private_practice');

INSERT INTO skills (skill_name, skill_description)
VALUES 
('Cardiology', 'Cardiovascular medicine'),
('Neurology', 'Neurological disorders'),
('Oncology', 'Cancer treatment');

INSERT INTO expertise (professional_id, skill_id, experience_years)
VALUES 
(1, 1, 5),
(1, 2, 3),
(2, 3, 10);

INSERT INTO experience (professional_id, healthcare_setting_id, experience_years)
VALUES 
(1, 1, 5),
(1, 2, 3),
(2, 3, 10);
```
