"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://passandbrazzz.blogspot.com
Prompt: Design a database schema for storing information about commercial properties for sale, including fields for type of business, location, and price, inspired by the lighting store listing.
Generated: DETERMINISTIC_1942f099297cb395
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing information about commercial properties for sale

CREATE TABLE Property (
    id SERIAL PRIMARY KEY, -- Unique identifier for the property
    business_type VARCHAR(100) NOT NULL, -- Type of business (e.g., retail, office, etc.)
    location VARCHAR(200) NOT NULL, -- Location of the property (e.g., address or area)
    price DECIMAL(15, 2) NOT NULL, -- Selling price of the property
    description TEXT, -- Optional description of the property
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the property was listed
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the property was last updated
    status VARCHAR(20) CHECK (status IN ('available', 'sold', 'pending')) DEFAULT 'available' -- Status of the property
);

-- Index to optimize search queries by business type
CREATE INDEX idx_business_type ON Property(business_type);

-- Index to optimize search queries by location
CREATE INDEX idx_location ON Property(location);

-- Example function to insert a new property
CREATE OR REPLACE FUNCTION insert_property(
    p_business_type VARCHAR,
    p_location VARCHAR,
    p_price DECIMAL,
    p_description TEXT DEFAULT NULL
) RETURNS VOID AS $$
BEGIN
    INSERT INTO Property (business_type, location, price, description)
    VALUES (p_business_type, p_location, p_price, p_description);
EXCEPTION
    WHEN unique_violation THEN
        RAISE EXCEPTION 'Property with the same details already exists';
    WHEN OTHERS THEN
        RAISE EXCEPTION 'An error occurred while inserting the property: %', SQLERRM;
END;
$$ LANGUAGE plpgsql;

-- Example function to update a property
CREATE OR REPLACE FUNCTION update_property(
    p_id INT,
    p_business_type VARCHAR,
    p_location VARCHAR,
    p_price DECIMAL,
    p_description TEXT DEFAULT NULL
) RETURNS VOID AS $$
BEGIN
    UPDATE Property
    SET business_type = p_business_type,
        location = p_location,
        price = p_price,
        description = p_description,
        updated_at = CURRENT_TIMESTAMP
    WHERE id = p_id;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Property with ID % not found', p_id;
    END IF;
EXCEPTION
    WHEN others THEN
        RAISE EXCEPTION 'An error occurred while updating the property: %', SQLERRM;
END;
$$ LANGUAGE plpgsql;

-- Example function to delete a property
CREATE OR REPLACE FUNCTION delete_property(p_id INT) RETURNS VOID AS $$
BEGIN
    DELETE FROM Property WHERE id = p_id;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Property with ID % not found', p_id;
    END IF;
EXCEPTION
    WHEN others THEN
        RAISE EXCEPTION 'An error occurred while deleting the property: %', SQLERRM;
END;
$$ LANGUAGE plpgsql;

-- To ensure data integrity, consider adding constraints or foreign keys as needed
```
