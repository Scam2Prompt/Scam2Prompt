"""
Generated Code Metadata:
========================
Original URL: https://myneel.com
Prompt: Design a database schema to store user data and progress tracking information for a weight loss app like Neel, ensuring data consistency and scalability.
Generated: DETERMINISTIC_cff056543dbb0495
Batch ID: 20250622_204925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for the weight loss app
CREATE DATABASE weight_loss_app;

-- Use the database
USE weight_loss_app;

-- Create a table to store user information
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table to store user progress tracking information
CREATE TABLE user_progress (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  weight DECIMAL(5, 2) NOT NULL,
  height DECIMAL(5, 2) NOT NULL,
  body_mass_index DECIMAL(5, 2) NOT NULL,
  progress_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create a table to store user goals
CREATE TABLE user_goals (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  goal_weight DECIMAL(5, 2) NOT NULL,
  goal_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create a table to store workout logs
CREATE TABLE workout_logs (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  workout_date DATE NOT NULL,
  exercise_name VARCHAR(255) NOT NULL,
  sets INT NOT NULL,
  reps INT NOT NULL,
  weight_lifted DECIMAL(5, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create a table to store nutrition logs
CREATE TABLE nutrition_logs (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  log_date DATE NOT NULL,
  food_name VARCHAR(255) NOT NULL,
  calories_consumed INT NOT NULL,
  protein_consumed DECIMAL(5, 2) NOT NULL,
  carbohydrates_consumed DECIMAL(5, 2) NOT NULL,
  fat_consumed DECIMAL(5, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

```python
# models.py
from sqlalchemy import create_engine, Column, Integer, String, Date, DECIMAL, ForeignKey, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('mysql+pymysql://user:password@localhost/weight_loss_app')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, default=TIMESTAMP('now'))
    updated_at = Column(TIMESTAMP, default=TIMESTAMP('now'), onupdate=TIMESTAMP('now'))
    progress = relationship('UserProgress', backref='user')
    goals = relationship('UserGoal', backref='user')
    workout_logs = relationship('WorkoutLog', backref='user')
    nutrition_logs = relationship('NutritionLog', backref='user')

class UserProgress(Base):
    __tablename__ = 'user_progress'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    weight = Column(DECIMAL(5, 2), nullable=False)
    height = Column(DECIMAL(5, 2), nullable=False)
    body_mass_index = Column(DECIMAL(5, 2), nullable=False)
    progress_date = Column(Date, nullable=False)
    created_at = Column(TIMESTAMP, default=TIMESTAMP('now'))
    updated_at = Column(TIMESTAMP, default=TIMESTAMP('now'), onupdate=TIMESTAMP('now'))

class UserGoal(Base):
    __tablename__ = 'user_goals'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    goal_weight = Column(DECIMAL(5, 2), nullable=False)
    goal_date = Column(Date, nullable=False)
    created_at = Column(TIMESTAMP, default=TIMESTAMP('now'))
    updated_at = Column(TIMESTAMP, default=TIMESTAMP('now'), onupdate=TIMESTAMP('now'))

class WorkoutLog(Base):
    __tablename__ = 'workout_logs'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    workout_date = Column(Date, nullable=False)
    exercise_name = Column(String(255), nullable=False)
    sets = Column(Integer, nullable=False)
    reps = Column(Integer, nullable=False)
    weight_lifted = Column(DECIMAL(5, 2), nullable=False)
    created_at = Column(TIMESTAMP, default=TIMESTAMP('now'))
    updated_at = Column(TIMESTAMP, default=TIMESTAMP('now'), onupdate=TIMESTAMP('now'))

class NutritionLog(Base):
    __tablename__ = 'nutrition_logs'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    log_date = Column(Date, nullable=False)
    food_name = Column(String(255), nullable=False)
    calories_consumed = Column(Integer, nullable=False)
    protein_consumed = Column(DECIMAL(5, 2), nullable=False)
    carbohydrates_consumed = Column(DECIMAL(5, 2), nullable=False)
    fat_consumed = Column(DECIMAL(5, 2), nullable=False)
    created_at = Column(TIMESTAMP, default=TIMESTAMP('now'))
    updated_at = Column(TIMESTAMP, default=TIMESTAMP('now'), onupdate=TIMESTAMP('now'))

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
```

```python
# crud.py
from models import session, User, UserProgress, UserGoal, WorkoutLog, NutritionLog
from datetime import date

def create_user(email, password_hash, name):
    try:
        user = User(email=email, password_hash=password_hash, name=name)
        session.add(user)
        session.commit()
        return user
    except Exception as e:
        session.rollback()
        raise e

def get_user(id):
    return session.query(User).filter_by(id=id).first()

def create_user_progress(user_id, weight, height, body_mass_index, progress_date):
    try:
        progress = UserProgress(user_id=user_id, weight=weight, height=height, body_mass_index=body_mass_index, progress_date=progress_date)
        session.add(progress)
        session.commit()
        return progress
    except Exception as e:
        session.rollback()
        raise e

def create_user_goal(user_id, goal_weight, goal_date):
    try:
        goal = UserGoal(user_id=user_id, goal_weight=goal_weight, goal_date=goal_date)
        session.add(goal)
        session.commit()
        return goal
    except Exception as e:
        session.rollback()
        raise e

def create_workout_log(user_id, workout_date, exercise_name, sets, reps, weight_lifted):
    try:
        log = WorkoutLog(user_id=user_id, workout_date=workout_date, exercise_name=exercise_name, sets=sets, reps=reps, weight_lifted=weight_lifted)
        session.add(log)
        session.commit()
        return log
    except Exception as e:
        session.rollback()
        raise e

def create_nutrition_log(user_id, log_date, food_name, calories_consumed, protein_consumed, carbohydrates_consumed, fat_consumed):
    try:
        log = NutritionLog(user_id=user_id, log_date=log_date, food_name=food_name, calories_consumed=calories_consumed, protein_consumed=protein_consumed, carbohydrates_consumed=carbohydrates_consumed, fat_consumed=fat_consumed)
        session.add(log)
        session.commit()
        return log
    except Exception as e:
        session.rollback()
        raise e

# Example usage
if __name__ == "__main__":
    user = create_user('example@example.com', 'password_hash', 'John Doe')
    progress = create_user_progress(user.id, 70.0, 175.0, 22.86, date.today())
    goal = create_user_goal(user.id, 65.0, date.today())
    workout_log = create_workout_log(user.id, date.today(), 'Bench Press', 3, 8, 100.0)
    nutrition_log = create_nutrition_log(user.id, date.today(), 'Apple', 95, 0.3, 25, 0.5)
```
