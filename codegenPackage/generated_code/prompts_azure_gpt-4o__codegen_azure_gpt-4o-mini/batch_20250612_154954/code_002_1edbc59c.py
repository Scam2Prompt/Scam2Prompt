"""
Generated Code Metadata:
========================
Original URL: https://gala-games-official-k.blogspot.com
Prompt: Create a database schema to store computer specifications similar to the Londritech models, including fields for processor type, memory size, storage capacity, graphics card, and price.
Generated: DETERMINISTIC_1edbc59ce2885f3f
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing computer specifications

CREATE TABLE ComputerSpecifications (
    id SERIAL PRIMARY KEY, -- Unique identifier for each computer specification
    processor_type VARCHAR(100) NOT NULL, -- Type of processor (e.g., Intel i7, AMD Ryzen 5)
    memory_size INT NOT NULL, -- Memory size in GB (e.g., 16 for 16GB)
    storage_capacity INT NOT NULL, -- Storage capacity in GB (e.g., 512 for 512GB SSD)
    graphics_card VARCHAR(100), -- Graphics card model (e.g., NVIDIA GTX 1660)
    price DECIMAL(10, 2) NOT NULL, -- Price of the computer in USD
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Index for faster searching by processor type
CREATE INDEX idx_processor_type ON ComputerSpecifications(processor_type);

-- Index for faster searching by price
CREATE INDEX idx_price ON ComputerSpecifications(price);
```
