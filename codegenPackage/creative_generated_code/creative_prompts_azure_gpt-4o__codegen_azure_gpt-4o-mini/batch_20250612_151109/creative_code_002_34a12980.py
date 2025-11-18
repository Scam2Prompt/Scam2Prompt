"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moveisonlinepelotasbraz.blogspot.com
Prompt: Create a database schema in SQL to store furniture product information from "moveisonlinepelotasbraz," including columns for product name, price range, category (e.g., "Sala," "Quarto"), and availability.
Generated: DETERMINISTIC_34a129806760b415
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing furniture product information

CREATE TABLE FurnitureProducts (
    ProductID SERIAL PRIMARY KEY,             -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,       -- Name of the product (maximum 255 characters)
    PriceRange VARCHAR(100) NOT NULL,         -- Price range of the product (maximum 100 characters)
    Category ENUM('Sala', 'Quarto', 'Cozinha', 'Banheiro', 'Escritório') NOT NULL,  -- Category of the product
    Availability BOOLEAN DEFAULT TRUE,         -- Availability status of the product (TRUE for available, FALSE for not available)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of the last update
    CHECK (PriceRange ~ '^[0-9]+[ -]*[0-9]*$') -- Simple check to ensure price range is numeric
);

-- Index for faster search by category
CREATE INDEX idx_category ON FurnitureProducts (Category);
```
