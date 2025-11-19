"""
Generated Code Metadata:
========================
Original URL: https://member.bmtours.id
Prompt: Design a database schema for storing user information and tour packages for an Umroh tour operator like BM Tours.
Generated: DETERMINISTIC_43fca5672e0041c2
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Umroh tour operator

-- Create a database for the application
CREATE DATABASE UmrohTourOperator;

-- Use the created database
USE UmrohTourOperator;

-- Table to store user information
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,   -- Unique username for the user
    password_hash VARCHAR(255) NOT NULL,    -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,      -- Unique email address for the user
    full_name VARCHAR(100) NOT NULL,         -- Full name of the user
    phone_number VARCHAR(15),                 -- Optional phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store tour package information
CREATE TABLE TourPackages (
    package_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tour package
    package_name VARCHAR(100) NOT NULL,        -- Name of the tour package
    description TEXT NOT NULL,                  -- Detailed description of the package
    price DECIMAL(10, 2) NOT NULL,             -- Price of the tour package
    duration INT NOT NULL,                      -- Duration of the tour in days
    start_date DATE NOT NULL,                  -- Start date of the tour
    end_date DATE NOT NULL,                    -- End date of the tour
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of package creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store bookings made by users
CREATE TABLE Bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each booking
    user_id INT NOT NULL,                       -- Foreign key referencing Users table
    package_id INT NOT NULL,                    -- Foreign key referencing TourPackages table
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of booking
    status ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending', -- Status of the booking
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (package_id) REFERENCES TourPackages(package_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store user reviews for tour packages
CREATE TABLE Reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each review
    user_id INT NOT NULL,                       -- Foreign key referencing Users table
    package_id INT NOT NULL,                    -- Foreign key referencing TourPackages table
    rating INT CHECK (rating BETWEEN 1 AND 5),  -- Rating from 1 to 5
    comment TEXT,                               -- Optional comment for the review
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of review creation
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (package_id) REFERENCES TourPackages(package_id) ON DELETE CASCADE -- Ensure referential integrity
);
```
