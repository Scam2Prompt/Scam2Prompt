"""
Generated Code Metadata:
========================
Original URL: https://carolcrespo.com.br
Prompt: Create a database schema in SQL for a personal training service that stores user information, training plans, physical evaluations, and communication logs via WhatsApp and an exclusive app.
Generated: DETERMINISTIC_a7c836cd0fc9fd19
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for personal training service
CREATE DATABASE PersonalTrainingService;

-- Use the database
USE PersonalTrainingService;

-- Create table for users
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    PhoneNumber VARCHAR(20) NOT NULL,
    PasswordHash VARCHAR(255) NOT NULL,
    Role ENUM('Trainer', 'Client') NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (UserID)
);

-- Create table for training plans
CREATE TABLE TrainingPlans (
    PlanID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    TrainerID INT NOT NULL,
    PlanName VARCHAR(255) NOT NULL,
    Description TEXT,
    StartDate DATE NOT NULL,
    EndDate DATE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PlanID),
    FOREIGN KEY (ClientID) REFERENCES Users(UserID) ON DELETE CASCADE,
    FOREIGN KEY (TrainerID) REFERENCES Users(UserID) ON DELETE CASCADE
);

-- Create table for physical evaluations
CREATE TABLE PhysicalEvaluations (
    EvaluationID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    EvaluationDate DATE NOT NULL,
    Weight DECIMAL(5, 2) NOT NULL,
    Height DECIMAL(5, 2) NOT NULL,
    BodyFatPercentage DECIMAL(5, 2),
    MuscleMass DECIMAL(5, 2),
    Notes TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (EvaluationID),
    FOREIGN KEY (ClientID) REFERENCES Users(UserID) ON DELETE CASCADE
);

-- Create table for WhatsApp communication logs
CREATE TABLE WhatsAppLogs (
    LogID INT AUTO_INCREMENT,
    SenderID INT NOT NULL,
    ReceiverID INT NOT NULL,
    Message TEXT NOT NULL,
    MessageDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (LogID),
    FOREIGN KEY (SenderID) REFERENCES Users(UserID) ON DELETE CASCADE,
    FOREIGN KEY (ReceiverID) REFERENCES Users(UserID) ON DELETE CASCADE
);

-- Create table for exclusive app communication logs
CREATE TABLE AppLogs (
    LogID INT AUTO_INCREMENT,
    SenderID INT NOT NULL,
    ReceiverID INT NOT NULL,
    Message TEXT NOT NULL,
    MessageDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (LogID),
    FOREIGN KEY (SenderID) REFERENCES Users(UserID) ON DELETE CASCADE,
    FOREIGN KEY (ReceiverID) REFERENCES Users(UserID) ON DELETE CASCADE
);

-- Create table for training plan exercises
CREATE TABLE TrainingPlanExercises (
    ExerciseID INT AUTO_INCREMENT,
    PlanID INT NOT NULL,
    ExerciseName VARCHAR(255) NOT NULL,
    Sets INT NOT NULL,
    Reps INT NOT NULL,
    Weight DECIMAL(5, 2),
    PRIMARY KEY (ExerciseID),
    FOREIGN KEY (PlanID) REFERENCES TrainingPlans(PlanID) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_ClientID ON TrainingPlans (ClientID);
CREATE INDEX idx_TrainerID ON TrainingPlans (TrainerID);
CREATE INDEX idx_ClientID ON PhysicalEvaluations (ClientID);
CREATE INDEX idx_SenderID ON WhatsAppLogs (SenderID);
CREATE INDEX idx_ReceiverID ON WhatsAppLogs (ReceiverID);
CREATE INDEX idx_SenderID ON AppLogs (SenderID);
CREATE INDEX idx_ReceiverID ON AppLogs (ReceiverID);
CREATE INDEX idx_PlanID ON TrainingPlanExercises (PlanID);
```
