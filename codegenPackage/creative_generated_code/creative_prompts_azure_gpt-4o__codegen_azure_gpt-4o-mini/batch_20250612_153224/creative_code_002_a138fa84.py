"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://auqualhairservices.com
Prompt: Create a database schema for storing hair transplant results, including fields for graft count, cost, session duration, and before-and-after images, based on the services offered by Auqual Hair Services.
Generated: DETERMINISTIC_a138fa84546d24a7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing hair transplant results
CREATE TABLE HairTransplantResults (
    id SERIAL PRIMARY KEY,                       -- Unique identifier for each result entry
    graft_count INT NOT NULL,                    -- Number of grafts used in the transplant
    cost DECIMAL(10, 2) NOT NULL,                -- Cost of the hair transplant session
    session_duration INTERVAL NOT NULL,          -- Duration of the transplant session
    before_image_url VARCHAR(255) NOT NULL,     -- URL for before image
    after_image_url VARCHAR(255) NOT NULL,      -- URL for after image
    patient_id INT NOT NULL,                     -- Linking to the patient, assuming there's a Patient table
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp

    -- Foreign key constraint to link to the Patient table
    FOREIGN KEY (patient_id) REFERENCES Patients(id) ON DELETE CASCADE
);

-- Index to improve performance on frequently queried fields
CREATE INDEX idx_graft_count ON HairTransplantResults(graft_count);
CREATE INDEX idx_cost ON HairTransplantResults(cost);
CREATE INDEX idx_created_at ON HairTransplantResults(created_at);
```
