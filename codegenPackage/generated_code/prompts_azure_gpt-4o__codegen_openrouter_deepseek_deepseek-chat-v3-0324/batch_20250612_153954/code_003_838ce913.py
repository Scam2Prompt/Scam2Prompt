"""
Generated Code Metadata:
========================
Original URL: https://millymally.pl
Prompt: Create a database schema in SQL for storing product details, including categories like "zabawki dla niemowląt," "chodziki," and "maty piankowe," as seen on the Milly Mally website.
Generated: DETERMINISTIC_838ce91385a434bf
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Milly Mally product catalog
CREATE TABLE categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    parent_category_id INT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (parent_category_id) REFERENCES categories(category_id) ON DELETE SET NULL
);

CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    discount_price DECIMAL(10, 2) NULL,
    sku VARCHAR(50) UNIQUE NOT NULL,
    stock_quantity INT NOT NULL DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE product_categories (
    product_id INT NOT NULL,
    category_id INT NOT NULL,
    PRIMARY KEY (product_id, category_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
);

CREATE TABLE product_images (
    image_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    display_order INT DEFAULT 0,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

CREATE TABLE product_attributes (
    attribute_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT
);

CREATE TABLE product_attribute_values (
    product_id INT NOT NULL,
    attribute_id INT NOT NULL,
    value TEXT NOT NULL,
    PRIMARY KEY (product_id, attribute_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (attribute_id) REFERENCES product_attributes(attribute_id) ON DELETE CASCADE
);

-- Insert initial categories
INSERT INTO categories (name, description) VALUES 
('Zabawki dla niemowląt', 'Bezpieczne i edukacyjne zabawki dla najmłodszych dzieci'),
('Chodziki', 'Pomocne urządzenia wspierające naukę chodzenia'),
('Maty piankowe', 'Miękkie podłoże zapewniające bezpieczną przestrzeń do zabawy');

-- Insert sample attributes
INSERT INTO product_attributes (name, description) VALUES 
('Wiek', 'Zalecany wiek dziecka'),
('Materiał', 'Główny materiał wykonania produktu'),
('Kolor', 'Dostępne kolory produktu'),
('Wymiary', 'Wymiary produktu w cm'),
('Waga', 'Maksymalna waga użytkownika w kg');
```
