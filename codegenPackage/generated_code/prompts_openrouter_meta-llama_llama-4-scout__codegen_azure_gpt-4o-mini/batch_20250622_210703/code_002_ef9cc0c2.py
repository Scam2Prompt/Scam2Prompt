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
-- Sample database schema for storing information about various holistic therapies

-- Create a table to store information about therapies
CREATE TABLE Therapies (
    TherapyID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each therapy
    TherapyName VARCHAR(100) NOT NULL,        -- Name of the therapy
    Description TEXT,                          -- Description of the therapy
    Benefits TEXT,                             -- Benefits of the therapy
    SideEffects TEXT,                          -- Potential side effects of the therapy
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Create a table to store information about practitioners
CREATE TABLE Practitioners (
    PractitionerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each practitioner
    Name VARCHAR(100) NOT NULL,                     -- Name of the practitioner
    Specialty VARCHAR(100),                          -- Specialty of the practitioner
    ContactInfo VARCHAR(255),                        -- Contact information for the practitioner
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Create a table to link therapies and practitioners
CREATE TABLE TherapyPractitioner (
    TherapyPractitionerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for the relationship
    TherapyID INT NOT NULL,                               -- Foreign key referencing Therapies
    PractitionerID INT NOT NULL,                          -- Foreign key referencing Practitioners
    FOREIGN KEY (TherapyID) REFERENCES Therapies(TherapyID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (PractitionerID) REFERENCES Practitioners(PractitionerID) ON DELETE CASCADE,  -- Ensures referential integrity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,       -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Create a table to store client feedback on therapies
CREATE TABLE Feedback (
    FeedbackID INT PRIMARY KEY AUTO_INCREMENT,          -- Unique identifier for each feedback entry
    TherapyID INT NOT NULL,                             -- Foreign key referencing Therapies
    ClientName VARCHAR(100),                            -- Name of the client providing feedback
    Rating INT CHECK (Rating BETWEEN 1 AND 5),         -- Rating given by the client (1 to 5 scale)
    Comments TEXT,                                      -- Additional comments from the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp of when the feedback was created
    FOREIGN KEY (TherapyID) REFERENCES Therapies(TherapyID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Sample data insertion for Therapies
INSERT INTO Therapies (TherapyName, Description, Benefits, SideEffects) VALUES
('Cupping/Hijama', 'A therapy that involves placing cups on the skin to create suction.', 'Improves blood flow, reduces inflammation, promotes relaxation.', 'Mild bruising, skin irritation.'),
('Fertility Massage', 'A specialized massage aimed at enhancing fertility.', 'Improves circulation, reduces stress, balances hormones.', 'Temporary discomfort, emotional release.'),
('Lymphatic Drainage', 'A gentle massage technique that encourages the movement of lymph fluids.', 'Reduces swelling, detoxifies the body, boosts immune function.', 'Fatigue, mild soreness.'),
('Medical Acupuncture', 'A form of acupuncture used for medical purposes.', 'Pain relief, stress reduction, improved overall health.', 'Soreness at needle sites, minor bleeding.');

-- Sample data insertion for Practitioners
INSERT INTO Practitioners (Name, Specialty, ContactInfo) VALUES
('Dr. Jane Smith', 'Acupuncturist', 'jane.smith@example.com'),
('John Doe', 'Massage Therapist', 'john.doe@example.com');

-- Sample data insertion for TherapyPractitioner
INSERT INTO TherapyPractitioner (TherapyID, PractitionerID) VALUES
(1, 1),  -- Cupping/Hijama with Dr. Jane Smith
(2, 2);  -- Fertility Massage with John Doe

-- Sample data insertion for Feedback
INSERT INTO Feedback (TherapyID, ClientName, Rating, Comments) VALUES
(1, 'Alice Johnson', 5, 'Amazing experience, felt rejuvenated!'),
(2, 'Bob Brown', 4, 'Very relaxing, but a bit uncomfortable at times.');
```
