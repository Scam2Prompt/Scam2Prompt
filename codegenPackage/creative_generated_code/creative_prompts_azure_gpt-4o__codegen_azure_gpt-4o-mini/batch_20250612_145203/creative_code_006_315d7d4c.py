"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://equinox.by
Prompt: Recommend a database schema for storing information about Chevrolet Equinox cars purchased from U.S. auctions, including fields for model year, mileage, auction price, and repair status.
Generated: DETERMINISTIC_315d7d4c7db52766
Batch ID: 20250612_145203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing Chevrolet Equinox cars purchased from U.S. auctions

CREATE TABLE ChevroletEquinox (
    id SERIAL PRIMARY KEY,                  -- Unique identifier for each car entry
    model_year INT NOT NULL,                -- Year the model was manufactured (e.g., 2020)
    mileage INT NOT NULL,                   -- Mileage of the car in miles
    auction_price DECIMAL(10, 2) NOT NULL, -- Price at which the car was purchased from the auction
    repair_status VARCHAR(50) NOT NULL,     -- Current status of repairs (e.g., 'Pending', 'In Progress', 'Completed')
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    CHECK (model_year >= 2000 AND model_year <= EXTRACT(YEAR FROM CURRENT_DATE)), -- Validate model year
    CHECK (mileage >= 0),                   -- Validate mileage is non-negative
    CHECK (auction_price >= 0)              -- Validate auction price is non-negative
);

-- Indexes for performance improvement
CREATE INDEX idx_model_year ON ChevroletEquinox(model_year);
CREATE INDEX idx_auction_price ON ChevroletEquinox(auction_price);
CREATE INDEX idx_repair_status ON ChevroletEquinox(repair_status);
```
