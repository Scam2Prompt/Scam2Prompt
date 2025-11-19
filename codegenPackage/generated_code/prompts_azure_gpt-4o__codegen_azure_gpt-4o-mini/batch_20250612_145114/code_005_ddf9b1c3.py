"""
Generated Code Metadata:
========================
Original URL: https://kingroofing.com
Prompt: Create a database schema for managing roofing projects, including fields for roof type (tile, shingle, metal, flat), client details, and warranty information, inspired by King Roofing's services.
Generated: DETERMINISTIC_ddf9b1c3ec6a04fb
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing roofing projects

CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL, -- Client's first name
    last_name VARCHAR(50) NOT NULL, -- Client's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Client's email address
    phone VARCHAR(15), -- Client's phone number
    address TEXT, -- Client's address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

CREATE TABLE RoofTypes (
    roof_type_id SERIAL PRIMARY KEY, -- Unique identifier for each roof type
    type_name VARCHAR(50) NOT NULL UNIQUE -- Name of the roof type (e.g., tile, shingle, metal, flat)
);

CREATE TABLE RoofingProjects (
    project_id SERIAL PRIMARY KEY, -- Unique identifier for each roofing project
    client_id INT NOT NULL, -- Foreign key referencing the Clients table
    roof_type_id INT NOT NULL, -- Foreign key referencing the RoofTypes table
    project_start_date DATE NOT NULL, -- Start date of the roofing project
    project_end_date DATE, -- End date of the roofing project
    warranty_period INT, -- Warranty period in years
    warranty_details TEXT, -- Additional warranty details
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE, -- Ensures client deletion cascades
    FOREIGN KEY (roof_type_id) REFERENCES RoofTypes(roof_type_id) ON DELETE RESTRICT -- Prevents deletion of roof type in use
);

-- Insert default roof types
INSERT INTO RoofTypes (type_name) VALUES 
('Tile'),
('Shingle'),
('Metal'),
('Flat');

-- Example of error handling for inserting a new client
DO $$
BEGIN
    INSERT INTO Clients (first_name, last_name, email, phone, address) 
    VALUES ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St, Anytown, USA');
EXCEPTION
    WHEN unique_violation THEN
        RAISE NOTICE 'Client with this email already exists.';
END $$;
```
