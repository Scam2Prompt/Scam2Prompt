"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kingroofing.com
Prompt: Create a database schema for managing roofing projects, including fields for roof type (tile, shingle, metal, flat), client details, and warranty information, inspired by King Roofing's services.
Generated: DETERMINISTIC_ddf9b1c3ec6a04fb
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing roofing projects
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY,  -- Unique identifier for each client
    name VARCHAR(100) NOT NULL,     -- Client's name
    phone VARCHAR(15) NULL,         -- Client's phone number
    email VARCHAR(100) UNIQUE NULL, -- Client's email address
    address VARCHAR(255) NULL,      -- Client's address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Record creation timestamp
);

CREATE TABLE RoofTypes (
    roof_type_id SERIAL PRIMARY KEY, -- Unique identifier for each roof type
    type_name VARCHAR(50) NOT NULL UNIQUE -- Name of the roof type (e.g., tile, shingle)
);

-- Insert default roof types into the RoofTypes table
INSERT INTO RoofTypes (type_name) VALUES 
('Tile'), 
('Shingle'), 
('Metal'), 
('Flat');

CREATE TABLE RoofingProjects (
    project_id SERIAL PRIMARY KEY,            -- Unique identifier for each roofing project
    client_id INT NOT NULL REFERENCES Clients(client_id) ON DELETE CASCADE, -- Foreign key to Clients
    roof_type_id INT NOT NULL REFERENCES RoofTypes(roof_type_id) ON DELETE CASCADE, -- Foreign key to RoofTypes
    project_description TEXT NULL,            -- Description of the roofing project
    start_date DATE NOT NULL,                 -- Project start date
    end_date DATE NULL,                       -- Project end date
    warranty_period INT NOT NULL,             -- Warranty period in years
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Ensure we handle any potential errors during the insertions
DO $$
BEGIN
    -- Example of inserting a client
    INSERT INTO Clients (name, phone, email, address)
    VALUES ('John Doe', '555-1234', 'john.doe@example.com', '123 Elm St, Springfield')
    ON CONFLICT (email) DO NOTHING;  -- Handle duplicate email entry

    -- Example of inserting a project
    INSERT INTO RoofingProjects (client_id, roof_type_id, project_description, start_date, warranty_period)
    VALUES (1, 1, 'Tile roofing installation', '2023-10-01', 10)
    ON CONFLICT (project_id) DO NOTHING;  -- Handle duplicate project entry
EXCEPTION
    WHEN unique_violation THEN
        RAISE NOTICE 'A project or client with the same details already exists.';
    WHEN OTHERS THEN
        RAISE ERROR 'An unexpected error occurred: %', SQLERRM;
END $$;
```
