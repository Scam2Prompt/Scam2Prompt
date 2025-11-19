"""
Generated Code Metadata:
========================
Original URL: https://lbicgroup.com
Prompt: "Design a database schema for storing information about transmission line accessories, such as fittings and clamps, manufactured by Swamiji Transmission Pvt. Ltd., and write a SQL query to retrieve product details."
Generated: DETERMINISTIC_649b3fb1c8ebbf1e
Batch ID: 20250622_212859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Swamiji Transmission Pvt. Ltd. transmission line accessories
CREATE TABLE manufacturers (
    manufacturer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    address TEXT,
    contact_number VARCHAR(20),
    email VARCHAR(100),
    website VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE product_categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    manufacturer_id INT NOT NULL,
    category_id INT NOT NULL,
    product_code VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    material VARCHAR(100),
    voltage_rating VARCHAR(50),
    current_rating VARCHAR(50),
    weight DECIMAL(10,2),
    unit_of_measure VARCHAR(20),
    price DECIMAL(10,2),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(manufacturer_id),
    FOREIGN KEY (category_id) REFERENCES product_categories(category_id)
);

CREATE TABLE product_images (
    image_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

CREATE TABLE product_specifications (
    specification_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    spec_name VARCHAR(100) NOT NULL,
    spec_value VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Insert sample manufacturer data
INSERT INTO manufacturers (name, address, contact_number, email, website)
VALUES ('Swamiji Transmission Pvt. Ltd.', '123 Industrial Area, Mumbai, India', '+91-22-12345678', 'info@swamijitransmission.com', 'www.swamijitransmission.com');

-- Insert sample product categories
INSERT INTO product_categories (name, description)
VALUES 
    ('Fittings', 'Various types of transmission line fittings'),
    ('Clamps', 'Different clamps used in transmission lines'),
    ('Hardware', 'Miscellaneous hardware accessories');

-- SQL query to retrieve product details
SELECT 
    p.product_id,
    p.product_code,
    p.name AS product_name,
    p.description,
    p.material,
    p.voltage_rating,
    p.current_rating,
    p.weight,
    p.unit_of_measure,
    p.price,
    pc.name AS category_name,
    m.name AS manufacturer_name,
    GROUP_CONCAT(DISTINCT CONCAT(ps.spec_name, ': ', ps.spec_value) SEPARATOR '; ') AS specifications,
    GROUP_CONCAT(DISTINCT pi.image_url ORDER BY pi.is_primary DESC SEPARATOR ', ') AS images
FROM 
    products p
JOIN 
    product_categories pc ON p.category_id = pc.category_id
JOIN 
    manufacturers m ON p.manufacturer_id = m.manufacturer_id
LEFT JOIN 
    product_specifications ps ON p.product_id = ps.product_id
LEFT JOIN 
    product_images pi ON p.product_id = pi.product_id
WHERE 
    p.manufacturer_id = (SELECT manufacturer_id FROM manufacturers WHERE name = 'Swamiji Transmission Pvt. Ltd.')
GROUP BY 
    p.product_id
ORDER BY 
    p.name;
```
