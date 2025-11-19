"""
Generated Code Metadata:
========================
Original URL: https://bienbonvoyage.com
Prompt: Design a basic database schema for a travel agency specializing in luxury adventures.
Generated: DETERMINISTIC_e2702cc6f564ff37
Batch ID: 20250622_212433
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a travel agency specializing in luxury adventures

-- Table: Users
-- Stores information about customers and staff
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FirstName VARCHAR(50) NOT NULL,        -- First name of the user
    LastName VARCHAR(50) NOT NULL,         -- Last name of the user
    Email VARCHAR(100) UNIQUE NOT NULL,    -- Email address of the user
    PhoneNumber VARCHAR(15),               -- Contact number of the user
    Role ENUM('Customer', 'Staff') NOT NULL, -- Role of the user (Customer or Staff)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of user creation
);

-- Table: Destinations
-- Stores information about travel destinations
CREATE TABLE Destinations (
    DestinationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each destination
    Name VARCHAR(100) NOT NULL,                   -- Name of the destination
    Country VARCHAR(50) NOT NULL,                 -- Country where the destination is located
    Description TEXT,                             -- Description of the destination
    PricePerPerson DECIMAL(10, 2) NOT NULL,       -- Price per person for the destination
    IsActive BOOLEAN DEFAULT TRUE,                -- Indicates if the destination is currently available
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of destination creation
);

-- Table: Bookings
-- Stores information about customer bookings
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each booking
    UserID INT NOT NULL,                      -- Reference to the user who made the booking
    DestinationID INT NOT NULL,               -- Reference to the booked destination
    NumberOfPeople INT NOT NULL,              -- Number of people included in the booking
    TotalPrice DECIMAL(10, 2) NOT NULL,       -- Total price for the booking
    BookingDate DATE NOT NULL,                -- Date of the booking
    Status ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending', -- Status of the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of booking creation
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (DestinationID) REFERENCES Destinations(DestinationID) ON DELETE CASCADE -- Foreign key constraint
);

-- Table: Reviews
-- Stores customer reviews for destinations
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each review
    UserID INT NOT NULL,                     -- Reference to the user who wrote the review
    DestinationID INT NOT NULL,              -- Reference to the reviewed destination
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the user (1 to 5)
    Comment TEXT,                            -- Review comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of review creation
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (DestinationID) REFERENCES Destinations(DestinationID) ON DELETE CASCADE -- Foreign key constraint
);

-- Table: Payments
-- Stores payment information for bookings
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each payment
    BookingID INT NOT NULL,                   -- Reference to the associated booking
    Amount DECIMAL(10, 2) NOT NULL,           -- Payment amount
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of payment
    PaymentMethod ENUM('Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer') NOT NULL, -- Payment method
    Status ENUM('Successful', 'Failed', 'Pending') DEFAULT 'Pending', -- Payment status
    FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID) ON DELETE CASCADE -- Foreign key constraint
);

-- Indexes for performance optimization
CREATE INDEX idx_user_email ON Users(Email); -- Index for quick lookup of users by email
CREATE INDEX idx_destination_name ON Destinations(Name); -- Index for quick lookup of destinations by name
CREATE INDEX idx_booking_status ON Bookings(Status); -- Index for quick lookup of bookings by status
CREATE INDEX idx_payment_status ON Payments(Status); -- Index for quick lookup of payments by status
```
