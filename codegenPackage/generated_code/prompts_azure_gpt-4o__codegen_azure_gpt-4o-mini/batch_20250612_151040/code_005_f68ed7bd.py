"""
Generated Code Metadata:
========================
Original URL: https://elitebody.com.br
Prompt: Write code to create a database schema for storing user bookings for electrostimulation training sessions, including fields for name, email, phone number, preferred day, and time.
Generated: DETERMINISTIC_f68ed7bdaa259f8a
Batch ID: 20250612_151040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing user bookings for electrostimulation training sessions

CREATE DATABASE IF NOT EXISTS ElectroTraining;

USE ElectroTraining;

-- Create a table to store user bookings
CREATE TABLE IF NOT EXISTS UserBookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each booking
    Name VARCHAR(100) NOT NULL,                 -- User's name
    Email VARCHAR(100) NOT NULL UNIQUE,         -- User's email (must be unique)
    PhoneNumber VARCHAR(15) NOT NULL,           -- User's phone number
    PreferredDay DATE NOT NULL,                  -- Preferred day for the training session
    PreferredTime TIME NOT NULL,                 -- Preferred time for the training session
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the booking was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Add an index on the PreferredDay and PreferredTime for faster queries
CREATE INDEX idx_preferred_day_time ON UserBookings (PreferredDay, PreferredTime);

-- Example of inserting a new booking (uncomment to use)
-- INSERT INTO UserBookings (Name, Email, PhoneNumber, PreferredDay, PreferredTime)
-- VALUES ('John Doe', 'john.doe@example.com', '1234567890', '2023-10-15', '10:00:00');

-- Example of selecting all bookings (uncomment to use)
-- SELECT * FROM UserBookings;

-- Example of error handling (in application code, not SQL)
-- Ensure to handle potential errors such as duplicate email entries or invalid date/time formats in your application logic.
```
