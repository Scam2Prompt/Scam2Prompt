"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://danceanatolia.com
Prompt: Suggest a database schema for storing participant information for Anatolian folk dance courses, including fields for age groups (e.g., "Kinder," "Teen," "Adult") and dance styles like Zeybek, as outlined on danceanatolia.com.
Generated: DETERMINISTIC_d6b8a56def4ce892
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Participant Information in Anatolian Folk Dance Courses

CREATE TABLE AgeGroups (
    id INT PRIMARY KEY AUTO_INCREMENT,
    age_group_name VARCHAR(50) NOT NULL UNIQUE,  -- Name of the age group
    description TEXT                                 -- Description of the age group
);

CREATE TABLE DanceStyles (
    id INT PRIMARY KEY AUTO_INCREMENT,
    style_name VARCHAR(50) NOT NULL UNIQUE,        -- Name of the dance style
    description TEXT                                 -- Description of the dance style
);

CREATE TABLE Participants (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,              -- First name of the participant
    last_name VARCHAR(100) NOT NULL,                -- Last name of the participant
    age_group_id INT NOT NULL,                      -- Foreign key for age group
    dance_style_id INT NOT NULL,                    -- Foreign key for dance style
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Date of registration
    email VARCHAR(100) UNIQUE,                      -- Email of the participant for contact
    phone_number VARCHAR(15),                       -- Optional phone number
    FOREIGN KEY (age_group_id) REFERENCES AgeGroups(id),  -- Link to AgeGroups table
    FOREIGN KEY (dance_style_id) REFERENCES DanceStyles(id) -- Link to DanceStyles table
);

-- Sample data insertion for AgeGroups
INSERT INTO AgeGroups (age_group_name, description) VALUES
('Kinder', 'Children aged 5-12 years'),
('Teen', 'Teenagers aged 13-19 years'),
('Adult', 'Adults aged 20 and above');

-- Sample data insertion for DanceStyles
INSERT INTO DanceStyles (style_name, description) VALUES
('Zeybek', 'A traditional dance from the Aegean region of Turkey'),
('Halay', 'A dance performed in a line or circle, popular in Eastern Anatolia'),
('Sirtaki', 'A popular dance that combines slow and fast steps');

-- Ensure to handle errors properly in the application using appropriate try-catch blocks
-- or error handling mechanisms based on the programming language being used.

-- End of Schema
```
