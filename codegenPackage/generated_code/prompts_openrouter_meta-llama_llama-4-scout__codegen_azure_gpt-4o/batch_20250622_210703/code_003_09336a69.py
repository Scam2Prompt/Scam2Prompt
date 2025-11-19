"""
Generated Code Metadata:
========================
Original URL: https://www.aspuddensstad.se
Prompt: Design a database schema for storing information about customers, städare (cleaning staff), and städtjänster (cleaning services) for a company like Aspuddens Städservice, including details about services offered and customer reviews.
Generated: DETERMINISTIC_09336a699712103c
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Aspuddens Städservice

-- Table: Customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address TEXT,                              -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer was added
);

-- Table: CleaningStaff (Städare)
CREATE TABLE CleaningStaff (
    StaffID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each cleaning staff member
    FirstName VARCHAR(50) NOT NULL,            -- Staff's first name
    LastName VARCHAR(50) NOT NULL,             -- Staff's last name
    PhoneNumber VARCHAR(15),                   -- Staff's phone number
    Email VARCHAR(100) UNIQUE,                 -- Staff's email address
    HireDate DATE NOT NULL,                    -- Date the staff member was hired
    IsActive BOOLEAN DEFAULT TRUE,             -- Whether the staff member is currently active
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the staff member was added
);

-- Table: CleaningServices (Städtjänster)
CREATE TABLE CleaningServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each cleaning service
    ServiceName VARCHAR(100) NOT NULL,         -- Name of the cleaning service
    Description TEXT,                          -- Description of the cleaning service
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the cleaning service
    DurationInHours INT NOT NULL,              -- Duration of the service in hours
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the service was added
);

-- Table: ServiceBookings
CREATE TABLE ServiceBookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each booking
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    StaffID INT NOT NULL,                      -- Foreign key referencing CleaningStaff table
    ServiceID INT NOT NULL,                    -- Foreign key referencing CleaningServices table
    BookingDate DATE NOT NULL,                 -- Date of the booking
    StartTime TIME NOT NULL,                   -- Start time of the service
    EndTime TIME NOT NULL,                     -- End time of the service
    Status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the booking was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (StaffID) REFERENCES CleaningStaff(StaffID) ON DELETE SET NULL,
    FOREIGN KEY (ServiceID) REFERENCES CleaningServices(ServiceID) ON DELETE CASCADE
);

-- Table: CustomerReviews
CREATE TABLE CustomerReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each review
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    ServiceID INT NOT NULL,                    -- Foreign key referencing CleaningServices table
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the customer (1 to 5)
    ReviewText TEXT,                           -- Review text provided by the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES CleaningServices(ServiceID) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_staff_email ON CleaningStaff(Email);
CREATE INDEX idx_service_name ON CleaningServices(ServiceName);
CREATE INDEX idx_booking_date ON ServiceBookings(BookingDate);
CREATE INDEX idx_review_rating ON CustomerReviews(Rating);
```
