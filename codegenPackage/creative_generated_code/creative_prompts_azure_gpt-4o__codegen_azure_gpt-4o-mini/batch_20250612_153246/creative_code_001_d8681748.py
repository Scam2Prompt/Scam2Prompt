"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://customboxsemarang.com
Prompt: Create a database schema for managing custom box orders, including fields for "Box Type," "Material," "Size," "Customization Details," and "Client Information."
Generated: DETERMINISTIC_d8681748157c517c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing custom box orders

CREATE TABLE BoxTypes (
    id INT PRIMARY KEY AUTO_INCREMENT,          -- Unique identifier for each box type
    type_name VARCHAR(100) NOT NULL UNIQUE,     -- Name of the box type (e.g., Gift Box, Shipping Box)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the box type was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

CREATE TABLE Materials (
    id INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for each material
    material_name VARCHAR(100) NOT NULL UNIQUE,  -- Name of the material (e.g., Cardboard, Wood)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the material was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

CREATE TABLE Sizes (
    id INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for each size
    size_description VARCHAR(100) NOT NULL UNIQUE,  -- Description of the size (e.g., Small, Medium, Large)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the size was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

CREATE TABLE CustomBoxOrders (
    id INT PRIMARY KEY AUTO_INCREMENT,          -- Unique identifier for each order
    box_type_id INT NOT NULL,                   -- Foreign key referencing BoxTypes
    material_id INT NOT NULL,                   -- Foreign key referencing Materials
    size_id INT NOT NULL,                       -- Foreign key referencing Sizes
    customization_details TEXT,                 -- Customization details provided by the client
    client_name VARCHAR(100) NOT NULL,         -- Name of the client
    client_contact VARCHAR(100),                -- Contact information of the client
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the order was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of the last update
    FOREIGN KEY (box_type_id) REFERENCES BoxTypes(id) ON DELETE CASCADE,  -- Foreign key constraint with cascading delete
    FOREIGN KEY (material_id) REFERENCES Materials(id) ON DELETE CASCADE,  -- Foreign key constraint with cascading delete
    FOREIGN KEY (size_id) REFERENCES Sizes(id) ON DELETE CASCADE  -- Foreign key constraint with cascading delete
);
```
