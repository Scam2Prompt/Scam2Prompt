"""
Generated Code Metadata:
========================
Original URL: https://lyvely-claim.pages.dev
Prompt: Create a database schema for managing content monetization features, including "Pay to View," "Memberships," and "Tips," as outlined on Lyvely.
Generated: DETERMINISTIC_addb7cc4a1c2ee92
Batch ID: 20250612_151705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for managing content monetization features

-- Create a database
CREATE DATABASE content_monetization;

-- Use the database
USE content_monetization;

-- Create a table for content creators
CREATE TABLE creators (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for content
CREATE TABLE content (
  id INT AUTO_INCREMENT,
  creator_id INT NOT NULL,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (creator_id) REFERENCES creators(id) ON DELETE CASCADE
);

-- Create a table for pay_to_view content
CREATE TABLE pay_to_view (
  id INT AUTO_INCREMENT,
  content_id INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (content_id) REFERENCES content(id) ON DELETE CASCADE
);

-- Create a table for memberships
CREATE TABLE memberships (
  id INT AUTO_INCREMENT,
  creator_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (creator_id) REFERENCES creators(id) ON DELETE CASCADE
);

-- Create a table for membership subscribers
CREATE TABLE membership_subscribers (
  id INT AUTO_INCREMENT,
  membership_id INT NOT NULL,
  subscriber_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (membership_id) REFERENCES memberships(id) ON DELETE CASCADE,
  FOREIGN KEY (subscriber_id) REFERENCES creators(id) ON DELETE CASCADE,
  UNIQUE KEY (membership_id, subscriber_id)
);

-- Create a table for tips
CREATE TABLE tips (
  id INT AUTO_INCREMENT,
  content_id INT,
  sender_id INT NOT NULL,
  receiver_id INT NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (content_id) REFERENCES content(id) ON DELETE SET NULL,
  FOREIGN KEY (sender_id) REFERENCES creators(id) ON DELETE CASCADE,
  FOREIGN KEY (receiver_id) REFERENCES creators(id) ON DELETE CASCADE
);

-- Create a table for transactions
CREATE TABLE transactions (
  id INT AUTO_INCREMENT,
  transaction_type ENUM('pay_to_view', 'membership', 'tip') NOT NULL,
  content_id INT,
  membership_id INT,
  tip_id INT,
  amount DECIMAL(10, 2) NOT NULL,
  status ENUM('pending', 'success', 'failed') NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (content_id) REFERENCES content(id) ON DELETE SET NULL,
  FOREIGN KEY (membership_id) REFERENCES memberships(id) ON DELETE SET NULL,
  FOREIGN KEY (tip_id) REFERENCES tips(id) ON DELETE SET NULL
);

-- Create indexes for better query performance
CREATE INDEX idx_creator_id ON content (creator_id);
CREATE INDEX idx_content_id ON pay_to_view (content_id);
CREATE INDEX idx_membership_id ON membership_subscribers (membership_id);
CREATE INDEX idx_subscriber_id ON membership_subscribers (subscriber_id);
CREATE INDEX idx_content_id ON tips (content_id);
CREATE INDEX idx_sender_id ON tips (sender_id);
CREATE INDEX idx_receiver_id ON tips (receiver_id);
CREATE INDEX idx_transaction_type ON transactions (transaction_type);
```

```sql
-- Example usage:

-- Insert a new creator
INSERT INTO creators (name, email) VALUES ('John Doe', 'john@example.com');

-- Insert a new content
INSERT INTO content (creator_id, title, description) VALUES (1, 'Example Content', 'This is an example content');

-- Insert a new pay to view content
INSERT INTO pay_to_view (content_id, price) VALUES (1, 9.99);

-- Insert a new membership
INSERT INTO memberships (creator_id, name, description, price) VALUES (1, 'Monthly Membership', 'Get access to exclusive content', 29.99);

-- Insert a new membership subscriber
INSERT INTO membership_subscribers (membership_id, subscriber_id) VALUES (1, 2);

-- Insert a new tip
INSERT INTO tips (content_id, sender_id, receiver_id, amount) VALUES (1, 2, 1, 5.00);

-- Insert a new transaction
INSERT INTO transactions (transaction_type, content_id, amount) VALUES ('pay_to_view', 1, 9.99);
```
