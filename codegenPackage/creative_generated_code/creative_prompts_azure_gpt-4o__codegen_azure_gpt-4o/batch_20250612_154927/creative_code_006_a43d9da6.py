"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://formulir.site
Prompt: Generate a database schema for storing user credentials and attendance records, including support for face recognition and QR code data, as seen on formulir.site.
Generated: DETERMINISTIC_a43d9da674a4ce0f
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing user credentials and attendance records
-- Includes support for face recognition data and QR code data

-- Table to store user credentials
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Username for login
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Email address for communication
    FullName VARCHAR(100) NOT NULL,        -- User's full name
    ProfilePicture BLOB,                   -- Optional profile picture for face recognition
    FaceRecognitionData BLOB,              -- Encoded face recognition data (e.g., embeddings)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the user was last updated
);

-- Table to store attendance records
CREATE TABLE AttendanceRecords (
    RecordID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    UserID INT NOT NULL,                     -- Reference to the Users table
    AttendanceDate DATE NOT NULL,            -- Date of the attendance
    CheckedInTime TIME,                      -- Time when the user checked in
    CheckedOutTime TIME,                     -- Time when the user checked out
    QRCodeData VARCHAR(255),                 -- QR code information used for attendance
    FaceRecognitionMatch BOOLEAN DEFAULT FALSE, -- Indicates if face recognition was used successfully
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Foreign key constraint
);

-- Indexes to improve query performance
CREATE INDEX IDX_Attendance_UserID_Date ON AttendanceRecords(UserID, AttendanceDate);
CREATE INDEX IDX_Users_Email ON Users(Email);
CREATE INDEX IDX_Users_Username ON Users(Username);
```
