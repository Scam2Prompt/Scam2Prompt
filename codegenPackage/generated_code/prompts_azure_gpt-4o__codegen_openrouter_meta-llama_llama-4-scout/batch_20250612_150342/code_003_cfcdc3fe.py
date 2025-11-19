"""
Generated Code Metadata:
========================
Original URL: https://taiko-t.com
Prompt: Suggest a database schema for tracking construction projects, including details like pole installation, electrical civil engineering tasks, and fence construction, inspired by the services of 株式会社タイコーテクノ.
Generated: DETERMINISTIC_cfcdc3fe0ee968b2
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- construction_projects database schema

CREATE TABLE Clients (
  ClientID INT AUTO_INCREMENT,
  CompanyName VARCHAR(255) NOT NULL,
  ContactPerson VARCHAR(100) NOT NULL,
  Email VARCHAR(100) NOT NULL,
  Phone VARCHAR(20) NOT NULL,
  Address VARCHAR(255) NOT NULL,
  PRIMARY KEY (ClientID)
);

CREATE TABLE Projects (
  ProjectID INT AUTO_INCREMENT,
  ClientID INT NOT NULL,
  ProjectName VARCHAR(255) NOT NULL,
  ProjectDescription TEXT,
  StartDate DATE NOT NULL,
  EndDate DATE,
  Status ENUM('ongoing', 'completed', 'cancelled') NOT NULL DEFAULT 'ongoing',
  PRIMARY KEY (ProjectID),
  FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
);

CREATE TABLE PoleInstallations (
  InstallationID INT AUTO_INCREMENT,
  ProjectID INT NOT NULL,
  PoleType ENUM('wooden', 'metal', 'concrete') NOT NULL,
  PoleHeight DECIMAL(5, 2) NOT NULL,
  InstallationDate DATE NOT NULL,
  PRIMARY KEY (InstallationID),
  FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID)
);

CREATE TABLE ElectricalCivilEngineeringTasks (
  TaskID INT AUTO_INCREMENT,
  ProjectID INT NOT NULL,
  TaskType ENUM('excavation', 'concrete pour', 'wiring') NOT NULL,
  TaskDescription TEXT,
  StartDate DATE NOT NULL,
  EndDate DATE,
  Status ENUM('ongoing', 'completed') NOT NULL DEFAULT 'ongoing',
  PRIMARY KEY (TaskID),
  FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID)
);

CREATE TABLE FenceConstructions (
  FenceID INT AUTO_INCREMENT,
  ProjectID INT NOT NULL,
  FenceType ENUM('wooden', 'metal', 'vinyl') NOT NULL,
  FenceLength DECIMAL(10, 2) NOT NULL,
  ConstructionDate DATE NOT NULL,
  PRIMARY KEY (FenceID),
  FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID)
);

CREATE TABLE Workers (
  WorkerID INT AUTO_INCREMENT,
  FirstName VARCHAR(50) NOT NULL,
  LastName VARCHAR(50) NOT NULL,
  Email VARCHAR(100) NOT NULL,
  Phone VARCHAR(20) NOT NULL,
  Role ENUM('engineer', 'technician', 'laborer') NOT NULL,
  PRIMARY KEY (WorkerID)
);

CREATE TABLE ProjectAssignments (
  ProjectID INT NOT NULL,
  WorkerID INT NOT NULL,
  AssignmentDate DATE NOT NULL,
  PRIMARY KEY (ProjectID, WorkerID),
  FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID),
  FOREIGN KEY (WorkerID) REFERENCES Workers(WorkerID)
);

CREATE TABLE Materials (
  MaterialID INT AUTO_INCREMENT,
  MaterialName VARCHAR(100) NOT NULL,
  MaterialType ENUM('wood', 'metal', 'concrete') NOT NULL,
  Quantity DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (MaterialID)
);

CREATE TABLE ProjectMaterials (
  ProjectID INT NOT NULL,
  MaterialID INT NOT NULL,
  QuantityUsed DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (ProjectID, MaterialID),
  FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID),
  FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID)
);

DELIMITER //
CREATE TRIGGER UpdateProjectStatus
BEFORE UPDATE ON PoleInstallations
FOR EACH ROW
BEGIN
  IF NEW.InstallationDate IS NOT NULL AND NEW.InstallationDate >= CURDATE() THEN
    UPDATE Projects
    SET Status = 'ongoing'
    WHERE ProjectID = NEW.ProjectID;
  ELSEIF NEW.InstallationDate IS NOT NULL AND NEW.InstallationDate < CURDATE() THEN
    UPDATE Projects
    SET Status = 'completed'
    WHERE ProjectID = NEW.ProjectID;
  END IF;
END;//
DELIMITER ;

DELIMITER //
CREATE TRIGGER UpdateTaskStatus
BEFORE UPDATE ON ElectricalCivilEngineeringTasks
FOR EACH ROW
BEGIN
  IF NEW.EndDate IS NOT NULL AND NEW.EndDate >= CURDATE() THEN
    UPDATE ElectricalCivilEngineeringTasks
    SET Status = 'ongoing'
    WHERE TaskID = NEW.TaskID;
  ELSEIF NEW.EndDate IS NOT NULL AND NEW.EndDate < CURDATE() THEN
    UPDATE ElectricalCivilEngineeringTasks
    SET Status = 'completed'
    WHERE TaskID = NEW.TaskID;
  END IF;
END;//
DELIMITER ;
```
