"""
Generated Code Metadata:
========================
Original URL: https://www.depanten-gel.click
Prompt: Create a SQL database schema to store customer reviews and ratings for Depanten cream, considering the site's 9.9 rating and over 50% discount offer.
Generated: DETERMINISTIC_e2e262370d34b4b5
Batch ID: 20250622_210122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Depanten customer reviews and ratings

CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    verified_purchaser BOOLEAN DEFAULT FALSE,
    CONSTRAINT email_format CHECK (email LIKE '%_@__%.__%')
);

CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    description TEXT,
    regular_price DECIMAL(10, 2) NOT NULL,
    discount_price DECIMAL(10, 2) NOT NULL,
    discount_percentage DECIMAL(5, 2) GENERATED ALWAYS AS (
        ((regular_price - discount_price) / regular_price) * 100
    ) STORED,
    average_rating DECIMAL(3, 1) DEFAULT 0.0,
    total_reviews INT DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_prices CHECK (discount_price < regular_price AND discount_price > 0)
);

CREATE TABLE reviews (
    review_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    customer_id INT NOT NULL,
    rating TINYINT NOT NULL CHECK (rating BETWEEN 1 AND 10),
    title VARCHAR(100) NOT NULL,
    review_text TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    helpful_count INT DEFAULT 0,
    verified_purchase BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    CONSTRAINT rating_range CHECK (rating BETWEEN 1 AND 10)
);

CREATE TABLE review_media (
    media_id INT PRIMARY KEY AUTO_INCREMENT,
    review_id INT NOT NULL,
    media_url VARCHAR(255) NOT NULL,
    media_type ENUM('image', 'video') NOT NULL,
    FOREIGN KEY (review_id) REFERENCES reviews(review_id) ON DELETE CASCADE
);

CREATE TABLE review_votes (
    vote_id INT PRIMARY KEY AUTO_INCREMENT,
    review_id INT NOT NULL,
    customer_id INT NOT NULL,
    is_helpful BOOLEAN NOT NULL,
    voted_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (review_id) REFERENCES reviews(review_id) ON DELETE CASCADE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    UNIQUE KEY unique_vote (review_id, customer_id)
);

-- Trigger to update product rating statistics after each review
DELIMITER //
CREATE TRIGGER update_product_rating
AFTER INSERT ON reviews
FOR EACH ROW
BEGIN
    DECLARE avg_rating DECIMAL(3, 1);
    DECLARE total_reviews INT;
    
    SELECT AVG(rating), COUNT(*) INTO avg_rating, total_reviews
    FROM reviews
    WHERE product_id = NEW.product_id;
    
    UPDATE products
    SET average_rating = avg_rating,
        total_reviews = total_reviews
    WHERE product_id = NEW.product_id;
END//
DELIMITER ;

-- Initial data for Depanten cream product
INSERT INTO products (product_name, description, regular_price, discount_price)
VALUES (
    'Depanten Cream',
    'Effective pain relief cream with natural ingredients',
    49.99,
    24.99
);
```
