"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.khadamy.com
Prompt: Write SQL queries to store and retrieve service data for "تركيب زجاج سيكوريت" and "تلميع سيارات متنقل" by city, based on the services listed on https://www.khadamy.com.
Generated: DETERMINISTIC_bfd3187ba80e5813
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a table to store service data
CREATE TABLE ServiceData (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,
    ServiceName VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Insert sample data for "تركيب زجاج سيكوريت" service
INSERT INTO ServiceData (ServiceName, City, Description)
VALUES 
    ('تركيب زجاج سيكوريت', 'الرياض', 'خدمة تركيب زجاج سيكوريت بأعلى جودة'),
    ('تركيب زجاج سيكوريت', 'جدة', 'خدمة تركيب زجاج سيكوريت بدقة واحترافية'),
    ('تركيب زجاج سيكوريت', 'الدمام', 'خبراء تركيب زجاج سيكوريت في الدمام');

-- Insert sample data for "تلميع سيارات متنقل" service
INSERT INTO ServiceData (ServiceName, City, Description)
VALUES 
    ('تلميع سيارات متنقل', 'الرياض', 'خدمة تلميع سيارات متنقل لتوفير الوقت والجهد'),
    ('تلميع سيارات متنقل', 'جدة', 'أفضل خدمة تلميع سيارات متنقل في جدة'),
    ('تلميع سيارات متنقل', 'الدمام', 'تلميع سيارات متنقل عالي الجودة في الدمام');

-- Query to retrieve all services by city
SELECT * FROM ServiceData WHERE City = ?; -- Use parameterized query to prevent SQL injection

-- Query to retrieve specific service details by service name
SELECT * FROM ServiceData WHERE ServiceName = ? AND City = ?; -- Use parameterized query

-- Update service details
UPDATE ServiceData
SET Description = ?, UpdatedAt = CURRENT_TIMESTAMP
WHERE ServiceID = ?; -- Use parameterized query for parameters

-- Delete a service entry by ServiceID
DELETE FROM ServiceData
WHERE ServiceID = ?; -- Use parameterized query for parameters
```
