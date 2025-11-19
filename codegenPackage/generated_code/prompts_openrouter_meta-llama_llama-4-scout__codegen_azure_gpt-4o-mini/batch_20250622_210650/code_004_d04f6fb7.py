"""
Generated Code Metadata:
========================
Original URL: https://nellyservis.sk
Prompt: "Design a database schema for storing information about window and door products, including their characteristics and installation services, inspired by the content on nellyservis.sk."
Generated: DETERMINISTIC_d04f6fb7d62ed642
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about window and door products, 
-- including their characteristics and installation services.

CREATE TABLE ProductCategories (
    id SERIAL PRIMARY KEY, -- Unique identifier for each product category
    name VARCHAR(100) NOT NULL, -- Name of the product category (e.g., Windows, Doors)
    description TEXT, -- Description of the product category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

CREATE TABLE Products (
    id SERIAL PRIMARY KEY, -- Unique identifier for each product
    category_id INT NOT NULL, -- Foreign key referencing ProductCategories
    name VARCHAR(100) NOT NULL, -- Name of the product
    description TEXT, -- Description of the product
    price DECIMAL(10, 2) NOT NULL, -- Price of the product
    dimensions VARCHAR(50), -- Dimensions of the product (e.g., width x height)
    material VARCHAR(50), -- Material of the product (e.g., wood, PVC)
    energy_efficiency_rating VARCHAR(10), -- Energy efficiency rating (e.g., A++, B)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (category_id) REFERENCES ProductCategories(id) ON DELETE CASCADE -- Ensures referential integrity
);

CREATE TABLE InstallationServices (
    id SERIAL PRIMARY KEY, -- Unique identifier for each installation service
    product_id INT NOT NULL, -- Foreign key referencing Products
    service_description TEXT, -- Description of the installation service
    service_price DECIMAL(10, 2) NOT NULL, -- Price of the installation service
    estimated_time VARCHAR(50), -- Estimated time for installation (e.g., hours, days)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (product_id) REFERENCES Products(id) ON DELETE CASCADE -- Ensures referential integrity
);

CREATE TABLE ProductImages (
    id SERIAL PRIMARY KEY, -- Unique identifier for each product image
    product_id INT NOT NULL, -- Foreign key referencing Products
    image_url VARCHAR(255) NOT NULL, -- URL of the product image
    alt_text VARCHAR(100), -- Alternative text for the image
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (product_id) REFERENCES Products(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_product_category ON Products(category_id);
CREATE INDEX idx_service_product ON InstallationServices(product_id);
CREATE INDEX idx_image_product ON ProductImages(product_id);
```
