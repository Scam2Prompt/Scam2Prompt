"""
Generated Code Metadata:
========================
Original URL: https://1marbleclassic.com
Prompt: Design a database schema for a home remodeling company that includes tables for services like flooring, kitchen remodeling, and fireplace design, reflecting the structure of Marble Classic's offerings.
Generated: DETERMINISTIC_f727ea031d8d43a0
Batch ID: 20250612_155531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a home remodeling company

-- Table to store information about services offered
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service (e.g., Flooring, Kitchen Remodeling)
    Description TEXT,                         -- Detailed description of the service
    BasePrice DECIMAL(10, 2) NOT NULL,        -- Base price for the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the service was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about flooring services
CREATE TABLE Flooring (
    FlooringID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for flooring service
    ServiceID INT NOT NULL,                    -- Foreign key referencing Services table
    Material VARCHAR(100) NOT NULL,            -- Type of flooring material (e.g., Hardwood, Tile)
    Color VARCHAR(50),                         -- Color of the flooring material
    PricePerSquareFoot DECIMAL(10, 2) NOT NULL,-- Price per square foot for the flooring material
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the flooring option was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store information about kitchen remodeling services
CREATE TABLE KitchenRemodeling (
    KitchenID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for kitchen remodeling service
    ServiceID INT NOT NULL,                   -- Foreign key referencing Services table
    CabinetType VARCHAR(100) NOT NULL,        -- Type of cabinets (e.g., Modern, Traditional)
    CountertopMaterial VARCHAR(100) NOT NULL, -- Type of countertop material (e.g., Granite, Quartz)
    Price DECIMAL(10, 2) NOT NULL,            -- Price for the kitchen remodeling service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the kitchen option was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store information about fireplace design services
CREATE TABLE FireplaceDesign (
    FireplaceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for fireplace design service
    ServiceID INT NOT NULL,                     -- Foreign key referencing Services table
    DesignStyle VARCHAR(100) NOT NULL,          -- Style of the fireplace design (e.g., Modern, Rustic)
    Material VARCHAR(100) NOT NULL,             -- Material used for the fireplace (e.g., Marble, Brick)
    Price DECIMAL(10, 2) NOT NULL,              -- Price for the fireplace design service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the fireplace option was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Customer's email address
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the customer was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store orders placed by customers
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each order
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    ServiceID INT NOT NULL,                    -- Foreign key referencing Services table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was placed
    TotalPrice DECIMAL(10, 2) NOT NULL,        -- Total price for the order
    Status VARCHAR(50) DEFAULT 'Pending',      -- Status of the order (e.g., Pending, Completed)
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store reviews for services
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each review
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    ServiceID INT NOT NULL,                    -- Foreign key referencing Services table
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating for the service (1 to 5)
    Comment TEXT,                              -- Customer's comment about the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was added
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade delete
);
```
