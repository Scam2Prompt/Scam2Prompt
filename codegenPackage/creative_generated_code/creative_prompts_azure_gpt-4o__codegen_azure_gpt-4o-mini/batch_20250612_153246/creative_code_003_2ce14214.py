"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sundancespasadvantage.com
Prompt: Write a SQL query to manage a database of dealers participating in the Sundance Spas Retail Advantage program, including columns for company name, location, showroom status, and training attendance.
Generated: DETERMINISTIC_2ce1421438ffb6cf
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to manage a database of dealers participating in the Sundance Spas Retail Advantage program

-- Create the table to store dealer information
CREATE TABLE Dealers (
    DealerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each dealer
    CompanyName VARCHAR(255) NOT NULL,        -- Name of the dealer company
    Location VARCHAR(255) NOT NULL,           -- Physical location of the dealer
    ShowroomStatus ENUM('Open', 'Closed') NOT NULL,  -- Status of the showroom
    TrainingAttendance BOOLEAN NOT NULL DEFAULT FALSE,  -- Attendance to training (true/false)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for last update
);

-- Insert sample data into the Dealers table
INSERT INTO Dealers (CompanyName, Location, ShowroomStatus, TrainingAttendance)
VALUES
    ('Sundance Spas of Denver', 'Denver, CO', 'Open', TRUE),
    ('Mountain Hot Tubs', 'Aspen, CO', 'Closed', FALSE),
    ('Lakeview Spas', 'Lake Tahoe, CA', 'Open', TRUE);

-- Function to update showroom status of a dealer
DELIMITER //

CREATE PROCEDURE UpdateShowroomStatus (
    IN p_DealerID INT,
    IN p_ShowroomStatus ENUM('Open', 'Closed')
)
BEGIN
    -- Update showroom status for the specified dealer
    UPDATE Dealers
    SET ShowroomStatus = p_ShowroomStatus,
        UpdatedAt = CURRENT_TIMESTAMP
    WHERE DealerID = p_DealerID;

    -- Check if the dealer exists
    IF ROW_COUNT() = 0 THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Dealer not found.';
    END IF;
END //

DELIMITER ;

-- Example of how to call the procedure to update showroom status
-- CALL UpdateShowroomStatus(1, 'Closed');

-- Function to retrieve all dealers
CREATE PROCEDURE GetAllDealers()
BEGIN
    SELECT * FROM Dealers;
END;

-- Example of how to call the procedure to get all dealers
-- CALL GetAllDealers();
```
