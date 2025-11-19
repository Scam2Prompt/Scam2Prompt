"""
Generated Code Metadata:
========================
Original URL: https://www.fravitur.com
Prompt: Create a SQL database schema to store information about travel destinations, packages, and promotions, using Fravitur's catalog as a guide for the types of data that need to be stored.
Generated: DETERMINISTIC_72fe7f30190ada85
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Travel Destinations, Packages, and Promotions

-- Create a table to store information about travel destinations
CREATE TABLE Destinations (
    DestinationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each destination
    Name VARCHAR(255) NOT NULL,                   -- Name of the destination
    Country VARCHAR(100) NOT NULL,                -- Country where the destination is located
    Region VARCHAR(100),                          -- Region within the country (optional)
    Description TEXT,                             -- Detailed description of the destination
    PopularityRating DECIMAL(3, 2),               -- Rating of the destination's popularity (e.g., 4.75)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the record was created
);

-- Create a table to store information about travel packages
CREATE TABLE Packages (
    PackageID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each package
    DestinationID INT NOT NULL,                   -- Foreign key linking to Destinations table
    Name VARCHAR(255) NOT NULL,                   -- Name of the travel package
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the package
    DurationDays INT NOT NULL,                    -- Duration of the package in days
    IncludedFeatures TEXT,                        -- Features included in the package (e.g., meals, tours)
    AvailabilityStart DATE NOT NULL,              -- Start date for package availability
    AvailabilityEnd DATE NOT NULL,                -- End date for package availability
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    FOREIGN KEY (DestinationID) REFERENCES Destinations(DestinationID) ON DELETE CASCADE
);

-- Create a table to store information about promotions
CREATE TABLE Promotions (
    PromotionID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each promotion
    PackageID INT NOT NULL,                       -- Foreign key linking to Packages table
    DiscountPercentage DECIMAL(5, 2) NOT NULL,    -- Discount percentage (e.g., 15.00 for 15%)
    PromotionStart DATE NOT NULL,                 -- Start date for the promotion
    PromotionEnd DATE NOT NULL,                   -- End date for the promotion
    Description TEXT,                             -- Description of the promotion
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    FOREIGN KEY (PackageID) REFERENCES Packages(PackageID) ON DELETE CASCADE
);

-- Create a table to store customer reviews for destinations
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each review
    DestinationID INT NOT NULL,                   -- Foreign key linking to Destinations table
    CustomerName VARCHAR(255) NOT NULL,           -- Name of the customer who wrote the review
    Rating DECIMAL(3, 2) NOT NULL,                -- Rating given by the customer (e.g., 4.50)
    Comment TEXT,                                 -- Review comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (DestinationID) REFERENCES Destinations(DestinationID) ON DELETE CASCADE
);

-- Create a table to store booking information
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each booking
    PackageID INT NOT NULL,                       -- Foreign key linking to Packages table
    CustomerName VARCHAR(255) NOT NULL,           -- Name of the customer making the booking
    CustomerEmail VARCHAR(255) NOT NULL,          -- Email of the customer
    BookingDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the booking was made
    NumberOfPeople INT NOT NULL,                  -- Number of people included in the booking
    TotalPrice DECIMAL(10, 2) NOT NULL,           -- Total price for the booking
    FOREIGN KEY (PackageID) REFERENCES Packages(PackageID) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_destinations_country ON Destinations(Country);
CREATE INDEX idx_packages_price ON Packages(Price);
CREATE INDEX idx_promotions_discount ON Promotions(DiscountPercentage);
CREATE INDEX idx_reviews_rating ON Reviews(Rating);
CREATE INDEX idx_bookings_customer_email ON Bookings(CustomerEmail);
```
