"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-official-k.blogspot.com
Prompt: Create a database schema to store computer specifications similar to the Londritech models, including fields for processor type, memory size, storage capacity, graphics card, and price.
Generated: DETERMINISTIC_1edbc59ce2885f3f
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database: ComputerSpecifications
-- This schema is designed to store detailed specifications for computer models.

CREATE TABLE ComputerModels (
    id SERIAL PRIMARY KEY,                    -- Unique identifier for each computer model
    processor_type VARCHAR(100) NOT NULL,     -- Type of processor (e.g., Intel, AMD)
    memory_size INT NOT NULL CHECK (memory_size >= 0), -- Size of memory in GB
    storage_capacity INT NOT NULL CHECK (storage_capacity >= 0), -- Storage capacity in GB
    graphics_card VARCHAR(100) NOT NULL,      -- Type of graphics card (e.g., NVIDIA, AMD)
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Price of the computer model in USD
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Indexing fields for performance optimization
CREATE INDEX idx_processor_type ON ComputerModels (processor_type);
CREATE INDEX idx_memory_size ON ComputerModels (memory_size);
CREATE INDEX idx_storage_capacity ON ComputerModels (storage_capacity);
CREATE INDEX idx_graphics_card ON ComputerModels (graphics_card);
CREATE INDEX idx_price ON ComputerModels (price);
```
