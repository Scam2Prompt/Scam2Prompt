"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Design a database schema for managing client projects in a cosmetic manufacturing business, reflecting the full-service approach outlined by Fabricare Cosmeticos.
Generated: DETERMINISTIC_250a8f375eaeb49d
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing client projects in a cosmetic manufacturing business

-- Create a database for the cosmetic manufacturing business
CREATE DATABASE FabricareCosmeticos;

USE FabricareCosmeticos;

-- Table to store information about clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    ClientName VARCHAR(255) NOT NULL, -- Name of the client
    ContactEmail VARCHAR(255) UNIQUE NOT NULL, -- Email for client communication
    PhoneNumber VARCHAR(20), -- Optional phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL, -- Name of the product
    Description TEXT, -- Description of the product
    Price DECIMAL(10, 2) NOT NULL, -- Price of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store client projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL, -- Foreign key referencing the client
    ProjectName VARCHAR(255) NOT NULL, -- Name of the project
    StartDate DATE NOT NULL, -- Project start date
    EndDate DATE, -- Project end date
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Pending', -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time the project was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensures that projects are deleted if the client is deleted
);

-- Table to store project tasks
CREATE TABLE ProjectTasks (
    TaskID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each task
    ProjectID INT NOT NULL, -- Foreign key referencing the project
    TaskDescription TEXT NOT NULL, -- Description of the task
    AssignedTo VARCHAR(255), -- Person responsible for the task
    DueDate DATE, -- Due date for the task
    Status ENUM('Not Started', 'In Progress', 'Completed') NOT NULL DEFAULT 'Not Started', -- Current status of the task
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time the task was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensures that tasks are deleted if the project is deleted
);

-- Table to store product formulations
CREATE TABLE Formulations (
    FormulationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each formulation
    ProductID INT NOT NULL, -- Foreign key referencing the product
    Ingredients TEXT NOT NULL, -- List of ingredients used in the formulation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time the formulation was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures that formulations are deleted if the product is deleted
);

-- Table to store project feedback
CREATE TABLE Feedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each feedback entry
    ProjectID INT NOT NULL, -- Foreign key referencing the project
    ClientID INT NOT NULL, -- Foreign key referencing the client
    FeedbackText TEXT NOT NULL, -- Text for the feedback provided by the client
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating provided by the client (1 to 5)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time the feedback was created
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Ensures feedback is deleted if the project is deleted
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensures feedback is deleted if the client is deleted
);
```
