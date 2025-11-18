"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dominguezparra.com
Prompt: Suggest a database schema for storing property details and client reviews, inspired by the structure of the Dominguez Parra website.
Generated: DETERMINISTIC_a32c951b2266d2ce
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing property details and client reviews
CREATE TABLE properties (
    property_id SERIAL PRIMARY KEY,              -- Unique identifier for each property
    address VARCHAR(255) NOT NULL,              -- Full address of the property
    city VARCHAR(100) NOT NULL,                  -- City where the property is located
    state VARCHAR(100) NOT NULL,                 -- State where the property is located
    zip_code VARCHAR(10) NOT NULL,               -- ZIP code for the property
    price NUMERIC(10, 2) NOT NULL,               -- Price of the property
    bedrooms INT NOT NULL,                        -- Number of bedrooms in the property
    bathrooms INT NOT NULL,                       -- Number of bathrooms in the property
    square_footage INT NOT NULL,                 -- Total square footage of the property
    property_type VARCHAR(50) NOT NULL,          -- Type of property (e.g., house, apartment)
    listing_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the property was listed
    description TEXT,                            -- Full description of the property
    status VARCHAR(20) CHECK (status IN ('active', 'sold', 'pending')) DEFAULT 'active' -- Current status of the property
);

CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,                -- Unique identifier for each client
    name VARCHAR(100) NOT NULL,                  -- Full name of the client
    email VARCHAR(100) NOT NULL UNIQUE,          -- Email address of the client (must be unique)
    phone VARCHAR(15),                           -- Phone number of the client
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date the client was created
);

CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,                -- Unique identifier for each review
    property_id INT NOT NULL,                    -- Foreign key referencing the property reviewed
    client_id INT NOT NULL,                      -- Foreign key referencing the client who made the review
    rating INT CHECK (rating >= 1 AND rating <= 5), -- Rating given by the client (1 to 5 stars)
    review_text TEXT,                           -- Text of the review
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the review was created
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Example indexes for improved query performance
CREATE INDEX idx_property_city ON properties(city);
CREATE INDEX idx_client_email ON clients(email);
CREATE INDEX idx_review_property ON reviews(property_id);
CREATE INDEX idx_review_client ON reviews(client_id);
```
