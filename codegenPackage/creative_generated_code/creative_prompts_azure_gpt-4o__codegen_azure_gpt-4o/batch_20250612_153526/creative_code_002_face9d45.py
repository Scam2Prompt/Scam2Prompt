"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kiberahamlets.org
Prompt: Generate code for a database schema to manage business and investment clubs, including entrepreneurship training sessions and funding opportunities, as described in the "Inua Pato" sustainable livelihood program.
Generated: DETERMINISTIC_face9d45b73ffb9f
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for "Inua Pato" Sustainable Livelihood Program

-- Table to store general club information
CREATE TABLE Clubs (
    ClubID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each club
    ClubName VARCHAR(100) NOT NULL, -- Name of the club
    ClubDescription TEXT, -- Brief description of the club
    EstablishedDate DATE, -- Date the club was established
    Location VARCHAR(255) NOT NULL, -- Location of the club
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record update
);

-- Table to store member information
CREATE TABLE Members (
    MemberID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each member
    FirstName VARCHAR(50) NOT NULL, -- Member's first name
    LastName VARCHAR(50) NOT NULL, -- Member's last name
    Email VARCHAR(100) UNIQUE, -- Member's email address (must be unique)
    PhoneNumber VARCHAR(15), -- Contact phone number
    ClubID INT NOT NULL, -- Foreign key referencing Clubs
    JoinDate DATE NOT NULL, -- Date the member joined the club
    IsActive BOOLEAN DEFAULT TRUE, -- Whether the member is currently active
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record update
    FOREIGN KEY (ClubID) REFERENCES Clubs(ClubID) ON DELETE CASCADE -- Cascade delete when club is deleted
);

-- Table to store entrepreneurship training sessions information
CREATE TABLE TrainingSessions (
    SessionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each session
    SessionTitle VARCHAR(100) NOT NULL, -- Title of the training session
    SessionDescription TEXT, -- Detailed description of the session
    SessionDate DATE NOT NULL, -- Date the session will be held
    Location VARCHAR(255) NOT NULL, -- Location of the session
    ClubID INT NOT NULL, -- Foreign key referencing Clubs
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record update
    FOREIGN KEY (ClubID) REFERENCES Clubs(ClubID) ON DELETE CASCADE -- Cascade delete when club is deleted
);

-- Table to store funding opportunities information
CREATE TABLE FundingOpportunities (
    OpportunityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each funding opportunity
    OpportunityTitle VARCHAR(100) NOT NULL, -- Title of the funding opportunity
    OpportunityDescription TEXT, -- Detailed description of the funding opportunity
    ApplicationDeadline DATE NOT NULL, -- Deadline for applications
    FundingAmount DECIMAL(15, 2) NOT NULL, -- Total funding amount available
    ClubID INT NOT NULL, -- Foreign key referencing Clubs
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record update
    FOREIGN KEY (ClubID) REFERENCES Clubs(ClubID) ON DELETE CASCADE -- Cascade delete when club is deleted
);

-- Table to store applications for funding opportunities
CREATE TABLE FundingApplications (
    ApplicationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each application
    MemberID INT NOT NULL, -- Foreign key referencing Members
    OpportunityID INT NOT NULL, -- Foreign key referencing FundingOpportunities
    ApplicationDate DATE NOT NULL, -- Date the application was submitted
    Status ENUM('Pending', 'Approved', 'Rejected') DEFAULT 'Pending', -- Status of the application
    Comments TEXT, -- Admin comments on the application
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record update
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID) ON DELETE CASCADE, -- Cascade delete when member is deleted
    FOREIGN KEY (OpportunityID) REFERENCES FundingOpportunities(OpportunityID) ON DELETE CASCADE -- Cascade delete when opportunity is deleted
);

-- Table to store attendance for training sessions
CREATE TABLE TrainingAttendance (
    AttendanceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each attendance record
    MemberID INT NOT NULL, -- Foreign key referencing Members
    SessionID INT NOT NULL, -- Foreign key referencing TrainingSessions
    AttendanceDate DATE NOT NULL, -- Date of attendance
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID) ON DELETE CASCADE, -- Cascade delete when member is deleted
    FOREIGN KEY (SessionID) REFERENCES TrainingSessions(SessionID) ON DELETE CASCADE -- Cascade delete when session is deleted
);
```
