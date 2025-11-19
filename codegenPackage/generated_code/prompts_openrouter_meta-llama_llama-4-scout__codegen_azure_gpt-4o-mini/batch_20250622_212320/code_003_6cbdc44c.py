"""
Generated Code Metadata:
========================
Original URL: https://formulir.site
Prompt: "Design a database schema for storing user information and attendance records using face recognition and QR code login methods."
Generated: DETERMINISTIC_6cbdc44cf73fde74
Batch ID: 20250622_212320
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing user information and attendance records
CREATE DATABASE UserAttendanceDB;

USE UserAttendanceDB;

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FirstName VARCHAR(50) NOT NULL,        -- User's first name
    LastName VARCHAR(50) NOT NULL,         -- User's last name
    Email VARCHAR(100) UNIQUE NOT NULL,    -- User's email address
    PhoneNumber VARCHAR(15),                -- User's phone number
    FaceRecognitionData BLOB NOT NULL,     -- Binary data for face recognition
    QRCodeData BLOB NOT NULL,              -- Binary data for QR code
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store attendance records
CREATE TABLE AttendanceRecords (
    AttendanceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each attendance record
    UserID INT NOT NULL,                         -- Foreign key referencing Users table
    AttendanceDate DATE NOT NULL,                -- Date of attendance
    CheckInTime TIME NOT NULL,                   -- Check-in time
    CheckOutTime TIME,                           -- Check-out time (nullable)
    Method ENUM('FaceRecognition', 'QRCode') NOT NULL, -- Method of attendance
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_user_email ON Users(Email);
CREATE INDEX idx_attendance_user ON AttendanceRecords(UserID);
CREATE INDEX idx_attendance_date ON AttendanceRecords(AttendanceDate);
```
