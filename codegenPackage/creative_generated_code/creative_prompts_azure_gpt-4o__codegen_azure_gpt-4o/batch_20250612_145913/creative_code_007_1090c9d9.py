"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tante4dx40.com
Prompt: Develop a SQL query to store and retrieve transaction records for payment methods like BCA, Mandiri, and CIMB from a database modeled after TANTE4D's payment system.
Generated: DETERMINISTIC_1090c9d9e9aeae96
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create the 'payment_methods' table to store payment method details.
CREATE TABLE payment_methods (
    id INT AUTO_INCREMENT PRIMARY KEY,         -- Unique ID for each payment method
    method_name VARCHAR(50) NOT NULL,          -- Name of the payment method like BCA, Mandiri, CIMB
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Create the 'transactions' table to store transaction details.
CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,         -- Unique ID for each transaction
    payment_method_id INT NOT NULL,            -- Foreign key referencing the payment method
    amount DECIMAL(10, 2) NOT NULL,            -- Transaction amount
    transaction_date TIMESTAMP NOT NULL,       -- The date and time of the transaction
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    FOREIGN KEY (payment_method_id) REFERENCES payment_methods(id) -- Establishes foreign key relationship
);

-- Insert sample data into 'payment_methods' table.
INSERT INTO payment_methods (method_name) VALUES 
('BCA'),
('Mandiri'),
('CIMB');

-- Example query to insert a transaction record.
INSERT INTO transactions (payment_method_id, amount, transaction_date)
VALUES 
(1, 100000.00, '2023-10-05 12:30:00'),   -- BCA transaction
(2, 250000.50, '2023-10-05 13:15:00'),   -- Mandiri transaction
(3, 500000.75, '2023-10-05 14:00:00');   -- CIMB transaction

-- Query to retrieve all transaction records along with their associated payment method.
SELECT 
    transactions.id AS transaction_id, 
    payment_methods.method_name AS payment_method,
    transactions.amount,
    transactions.transaction_date,
    transactions.created_at,
    transactions.updated_at
FROM 
    transactions
JOIN 
    payment_methods 
ON 
    transactions.payment_method_id = payment_methods.id
ORDER BY 
    transactions.transaction_date DESC; -- Order transactions by date in descending order
```
