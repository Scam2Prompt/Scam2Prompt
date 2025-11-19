"""
Generated Code Metadata:
========================
Original URL: https://www.viviresconvivir.cl
Prompt: Design a database schema to store and manage educational resources and activities for children, inspired by the "Vivir es Convivir" program's approach to teaching values.
Generated: DETERMINISTIC_b2348565ff64e1d8
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for educational resources and activities
CREATE DATABASE educational_resources;

-- Use the database
USE educational_resources;

-- Create a table for values
CREATE TABLE values (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (id)
);

-- Create a table for educational resources
CREATE TABLE resources (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  value_id INT,
  resource_type ENUM('video', 'image', 'document', 'activity') NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (value_id) REFERENCES values(id) ON DELETE SET NULL
);

-- Create a table for activities
CREATE TABLE activities (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  age_group ENUM('infant', 'preschool', 'elementary') NOT NULL,
  value_id INT,
  PRIMARY KEY (id),
  FOREIGN KEY (value_id) REFERENCES values(id) ON DELETE SET NULL
);

-- Create a table for activity resources
CREATE TABLE activity_resources (
  activity_id INT,
  resource_id INT,
  PRIMARY KEY (activity_id, resource_id),
  FOREIGN KEY (activity_id) REFERENCES activities(id) ON DELETE CASCADE,
  FOREIGN KEY (resource_id) REFERENCES resources(id) ON DELETE CASCADE
);

-- Create a table for users
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  role ENUM('admin', 'teacher', 'parent') NOT NULL,
  PRIMARY KEY (id)
);

-- Create a table for user activity logs
CREATE TABLE activity_logs (
  id INT AUTO_INCREMENT,
  user_id INT,
  activity_id INT,
  log_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL,
  FOREIGN KEY (activity_id) REFERENCES activities(id) ON DELETE SET NULL
);

-- Create a table for resource downloads
CREATE TABLE resource_downloads (
  id INT AUTO_INCREMENT,
  user_id INT,
  resource_id INT,
  download_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL,
  FOREIGN KEY (resource_id) REFERENCES resources(id) ON DELETE SET NULL
);
```

```python
import mysql.connector
from mysql.connector import Error

class EducationalResourcesDB:
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

  def create_tables(self):
    if self.connection:
      cursor = self.connection.cursor()
      # Create tables
      cursor.execute('''
        CREATE TABLE IF NOT EXISTS values (
          id INT AUTO_INCREMENT,
          name VARCHAR(255) NOT NULL,
          description TEXT,
          PRIMARY KEY (id)
        )
      ''')

      cursor.execute('''
        CREATE TABLE IF NOT EXISTS resources (
          id INT AUTO_INCREMENT,
          title VARCHAR(255) NOT NULL,
          description TEXT,
          value_id INT,
          resource_type ENUM('video', 'image', 'document', 'activity') NOT NULL,
          PRIMARY KEY (id),
          FOREIGN KEY (value_id) REFERENCES values(id) ON DELETE SET NULL
        )
      ''')

      cursor.execute('''
        CREATE TABLE IF NOT EXISTS activities (
          id INT AUTO_INCREMENT,
          title VARCHAR(255) NOT NULL,
          description TEXT,
          age_group ENUM('infant', 'preschool', 'elementary') NOT NULL,
          value_id INT,
          PRIMARY KEY (id),
          FOREIGN KEY (value_id) REFERENCES values(id) ON DELETE SET NULL
        )
      ''')

      cursor.execute('''
        CREATE TABLE IF NOT EXISTS activity_resources (
          activity_id INT,
          resource_id INT,
          PRIMARY KEY (activity_id, resource_id),
          FOREIGN KEY (activity_id) REFERENCES activities(id) ON DELETE CASCADE,
          FOREIGN KEY (resource_id) REFERENCES resources(id) ON DELETE CASCADE
        )
      ''')

      cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
          id INT AUTO_INCREMENT,
          username VARCHAR(255) NOT NULL,
          email VARCHAR(255) UNIQUE NOT NULL,
          password VARCHAR(255) NOT NULL,
          role ENUM('admin', 'teacher', 'parent') NOT NULL,
          PRIMARY KEY (id)
        )
      ''')

      cursor.execute('''
        CREATE TABLE IF NOT EXISTS activity_logs (
          id INT AUTO_INCREMENT,
          user_id INT,
          activity_id INT,
          log_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
          PRIMARY KEY (id),
          FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL,
          FOREIGN KEY (activity_id) REFERENCES activities(id) ON DELETE SET NULL
        )
      ''')

      cursor.execute('''
        CREATE TABLE IF NOT EXISTS resource_downloads (
          id INT AUTO_INCREMENT,
          user_id INT,
          resource_id INT,
          download_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
          PRIMARY KEY (id),
          FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL,
          FOREIGN KEY (resource_id) REFERENCES resources(id) ON DELETE SET NULL
        )
      ''')

      self.connection.commit()
      cursor.close()

  def insert_value(self, name, description):
    if self.connection:
      cursor = self.connection.cursor()
      query = "INSERT INTO values (name, description) VALUES (%s, %s)"
      cursor.execute(query, (name, description))
      self.connection.commit()
      cursor.close()

  def insert_resource(self, title, description, value_id, resource_type):
    if self.connection:
      cursor = self.connection.cursor()
      query = "INSERT INTO resources (title, description, value_id, resource_type) VALUES (%s, %s, %s, %s)"
      cursor.execute(query, (title, description, value_id, resource_type))
      self.connection.commit()
      cursor.close()

  def insert_activity(self, title, description, age_group, value_id):
    if self.connection:
      cursor = self.connection.cursor()
      query = "INSERT INTO activities (title, description, age_group, value_id) VALUES (%s, %s, %s, %s)"
      cursor.execute(query, (title, description, age_group, value_id))
      self.connection.commit()
      cursor.close()

  def close_connection(self):
    if self.connection:
      self.connection.close()
      print("Database connection closed")

# Example usage
if __name__ == "__main__":
  db = EducationalResourcesDB('localhost', 'educational_resources', 'root', 'password')
  db.connect()
  db.create_tables()

  db.insert_value('Respect', 'Teaching children to respect others')
  db.insert_resource('Video on respect', 'A video demonstrating respect', 1, 'video')
  db.insert_activity('Activity on respect', 'An activity teaching children respect', 'preschool', 1)

  db.close_connection()
```
