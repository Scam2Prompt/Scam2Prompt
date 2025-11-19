"""
Generated Code Metadata:
========================
Original URL: https://www.gardenpathquilts.com
Prompt: Design a database schema for storing quilt designs, including fields for quilt type, dimensions, and fabric requirements.
Generated: DETERMINISTIC_c019d709317c3838
Batch ID: 20250622_212844
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing quilt designs

CREATE TABLE QuiltDesigns (
    QuiltID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each quilt design
    QuiltType VARCHAR(100) NOT NULL,         -- Type of quilt (e.g., patchwork, applique)
    Dimensions VARCHAR(50) NOT NULL,         -- Dimensions of the quilt (e.g., "60x80 inches")
    FabricRequirements TEXT NOT NULL,         -- Description of fabric requirements (e.g., "5 yards of cotton fabric")
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the quilt design was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of the last update
    CONSTRAINT chk_dimensions CHECK (Dimensions REGEXP '^[0-9]+x[0-9]+ inches$')  -- Ensure dimensions follow the format "NxM inches"
);

-- Index for faster querying by QuiltType
CREATE INDEX idx_quilt_type ON QuiltDesigns (QuiltType);

-- Sample insert statement for testing
INSERT INTO QuiltDesigns (QuiltType, Dimensions, FabricRequirements) 
VALUES ('Patchwork', '60x80 inches', '5 yards of cotton fabric');

-- Error handling for insertions (example)
DELIMITER //
CREATE PROCEDURE AddQuiltDesign(
    IN p_QuiltType VARCHAR(100),
    IN p_Dimensions VARCHAR(50),
    IN p_FabricRequirements TEXT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Handle the error (e.g., log it, return a message)
        SELECT 'Error occurred while adding quilt design.' AS ErrorMessage;
    END;

    INSERT INTO QuiltDesigns (QuiltType, Dimensions, FabricRequirements)
    VALUES (p_QuiltType, p_Dimensions, p_FabricRequirements);
END //
DELIMITER ;

-- Example of calling the procedure
CALL AddQuiltDesign('Applique', '50x70 inches', '3 yards of cotton fabric');
```
