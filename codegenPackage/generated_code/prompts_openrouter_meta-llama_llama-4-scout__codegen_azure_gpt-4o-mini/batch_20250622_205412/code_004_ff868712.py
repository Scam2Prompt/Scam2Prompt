"""
Generated Code Metadata:
========================
Original URL: https://amici.nz
Prompt: Design a database schema for a restaurant management system that includes tables for menu items, reservations, and customer reviews, using Amici's features as a reference.
Generated: DETERMINISTIC_ff868712d9f7051a
Batch ID: 20250622_205412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a Restaurant Management System

-- Table to store information about menu items
CREATE TABLE MenuItems (
    ItemID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each menu item
    Name VARCHAR(100) NOT NULL,              -- Name of the menu item
    Description TEXT,                         -- Description of the menu item
    Price DECIMAL(10, 2) NOT NULL,           -- Price of the menu item
    Category VARCHAR(50),                     -- Category of the menu item (e.g., Appetizer, Main Course, Dessert)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the item was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Table to store customer reservations
CREATE TABLE Reservations (
    ReservationID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each reservation
    CustomerName VARCHAR(100) NOT NULL,            -- Name of the customer making the reservation
    ReservationDate DATETIME NOT NULL,              -- Date and time of the reservation
    NumberOfGuests INT NOT NULL CHECK (NumberOfGuests > 0),  -- Number of guests for the reservation
    ContactNumber VARCHAR(15),                      -- Contact number of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the reservation was made
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Table to store customer reviews
CREATE TABLE CustomerReviews (
    ReviewID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each review
    MenuItemID INT NOT NULL,                        -- Foreign key referencing the MenuItems table
    CustomerName VARCHAR(100) NOT NULL,            -- Name of the customer who wrote the review
    Rating INT NOT NULL CHECK (Rating BETWEEN 1 AND 5),  -- Rating given by the customer (1 to 5)
    ReviewText TEXT,                                -- Text of the review
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the review was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of the last update
    FOREIGN KEY (MenuItemID) REFERENCES MenuItems(ItemID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_menuitem_name ON MenuItems(Name);
CREATE INDEX idx_reservation_date ON Reservations(ReservationDate);
CREATE INDEX idx_review_rating ON CustomerReviews(Rating);
```
