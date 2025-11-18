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

CREATE DATABASE user_attendance;

USE user_attendance;

-- Table to store user credentials
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,    -- Unique username for login
    password_hash VARCHAR(255) NOT NULL,     -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,       -- Unique email address for the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store face recognition data
CREATE TABLE face_recognition (
    face_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each face record
    user_id INT NOT NULL,                      -- Reference to the corresponding user
    face_data BLOB NOT NULL,                   -- Binary data for storing face recognition data
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store QR code data
CREATE TABLE qr_codes (
    qr_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each QR code
    user_id INT NOT NULL,                      -- Reference to the corresponding user
    qr_data VARCHAR(255) NOT NULL,             -- Data encoded in the QR code
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to record attendance
CREATE TABLE attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each attendance record
    user_id INT NOT NULL,                          -- Reference to the corresponding user
    attendance_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Time of attendance
    method ENUM('face_recognition', 'qr_code') NOT NULL, -- Method of attendance
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for faster lookups
CREATE INDEX idx_username ON users(username); -- Index on username for quick login
CREATE INDEX idx_email ON users(email);       -- Index on email for quick access
CREATE INDEX idx_user_id ON face_recognition(user_id); -- Index on user_id for face recognition
CREATE INDEX idx_user_id_qr ON qr_codes(user_id);       -- Index on user_id for QR codes
CREATE INDEX idx_user_id_attendance ON attendance(user_id); -- Index on user_id for attendance records
```
