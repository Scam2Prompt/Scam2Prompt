"""
Generated Code Metadata:
========================
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Create a database schema for storing information about tools and equipment, including fields for "material," "mechanism," "implemento," and "aparelho," inspired by the Geyciane Ferramentas content.
Generated: DETERMINISTIC_78a793b0088e017c
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tools and equipment management system
CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE materials (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE mechanisms (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE tools (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category_id INT,
    material_id INT,
    mechanism_id INT,
    description TEXT,
    specifications JSON,
    quantity INT DEFAULT 0,
    price DECIMAL(10, 2),
    barcode VARCHAR(50) UNIQUE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(id),
    FOREIGN KEY (material_id) REFERENCES materials(id),
    FOREIGN KEY (mechanism_id) REFERENCES mechanisms(id)
);

CREATE TABLE equipment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category_id INT,
    material_id INT,
    description TEXT,
    specifications JSON,
    serial_number VARCHAR(50) UNIQUE,
    purchase_date DATE,
    warranty_expiry DATE,
    maintenance_interval INT COMMENT 'Interval in days',
    last_maintenance_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(id),
    FOREIGN KEY (material_id) REFERENCES materials(id)
);

CREATE TABLE tool_equipment_relations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tool_id INT,
    equipment_id INT,
    relation_type ENUM('COMPATIBLE', 'REQUIRED', 'OPTIONAL') NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (tool_id) REFERENCES tools(id) ON DELETE CASCADE,
    FOREIGN KEY (equipment_id) REFERENCES equipment(id) ON DELETE CASCADE,
    UNIQUE KEY unique_relation (tool_id, equipment_id, relation_type)
);

CREATE TABLE suppliers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    address TEXT,
    website VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE tool_suppliers (
    tool_id INT,
    supplier_id INT,
    supplier_part_number VARCHAR(50),
    PRIMARY KEY (tool_id, supplier_id),
    FOREIGN KEY (tool_id) REFERENCES tools(id) ON DELETE CASCADE,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(id) ON DELETE CASCADE
);

CREATE TABLE equipment_suppliers (
    equipment_id INT,
    supplier_id INT,
    supplier_part_number VARCHAR(50),
    PRIMARY KEY (equipment_id, supplier_id),
    FOREIGN KEY (equipment_id) REFERENCES equipment(id) ON DELETE CASCADE,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(id) ON DELETE CASCADE
);

-- Indexes for better performance
CREATE INDEX idx_tools_category ON tools(category_id);
CREATE INDEX idx_tools_material ON tools(material_id);
CREATE INDEX idx_tools_mechanism ON tools(mechanism_id);
CREATE INDEX idx_equipment_category ON equipment(category_id);
CREATE INDEX idx_equipment_material ON equipment(material_id);
CREATE INDEX idx_tool_equipment_tool ON tool_equipment_relations(tool_id);
CREATE INDEX idx_tool_equipment_equipment ON tool_equipment_relations(equipment_id);
```
