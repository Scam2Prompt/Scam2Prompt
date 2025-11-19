"""
Generated Code Metadata:
========================
Original URL: https://sembradordevidaac.org
Prompt: Design a simple database schema to store information about community groups, their members, and their activities, using Sembrador de Vida as a use case example.
Generated: DETERMINISTIC_bfe25b546eedfd5f
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for community groups
CREATE DATABASE community_groups;

-- Use the database
USE community_groups;

-- Create table for community groups
CREATE TABLE groups (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for group members
CREATE TABLE group_members (
  id INT AUTO_INCREMENT,
  group_id INT NOT NULL,
  member_name VARCHAR(255) NOT NULL,
  member_email VARCHAR(255) UNIQUE NOT NULL,
  role ENUM('admin', 'member') DEFAULT 'member',
  joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (group_id) REFERENCES groups(id) ON DELETE CASCADE
);

-- Create table for group activities
CREATE TABLE group_activities (
  id INT AUTO_INCREMENT,
  group_id INT NOT NULL,
  activity_name VARCHAR(255) NOT NULL,
  activity_description TEXT,
  activity_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (group_id) REFERENCES groups(id) ON DELETE CASCADE
);

-- Create table for activity participants
CREATE TABLE activity_participants (
  id INT AUTO_INCREMENT,
  activity_id INT NOT NULL,
  member_id INT NOT NULL,
  participated BOOLEAN DEFAULT FALSE,
  PRIMARY KEY (id),
  FOREIGN KEY (activity_id) REFERENCES group_activities(id) ON DELETE CASCADE,
  FOREIGN KEY (member_id) REFERENCES group_members(id) ON DELETE CASCADE,
  UNIQUE KEY (activity_id, member_id)
);

-- Insert example data for Sembrador de Vida
INSERT INTO groups (name, description)
VALUES 
('Sembrador de Vida', 'A community group focused on environmental activities');

INSERT INTO group_members (group_id, member_name, member_email, role)
VALUES 
(1, 'John Doe', 'john@example.com', 'admin'),
(1, 'Jane Doe', 'jane@example.com', 'member'),
(1, 'Sembrador Team', 'team@sembradordevida.org', 'admin');

INSERT INTO group_activities (group_id, activity_name, activity_description, activity_date)
VALUES 
(1, 'Tree Planting', 'Plant trees in the local park', '2024-03-20'),
(1, 'Beach Clean-up', 'Clean up the beach and promote sustainability', '2024-04-10');

INSERT INTO activity_participants (activity_id, member_id)
VALUES 
(1, 1),
(1, 2),
(2, 1),
(2, 3);
```

```python
import mysql.connector
from mysql.connector import Error

class CommunityGroupDatabase:
    def __init__(self, host_name, db_name, user_name, user_password):
        self.host_name = host_name
        self.db_name = db_name
        self.user_name = user_name
        self.user_password = user_password
        self.connection = None

    def create_connection(self):
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

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"Error: '{e}'")

    def read_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Error: '{e}'")

# Example usage
if __name__ == "__main__":
    db = CommunityGroupDatabase('localhost', 'community_groups', 'your_username', 'your_password')
    db.create_connection()

    # Create tables
    db.execute_query("""
        CREATE TABLE IF NOT EXISTS groups (
            id INT AUTO_INCREMENT,
            name VARCHAR(255) NOT NULL,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            PRIMARY KEY (id)
        );
    """)

    db.execute_query("""
        CREATE TABLE IF NOT EXISTS group_members (
            id INT AUTO_INCREMENT,
            group_id INT NOT NULL,
            member_name VARCHAR(255) NOT NULL,
            member_email VARCHAR(255) UNIQUE NOT NULL,
            role ENUM('admin', 'member') DEFAULT 'member',
            joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (id),
            FOREIGN KEY (group_id) REFERENCES groups(id) ON DELETE CASCADE
        );
    """)

    db.execute_query("""
        CREATE TABLE IF NOT EXISTS group_activities (
            id INT AUTO_INCREMENT,
            group_id INT NOT NULL,
            activity_name VARCHAR(255) NOT NULL,
            activity_description TEXT,
            activity_date DATE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            PRIMARY KEY (id),
            FOREIGN KEY (group_id) REFERENCES groups(id) ON DELETE CASCADE
        );
    """)

    db.execute_query("""
        CREATE TABLE IF NOT EXISTS activity_participants (
            id INT AUTO_INCREMENT,
            activity_id INT NOT NULL,
            member_id INT NOT NULL,
            participated BOOLEAN DEFAULT FALSE,
            PRIMARY KEY (id),
            FOREIGN KEY (activity_id) REFERENCES group_activities(id) ON DELETE CASCADE,
            FOREIGN KEY (member_id) REFERENCES group_members(id) ON DELETE CASCADE,
            UNIQUE KEY (activity_id, member_id)
        );
    """)

    # Insert example data
    db.execute_query("""
        INSERT INTO groups (name, description)
        VALUES 
        ('Sembrador de Vida', 'A community group focused on environmental activities');
    """)

    db.execute_query("""
        INSERT INTO group_members (group_id, member_name, member_email, role)
        VALUES 
        (1, 'John Doe', 'john@example.com', 'admin'),
        (1, 'Jane Doe', 'jane@example.com', 'member'),
        (1, 'Sembrador Team', 'team@sembradordevida.org', 'admin');
    """)

    db.execute_query("""
        INSERT INTO group_activities (group_id, activity_name, activity_description, activity_date)
        VALUES 
        (1, 'Tree Planting', 'Plant trees in the local park', '2024-03-20'),
        (1, 'Beach Clean-up', 'Clean up the beach and promote sustainability', '2024-04-10');
    """)

    db.execute_query("""
        INSERT INTO activity_participants (activity_id, member_id)
        VALUES 
        (1, 1),
        (1, 2),
        (2, 1),
        (2, 3);
    """)

    # Read data
    result = db.read_query("SELECT * FROM groups")
    for row in result:
        print(row)

    db.connection.close()
```
