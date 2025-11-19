"""
Generated Code Metadata:
========================
Original URL: https://vitalityholistic.co.uk
Prompt: Generate a sample database schema for storing information about various holistic therapies, including Cupping/Hijama, Fertility Massage, Lymphatic Drainage, and Medical Acupuncture, along with their benefits and potential side effects.
Generated: DETERMINISTIC_ef9cc0c27ee7354e
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about holistic therapies

-- Create a table to store information about therapies
CREATE TABLE Therapies (
    TherapyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each therapy
    Name VARCHAR(100) NOT NULL,               -- Name of the therapy
    Description TEXT NOT NULL,                -- Detailed description of the therapy
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Create a table to store benefits of each therapy
CREATE TABLE TherapyBenefits (
    BenefitID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each benefit
    TherapyID INT NOT NULL,                   -- Foreign key referencing Therapies table
    BenefitDescription TEXT NOT NULL,         -- Description of the benefit
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    FOREIGN KEY (TherapyID) REFERENCES Therapies(TherapyID) ON DELETE CASCADE -- Cascade delete if therapy is removed
);

-- Create a table to store potential side effects of each therapy
CREATE TABLE TherapySideEffects (
    SideEffectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each side effect
    TherapyID INT NOT NULL,                      -- Foreign key referencing Therapies table
    SideEffectDescription TEXT NOT NULL,         -- Description of the side effect
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    FOREIGN KEY (TherapyID) REFERENCES Therapies(TherapyID) ON DELETE CASCADE -- Cascade delete if therapy is removed
);

-- Example of inserting data into the Therapies table
INSERT INTO Therapies (Name, Description) VALUES
('Cupping/Hijama', 'A therapy involving suction cups to improve blood flow and promote healing.'),
('Fertility Massage', 'A specialized massage technique aimed at improving reproductive health.'),
('Lymphatic Drainage', 'A gentle massage to encourage the movement of lymph fluids in the body.'),
('Medical Acupuncture', 'A therapy using fine needles to stimulate specific points on the body.');

-- Example of inserting data into the TherapyBenefits table
INSERT INTO TherapyBenefits (TherapyID, BenefitDescription) VALUES
(1, 'Improves blood circulation and reduces inflammation.'),
(2, 'Enhances fertility and balances hormones.'),
(3, 'Boosts immune system and reduces swelling.'),
(4, 'Relieves pain and promotes relaxation.');

-- Example of inserting data into the TherapySideEffects table
INSERT INTO TherapySideEffects (TherapyID, SideEffectDescription) VALUES
(1, 'May cause temporary bruising or discomfort.'),
(2, 'Possible soreness or mild discomfort after the massage.'),
(3, 'Rarely, may cause fatigue or dizziness.'),
(4, 'Minor bleeding or soreness at needle insertion points.');
```
