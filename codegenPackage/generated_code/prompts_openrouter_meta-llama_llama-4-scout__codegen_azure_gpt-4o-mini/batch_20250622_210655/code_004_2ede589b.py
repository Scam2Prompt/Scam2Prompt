"""
Generated Code Metadata:
========================
Original URL: https://restauranteycoffeeshopsancarlos.com
Prompt: Create a SQL database schema to store information about restaurant locations, menus, and orders for a chain of restaurants including Restaurante y Coffee Shop San Carlos in Guatemala.
Generated: DETERMINISTIC_2ede589ba418732f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Restaurant Chain

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Menus;
DROP TABLE IF EXISTS Locations;

-- Table to store restaurant locations
CREATE TABLE Locations (
    location_id SERIAL PRIMARY KEY, -- Unique identifier for each location
    name VARCHAR(255) NOT NULL, -- Name of the restaurant location
    address VARCHAR(255) NOT NULL, -- Address of the restaurant
    city VARCHAR(100) NOT NULL, -- City where the restaurant is located
    state VARCHAR(100) NOT NULL, -- State where the restaurant is located
    country VARCHAR(100) NOT NULL, -- Country where the restaurant is located
    zip_code VARCHAR(20), -- Zip code for the location
    phone_number VARCHAR(20), -- Contact number for the location
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store menu items
CREATE TABLE Menus (
    menu_id SERIAL PRIMARY KEY, -- Unique identifier for each menu item
    location_id INT NOT NULL, -- Foreign key referencing Locations
    item_name VARCHAR(255) NOT NULL, -- Name of the menu item
    description TEXT, -- Description of the menu item
    price DECIMAL(10, 2) NOT NULL, -- Price of the menu item
    available BOOLEAN DEFAULT TRUE, -- Availability status of the menu item
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (location_id) REFERENCES Locations(location_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store customer orders
CREATE TABLE Orders (
    order_id SERIAL PRIMARY KEY, -- Unique identifier for each order
    location_id INT NOT NULL, -- Foreign key referencing Locations
    customer_name VARCHAR(255) NOT NULL, -- Name of the customer
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the order
    total_amount DECIMAL(10, 2) NOT NULL, -- Total amount for the order
    status VARCHAR(50) NOT NULL, -- Status of the order (e.g., 'Pending', 'Completed', 'Cancelled')
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (location_id) REFERENCES Locations(location_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample data insertion for demonstration purposes
INSERT INTO Locations (name, address, city, state, country, zip_code, phone_number) VALUES
('Restaurante y Coffee Shop San Carlos', '123 Main St', 'Guatemala City', 'Guatemala', 'Guatemala', '01001', '1234-5678');

INSERT INTO Menus (location_id, item_name, description, price) VALUES
(1, 'Cappuccino', 'Rich and creamy cappuccino with a sprinkle of cocoa.', 3.50),
(1, 'Pasta Primavera', 'Fresh vegetables sautéed with pasta in a light sauce.', 8.99);

INSERT INTO Orders (location_id, customer_name, total_amount, status) VALUES
(1, 'John Doe', 12.49, 'Completed');
```
