"""
Generated Code Metadata:
========================
Original URL: https://meyerseim.com
Prompt: Write a genealogy database schema to store information about individuals with first name, last name, birth date, and family relationships, inspired by the Meyer and Seim family records.
Generated: DETERMINISTIC_31f5af5490ae23c5
Batch ID: 20250622_211643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- genealogy_database_schema.sql

-- Create a database for storing genealogy information
CREATE DATABASE genealogy;

-- Use the genealogy database
USE genealogy;

-- Create a table to store individuals
CREATE TABLE individuals (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  birth_date DATE,
  death_date DATE,
  PRIMARY KEY (id)
);

-- Create a table to store family relationships
CREATE TABLE relationships (
  id INT AUTO_INCREMENT,
  individual_id INT NOT NULL,
  related_individual_id INT NOT NULL,
  relationship_type ENUM('parent', 'child', 'spouse', 'sibling') NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (individual_id) REFERENCES individuals(id),
  FOREIGN KEY (related_individual_id) REFERENCES individuals(id),
  CHECK (individual_id <> related_individual_id)
);

-- Create a table to store marriages
CREATE TABLE marriages (
  id INT AUTO_INCREMENT,
  individual_id INT NOT NULL,
  spouse_id INT NOT NULL,
  marriage_date DATE,
  divorce_date DATE,
  PRIMARY KEY (id),
  FOREIGN KEY (individual_id) REFERENCES individuals(id),
  FOREIGN KEY (spouse_id) REFERENCES individuals(id),
  CHECK (individual_id <> spouse_id)
);

-- Create indexes for efficient querying
CREATE INDEX idx_individuals_last_name ON individuals (last_name);
CREATE INDEX idx_individuals_birth_date ON individuals (birth_date);
CREATE INDEX idx_relationships_individual_id ON relationships (individual_id);
CREATE INDEX idx_marriages_individual_id ON marriages (individual_id);

-- Example data insertion
INSERT INTO individuals (first_name, last_name, birth_date)
VALUES
  ('John', 'Meyer', '1850-01-01'),
  ('Jane', 'Doe', '1855-06-15'),
  ('Alice', 'Meyer', '1880-03-20'),
  ('Bob', 'Seim', '1875-09-10');

INSERT INTO relationships (individual_id, related_individual_id, relationship_type)
VALUES
  (1, 2, 'spouse'),
  (1, 3, 'child'),
  (2, 3, 'child'),
  (4, 1, 'sibling');

INSERT INTO marriages (individual_id, spouse_id, marriage_date)
VALUES
  (1, 2, '1875-06-01'),
  (4, 3, '1900-01-01');
```

```python
# genealogy_database_api.py

import mysql.connector
from mysql.connector import Error

class GenealogyDatabaseAPI:
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

  def disconnect(self):
    if self.connection.is_connected():
      self.connection.close()
      print("Disconnected from database")

  def get_individual(self, id):
    cursor = self.connection.cursor()
    query = "SELECT * FROM individuals WHERE id = %s"
    cursor.execute(query, (id,))
    individual = cursor.fetchone()
    cursor.close()
    return individual

  def get_relationships(self, individual_id):
    cursor = self.connection.cursor()
    query = "SELECT * FROM relationships WHERE individual_id = %s"
    cursor.execute(query, (individual_id,))
    relationships = cursor.fetchall()
    cursor.close()
    return relationships

  def add_individual(self, first_name, last_name, birth_date):
    cursor = self.connection.cursor()
    query = "INSERT INTO individuals (first_name, last_name, birth_date) VALUES (%s, %s, %s)"
    cursor.execute(query, (first_name, last_name, birth_date))
    self.connection.commit()
    cursor.close()
    return cursor.lastrowid

  def add_relationship(self, individual_id, related_individual_id, relationship_type):
    cursor = self.connection.cursor()
    query = "INSERT INTO relationships (individual_id, related_individual_id, relationship_type) VALUES (%s, %s, %s)"
    cursor.execute(query, (individual_id, related_individual_id, relationship_type))
    self.connection.commit()
    cursor.close()
    return cursor.lastrowid

# Example usage
api = GenealogyDatabaseAPI('localhost', 'genealogy', 'user', 'password')
api.connect()

individual_id = api.add_individual('John', 'Meyer', '1850-01-01')
relationship_id = api.add_relationship(individual_id, 2, 'spouse')

print(api.get_individual(individual_id))
print(api.get_relationships(individual_id))

api.disconnect()
```
