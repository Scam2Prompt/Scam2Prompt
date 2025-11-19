"""
Generated Code Metadata:
========================
Original URL: https://fodyem.com
Prompt: Generate a database schema for managing travel packages, including fields for destinations like "Abidjan" and "Maroc & CAN," pricing, and availability.
Generated: DETERMINISTIC_c66b0a91b99c12ff
Batch ID: 20250612_151040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing travel packages

CREATE TABLE destinations (
    id SERIAL PRIMARY KEY, -- Unique identifier for each destination
    name VARCHAR(255) NOT NULL UNIQUE, -- Name of the destination
    description TEXT, -- Description of the destination
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

CREATE TABLE travel_packages (
    id SERIAL PRIMARY KEY, -- Unique identifier for each travel package
    destination_id INT NOT NULL, -- Foreign key referencing the destination
    price DECIMAL(10, 2) NOT NULL, -- Price of the travel package
    availability BOOLEAN NOT NULL DEFAULT TRUE, -- Availability status of the package
    start_date DATE NOT NULL, -- Start date of the travel package
    end_date DATE NOT NULL, -- End date of the travel package
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (destination_id) REFERENCES destinations(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample data insertion for destinations
INSERT INTO destinations (name, description) VALUES
('Abidjan', 'The economic capital of Côte d\'Ivoire, known for its vibrant culture and beautiful beaches.'),
('Maroc & CAN', 'A travel package that includes destinations in Morocco and Canada.');

-- Sample data insertion for travel packages
INSERT INTO travel_packages (destination_id, price, availability, start_date, end_date) VALUES
(1, 1200.00, TRUE, '2023-12-01', '2023-12-15'), -- Package for Abidjan
(2, 1500.00, TRUE, '2024-01-10', '2024-01-20'); -- Package for Maroc & CAN
```
