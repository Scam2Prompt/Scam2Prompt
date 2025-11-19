"""
Generated Code Metadata:
========================
Original URL: https://elon.live
Prompt: Design a database schema to store information about marijuana users, growers, and distributors under a decriminalization program, including fields for user fees and possession limits.
Generated: DETERMINISTIC_1145c32be7f1e63d
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for decriminalization program
CREATE DATABASE decriminalization_program;

-- Use database
USE decriminalization_program;

-- Create table for users
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  user_type ENUM('user', 'grower', 'distributor') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for user fees
CREATE TABLE user_fees (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  fee_type ENUM('annual', 'monthly') NOT NULL,
  fee_amount DECIMAL(10, 2) NOT NULL,
  payment_date DATE,
  payment_method VARCHAR(50),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for possession limits
CREATE TABLE possession_limits (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  limit_type ENUM('daily', 'monthly') NOT NULL,
  limit_quantity DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for growers
CREATE TABLE growers (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  grow_location VARCHAR(255) NOT NULL,
  grow_capacity DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for distributors
CREATE TABLE distributors (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  distribution_location VARCHAR(255) NOT NULL,
  distribution_capacity DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for transactions
CREATE TABLE transactions (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  transaction_type ENUM('purchase', 'sale') NOT NULL,
  transaction_date DATE NOT NULL,
  quantity DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create indexes for foreign keys
CREATE INDEX idx_user_fees_user_id ON user_fees(user_id);
CREATE INDEX idx_possession_limits_user_id ON possession_limits(user_id);
CREATE INDEX idx_growers_user_id ON growers(user_id);
CREATE INDEX idx_distributors_user_id ON distributors(user_id);
CREATE INDEX idx_transactions_user_id ON transactions(user_id);
```

```sql
-- sample_data.sql

-- Insert sample data into users table
INSERT INTO users (first_name, last_name, email, phone_number, address, user_type)
VALUES
  ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'user'),
  ('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St', 'grower'),
  ('Bob', 'Johnson', 'bob.johnson@example.com', '555-123-4567', '789 Oak St', 'distributor');

-- Insert sample data into user_fees table
INSERT INTO user_fees (user_id, fee_type, fee_amount, payment_date, payment_method)
VALUES
  (1, 'annual', 100.00, '2022-01-01', 'cash'),
  (2, 'monthly', 10.00, '2022-02-01', 'credit'),
  (3, 'annual', 500.00, '2022-03-01', 'check');

-- Insert sample data into possession_limits table
INSERT INTO possession_limits (user_id, limit_type, limit_quantity)
VALUES
  (1, 'daily', 10.00),
  (2, 'monthly', 100.00),
  (3, 'daily', 50.00);

-- Insert sample data into growers table
INSERT INTO growers (user_id, grow_location, grow_capacity)
VALUES
  (2, '123 Grow St', 1000.00),
  (3, '456 Farm St', 5000.00);

-- Insert sample data into distributors table
INSERT INTO distributors (user_id, distribution_location, distribution_capacity)
VALUES
  (3, '789 Dist St', 10000.00);

-- Insert sample data into transactions table
INSERT INTO transactions (user_id, transaction_type, transaction_date, quantity)
VALUES
  (1, 'purchase', '2022-01-15', 5.00),
  (2, 'sale', '2022-02-20', 20.00),
  (3, 'purchase', '2022-03-10', 10.00);
```
