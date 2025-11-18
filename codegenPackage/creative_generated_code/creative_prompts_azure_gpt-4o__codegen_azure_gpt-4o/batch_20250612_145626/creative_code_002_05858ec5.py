"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lover4d.site
Prompt: Create a database schema in SQL to store lottery results for multiple regions (e.g., Singapore, Sydney, and Qatar) with fields for date, region, and winning numbers, inspired by the 4DLOVER website's results section.
Generated: DETERMINISTIC_05858ec501e551ee
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a schema to store lottery results for multiple regions
CREATE TABLE LotteryResults (
    id SERIAL PRIMARY KEY,               -- Unique identifier for each record
    draw_date DATE NOT NULL,             -- Date of the draw
    region VARCHAR(100) NOT NULL,        -- Region of the lottery (e.g., Singapore, Sydney, Qatar)
    winning_numbers VARCHAR(50) NOT NULL, -- Winning numbers (e.g., 4D numbers, stored as comma-separated values)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Add a unique constraint to prevent duplicate entries for the same date and region
ALTER TABLE LotteryResults
ADD CONSTRAINT unique_draw UNIQUE (draw_date, region);

-- Example query to insert data (for validation purposes)
-- INSERT INTO LotteryResults (draw_date, region, winning_numbers)
-- VALUES ('2023-10-15', 'Singapore', '1234,5678,9012');

-- Example query to retrieve lottery results for a specific region and date
-- SELECT * FROM LotteryResults WHERE region = 'Singapore' AND draw_date = '2023-10-15';
```
