"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balancer-app.pages.dev
Prompt: Write a database schema for a restaurant management system that includes tables for menu items, reservations, and takeaway orders, inspired by the structure of RAVIOLI HOUSE's offerings.
Generated: DETERMINISTIC_d85ed1265e965aa4
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Restaurant Management System: Inspired by RAVIOLI HOUSE

-- Table: MenuItems
-- Stores details of all menu items offered by the restaurant
CREATE TABLE MenuItems (
    MenuItemID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each menu item
    Name VARCHAR(255) NOT NULL,                -- Name of the menu item
    Description TEXT,                          -- Description of the menu item
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the menu item
    Category VARCHAR(100),                     -- Category (e.g., Appetizer, Main Course, Dessert)
    IsAvailable BOOLEAN DEFAULT TRUE,          -- Availability status (true: available, false: unavailable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record update
);

-- Table: Reservations
-- Stores details of reservations made by customers
CREATE TABLE Reservations (
    ReservationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each reservation
    CustomerName VARCHAR(255) NOT NULL,          -- Name of the customer making the reservation
    CustomerPhone VARCHAR(15) NOT NULL,          -- Contact number of the customer
    ReservationDate DATE NOT NULL,               -- Date of the reservation
    ReservationTime TIME NOT NULL,               -- Time of the reservation
    NumberOfGuests INT NOT NULL,                 -- Number of guests for the reservation
    SpecialRequests TEXT,                        -- Special requests made by the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record update
);

-- Table: TakeawayOrders
-- Stores details of takeaway orders placed by customers
CREATE TABLE TakeawayOrders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each takeaway order
    CustomerName VARCHAR(255) NOT NULL,          -- Name of the customer placing the order
    CustomerPhone VARCHAR(15) NOT NULL,          -- Contact number of the customer
    OrderDate DATE NOT NULL,                     -- Date the order was placed
    OrderTime TIME NOT NULL,                     -- Time the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,         -- Total amount for the order
    Status ENUM('Pending', 'Preparing', 'Ready', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Order status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record update
);

-- Table: TakeawayOrderDetails
-- Stores the details of menu items included in each takeaway order
CREATE TABLE TakeawayOrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key linking to TakeawayOrders table
    MenuItemID INT NOT NULL,                      -- Foreign key linking to MenuItems table
    Quantity INT NOT NULL,                        -- Quantity of the menu item
    Subtotal DECIMAL(10, 2) NOT NULL,             -- Calculated subtotal for the item (Price * Quantity)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record update
    FOREIGN KEY (OrderID) REFERENCES TakeawayOrders(OrderID) ON DELETE CASCADE, -- Cascade delete if takeaway order is deleted
    FOREIGN KEY (MenuItemID) REFERENCES MenuItems(MenuItemID) ON DELETE CASCADE -- Cascade delete if menu item is deleted
);

-- Indexing for performance optimization
CREATE INDEX idx_menuitems_category ON MenuItems (Category);
CREATE INDEX idx_reservations_date_time ON Reservations (ReservationDate, ReservationTime);
CREATE INDEX idx_takeawayorders_status ON TakeawayOrders (Status);
```

This schema is designed to be scalable and robust, ensuring proper normalization and indexing for efficient data querying and maintenance.
