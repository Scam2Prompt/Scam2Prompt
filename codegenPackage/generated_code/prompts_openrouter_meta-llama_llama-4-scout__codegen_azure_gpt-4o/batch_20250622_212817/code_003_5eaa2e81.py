"""
Generated Code Metadata:
========================
Original URL: https://phantom-ss.com
Prompt: Design a database schema to store information about car audio systems, including components like amplifiers, speakers, and subwoofers, as described in the car's audio setup.
Generated: DETERMINISTIC_5eaa2e815ef7f158
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about car audio systems

-- Table to store information about car audio setups
CREATE TABLE CarAudioSetup (
    SetupID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each audio setup
    CarModel VARCHAR(100) NOT NULL,         -- Model of the car
    CarMake VARCHAR(100) NOT NULL,          -- Make of the car
    Year INT NOT NULL,                      -- Year of the car
    SetupName VARCHAR(100),                 -- Name or description of the audio setup
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the setup was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about amplifiers
CREATE TABLE Amplifiers (
    AmplifierID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each amplifier
    SetupID INT NOT NULL,                       -- Foreign key linking to CarAudioSetup
    Brand VARCHAR(100) NOT NULL,                -- Brand of the amplifier
    Model VARCHAR(100) NOT NULL,                -- Model of the amplifier
    PowerOutput INT NOT NULL,                   -- Power output in watts
    Channels INT NOT NULL,                      -- Number of channels
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the amplifier was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (SetupID) REFERENCES CarAudioSetup(SetupID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store information about speakers
CREATE TABLE Speakers (
    SpeakerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each speaker
    SetupID INT NOT NULL,                     -- Foreign key linking to CarAudioSetup
    Brand VARCHAR(100) NOT NULL,              -- Brand of the speaker
    Model VARCHAR(100) NOT NULL,              -- Model of the speaker
    Type ENUM('Coaxial', 'Component', 'Other') NOT NULL, -- Type of speaker
    Size DECIMAL(5,2) NOT NULL,               -- Size of the speaker in inches
    PowerHandling INT NOT NULL,               -- Power handling in watts
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the speaker was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (SetupID) REFERENCES CarAudioSetup(SetupID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store information about subwoofers
CREATE TABLE Subwoofers (
    SubwooferID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each subwoofer
    SetupID INT NOT NULL,                       -- Foreign key linking to CarAudioSetup
    Brand VARCHAR(100) NOT NULL,                -- Brand of the subwoofer
    Model VARCHAR(100) NOT NULL,                -- Model of the subwoofer
    Size DECIMAL(5,2) NOT NULL,                 -- Size of the subwoofer in inches
    PowerHandling INT NOT NULL,                 -- Power handling in watts
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the subwoofer was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (SetupID) REFERENCES CarAudioSetup(SetupID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store additional components in the audio setup
CREATE TABLE AdditionalComponents (
    ComponentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each component
    SetupID INT NOT NULL,                       -- Foreign key linking to CarAudioSetup
    ComponentType VARCHAR(100) NOT NULL,        -- Type of component (e.g., Equalizer, Processor)
    Brand VARCHAR(100) NOT NULL,                -- Brand of the component
    Model VARCHAR(100) NOT NULL,                -- Model of the component
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the component was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (SetupID) REFERENCES CarAudioSetup(SetupID) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for optimizing queries
CREATE INDEX idx_car_model ON CarAudioSetup(CarModel);
CREATE INDEX idx_amplifier_brand ON Amplifiers(Brand);
CREATE INDEX idx_speaker_brand ON Speakers(Brand);
CREATE INDEX idx_subwoofer_brand ON Subwoofers(Brand);
CREATE INDEX idx_component_type ON AdditionalComponents(ComponentType);
```
