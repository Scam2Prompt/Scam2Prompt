"""
Generated Code Metadata:
========================
Original URL: https://multandesigns.com
Prompt: "Design a database schema for storing information about traditional Pakistani clothing items, including their fabric, embroidery type, and price."
Generated: DETERMINISTIC_e4322808944bf4d9
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about traditional Pakistani clothing items

CREATE TABLE Fabric (
    fabric_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each fabric
    fabric_name VARCHAR(100) NOT NULL,         -- Name of the fabric (e.g., Cotton, Silk)
    description TEXT,                           -- Description of the fabric
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for record updates
);

CREATE TABLE EmbroideryType (
    embroidery_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each embroidery type
    embroidery_name VARCHAR(100) NOT NULL,         -- Name of the embroidery type (e.g., Chikan, Zardozi)
    description TEXT,                               -- Description of the embroidery type
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for record updates
);

CREATE TABLE ClothingItem (
    item_id INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for each clothing item
    item_name VARCHAR(100) NOT NULL,                -- Name of the clothing item (e.g., Shalwar Kameez)
    fabric_id INT NOT NULL,                          -- Foreign key referencing Fabric
    embroidery_id INT NOT NULL,                      -- Foreign key referencing EmbroideryType
    price DECIMAL(10, 2) NOT NULL,                  -- Price of the clothing item
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for record updates
    FOREIGN KEY (fabric_id) REFERENCES Fabric(fabric_id) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (embroidery_id) REFERENCES EmbroideryType(embroidery_id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Sample data insertion (uncomment to use)
-- INSERT INTO Fabric (fabric_name, description) VALUES ('Cotton', 'Lightweight and breathable fabric');
-- INSERT INTO Fabric (fabric_name, description) VALUES ('Silk', 'Luxurious and smooth fabric');
-- INSERT INTO EmbroideryType (embroidery_name, description) VALUES ('Chikan', 'Traditional hand-embroidery from Lucknow');
-- INSERT INTO EmbroideryType (embroidery_name, description) VALUES ('Zardozi', 'Heavy embroidery with gold and silver threads');
-- INSERT INTO ClothingItem (item_name, fabric_id, embroidery_id, price) VALUES ('Shalwar Kameez', 1, 1, 1500.00);
-- INSERT INTO ClothingItem (item_name, fabric_id, embroidery_id, price) VALUES ('Lehenga', 2, 2, 5000.00);
```
