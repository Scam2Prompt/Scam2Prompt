"""
Generated Code Metadata:
========================
Original URL: https://tante4dx40.com
Prompt: Develop a SQL query to store and retrieve transaction records for payment methods like BCA, Mandiri, and CIMB from a database modeled after TANTE4D's payment system.
Generated: DETERMINISTIC_1090c9d9e9aeae96
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script for TANTE4D payment system transaction records

-- Create transaction table to store payment records
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id VARCHAR(36) PRIMARY KEY,
    user_id VARCHAR(36) NOT NULL,
    payment_method ENUM('BCA', 'Mandiri', 'CIMB', 'Other') NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('Pending', 'Completed', 'Failed', 'Cancelled') NOT NULL,
    reference_number VARCHAR(50),
    bank_account_number VARCHAR(50),
    bank_account_name VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_user_id (user_id),
    INDEX idx_payment_method (payment_method),
    INDEX idx_status (status),
    INDEX idx_transaction_date (transaction_date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Stored procedure to create a new transaction
DELIMITER //
CREATE PROCEDURE create_transaction(
    IN p_transaction_id VARCHAR(36),
    IN p_user_id VARCHAR(36),
    IN p_payment_method VARCHAR(20),
    IN p_amount DECIMAL(15, 2),
    IN p_status VARCHAR(20),
    IN p_reference_number VARCHAR(50),
    IN p_bank_account_number VARCHAR(50),
    IN p_bank_account_name VARCHAR(100),
    IN p_notes TEXT
)
BEGIN
    INSERT INTO transactions (
        transaction_id,
        user_id,
        payment_method,
        amount,
        status,
        reference_number,
        bank_account_number,
        bank_account_name,
        notes
    ) VALUES (
        p_transaction_id,
        p_user_id,
        p_payment_method,
        p_amount,
        p_status,
        p_reference_number,
        p_bank_account_number,
        p_bank_account_name,
        p_notes
    );
END //
DELIMITER ;

-- Stored procedure to update transaction status
DELIMITER //
CREATE PROCEDURE update_transaction_status(
    IN p_transaction_id VARCHAR(36),
    IN p_status VARCHAR(20)
)
BEGIN
    UPDATE transactions
    SET status = p_status
    WHERE transaction_id = p_transaction_id;
END //
DELIMITER ;

-- Query to get all transactions for a specific user
SELECT 
    transaction_id,
    payment_method,
    amount,
    transaction_date,
    status,
    reference_number,
    bank_account_number,
    bank_account_name,
    notes
FROM transactions
WHERE user_id = 'user_id_placeholder'
ORDER BY transaction_date DESC;

-- Query to get transactions by payment method and date range
SELECT 
    transaction_id,
    user_id,
    amount,
    transaction_date,
    status,
    reference_number
FROM transactions
WHERE payment_method = 'BCA' -- Can be replaced with 'Mandiri' or 'CIMB'
AND transaction_date BETWEEN '2023-01-01' AND '2023-12-31'
ORDER BY transaction_date DESC;

-- Query to get transaction summary by payment method
SELECT 
    payment_method,
    COUNT(*) AS total_transactions,
    SUM(amount) AS total_amount,
    SUM(CASE WHEN status = 'Completed' THEN amount ELSE 0 END) AS completed_amount
FROM transactions
GROUP BY payment_method;

-- Query to get failed transactions
SELECT 
    transaction_id,
    user_id,
    payment_method,
    amount,
    transaction_date,
    reference_number,
    notes
FROM transactions
WHERE status = 'Failed'
ORDER BY transaction_date DESC
LIMIT 100;
```
