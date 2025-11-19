"""
Generated Code Metadata:
========================
Original URL: https://testul-poligraf.ro
Prompt: "Write a SQL query to retrieve polygraph test results for a specific client, including test dates, types, and outcomes, from a database."
Generated: DETERMINISTIC_815fd2bcc8931b07
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Retrieve polygraph test results for a specific client
-- ==============================================

-- Define the stored procedure
CREATE PROCEDURE sp_GetPolygraphTestResultsByClient
    @ClientId INT
AS
BEGIN
    -- Check if the client ID is valid
    IF @ClientId IS NULL OR @ClientId < 1
    BEGIN
        RAISERROR('Invalid client ID', 16, 1);
        RETURN;
    END

    -- Retrieve polygraph test results
    SELECT 
        pt.TestDate,
        pt.TestType,
        pt.Outcome,
        c.ClientName
    FROM 
        PolygraphTests pt
    INNER JOIN 
        Clients c ON pt.ClientId = c.ClientId
    WHERE 
        pt.ClientId = @ClientId
    ORDER BY 
        pt.TestDate DESC;
END
GO

-- Example usage
EXEC sp_GetPolygraphTestResultsByClient @ClientId = 1;
GO

-- Alternatively, you can use a SELECT statement directly
-- ==============================================

SELECT 
    pt.TestDate,
    pt.TestType,
    pt.Outcome,
    c.ClientName
FROM 
    PolygraphTests pt
INNER JOIN 
    Clients c ON pt.ClientId = c.ClientId
WHERE 
    pt.ClientId = @ClientId
ORDER BY 
    pt.TestDate DESC;
```

**Schema Assumptions:**

```sql
CREATE TABLE Clients (
    ClientId INT PRIMARY KEY,
    ClientName VARCHAR(255) NOT NULL
);

CREATE TABLE PolygraphTests (
    TestId INT PRIMARY KEY,
    ClientId INT NOT NULL,
    TestDate DATE NOT NULL,
    TestType VARCHAR(255) NOT NULL,
    Outcome VARCHAR(255) NOT NULL,
    FOREIGN KEY (ClientId) REFERENCES Clients(ClientId)
);
```
