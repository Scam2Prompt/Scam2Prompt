"""
Generated Code Metadata:
========================
Original URL: https://andiasfrozenyogurt.com
Prompt: Write a SQL query to analyze customer reviews and ratings for a frozen yogurt business, focusing on aspects like service, flavor variety, and overall experience.
Generated: DETERMINISTIC_de92fe5e00584c2a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for frozen yogurt business
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    PRIMARY KEY (customer_id)
);

CREATE TABLE IF NOT EXISTS reviews (
    review_id INT AUTO_INCREMENT,
    customer_id INT NOT NULL,
    service_rating TINYINT NOT NULL,
    flavor_variety_rating TINYINT NOT NULL,
    overall_experience_rating TINYINT NOT NULL,
    review_text TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (review_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- SQL query to analyze customer reviews and ratings
SELECT 
    c.customer_id,
    c.name,
    AVG(r.service_rating) AS avg_service_rating,
    AVG(r.flavor_variety_rating) AS avg_flavor_variety_rating,
    AVG(r.overall_experience_rating) AS avg_overall_experience_rating,
    COUNT(r.review_id) AS total_reviews
FROM 
    customers c
JOIN 
    reviews r ON c.customer_id = r.customer_id
GROUP BY 
    c.customer_id, c.name
ORDER BY 
    avg_overall_experience_rating DESC;

-- Query to get average ratings across all customers
SELECT 
    AVG(service_rating) AS avg_service_rating,
    AVG(flavor_variety_rating) AS avg_flavor_variety_rating,
    AVG(overall_experience_rating) AS avg_overall_experience_rating
FROM 
    reviews;

-- Query to get top-rated aspects (service, flavor variety) across all reviews
SELECT 
    'Service' AS aspect,
    AVG(service_rating) AS avg_rating
FROM 
    reviews
UNION ALL
SELECT 
    'Flavor Variety' AS aspect,
    AVG(flavor_variety_rating) AS avg_rating
FROM 
    reviews
ORDER BY 
    avg_rating DESC;

-- Stored procedure to insert a new review
DELIMITER //
CREATE PROCEDURE insert_review(
    IN p_customer_id INT,
    IN p_service_rating TINYINT,
    IN p_flavor_variety_rating TINYINT,
    IN p_overall_experience_rating TINYINT,
    IN p_review_text TEXT
)
BEGIN
    IF p_customer_id IS NULL OR p_service_rating IS NULL OR p_flavor_variety_rating IS NULL OR p_overall_experience_rating IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Customer ID and ratings are required';
    END IF;

    IF p_service_rating < 1 OR p_service_rating > 5 OR p_flavor_variety_rating < 1 OR p_flavor_variety_rating > 5 OR p_overall_experience_rating < 1 OR p_overall_experience_rating > 5 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Ratings must be between 1 and 5';
    END IF;

    INSERT INTO reviews (customer_id, service_rating, flavor_variety_rating, overall_experience_rating, review_text)
    VALUES (p_customer_id, p_service_rating, p_flavor_variety_rating, p_overall_experience_rating, p_review_text);
END//
DELIMITER ;
```
