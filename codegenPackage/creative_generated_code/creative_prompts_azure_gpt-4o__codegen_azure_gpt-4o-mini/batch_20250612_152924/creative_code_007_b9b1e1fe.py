"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safargenie.com
Prompt: Write a SQL query to store and retrieve tour package information, including themes like Temple Tours and Hill Station Tours, as seen on the "Safar Genie" website.
Generated: DETERMINISTIC_b9b1e1fe6548501e
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a table to store tour package information
CREATE TABLE tour_packages (
    package_id INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each tour package
    package_name VARCHAR(255) NOT NULL, -- Name of the tour package
    theme VARCHAR(100) NOT NULL, -- Theme of the tour (e.g., Temple Tours, Hill Station Tours)
    description TEXT, -- Description of the tour package
    price DECIMAL(10, 2) NOT NULL, -- Price of the tour package
    duration INT NOT NULL, -- Duration of the tour in days
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Insert sample data into the tour_packages table
INSERT INTO tour_packages (package_name, theme, description, price, duration)
VALUES 
    ('Spiritual Temple Tour', 'Temple Tours', 'A captivating journey through the most revered temples.', 4999.99, 5),
    ('Himalayan Hill Station Retreat', 'Hill Station Tours', 'Relax and rejuvenate in the serene hills of the Himalayas.', 7999.99, 7),
    ('Cultural Temple Pilgrimage', 'Temple Tours', 'Explore the rich cultural heritage of ancient temples.', 3499.99, 4),
    ('Adventure Hill Station Excursion', 'Hill Station Tours', 'Thrilling adventures amidst the beautiful hill stations.', 5999.99, 6);

-- Retrieve all tour packages from the table
SELECT 
    package_id,
    package_name,
    theme,
    description,
    price,
    duration,
    created_at,
    updated_at
FROM 
    tour_packages
ORDER BY 
    created_at DESC; -- Order by the date of creation in descending order
```
