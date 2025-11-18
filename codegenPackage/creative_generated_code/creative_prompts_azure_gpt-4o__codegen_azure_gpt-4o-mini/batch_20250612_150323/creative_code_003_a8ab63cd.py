"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.ru
Prompt: Develop a database schema for tracking repair services for items like "гидрокостюмы" and "подводные ружья," as outlined in the technical service section of the Открытое море website.
Generated: DETERMINISTIC_a8ab63cdf767625a
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for tracking repair services for items like "гидрокостюмы" and "подводные ружья"

-- Create a table to store item types
CREATE TABLE ItemTypes (
    id SERIAL PRIMARY KEY,                -- Unique identifier for each item type
    name VARCHAR(100) NOT NULL UNIQUE,    -- Name of the item type (e.g., "гидрокостюмы")
    description TEXT                      -- Optional description of the item type
);

-- Create a table to store customers
CREATE TABLE Customers (
    id SERIAL PRIMARY KEY,                -- Unique identifier for each customer
    first_name VARCHAR(50) NOT NULL,      -- First name of the customer
    last_name VARCHAR(50) NOT NULL,       -- Last name of the customer
    email VARCHAR(100) UNIQUE,             -- Email address of the customer
    phone VARCHAR(20),                     -- Phone number of the customer
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp of when the customer was added
);

-- Create a table to store repair services
CREATE TABLE RepairServices (
    id SERIAL PRIMARY KEY,                -- Unique identifier for each repair service
    item_type_id INT NOT NULL,            -- Foreign key referencing ItemTypes
    customer_id INT NOT NULL,              -- Foreign key referencing Customers
    repair_description TEXT NOT NULL,      -- Description of the repair service
    status VARCHAR(20) DEFAULT 'Pending',  -- Status of the repair (e.g., Pending, In Progress, Completed)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the service was requested
    completed_at TIMESTAMP,                -- Timestamp of when the repair was completed
    FOREIGN KEY (item_type_id) REFERENCES ItemTypes(id) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (customer_id) REFERENCES Customers(id) ON DELETE CASCADE      -- Ensures referential integrity
);

-- Create indexes to improve query performance
CREATE INDEX idx_item_type ON RepairServices(item_type_id);
CREATE INDEX idx_customer ON RepairServices(customer_id);

-- Sample data insertion for demonstration purposes
INSERT INTO ItemTypes (name, description) VALUES
    ('гидрокостюмы', 'Специальная одежда для подводной деятельности'),
    ('подводные ружья', 'Оружие для подводной охоты');

INSERT INTO Customers (first_name, last_name, email, phone) VALUES
    ('Иван', 'Иванов', 'ivan@example.com', '+79991234567'),
    ('Петр', 'Петров', 'petr@example.com', '+79993456789');

-- Example of inserting a repair service
INSERT INTO RepairServices (item_type_id, customer_id, repair_description) VALUES
    (1, 1, 'Замена молнии на гидрокостюме'),
    (2, 2, 'Ремонт подводного ружья после охоты');
```
