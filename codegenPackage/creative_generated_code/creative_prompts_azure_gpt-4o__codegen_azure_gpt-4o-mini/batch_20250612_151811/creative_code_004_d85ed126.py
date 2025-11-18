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
-- Database schema for a restaurant management system

-- Drop existing tables if they exist (for fresh setup/testing)
DROP TABLE IF EXISTS MenuItems;
DROP TABLE IF EXISTS Reservations;
DROP TABLE IF EXISTS TakeawayOrders;

-- Table for Menu Items
CREATE TABLE MenuItems (
    ItemID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for menu items
    ItemName VARCHAR(100) NOT NULL,             -- Name of the menu item
    Description TEXT,                            -- Description of the menu item
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the menu item
    Category VARCHAR(50) NOT NULL,              -- Category of the item (e.g., Appetizer, Main Course, Dessert, Beverage)
    IsAvailable BOOLEAN DEFAULT TRUE,            -- Availability status of the menu item
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the item was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for last update
);

-- Table for Reservations
CREATE TABLE Reservations (
    ReservationID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for reservations
    CustomerName VARCHAR(100) NOT NULL,           -- Name of the customer making the reservation
    ReservationDate DATETIME NOT NULL,             -- Date and time of the reservation
    PartySize INT NOT NULL,                        -- Number of guests
    ContactNumber VARCHAR(15),                     -- Contact number of the customer
    SpecialRequests TEXT,                          -- Any special requests from the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when reservation was made
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for last update
);

-- Table for Takeaway Orders
CREATE TABLE TakeawayOrders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for takeaway orders
    CustomerName VARCHAR(100) NOT NULL,           -- Name of the customer placing the order
    OrderDate DATETIME NOT NULL,                   -- Date and time when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,          -- Total amount of the order
    OrderStatus ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Current status of the order
    ContactNumber VARCHAR(15),                     -- Contact number of the customer
    DeliveryAddress VARCHAR(255) NOT NULL,        -- Address for order pickup
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when order was made
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for last update
);

-- Sample data insertion (for demonstration purposes)
-- Uncomment to insert sample data after creating the tables

-- INSERT INTO MenuItems (ItemName, Description, Price, Category) VALUES
-- ('Spaghetti Bolognese', 'Traditional spaghetti with a rich meat sauce', 12.50, 'Main Course'),
-- ('Caesar Salad', 'Crisp romaine lettuce with Caesar dressing', 8.00, 'Appetizer'),
-- ('Tiramisu', 'Classic Italian coffee-flavored dessert', 6.50, 'Dessert');

-- INSERT INTO Reservations (CustomerName, ReservationDate, PartySize, ContactNumber, SpecialRequests) VALUES
-- ('John Doe', '2023-10-15 19:00:00', 4, '1234567890', 'Window seat preferred');

-- INSERT INTO TakeawayOrders (CustomerName, OrderDate, TotalAmount, OrderStatus, ContactNumber, DeliveryAddress) VALUES
-- ('Jane Smith', '2023-10-14 20:00:00', 25.00, 'Pending', '0987654321', '123 Main St, Anytown, USA');
```
