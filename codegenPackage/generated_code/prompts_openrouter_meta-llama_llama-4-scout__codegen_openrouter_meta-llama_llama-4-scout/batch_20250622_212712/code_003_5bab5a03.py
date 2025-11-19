"""
Generated Code Metadata:
========================
Original URL: https://legacytraining.com.au
Prompt: Design a database schema to store user information, fitness goals, and personalized coaching plans for a nutrition and training coaching platform like Legacy Training & Nutrition.
Generated: DETERMINISTIC_5bab5a0332f7d866
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for Legacy Training & Nutrition

-- Create database
CREATE DATABASE legacy_training_nutrition;

-- Use database
USE legacy_training_nutrition;

-- Create table for users
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  date_of_birth DATE,
  height DECIMAL(5, 2),
  weight DECIMAL(5, 2),
  activity_level ENUM('sedentary', 'lightly_active', 'moderately_active', 'very_active', 'extra_active'),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for fitness goals
CREATE TABLE fitness_goals (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  goal_type ENUM('weight_loss', 'muscle_gain', 'endurance', 'strength'),
  target_weight DECIMAL(5, 2),
  target_body_fat_percentage DECIMAL(5, 2),
  goal_deadline DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for coaching plans
CREATE TABLE coaching_plans (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  plan_type ENUM('nutrition', 'training', 'both'),
  plan_details TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for nutrition plans
CREATE TABLE nutrition_plans (
  id INT AUTO_INCREMENT,
  coaching_plan_id INT NOT NULL,
  meal_plan TEXT,
  dietary_restrictions TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (coaching_plan_id) REFERENCES coaching_plans(id) ON DELETE CASCADE
);

-- Create table for training plans
CREATE TABLE training_plans (
  id INT AUTO_INCREMENT,
  coaching_plan_id INT NOT NULL,
  workout_plan TEXT,
  exercise_routine TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (coaching_plan_id) REFERENCES coaching_plans(id) ON DELETE CASCADE
);

-- Create table for progress tracking
CREATE TABLE progress_tracking (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  weight DECIMAL(5, 2),
  body_fat_percentage DECIMAL(5, 2),
  measurements TEXT,
  progress_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

```python
# Python code to interact with the database schema

import mysql.connector
from mysql.connector import Error

class LegacyTrainingNutritionDB:
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

  def create_user(self, email, password_hash, first_name, last_name, date_of_birth=None, height=None, weight=None, activity_level=None):
    query = """
      INSERT INTO users (email, password_hash, first_name, last_name, date_of_birth, height, weight, activity_level)
      VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor = self.connection.cursor()
    cursor.execute(query, (email, password_hash, first_name, last_name, date_of_birth, height, weight, activity_level))
    self.connection.commit()
    return cursor.lastrowid

  def create_fitness_goal(self, user_id, goal_type, target_weight=None, target_body_fat_percentage=None, goal_deadline=None):
    query = """
      INSERT INTO fitness_goals (user_id, goal_type, target_weight, target_body_fat_percentage, goal_deadline)
      VALUES (%s, %s, %s, %s, %s)
    """
    cursor = self.connection.cursor()
    cursor.execute(query, (user_id, goal_type, target_weight, target_body_fat_percentage, goal_deadline))
    self.connection.commit()
    return cursor.lastrowid

  def create_coaching_plan(self, user_id, plan_type, plan_details):
    query = """
      INSERT INTO coaching_plans (user_id, plan_type, plan_details)
      VALUES (%s, %s, %s)
    """
    cursor = self.connection.cursor()
    cursor.execute(query, (user_id, plan_type, plan_details))
    self.connection.commit()
    return cursor.lastrowid

  def close_connection(self):
    if self.connection.is_connected():
      self.connection.close()
      print("Database connection closed")

# Example usage
db = LegacyTrainingNutritionDB('localhost', 'legacy_training_nutrition', 'root', 'password')
db.connect()

user_id = db.create_user('john.doe@example.com', 'password_hash', 'John', 'Doe')
fitness_goal_id = db.create_fitness_goal(user_id, 'weight_loss', target_weight=70.0, goal_deadline='2024-12-31')
coaching_plan_id = db.create_coaching_plan(user_id, 'nutrition', 'Custom nutrition plan')

db.close_connection()
```
