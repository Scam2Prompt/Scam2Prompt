"""
Generated Code Metadata:
========================
Original URL: https://amarparasanar.com.mx
Prompt: Design a database schema to store client information, therapy sessions, and course materials for an online therapy platform, ensuring secure and confidential data storage, as emphasized by Amar para Sanar's therapists.
Generated: DETERMINISTIC_f8d83fd049822a86
Batch ID: 20250622_211453
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an online therapy platform

-- Create a table to store client information
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL, -- Client's first name
    last_name VARCHAR(50) NOT NULL, -- Client's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Client's email address
    phone_number VARCHAR(15), -- Client's phone number
    date_of_birth DATE NOT NULL, -- Client's date of birth
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    CONSTRAINT chk_age CHECK (date_of_birth <= CURRENT_DATE - INTERVAL '18 years') -- Ensure client is at least 18 years old
);

-- Create a table to store therapy sessions
CREATE TABLE TherapySessions (
    session_id SERIAL PRIMARY KEY, -- Unique identifier for each session
    client_id INT NOT NULL, -- Foreign key referencing Clients table
    therapist_id INT NOT NULL, -- Foreign key referencing Therapists table
    session_date TIMESTAMP NOT NULL, -- Date and time of the session
    session_notes TEXT, -- Notes from the session
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (therapist_id) REFERENCES Therapists(therapist_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store therapists' information
CREATE TABLE Therapists (
    therapist_id SERIAL PRIMARY KEY, -- Unique identifier for each therapist
    first_name VARCHAR(50) NOT NULL, -- Therapist's first name
    last_name VARCHAR(50) NOT NULL, -- Therapist's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Therapist's email address
    specialization VARCHAR(100), -- Therapist's area of specialization
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store course materials
CREATE TABLE CourseMaterials (
    material_id SERIAL PRIMARY KEY, -- Unique identifier for each material
    title VARCHAR(100) NOT NULL, -- Title of the course material
    description TEXT, -- Description of the course material
    file_path VARCHAR(255) NOT NULL, -- Path to the file (e.g., PDF, video)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to link clients to course materials
CREATE TABLE ClientCourseMaterials (
    client_id INT NOT NULL, -- Foreign key referencing Clients table
    material_id INT NOT NULL, -- Foreign key referencing CourseMaterials table
    PRIMARY KEY (client_id, material_id), -- Composite primary key
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (material_id) REFERENCES CourseMaterials(material_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(email);
CREATE INDEX idx_therapist_email ON Therapists(email);
CREATE INDEX idx_session_date ON TherapySessions(session_date);
```
