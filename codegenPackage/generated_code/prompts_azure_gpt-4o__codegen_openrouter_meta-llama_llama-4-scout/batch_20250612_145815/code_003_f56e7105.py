"""
Generated Code Metadata:
========================
Original URL: https://rentsy.pro
Prompt: Create a database schema for managing user subscriptions, payment history, and referral tracking, similar to the features described on Rentsy.
Generated: DETERMINISTIC_f56e71053442b412
Batch ID: 20250612_145815
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database
CREATE DATABASE rentsy_subscription;

-- Use database
USE rentsy_subscription;

-- Create table for users
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for subscription plans
CREATE TABLE subscription_plans (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for user subscriptions
CREATE TABLE user_subscriptions (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  subscription_plan_id INT NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE,
  status ENUM('active', 'inactive', 'expired') NOT NULL DEFAULT 'active',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (subscription_plan_id) REFERENCES subscription_plans(id) ON DELETE CASCADE
);

-- Create table for payment history
CREATE TABLE payment_history (
  id INT AUTO_INCREMENT,
  user_subscription_id INT NOT NULL,
  payment_date DATE NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  payment_method ENUM('credit_card', 'paypal', 'bank_transfer') NOT NULL,
  status ENUM('success', 'failed', 'pending') NOT NULL DEFAULT 'success',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_subscription_id) REFERENCES user_subscriptions(id) ON DELETE CASCADE
);

-- Create table for referrals
CREATE TABLE referrals (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  referred_user_id INT NOT NULL,
  referral_date DATE NOT NULL,
  reward DECIMAL(10, 2),
  status ENUM('pending', 'claimed', 'expired') NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (referred_user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for referral rewards
CREATE TABLE referral_rewards (
  id INT AUTO_INCREMENT,
  referral_id INT NOT NULL,
  reward_date DATE NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (referral_id) REFERENCES referrals(id) ON DELETE CASCADE
);

-- Create indexes
CREATE INDEX idx_user_subscriptions_user_id ON user_subscriptions (user_id);
CREATE INDEX idx_user_subscriptions_subscription_plan_id ON user_subscriptions (subscription_plan_id);
CREATE INDEX idx_payment_history_user_subscription_id ON payment_history (user_subscription_id);
CREATE INDEX idx_referrals_user_id ON referrals (user_id);
CREATE INDEX idx_referrals_referred_user_id ON referrals (referred_user_id);
```

```python
# subscription_service.py

import mysql.connector
from mysql.connector import Error

class SubscriptionService:
    def __init__(self, db_config):
        self.db_config = db_config
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.db_config['host'],
                database=self.db_config['database'],
                user=self.db_config['user'],
                password=self.db_config['password']
            )
            print("Connected to database")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def create_user(self, email, name):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO users (email, name) VALUES (%s, %s)"
            cursor.execute(query, (email, name))
            self.connection.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error creating user: {e}")
            return None

    def create_subscription_plan(self, name, description, price):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO subscription_plans (name, description, price) VALUES (%s, %s, %s)"
            cursor.execute(query, (name, description, price))
            self.connection.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error creating subscription plan: {e}")
            return None

    def subscribe_user(self, user_id, subscription_plan_id, start_date):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO user_subscriptions (user_id, subscription_plan_id, start_date) VALUES (%s, %s, %s)"
            cursor.execute(query, (user_id, subscription_plan_id, start_date))
            self.connection.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error subscribing user: {e}")
            return None

    def record_payment(self, user_subscription_id, payment_date, amount, payment_method):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO payment_history (user_subscription_id, payment_date, amount, payment_method) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (user_subscription_id, payment_date, amount, payment_method))
            self.connection.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error recording payment: {e}")
            return None

    def create_referral(self, user_id, referred_user_id, referral_date):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO referrals (user_id, referred_user_id, referral_date) VALUES (%s, %s, %s)"
            cursor.execute(query, (user_id, referred_user_id, referral_date))
            self.connection.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error creating referral: {e}")
            return None

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")

# Example usage
db_config = {
    'host': 'localhost',
    'database': 'rentsy_subscription',
    'user': 'root',
    'password': 'password'
}

subscription_service = SubscriptionService(db_config)
subscription_service.connect()

user_id = subscription_service.create_user('john.doe@example.com', 'John Doe')
subscription_plan_id = subscription_service.create_subscription_plan('Monthly', 'Monthly subscription plan', 9.99)
subscription_id = subscription_service.subscribe_user(user_id, subscription_plan_id, '2022-01-01')
payment_id = subscription_service.record_payment(subscription_id, '2022-01-15', 9.99, 'credit_card')
referral_id = subscription_service.create_referral(user_id, 2, '2022-01-20')

subscription_service.close_connection()
```
