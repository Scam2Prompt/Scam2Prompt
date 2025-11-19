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
-- Database schema for a restaurant management system

-- Table: MenuItems
-- Stores information about the menu items offered by the restaurant
CREATE TABLE MenuItems (
    MenuItemID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each menu item
    Name VARCHAR(255) NOT NULL,                -- Name of the menu item
    Description TEXT,                          -- Description of the menu item
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the menu item
    Category VARCHAR(100),                     -- Category (e.g., Appetizer, Main Course, Dessert)
    IsAvailable BOOLEAN DEFAULT TRUE           -- Availability status of the menu item
);

-- Table: Reservations
-- Stores information about customer reservations
CREATE TABLE Reservations (
    ReservationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each reservation
    CustomerName VARCHAR(255) NOT NULL,           -- Name of the customer making the reservation
    CustomerPhone VARCHAR(15) NOT NULL,           -- Phone number of the customer
    ReservationDate DATE NOT NULL,                -- Date of the reservation
    ReservationTime TIME NOT NULL,                -- Time of the reservation
    NumberOfGuests INT NOT NULL,                  -- Number of guests for the reservation
    SpecialRequests TEXT,                         -- Any special requests from the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the reservation was created
);

-- Table: CustomerReviews
-- Stores customer reviews for the restaurant
CREATE TABLE CustomerReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each review
    CustomerName VARCHAR(255) NOT NULL,      -- Name of the customer leaving the review
    Rating INT NOT NULL CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the customer (1 to 5)
    ReviewText TEXT,                         -- Text of the review
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the review was created
);

-- Foreign Key Relationships (if applicable)
-- Note: In this schema, there are no direct relationships between tables, but they can be added as needed.
-- For example, linking reservations to menu items or reviews to reservations/customers.

-- Indexes for performance optimization
CREATE INDEX idx_MenuItems_Category ON MenuItems (Category); -- Index for faster category-based queries
CREATE INDEX idx_Reservations_DateTime ON Reservations (ReservationDate, ReservationTime); -- Index for faster reservation lookups
CREATE INDEX idx_CustomerReviews_Rating ON CustomerReviews (Rating); -- Index for faster rating-based queries
```
