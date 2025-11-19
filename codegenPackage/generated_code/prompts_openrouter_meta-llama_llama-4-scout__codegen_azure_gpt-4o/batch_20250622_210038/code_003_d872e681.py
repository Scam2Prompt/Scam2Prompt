"""
Generated Code Metadata:
========================
Original URL: https://www.dexodoor.com
Prompt: "Design a database schema for storing client testimonials, project details, and product information for a company specializing in UPVC window and door systems installations."
Generated: DETERMINISTIC_d872e681365a04f7
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing client testimonials, project details, and product information
-- for a company specializing in UPVC window and door systems installations.

-- Table to store client testimonials
CREATE TABLE ClientTestimonials (
    TestimonialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each testimonial
    ClientName VARCHAR(255) NOT NULL,             -- Name of the client providing the testimonial
    ClientEmail VARCHAR(255),                     -- Email of the client (optional)
    TestimonialText TEXT NOT NULL,                -- The testimonial text provided by the client
    Rating INT CHECK (Rating BETWEEN 1 AND 5),    -- Rating provided by the client (1 to 5)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the testimonial was created
);

-- Table to store project details
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL,            -- Name of the project
    ClientName VARCHAR(255) NOT NULL,             -- Name of the client for the project
    ProjectDescription TEXT,                      -- Detailed description of the project
    StartDate DATE NOT NULL,                      -- Start date of the project
    EndDate DATE,                                 -- End date of the project (optional)
    Status ENUM('Pending', 'In Progress', 'Completed') NOT NULL, -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the project was created
);

-- Table to store product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,            -- Name of the product
    ProductDescription TEXT,                      -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product
    StockQuantity INT NOT NULL,                   -- Quantity of the product in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the product was added
);

-- Table to store the relationship between projects and products
CREATE TABLE ProjectProducts (
    ProjectProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    ProjectID INT NOT NULL,                          -- Foreign key referencing Projects table
    ProductID INT NOT NULL,                          -- Foreign key referencing Products table
    Quantity INT NOT NULL,                           -- Quantity of the product used in the project
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table to store the relationship between testimonials and projects
CREATE TABLE ProjectTestimonials (
    ProjectTestimonialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    ProjectID INT NOT NULL,                              -- Foreign key referencing Projects table
    TestimonialID INT NOT NULL,                          -- Foreign key referencing ClientTestimonials table
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE,
    FOREIGN KEY (TestimonialID) REFERENCES ClientTestimonials(TestimonialID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_ClientName ON ClientTestimonials(ClientName);
CREATE INDEX idx_ProjectName ON Projects(ProjectName);
CREATE INDEX idx_ProductName ON Products(ProductName);
```
