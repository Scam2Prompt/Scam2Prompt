"""
Generated Code Metadata:
========================
Original URL: https://tante4dx43.com
Prompt: Create a database schema for storing lottery results (e.g., HK Siang, Singapore, Malaysia) as shown on TANTE4D, including date and result fields.
Generated: DETERMINISTIC_631d56645d7424e6
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for lottery results tracking system
CREATE TABLE lottery_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL,
    description TEXT,
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_lottery_name_country UNIQUE (name, country)
);

CREATE TABLE lottery_draws (
    id SERIAL PRIMARY KEY,
    lottery_type_id INTEGER NOT NULL,
    draw_date DATE NOT NULL,
    draw_time TIME,
    reference_number VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_lottery_type FOREIGN KEY (lottery_type_id) REFERENCES lottery_types(id),
    CONSTRAINT unique_draw_date_lottery UNIQUE (lottery_type_id, draw_date)
);

CREATE TABLE lottery_results (
    id SERIAL PRIMARY KEY,
    draw_id INTEGER NOT NULL,
    result_type VARCHAR(20) NOT NULL, -- 'main', 'consolation', 'special', etc.
    position INTEGER, -- For ordered results (1st prize, 2nd prize, etc.)
    number VARCHAR(20) NOT NULL, -- The actual lottery number
    prize_amount DECIMAL(15, 2), -- Optional prize amount if available
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_draw FOREIGN KEY (draw_id) REFERENCES lottery_draws(id),
    CONSTRAINT unique_result_per_draw UNIQUE (draw_id, result_type, position, number)
);

-- Indexes for performance
CREATE INDEX idx_lottery_draws_date ON lottery_draws(draw_date);
CREATE INDEX idx_lottery_draws_type ON lottery_draws(lottery_type_id);
CREATE INDEX idx_lottery_results_draw ON lottery_results(draw_id);
CREATE INDEX idx_lottery_results_number ON lottery_results(number);

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers to automatically update timestamps
CREATE TRIGGER update_lottery_types_timestamp
BEFORE UPDATE ON lottery_types
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_lottery_draws_timestamp
BEFORE UPDATE ON lottery_draws
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
