"""
Generated Code Metadata:
========================
Original URL: https://thedaybrightener.com
Prompt: Design a database schema to store sweepstakes entries and their corresponding prize information, inspired by the structure implied on thedaybrightener.com.
Generated: DETERMINISTIC_ee1e717e3fd39db6
Batch ID: 20250622_205236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for sweepstakes
CREATE DATABASE sweepstakes_db;

-- Use sweepstakes database
USE sweepstakes_db;

-- Create table for sweepstakes
CREATE TABLE sweepstakes (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `start_date` DATE NOT NULL,
  `end_date` DATE NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for prizes
CREATE TABLE prizes (
  `id` INT AUTO_INCREMENT,
  `sweepstakes_id` INT NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `value` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`sweepstakes_id`) REFERENCES sweepstakes(`id`) ON DELETE CASCADE
);

-- Create table for entries
CREATE TABLE entries (
  `id` INT AUTO_INCREMENT,
  `sweepstakes_id` INT NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL UNIQUE,
  `phone` VARCHAR(20),
  `address` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`sweepstakes_id`) REFERENCES sweepstakes(`id`) ON DELETE CASCADE
);

-- Create table for winners
CREATE TABLE winners (
  `id` INT AUTO_INCREMENT,
  `sweepstakes_id` INT NOT NULL,
  `entry_id` INT NOT NULL,
  `prize_id` INT NOT NULL,
  `announcement_date` DATE NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`sweepstakes_id`) REFERENCES sweepstakes(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`entry_id`) REFERENCES entries(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`prize_id`) REFERENCES prizes(`id`) ON DELETE CASCADE,
  UNIQUE KEY (`sweepstakes_id`, `entry_id`)
);

-- Create indexes for foreign keys
CREATE INDEX idx_sweepstakes_id_prizes ON prizes (sweepstakes_id);
CREATE INDEX idx_sweepstakes_id_entries ON entries (sweepstakes_id);
CREATE INDEX idx_sweepstakes_id_winners ON winners (sweepstakes_id);
CREATE INDEX idx_entry_id_winners ON winners (entry_id);
CREATE INDEX idx_prize_id_winners ON winners (prize_id);
```

```python
# sweepstakes.py

import mysql.connector
from mysql.connector import Error

class SweepstakesDB:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Connected to database")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def create_sweepstakes(self, name, description, start_date, end_date):
        query = """
            INSERT INTO sweepstakes (name, description, start_date, end_date)
            VALUES (%s, %s, %s, %s)
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, (name, description, start_date, end_date))
            self.connection.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error creating sweepstakes: {e}")
        finally:
            cursor.close()

    def create_prize(self, sweepstakes_id, name, description, value):
        query = """
            INSERT INTO prizes (sweepstakes_id, name, description, value)
            VALUES (%s, %s, %s, %s)
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, (sweepstakes_id, name, description, value))
            self.connection.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error creating prize: {e}")
        finally:
            cursor.close()

    def create_entry(self, sweepstakes_id, name, email, phone=None, address=None):
        query = """
            INSERT INTO entries (sweepstakes_id, name, email, phone, address)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, (sweepstakes_id, name, email, phone, address))
            self.connection.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error creating entry: {e}")
        finally:
            cursor.close()

    def declare_winner(self, sweepstakes_id, entry_id, prize_id, announcement_date):
        query = """
            INSERT INTO winners (sweepstakes_id, entry_id, prize_id, announcement_date)
            VALUES (%s, %s, %s, %s)
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, (sweepstakes_id, entry_id, prize_id, announcement_date))
            self.connection.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error declaring winner: {e}")
        finally:
            cursor.close()

# Example usage
if __name__ == "__main__":
    db = SweepstakesDB("localhost", "sweepstakes_db", "user", "password")
    db.connect()

    sweepstakes_id = db.create_sweepstakes("Example Sweepstakes", "This is an example sweepstakes", "2022-01-01", "2022-01-31")
    prize_id = db.create_prize(sweepstakes_id, "Example Prize", "This is an example prize", 100.00)
    entry_id = db.create_entry(sweepstakes_id, "John Doe", "john@example.com")
    db.declare_winner(sweepstakes_id, entry_id, prize_id, "2022-02-01")
```
