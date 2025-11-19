"""
Generated Code Metadata:
========================
Original URL: https://anywhere-adventure.com
Prompt: "Create a sample database schema to store information about travel destinations, tour packages, and customer reviews for a company like Anywhere Adventures."
Generated: DETERMINISTIC_93d56a9082e97077
Batch ID: 20250622_212643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Sample database schema for Anywhere Adventures

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS CustomerReviews;
DROP TABLE IF EXISTS TourPackages;
DROP TABLE IF EXISTS TravelDestinations;

-- Table to store information about travel destinations
CREATE TABLE TravelDestinations (
    DestinationID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each destination
    Name VARCHAR(255) NOT NULL,                   -- Name of the travel destination
    Description TEXT,                              -- Description of the destination
    Country VARCHAR(100) NOT NULL,                -- Country where the destination is located
    Region VARCHAR(100),                           -- Region within the country
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Table to store information about tour packages
CREATE TABLE TourPackages (
    PackageID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each tour package
    DestinationID INT NOT NULL,                    -- Foreign key referencing TravelDestinations
    PackageName VARCHAR(255) NOT NULL,            -- Name of the tour package
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the tour package
    Duration INT NOT NULL,                         -- Duration of the tour in days
    Itinerary TEXT,                               -- Detailed itinerary for the tour package
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    FOREIGN KEY (DestinationID) REFERENCES TravelDestinations(DestinationID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store customer reviews for tour packages
CREATE TABLE CustomerReviews (
    ReviewID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each review
    PackageID INT NOT NULL,                        -- Foreign key referencing TourPackages
    CustomerName VARCHAR(255) NOT NULL,           -- Name of the customer who wrote the review
    Rating INT CHECK (Rating BETWEEN 1 AND 5),    -- Rating given by the customer (1 to 5)
    ReviewText TEXT,                               -- Text of the review
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample data insertion (optional)
INSERT INTO TravelDestinations (Name, Description, Country, Region) VALUES
('Grand Canyon', 'A steep-sided canyon carved by the Colorado River.', 'USA', 'Arizona'),
('Eiffel Tower', 'A wrought-iron lattice tower on the Champ de Mars in Paris.', 'France', 'Île-de-France');

INSERT INTO TourPackages (DestinationID, PackageName, Price, Duration, Itinerary) VALUES
(1, 'Grand Canyon Adventure', 299.99, 3, 'Explore the canyon, hiking and rafting.'),
(2, 'Paris City Tour', 499.99, 5, 'Visit the Eiffel Tower, Louvre Museum, and more.');

INSERT INTO CustomerReviews (PackageID, CustomerName, Rating, ReviewText) VALUES
(1, 'John Doe', 5, 'An unforgettable experience!'),
(2, 'Jane Smith', 4, 'Loved the tour, but it was a bit rushed.');
```
