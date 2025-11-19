"""
Generated Code Metadata:
========================
Original URL: https://atlas.visit.express
Prompt: "Design a simple database schema for storing experiences, bookings, and user information for a platform like Visit Express."
Generated: DETERMINISTIC_61ecc7a935226c0c
Batch ID: 20250622_212709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Visit Express platform

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FirstName VARCHAR(50) NOT NULL,        -- User's first name
    LastName VARCHAR(50) NOT NULL,         -- User's last name
    Email VARCHAR(100) NOT NULL UNIQUE,    -- User's email address (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,   -- Hashed password for security
    PhoneNumber VARCHAR(15),              -- Optional phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store experiences offered on the platform
CREATE TABLE Experiences (
    ExperienceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each experience
    Title VARCHAR(100) NOT NULL,                -- Title of the experience
    Description TEXT NOT NULL,                  -- Detailed description of the experience
    Location VARCHAR(100) NOT NULL,             -- Location of the experience
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the experience
    MaxParticipants INT NOT NULL,               -- Maximum number of participants allowed
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the experience was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store bookings made by users
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each booking
    UserID INT NOT NULL,                      -- Foreign key referencing Users table
    ExperienceID INT NOT NULL,                -- Foreign key referencing Experiences table
    BookingDate DATE NOT NULL,                -- Date of the booking
    NumberOfParticipants INT NOT NULL,        -- Number of participants for the booking
    TotalPrice DECIMAL(10, 2) NOT NULL,       -- Total price for the booking
    Status ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending', -- Status of the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the booking was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is deleted
    FOREIGN KEY (ExperienceID) REFERENCES Experiences(ExperienceID) ON DELETE CASCADE -- Cascade delete if experience is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_user_email ON Users (Email); -- Index for quick lookup by email
CREATE INDEX idx_experience_location ON Experiences (Location); -- Index for quick lookup by location
CREATE INDEX idx_booking_user_experience ON Bookings (UserID, ExperienceID); -- Composite index for user and experience lookup
```
