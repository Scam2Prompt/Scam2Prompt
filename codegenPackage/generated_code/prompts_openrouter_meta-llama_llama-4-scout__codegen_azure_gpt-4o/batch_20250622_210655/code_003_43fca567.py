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
-- Database schema for storing user information and tour packages for an Umroh tour operator

-- Create a table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FullName VARCHAR(100) NOT NULL,        -- Full name of the user
    Email VARCHAR(100) UNIQUE NOT NULL,    -- Email address (must be unique)
    PhoneNumber VARCHAR(15) NOT NULL,      -- Contact phone number
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    Address TEXT,                          -- Address of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store tour package information
CREATE TABLE TourPackages (
    PackageID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each package
    PackageName VARCHAR(100) NOT NULL,        -- Name of the tour package
    Description TEXT NOT NULL,                -- Detailed description of the package
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the package
    DurationDays INT NOT NULL,                -- Duration of the package in days
    DepartureDate DATE NOT NULL,              -- Departure date for the package
    ReturnDate DATE NOT NULL,                 -- Return date for the package
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the package was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store bookings made by users
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each booking
    UserID INT NOT NULL,                      -- Foreign key referencing Users table
    PackageID INT NOT NULL,                   -- Foreign key referencing TourPackages table
    BookingDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the booking was made
    Status ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending', -- Status of the booking
    TotalPrice DECIMAL(10, 2) NOT NULL,       -- Total price for the booking
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is deleted
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID) ON DELETE CASCADE -- Cascade delete if package is deleted
);

-- Create a table to store payment information
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each payment
    BookingID INT NOT NULL,                   -- Foreign key referencing Bookings table
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the payment was made
    Amount DECIMAL(10, 2) NOT NULL,           -- Amount paid
    PaymentMethod ENUM('Credit Card', 'Bank Transfer', 'Cash') NOT NULL, -- Payment method
    Status ENUM('Pending', 'Completed', 'Failed') DEFAULT 'Pending', -- Status of the payment
    FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID) ON DELETE CASCADE -- Cascade delete if booking is deleted
);

-- Create indexes for faster queries
CREATE INDEX idx_users_email ON Users(Email); -- Index for email lookup
CREATE INDEX idx_tourpackages_departuredate ON TourPackages(DepartureDate); -- Index for departure date lookup
CREATE INDEX idx_bookings_userid ON Bookings(UserID); -- Index for user bookings lookup
CREATE INDEX idx_payments_bookingid ON Payments(BookingID); -- Index for payment lookup by booking
```
