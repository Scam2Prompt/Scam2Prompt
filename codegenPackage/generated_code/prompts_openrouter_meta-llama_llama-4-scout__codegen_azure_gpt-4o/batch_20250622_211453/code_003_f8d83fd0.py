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
-- This schema is designed to store client information, therapy sessions, and course materials
-- with a focus on secure and confidential data storage.

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(100) NOT NULL,         -- Client's first name
    LastName VARCHAR(100) NOT NULL,          -- Client's last name
    Email VARCHAR(255) NOT NULL UNIQUE,      -- Client's email address (unique for login)
    PhoneNumber VARCHAR(15),                 -- Optional phone number
    PasswordHash VARCHAR(255) NOT NULL,      -- Hashed password for secure authentication
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store therapy session information
CREATE TABLE TherapySessions (
    SessionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each session
    ClientID INT NOT NULL,                    -- Foreign key referencing the client
    TherapistName VARCHAR(255) NOT NULL,      -- Name of the therapist conducting the session
    SessionDate DATETIME NOT NULL,            -- Date and time of the session
    SessionNotes TEXT,                        -- Confidential notes from the session
    IsCompleted BOOLEAN DEFAULT FALSE,        -- Status of the session (completed or not)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of session creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store course materials
CREATE TABLE CourseMaterials (
    MaterialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each material
    Title VARCHAR(255) NOT NULL,               -- Title of the course material
    Description TEXT,                          -- Description of the material
    FilePath VARCHAR(255) NOT NULL,            -- Path to the file (stored securely)
    UploadedBy VARCHAR(255) NOT NULL,          -- Name of the uploader (e.g., therapist/admin)
    UploadedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of upload
    IsActive BOOLEAN DEFAULT TRUE              -- Status of the material (active or archived)
);

-- Table to track which clients have access to which course materials
CREATE TABLE ClientCourseAccess (
    AccessID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each access record
    ClientID INT NOT NULL,                   -- Foreign key referencing the client
    MaterialID INT NOT NULL,                 -- Foreign key referencing the course material
    AccessGrantedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when access was granted
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (MaterialID) REFERENCES CourseMaterials(MaterialID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients (Email);
CREATE INDEX idx_session_client ON TherapySessions (ClientID);
CREATE INDEX idx_access_client_material ON ClientCourseAccess (ClientID, MaterialID);

-- Security considerations:
-- 1. Passwords are stored as hashes (e.g., bcrypt) and never in plain text.
-- 2. Sensitive data (e.g., session notes) should be encrypted at the application level.
-- 3. File paths for course materials should point to a secure storage system (e.g., AWS S3).
-- 4. Ensure database connections use SSL/TLS for secure communication.
-- 5. Regularly audit and monitor access to sensitive data.
```
