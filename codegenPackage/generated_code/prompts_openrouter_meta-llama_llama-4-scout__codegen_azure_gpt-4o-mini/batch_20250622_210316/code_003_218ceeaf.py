"""
Generated Code Metadata:
========================
Original URL: https://mollinari.com.pl
Prompt: Design a database schema for storing information about a restaurant like Mollinari, including tables for menu items, reservations, and customer reviews.
Generated: DETERMINISTIC_218ceeafc78a901d
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a restaurant management system

-- Table to store information about menu items
CREATE TABLE MenuItems (
    ItemID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each menu item
    Name VARCHAR(100) NOT NULL,              -- Name of the menu item
    Description TEXT,                         -- Description of the menu item
    Price DECIMAL(10, 2) NOT NULL,           -- Price of the menu item
    Category VARCHAR(50),                     -- Category of the menu item (e.g., Appetizer, Main Course, Dessert)
    IsAvailable BOOLEAN DEFAULT TRUE          -- Availability status of the menu item
);

-- Table to store customer reservations
CREATE TABLE Reservations (
    ReservationID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each reservation
    CustomerName VARCHAR(100) NOT NULL,            -- Name of the customer making the reservation
    ReservationDate DATETIME NOT NULL,              -- Date and time of the reservation
    NumberOfGuests INT NOT NULL,                    -- Number of guests for the reservation
    ContactNumber VARCHAR(15),                      -- Contact number of the customer
    SpecialRequests TEXT,                           -- Any special requests from the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Timestamp of when the reservation was created
);

-- Table to store customer reviews
CREATE TABLE CustomerReviews (
    ReviewID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each review
    MenuItemID INT NOT NULL,                        -- Foreign key referencing the MenuItems table
    CustomerName VARCHAR(100) NOT NULL,             -- Name of the customer who wrote the review
    Rating INT CHECK (Rating BETWEEN 1 AND 5),      -- Rating given by the customer (1 to 5)
    ReviewText TEXT,                                -- Text of the review
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the review was created
    FOREIGN KEY (MenuItemID) REFERENCES MenuItems(ItemID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_menuitem_name ON MenuItems(Name);
CREATE INDEX idx_reservation_date ON Reservations(ReservationDate);
CREATE INDEX idx_review_rating ON CustomerReviews(Rating);
```
