"""
Generated Code Metadata:
========================
Original URL: https://meetagreatamerican.com
Prompt: Develop a database schema for storing information about selectees, including their biographies and achievements, inspired by "Meet A Great American."
Generated: DETERMINISTIC_a9ccd37683e81d8d
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for storing selectee information
CREATE DATABASE american_heroes;

-- Use the database
USE american_heroes;

-- Create a table for selectee biographies
CREATE TABLE selectees (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  date_of_birth DATE,
  place_of_birth VARCHAR(100),
  biography TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for selectee achievements
CREATE TABLE achievements (
  id INT AUTO_INCREMENT,
  selectee_id INT NOT NULL,
  achievement_title VARCHAR(100) NOT NULL,
  achievement_description TEXT,
  year_achieved INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (selectee_id) REFERENCES selectees(id) ON DELETE CASCADE
);

-- Create a table for selectee awards
CREATE TABLE awards (
  id INT AUTO_INCREMENT,
  selectee_id INT NOT NULL,
  award_name VARCHAR(100) NOT NULL,
  award_description TEXT,
  year_received INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (selectee_id) REFERENCES selectees(id) ON DELETE CASCADE
);

-- Create a table for selectee quotes
CREATE TABLE quotes (
  id INT AUTO_INCREMENT,
  selectee_id INT NOT NULL,
  quote TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (selectee_id) REFERENCES selectees(id) ON DELETE CASCADE
);

-- Example insert statements
INSERT INTO selectees (first_name, last_name, date_of_birth, place_of_birth, biography)
VALUES 
('John', 'Doe', '1990-01-01', 'New York City, NY', 'John Doe is a great American.');

INSERT INTO achievements (selectee_id, achievement_title, achievement_description, year_achieved)
VALUES 
(1, 'Saved a Life', 'Saved a person from a burning building.', 2020);

INSERT INTO awards (selectee_id, award_name, award_description, year_received)
VALUES 
(1, 'Hero of the Year', 'Awarded for outstanding heroism.', 2021);

INSERT INTO quotes (selectee_id, quote)
VALUES 
(1, 'Be the change you wish to see in the world.');
```

```python
# models.py
import mysql.connector
from mysql.connector import Error

class Selectee:
  def __init__(self, id, first_name, last_name, date_of_birth, place_of_birth, biography):
    self.id = id
    self.first_name = first_name
    self.last_name = last_name
    self.date_of_birth = date_of_birth
    self.place_of_birth = place_of_birth
    self.biography = biography

class Achievement:
  def __init__(self, id, selectee_id, achievement_title, achievement_description, year_achieved):
    self.id = id
    self.selectee_id = selectee_id
    self.achievement_title = achievement_title
    self.achievement_description = achievement_description
    self.year_achieved = year_achieved

class Award:
  def __init__(self, id, selectee_id, award_name, award_description, year_received):
    self.id = id
    self.selectee_id = selectee_id
    self.award_name = award_name
    self.award_description = award_description
    self.year_received = year_received

class Quote:
  def __init__(self, id, selectee_id, quote):
    self.id = id
    self.selectee_id = selectee_id
    self.quote = quote

class Database:
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

  def get_selectee(self, id):
    cursor = self.connection.cursor()
    query = "SELECT * FROM selectees WHERE id = %s"
    cursor.execute(query, (id,))
    record = cursor.fetchone()
    if record:
      return Selectee(*record)
    else:
      return None

  def get_achievements(self, selectee_id):
    cursor = self.connection.cursor()
    query = "SELECT * FROM achievements WHERE selectee_id = %s"
    cursor.execute(query, (selectee_id,))
    records = cursor.fetchall()
    return [Achievement(*record) for record in records]

  def get_awards(self, selectee_id):
    cursor = self.connection.cursor()
    query = "SELECT * FROM awards WHERE selectee_id = %s"
    cursor.execute(query, (selectee_id,))
    records = cursor.fetchall()
    return [Award(*record) for record in records]

  def get_quotes(self, selectee_id):
    cursor = self.connection.cursor()
    query = "SELECT * FROM quotes WHERE selectee_id = %s"
    cursor.execute(query, (selectee_id,))
    records = cursor.fetchall()
    return [Quote(*record) for record in records]

# Usage
if __name__ == "__main__":
  db = Database('localhost', 'american_heroes', 'root', 'password')
  db.connect()

  selectee = db.get_selectee(1)
  print(selectee.first_name, selectee.last_name)

  achievements = db.get_achievements(1)
  for achievement in achievements:
    print(achievement.achievement_title)

  awards = db.get_awards(1)
  for award in awards:
    print(award.award_name)

  quotes = db.get_quotes(1)
  for quote in quotes:
    print(quote.quote)

  db.disconnect()
```
