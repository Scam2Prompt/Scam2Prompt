"""
Generated Code Metadata:
========================
Original URL: https://simice-tec-elevators.cz
Prompt: "Design a database schema to store information about elevator modernization projects, including details about replaced parts, such as COP/LOP panels with VEGA touchscreens, and upgrades to open protocol controls from Beta Control."
Generated: DETERMINISTIC_cae88eda6725c29e
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for elevator modernization projects

CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT,
    ProjectName VARCHAR(255) NOT NULL,
    ProjectDescription TEXT,
    StartDate DATE,
    EndDate DATE,
    PRIMARY KEY (ProjectID)
);

CREATE TABLE ReplacedParts (
    PartID INT AUTO_INCREMENT,
    ProjectID INT,
    PartName VARCHAR(255) NOT NULL,
    PartDescription TEXT,
    ReplacementDate DATE,
    PRIMARY KEY (PartID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID)
);

CREATE TABLE COP_LOP_Panels (
    PanelID INT AUTO_INCREMENT,
    PartID INT,
    ScreenType VARCHAR(100),
    ScreenModel VARCHAR(100),
    InstallationDate DATE,
    PRIMARY KEY (PanelID),
    FOREIGN KEY (PartID) REFERENCES ReplacedParts(PartID)
);

CREATE TABLE VEGA_Touchscreens (
    TouchscreenID INT AUTO_INCREMENT,
    PanelID INT,
    TouchscreenModel VARCHAR(100),
    InstallationDate DATE,
    PRIMARY KEY (TouchscreenID),
    FOREIGN KEY (PanelID) REFERENCES COP_LOP_Panels(PanelID)
);

CREATE TABLE ControlUpgrades (
    UpgradeID INT AUTO_INCREMENT,
    ProjectID INT,
    ControlType VARCHAR(100) NOT NULL,
    OldControlModel VARCHAR(100),
    NewControlModel VARCHAR(100),
    UpgradeDate DATE,
    PRIMARY KEY (UpgradeID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID)
);

CREATE TABLE Open_Protocol_Controls (
    ControlID INT AUTO_INCREMENT,
    UpgradeID INT,
    ControlModel VARCHAR(100) NOT NULL,
    FirmwareVersion VARCHAR(100),
    InstallationDate DATE,
    PRIMARY KEY (ControlID),
    FOREIGN KEY (UpgradeID) REFERENCES ControlUpgrades(UpgradeID)
);

CREATE TABLE Beta_Control_Upgrades (
    BetaUpgradeID INT AUTO_INCREMENT,
    ControlID INT,
    OldFirmwareVersion VARCHAR(100),
    NewFirmwareVersion VARCHAR(100),
    UpgradeDate DATE,
    PRIMARY KEY (BetaUpgradeID),
    FOREIGN KEY (ControlID) REFERENCES Open_Protocol_Controls(ControlID)
);

-- Insert sample data
INSERT INTO Projects (ProjectName, ProjectDescription, StartDate, EndDate)
VALUES 
('Elevator Modernization Project 1', 'Modernization of elevator 1', '2022-01-01', '2022-06-01'),
('Elevator Modernization Project 2', 'Modernization of elevator 2', '2022-07-01', '2022-12-01');

INSERT INTO ReplacedParts (ProjectID, PartName, PartDescription, ReplacementDate)
VALUES 
(1, 'COP Panel', 'Replaced COP panel with VEGA touchscreen', '2022-02-01'),
(1, 'LOP Panel', 'Replaced LOP panel with VEGA touchscreen', '2022-03-01'),
(2, 'COP Panel', 'Replaced COP panel with VEGA touchscreen', '2022-08-01');

INSERT INTO COP_LOP_Panels (PartID, ScreenType, ScreenModel, InstallationDate)
VALUES 
(1, 'COP', 'VEGA-100', '2022-02-01'),
(2, 'LOP', 'VEGA-200', '2022-03-01'),
(3, 'COP', 'VEGA-100', '2022-08-01');

INSERT INTO VEGA_Touchscreens (PanelID, TouchscreenModel, InstallationDate)
VALUES 
(1, 'VEGA-TS-100', '2022-02-01'),
(2, 'VEGA-TS-200', '2022-03-01'),
(3, 'VEGA-TS-100', '2022-08-01');

INSERT INTO ControlUpgrades (ProjectID, ControlType, OldControlModel, NewControlModel, UpgradeDate)
VALUES 
(1, 'Open Protocol Control', 'Beta Control 1.0', 'Open Protocol Control 2.0', '2022-04-01'),
(2, 'Open Protocol Control', 'Beta Control 1.0', 'Open Protocol Control 2.0', '2022-09-01');

INSERT INTO Open_Protocol_Controls (UpgradeID, ControlModel, FirmwareVersion, InstallationDate)
VALUES 
(1, 'Open Protocol Control 2.0', 'FW 1.0', '2022-04-01'),
(2, 'Open Protocol Control 2.0', 'FW 1.0', '2022-09-01');

INSERT INTO Beta_Control_Upgrades (ControlID, OldFirmwareVersion, NewFirmwareVersion, UpgradeDate)
VALUES 
(1, 'FW 0.9', 'FW 1.0', '2022-04-01'),
(2, 'FW 0.9', 'FW 1.0', '2022-09-01');

-- Query to retrieve all project information
SELECT 
    p.ProjectName, 
    p.ProjectDescription, 
    rp.PartName, 
    c.COP_LOP_Panels,
    v.VEGA_Touchscreens,
    cu.ControlType, 
    opc.ControlModel
FROM 
    Projects p
JOIN 
    ReplacedParts rp ON p.ProjectID = rp.ProjectID
LEFT JOIN 
    (SELECT PartID, ScreenType, ScreenModel FROM COP_LOP_Panels) c ON rp.PartID = c.PartID
LEFT JOIN 
    (SELECT PanelID, TouchscreenModel FROM VEGA_Touchscreens) v ON c.PanelID = v.PanelID
LEFT JOIN 
    ControlUpgrades cu ON p.ProjectID = cu.ProjectID
LEFT JOIN 
    Open_Protocol_Controls opc ON cu.UpgradeID = opc.UpgradeID;
```
