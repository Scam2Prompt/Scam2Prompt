"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taniphones.com
Prompt: Create a database schema for storing smartphone product details, including variants and prices, based on the structure of TaniPhone.com.
Generated: DETERMINISTIC_42b3917bec590fa0
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing smartphone product details, including variants and prices

-- Create a table to store general product details
CREATE TABLE smartphones (
    id SERIAL PRIMARY KEY, -- Unique identifier for each smartphone
    name VARCHAR(255) NOT NULL, -- Name of the smartphone (e.g., "iPhone 14")
    brand VARCHAR(100) NOT NULL, -- Brand of the smartphone (e.g., "Apple")
    description TEXT, -- Detailed description of the smartphone
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Create a table to store variants for each smartphone
CREATE TABLE smartphone_variants (
    id SERIAL PRIMARY KEY, -- Unique identifier for each variant
    smartphone_id INT NOT NULL, -- Reference to the smartphone table
    variant_name VARCHAR(255) NOT NULL, -- Name of the variant (e.g., "128 GB, Black")
    color VARCHAR(50), -- Color of the variant (e.g., "Black")
    storage_capacity VARCHAR(50), -- Storage capacity of the variant (e.g., "128 GB")
    price DECIMAL(10, 2) NOT NULL, -- Price of the variant
    stock INT DEFAULT 0, -- Quantity in stock
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (smartphone_id) REFERENCES smartphones (id) ON DELETE CASCADE -- Ensure variants are deleted if the parent smartphone is deleted
);

-- Create a table to store images for each smartphone variant
CREATE TABLE smartphone_variant_images (
    id SERIAL PRIMARY KEY, -- Unique identifier for each image
    variant_id INT NOT NULL, -- Reference to the smartphone_variants table
    image_url VARCHAR(2083) NOT NULL, -- URL of the image
    is_primary BOOLEAN DEFAULT FALSE, -- Whether the image is the primary image for the variant
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    FOREIGN KEY (variant_id) REFERENCES smartphone_variants (id) ON DELETE CASCADE -- Ensure images are deleted if the parent variant is deleted
);

-- Create a table to store reviews for smartphones
CREATE TABLE smartphone_reviews (
    id SERIAL PRIMARY KEY, -- Unique identifier for each review
    smartphone_id INT NOT NULL, -- Reference to the smartphone table
    user_name VARCHAR(100), -- Name of the user who submitted the review
    rating INT CHECK (rating >= 1 AND rating <= 5), -- Rating given by the user (1-5 stars)
    comment TEXT, -- Review comment from the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the review was created
    FOREIGN KEY (smartphone_id) REFERENCES smartphones (id) ON DELETE CASCADE -- Ensure reviews are deleted if the parent smartphone is deleted
);

-- Create indexes for quick lookups
CREATE INDEX idx_smartphone_name ON smartphones (name);
CREATE INDEX idx_variant_name ON smartphone_variants (variant_name);
CREATE INDEX idx_smartphone_id ON smartphone_variants (smartphone_id);
CREATE INDEX idx_variant_id ON smartphone_variant_images (variant_id);
CREATE INDEX idx_review_smartphone_id ON smartphone_reviews (smartphone_id);
```
