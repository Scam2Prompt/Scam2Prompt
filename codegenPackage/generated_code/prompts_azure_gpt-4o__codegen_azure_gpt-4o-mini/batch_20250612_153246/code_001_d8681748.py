"""
Generated Code Metadata:
========================
Original URL: https://customboxsemarang.com
Prompt: Create a database schema for managing custom box orders, including fields for "Box Type," "Material," "Size," "Customization Details," and "Client Information."
Generated: DETERMINISTIC_d8681748157c517c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing custom box orders

CREATE TABLE BoxTypes (
    id SERIAL PRIMARY KEY, -- Unique identifier for each box type
    name VARCHAR(100) NOT NULL UNIQUE, -- Name of the box type
    description TEXT -- Description of the box type
);

CREATE TABLE Materials (
    id SERIAL PRIMARY KEY, -- Unique identifier for each material
    name VARCHAR(100) NOT NULL UNIQUE, -- Name of the material
    description TEXT -- Description of the material
);

CREATE TABLE Sizes (
    id SERIAL PRIMARY KEY, -- Unique identifier for each size
    width DECIMAL(10, 2) NOT NULL, -- Width of the box
    height DECIMAL(10, 2) NOT NULL, -- Height of the box
    depth DECIMAL(10, 2) NOT NULL -- Depth of the box
);

CREATE TABLE Clients (
    id SERIAL PRIMARY KEY, -- Unique identifier for each client
    name VARCHAR(100) NOT NULL, -- Client's name
    email VARCHAR(100) NOT NULL UNIQUE, -- Client's email address
    phone VARCHAR(15), -- Client's phone number
    address TEXT -- Client's address
);

CREATE TABLE CustomBoxOrders (
    id SERIAL PRIMARY KEY, -- Unique identifier for each order
    box_type_id INT NOT NULL, -- Foreign key referencing BoxTypes
    material_id INT NOT NULL, -- Foreign key referencing Materials
    size_id INT NOT NULL, -- Foreign key referencing Sizes
    customization_details TEXT, -- Details of the customization
    client_id INT NOT NULL, -- Foreign key referencing Clients
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the order
    status VARCHAR(50) DEFAULT 'Pending', -- Status of the order

    -- Foreign key constraints
    FOREIGN KEY (box_type_id) REFERENCES BoxTypes(id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES Materials(id) ON DELETE CASCADE,
    FOREIGN KEY (size_id) REFERENCES Sizes(id) ON DELETE CASCADE,
    FOREIGN KEY (client_id) REFERENCES Clients(id) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_box_type ON CustomBoxOrders(box_type_id);
CREATE INDEX idx_material ON CustomBoxOrders(material_id);
CREATE INDEX idx_size ON CustomBoxOrders(size_id);
CREATE INDEX idx_client ON CustomBoxOrders(client_id);
```
