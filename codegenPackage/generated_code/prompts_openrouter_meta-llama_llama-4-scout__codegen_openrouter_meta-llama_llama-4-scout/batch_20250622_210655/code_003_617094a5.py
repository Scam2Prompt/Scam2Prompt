"""
Generated Code Metadata:
========================
Original URL: https://chatnchill.com
Prompt: Design a database schema for storing information about beach bar events, including Sunday Pig Roast, weddings, and other activities offered by Chat 'N' Chill.
Generated: DETERMINISTIC_617094a5b20d23c5
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for Chat 'N' Chill events
CREATE DATABASE chat_n_chill;

-- Use the database
USE chat_n_chill;

-- Create table for events
CREATE TABLE events (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  event_date DATE NOT NULL,
  start_time TIME NOT NULL,
  end_time TIME NOT NULL,
  location VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for event types
CREATE TABLE event_types (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Insert default event types
INSERT INTO event_types (name, description) 
VALUES 
('Sunday Pig Roast', 'A classic Sunday roast with pig as the main course'),
('Wedding', 'A wedding ceremony and reception'),
('Other', 'Any other type of event');

-- Create table for event attendees
CREATE TABLE attendees (
  id INT AUTO_INCREMENT,
  event_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE
);

-- Create table for event offerings
CREATE TABLE offerings (
  id INT AUTO_INCREMENT,
  event_id INT NOT NULL,
  offering_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE
);

-- Create table for event type associations
CREATE TABLE event_type_associations (
  event_id INT NOT NULL,
  event_type_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (event_id, event_type_id),
  FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE,
  FOREIGN KEY (event_type_id) REFERENCES event_types(id) ON DELETE CASCADE
);
```

```python
# event_service.py

import mysql.connector
from mysql.connector import Error

class EventService:
  def __init__(self, host_name, db_name, user_name, user_password):
    self.host_name = host_name
    self.db_name = db_name
    self.user_name = user_name
    self.user_password = user_password
    self.connection = None

  def connect(self):
    try:
      self.connection = mysql.connector.connect(
        host=self.host_name,
        database=self.db_name,
        user=self.user_name,
        password=self.user_password
      )
      print("Connection to database established")
    except Error as e:
      print(f"Error: '{e}'")

  def create_event(self, event):
    try:
      cursor = self.connection.cursor()
      query = """
        INSERT INTO events (name, description, event_date, start_time, end_time, location)
        VALUES (%s, %s, %s, %s, %s, %s)
      """
      cursor.execute(query, (
        event['name'], 
        event['description'], 
        event['event_date'], 
        event['start_time'], 
        event['end_time'], 
        event['location']
      ))
      self.connection.commit()
      return cursor.lastrowid
    except Error as e:
      print(f"Error: '{e}'")

  def get_event(self, event_id):
    try:
      cursor = self.connection.cursor()
      query = """
        SELECT * FROM events
        WHERE id = %s
      """
      cursor.execute(query, (event_id,))
      return cursor.fetchone()
    except Error as e:
      print(f"Error: '{e}'")

  def close_connection(self):
    if self.connection.is_connected():
      self.connection.close()
      print("MySQL connection is closed")

# Example usage
if __name__ == "__main__":
  host_name = 'localhost'
  db_name = 'chat_n_chill'
  user_name = 'your_username'
  user_password = 'your_password'

  event_service = EventService(host_name, db_name, user_name, user_password)
  event_service.connect()

  event = {
    'name': 'Sunday Pig Roast',
    'description': 'A classic Sunday roast',
    'event_date': '2024-09-29',
    'start_time': '10:00:00',
    'end_time': '14:00:00',
    'location': 'Chat \'N\' Chill Beach Bar'
  }

  event_id = event_service.create_event(event)
  print(f"Event created with ID: {event_id}")

  event_service.close_connection()
```
