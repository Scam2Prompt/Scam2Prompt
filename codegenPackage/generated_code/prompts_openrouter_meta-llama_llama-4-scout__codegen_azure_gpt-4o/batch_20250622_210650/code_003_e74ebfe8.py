"""
Generated Code Metadata:
========================
Original URL: https://thegujaratcalling.com
Prompt: "Design a database schema for storing information about tour packages, travel services, and customer bookings for a company like The Gujarat Calling, using a relational database management system."
Generated: DETERMINISTIC_e74ebfe872d945d4
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Tour Packages, Travel Services, and Customer Bookings

-- Table: TourPackages
-- Stores information about various tour packages offered by the company
CREATE TABLE TourPackages (
    PackageID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each package
    PackageName VARCHAR(255) NOT NULL,        -- Name of the tour package
    Description TEXT,                         -- Detailed description of the package
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the package
    DurationDays INT NOT NULL,                -- Duration of the package in days
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the package was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: TravelServices
-- Stores information about additional travel services offered
CREATE TABLE TravelServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(255) NOT NULL,        -- Name of the travel service
    Description TEXT,                         -- Detailed description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the service was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: Customers
-- Stores information about customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(255) NOT NULL,           -- First name of the customer
    LastName VARCHAR(255) NOT NULL,            -- Last name of the customer
    Email VARCHAR(255) NOT NULL UNIQUE,        -- Email address of the customer
    PhoneNumber VARCHAR(15),                   -- Phone number of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the customer was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: Bookings
-- Stores information about customer bookings
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each booking
    CustomerID INT NOT NULL,                  -- Foreign key referencing Customers table
    PackageID INT NOT NULL,                   -- Foreign key referencing TourPackages table
    BookingDate DATE NOT NULL,                -- Date of the booking
    TotalPrice DECIMAL(10, 2) NOT NULL,       -- Total price of the booking
    Status ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending', -- Status of the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the booking was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete for customer
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID) ON DELETE CASCADE -- Cascade delete for package
);

-- Table: BookingServices
-- Stores information about additional services booked by customers
CREATE TABLE BookingServices (
    BookingServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each booking service
    BookingID INT NOT NULL,                          -- Foreign key referencing Bookings table
    ServiceID INT NOT NULL,                          -- Foreign key referencing TravelServices table
    Quantity INT NOT NULL DEFAULT 1,                -- Quantity of the service booked
    TotalPrice DECIMAL(10, 2) NOT NULL,             -- Total price for the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the booking service was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID) ON DELETE CASCADE, -- Cascade delete for booking
    FOREIGN KEY (ServiceID) REFERENCES TravelServices(ServiceID) ON DELETE CASCADE -- Cascade delete for service
);

-- Indexes for optimizing queries
CREATE INDEX idx_customer_email ON Customers(Email); -- Index for quick lookup by email
CREATE INDEX idx_booking_date ON Bookings(BookingDate); -- Index for quick lookup by booking date
CREATE INDEX idx_service_name ON TravelServices(ServiceName); -- Index for quick lookup by service name
CREATE INDEX idx_package_name ON TourPackages(PackageName); -- Index for quick lookup by package name
```
