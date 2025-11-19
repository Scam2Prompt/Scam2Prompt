"""
Generated Code Metadata:
========================
Original URL: https://lover4d.site
Prompt: Create a database schema in SQL to store lottery results for multiple regions (e.g., Singapore, Sydney, and Qatar) with fields for date, region, and winning numbers, inspired by the 4DLOVER website's results section.
Generated: DETERMINISTIC_05858ec501e551ee
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing lottery results from multiple regions
CREATE TABLE regions (
    region_id INT PRIMARY KEY AUTO_INCREMENT,
    region_name VARCHAR(50) NOT NULL,
    region_code VARCHAR(10) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE lottery_draws (
    draw_id INT PRIMARY KEY AUTO_INCREMENT,
    region_id INT NOT NULL,
    draw_date DATE NOT NULL,
    draw_time TIME,
    draw_name VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (region_id) REFERENCES regions(region_id),
    UNIQUE KEY unique_draw (region_id, draw_date, draw_name)
);

CREATE TABLE winning_numbers (
    number_id INT PRIMARY KEY AUTO_INCREMENT,
    draw_id INT NOT NULL,
    prize_rank INT NOT NULL,
    winning_number VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (draw_id) REFERENCES lottery_draws(draw_id),
    UNIQUE KEY unique_winning_number (draw_id, prize_rank)
);

-- Indexes for performance optimization
CREATE INDEX idx_draw_date ON lottery_draws(draw_date);
CREATE INDEX idx_region_draw ON lottery_draws(region_id, draw_date);
CREATE INDEX idx_winning_number ON winning_numbers(winning_number);

-- Sample data for regions
INSERT INTO regions (region_name, region_code) VALUES
('Singapore', 'SG'),
('Sydney', 'SYD'),
('Qatar', 'QA');
```
