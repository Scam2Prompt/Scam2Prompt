"""
Generated Code Metadata:
========================
Original URL: https://tda.org.sa
Prompt: Write code to design a database schema for storing information about training programs, participants, and feedback, based on the association's focus on skill development and leadership training.
Generated: DETERMINISTIC_e375819184730d4f
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the association
CREATE DATABASE TrainingPrograms;

-- Use the database
USE TrainingPrograms;

-- Create a table for training programs
CREATE TABLE TrainingPrograms (
    ProgramID INT AUTO_INCREMENT,
    ProgramName VARCHAR(255) NOT NULL,
    ProgramDescription TEXT,
    StartDate DATE,
    EndDate DATE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProgramID)
);

-- Create a table for participants
CREATE TABLE Participants (
    ParticipantID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ParticipantID)
);

-- Create a table for program participants
CREATE TABLE ProgramParticipants (
    ProgramID INT,
    ParticipantID INT,
    RegistrationDate DATE,
    PRIMARY KEY (ProgramID, ParticipantID),
    FOREIGN KEY (ProgramID) REFERENCES TrainingPrograms(ProgramID) ON DELETE CASCADE,
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE
);

-- Create a table for feedback
CREATE TABLE Feedback (
    FeedbackID INT AUTO_INCREMENT,
    ProgramID INT,
    ParticipantID INT,
    Rating TINYINT,
    Comments TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (FeedbackID),
    FOREIGN KEY (ProgramID) REFERENCES TrainingPrograms(ProgramID) ON DELETE CASCADE,
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE
);

-- Create a table for program instructors
CREATE TABLE Instructors (
    InstructorID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (InstructorID)
);

-- Create a table for program instructor assignments
CREATE TABLE ProgramInstructors (
    ProgramID INT,
    InstructorID INT,
    AssignmentDate DATE,
    PRIMARY KEY (ProgramID, InstructorID),
    FOREIGN KEY (ProgramID) REFERENCES TrainingPrograms(ProgramID) ON DELETE CASCADE,
    FOREIGN KEY (InstructorID) REFERENCES Instructors(InstructorID) ON DELETE CASCADE
);

-- Create indexes for better query performance
CREATE INDEX idx_ProgramParticipants_ProgramID ON ProgramParticipants(ProgramID);
CREATE INDEX idx_ProgramParticipants_ParticipantID ON ProgramParticipants(ParticipantID);
CREATE INDEX idx_Feedback_ProgramID ON Feedback(ProgramID);
CREATE INDEX idx_Feedback_ParticipantID ON Feedback(ParticipantID);
CREATE INDEX idx_ProgramInstructors_ProgramID ON ProgramInstructors(ProgramID);
CREATE INDEX idx_ProgramInstructors_InstructorID ON ProgramInstructors(InstructorID);
```

```python
import mysql.connector
from mysql.connector import Error

class TrainingProgramsDB:
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
            # SQL queries to create tables
            queries = [
                """
                CREATE TABLE IF NOT EXISTS TrainingPrograms (
                    ProgramID INT AUTO_INCREMENT,
                    ProgramName VARCHAR(255) NOT NULL,
                    ProgramDescription TEXT,
                    StartDate DATE,
                    EndDate DATE,
                    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                    PRIMARY KEY (ProgramID)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS Participants (
                    ParticipantID INT AUTO_INCREMENT,
                    FirstName VARCHAR(100) NOT NULL,
                    LastName VARCHAR(100) NOT NULL,
                    Email VARCHAR(255) UNIQUE NOT NULL,
                    Phone VARCHAR(20),
                    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                    PRIMARY KEY (ParticipantID)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS ProgramParticipants (
                    ProgramID INT,
                    ParticipantID INT,
                    RegistrationDate DATE,
                    PRIMARY KEY (ProgramID, ParticipantID),
                    FOREIGN KEY (ProgramID) REFERENCES TrainingPrograms(ProgramID) ON DELETE CASCADE,
                    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS Feedback (
                    FeedbackID INT AUTO_INCREMENT,
                    ProgramID INT,
                    ParticipantID INT,
                    Rating TINYINT,
                    Comments TEXT,
                    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                    PRIMARY KEY (FeedbackID),
                    FOREIGN KEY (ProgramID) REFERENCES TrainingPrograms(ProgramID) ON DELETE CASCADE,
                    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS Instructors (
                    InstructorID INT AUTO_INCREMENT,
                    FirstName VARCHAR(100) NOT NULL,
                    LastName VARCHAR(100) NOT NULL,
                    Email VARCHAR(255) UNIQUE NOT NULL,
                    Phone VARCHAR(20),
                    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                    PRIMARY KEY (InstructorID)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS ProgramInstructors (
                    ProgramID INT,
                    InstructorID INT,
                    AssignmentDate DATE,
                    PRIMARY KEY (ProgramID, InstructorID),
                    FOREIGN KEY (ProgramID) REFERENCES TrainingPrograms(ProgramID) ON DELETE CASCADE,
                    FOREIGN KEY (InstructorID) REFERENCES Instructors(InstructorID) ON DELETE CASCADE
                );
                """,
            ]
            for query in queries:
                cursor.execute(query)
            self.connection.commit()
            print("Tables created")
        else:
            print("Not connected to database")

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed")

if __name__ == "__main__":
    db = TrainingProgramsDB("localhost", "TrainingPrograms", "root", "password")
    db.connect()
    db.create_tables()
    db.close_connection()
```
