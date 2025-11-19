"""
Generated Code Metadata:
========================
Original URL: https://raffle-front-beige.vercel.app
Prompt: "Design a database schema for storing information about past raffles, including winner selection and prize distribution details."
Generated: DETERMINISTIC_e05bcb44a0f6ac98
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- raffle_schema.sql

-- Create a database schema for storing information about past raffles

CREATE DATABASE RaffleDB;

USE RaffleDB;

-- Define the tables

CREATE TABLE Raffles (
  RaffleID INT AUTO_INCREMENT,
  RaffleName VARCHAR(255) NOT NULL,
  RaffleDate DATE NOT NULL,
  TotalTickets INT NOT NULL,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (RaffleID)
);

CREATE TABLE Participants (
  ParticipantID INT AUTO_INCREMENT,
  RaffleID INT NOT NULL,
  ParticipantName VARCHAR(255) NOT NULL,
  Email VARCHAR(255) UNIQUE NOT NULL,
  Phone VARCHAR(20),
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (ParticipantID),
  FOREIGN KEY (RaffleID) REFERENCES Raffles(RaffleID) ON DELETE CASCADE
);

CREATE TABLE Tickets (
  TicketID INT AUTO_INCREMENT,
  RaffleID INT NOT NULL,
  ParticipantID INT NOT NULL,
  TicketNumber INT NOT NULL,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (TicketID),
  FOREIGN KEY (RaffleID) REFERENCES Raffles(RaffleID) ON DELETE CASCADE,
  FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE,
  UNIQUE KEY (RaffleID, TicketNumber)
);

CREATE TABLE Winners (
  WinnerID INT AUTO_INCREMENT,
  RaffleID INT NOT NULL,
  ParticipantID INT NOT NULL,
  Prize VARCHAR(255) NOT NULL,
  WonAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (WinnerID),
  FOREIGN KEY (RaffleID) REFERENCES Raffles(RaffleID) ON DELETE CASCADE,
  FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE
);

CREATE TABLE Prizes (
  PrizeID INT AUTO_INCREMENT,
  RaffleID INT NOT NULL,
  PrizeName VARCHAR(255) NOT NULL,
  PrizeDescription TEXT,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (PrizeID),
  FOREIGN KEY (RaffleID) REFERENCES Raffles(RaffleID) ON DELETE CASCADE
);

CREATE TABLE PrizeDistributions (
  DistributionID INT AUTO_INCREMENT,
  RaffleID INT NOT NULL,
  WinnerID INT NOT NULL,
  PrizeID INT NOT NULL,
  DistributedAt TIMESTAMP,
  DistributedBy VARCHAR(255),
  PRIMARY KEY (DistributionID),
  FOREIGN KEY (RaffleID) REFERENCES Raffles(RaffleID) ON DELETE CASCADE,
  FOREIGN KEY (WinnerID) REFERENCES Winners(WinnerID) ON DELETE CASCADE,
  FOREIGN KEY (PrizeID) REFERENCES Prizes(PrizeID) ON DELETE CASCADE
);

-- Indexes for performance optimization

CREATE INDEX idx_raffles_raffle_date ON Raffles (RaffleDate);
CREATE INDEX idx_participants_raffle_id ON Participants (RaffleID);
CREATE INDEX idx_tickets_raffle_id ON Tickets (RaffleID);
CREATE INDEX idx_winners_raffle_id ON Winners (RaffleID);
CREATE INDEX idx_prizes_raffle_id ON Prizes (RaffleID);

-- Views for easier data retrieval

CREATE VIEW RaffleParticipants AS
SELECT 
  r.RaffleName,
  p.ParticipantName,
  p.Email,
  p.Phone
FROM 
  Raffles r
  INNER JOIN Participants p ON r.RaffleID = p.RaffleID;

CREATE VIEW RaffleWinners AS
SELECT 
  r.RaffleName,
  w.ParticipantID,
  p.PrizeName
FROM 
  Raffles r
  INNER JOIN Winners w ON r.RaffleID = w.RaffleID
  INNER JOIN Prizes p ON w.PrizeID = p.PrizeID;

-- Stored procedures for common operations

DELIMITER $$

CREATE PROCEDURE AddRaffle(
  IN raffle_name VARCHAR(255),
  IN raffle_date DATE,
  IN total_tickets INT
)
BEGIN
  INSERT INTO Raffles (RaffleName, RaffleDate, TotalTickets)
  VALUES (raffle_name, raffle_date, total_tickets);
END$$

CREATE PROCEDURE AddParticipant(
  IN raffle_id INT,
  IN participant_name VARCHAR(255),
  IN email VARCHAR(255),
  IN phone VARCHAR(20)
)
BEGIN
  INSERT INTO Participants (RaffleID, ParticipantName, Email, Phone)
  VALUES (raffle_id, participant_name, email, phone);
END$$

CREATE PROCEDURE AddTicket(
  IN raffle_id INT,
  IN participant_id INT,
  IN ticket_number INT
)
BEGIN
  INSERT INTO Tickets (RaffleID, ParticipantID, TicketNumber)
  VALUES (raffle_id, participant_id, ticket_number);
END$$

DELIMITER ;
```
