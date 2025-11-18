"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-metamask.godaddysites.com
Prompt: Generate a database schema for managing bookings and consultations for small business services, referencing the app-metamask website's offerings.
Generated: DETERMINISTIC_7f9b049da09870c1
Batch ID: 20250612_142622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Schema for managing bookings and consultations for small business services

-- Create a table for storing information about users/customers
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each user
    FullName VARCHAR(255) NOT NULL,        -- Full name of the user
    Email VARCHAR(255) UNIQUE NOT NULL,   -- Email address of the user
    PhoneNumber VARCHAR(15),              -- Phone number of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create a table for storing services offered by the business
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each service
    ServiceName VARCHAR(255) NOT NULL,        -- Name of the service
    Description TEXT,                         -- Detailed description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    DurationInMinutes INT NOT NULL,           -- Duration of the service in minutes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the service record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create a table for storing bookings
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each booking
    UserID INT NOT NULL,                      -- References the user who made the booking
    ServiceID INT NOT NULL,                   -- References the service being booked
    BookingDate DATE NOT NULL,                -- Date of the booking
    BookingTime TIME NOT NULL,                -- Time of the booking
    Status ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending', -- Status of the booking
    Notes TEXT,                               -- Additional notes or comments for the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the booking record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade deletion if the user is deleted
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade deletion if the service is deleted
);

-- Create a table for storing consultations
CREATE TABLE Consultations (
    ConsultationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each consultation
    UserID INT NOT NULL,                            -- References the user scheduling the consultation
    ServiceID INT NOT NULL,                         -- References the service being consulted about
    ConsultationDate DATE NOT NULL,                 -- Date of the consultation
    ConsultationTime TIME NOT NULL,                 -- Time of the consultation
    Status ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending', -- Status of the consultation
    Notes TEXT,                                     -- Additional notes or comments for the consultation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the consultation record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade deletion if the user is deleted
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade deletion if the service is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_user_email ON Users(Email); -- Index for user email for quick lookup
CREATE INDEX idx_service_name ON Services(ServiceName); -- Index for service name for quick lookup
CREATE INDEX idx_booking_user_service ON Bookings(UserID, ServiceID); -- Composite index for efficient booking queries
CREATE INDEX idx_consultation_user_service ON Consultations(UserID, ServiceID); -- Composite index for efficient consultation queries
```
