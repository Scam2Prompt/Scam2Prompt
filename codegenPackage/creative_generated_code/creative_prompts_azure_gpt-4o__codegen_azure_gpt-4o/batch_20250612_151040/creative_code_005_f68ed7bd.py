"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elitebody.com.br
Prompt: Write code to create a database schema for storing user bookings for electrostimulation training sessions, including fields for name, email, phone number, preferred day, and time.
Generated: DETERMINISTIC_f68ed7bdaa259f8a
Batch ID: 20250612_151040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- File: electrostimulation_booking_schema.sql

-- This script creates a database schema to store user bookings for electrostimulation training sessions.

-- Create the table to store user bookings
CREATE TABLE UserBookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each booking
    Name VARCHAR(100) NOT NULL,                  -- Full name of the user
    Email VARCHAR(100) NOT NULL,                 -- Email address of the user
    PhoneNumber VARCHAR(15) NOT NULL,            -- Phone number of the user
    PreferredDay DATE NOT NULL,                  -- Preferred day for the training session
    PreferredTime TIME NOT NULL,                 -- Preferred time for the training session
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the booking was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the booking was last updated
);

-- Add an index for the email field to speed up lookups
CREATE INDEX idx_email ON UserBookings (Email);

-- Add an index for PreferredDay and PreferredTime for scheduling queries
CREATE INDEX idx_preferred_datetime ON UserBookings (PreferredDay, PreferredTime);

-- Ensure data integrity by checking for valid email format
CREATE TRIGGER validate_email_format 
BEFORE INSERT ON UserBookings
FOR EACH ROW
BEGIN
    IF NEW.Email NOT LIKE '%@%.%' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid email format.';
    END IF;
END;

-- Example of additional error handling: ensuring no duplicate bookings for the same user on the same day and time
CREATE UNIQUE INDEX idx_unique_booking ON UserBookings (Email, PreferredDay, PreferredTime);
```
