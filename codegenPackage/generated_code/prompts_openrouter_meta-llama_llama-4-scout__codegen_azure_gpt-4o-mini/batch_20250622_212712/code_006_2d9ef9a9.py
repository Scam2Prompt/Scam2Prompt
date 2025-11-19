"""
Generated Code Metadata:
========================
Original URL: https://nassauccw.com
Prompt: Design a database schema to store information about CCW permit applicants and their application status, inspired by the services offered by Trigon Tactics for managing the application process.
Generated: DETERMINISTIC_2d9ef9a9f8466020
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for CCW Permit Applicants

-- Create a table to store information about applicants
CREATE TABLE Applicants (
    applicant_id SERIAL PRIMARY KEY, -- Unique identifier for each applicant
    first_name VARCHAR(50) NOT NULL, -- Applicant's first name
    last_name VARCHAR(50) NOT NULL, -- Applicant's last name
    date_of_birth DATE NOT NULL, -- Applicant's date of birth
    address VARCHAR(255) NOT NULL, -- Applicant's residential address
    city VARCHAR(50) NOT NULL, -- City of residence
    state VARCHAR(50) NOT NULL, -- State of residence
    zip_code VARCHAR(10) NOT NULL, -- Zip code of residence
    phone_number VARCHAR(15), -- Applicant's phone number
    email VARCHAR(100), -- Applicant's email address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store application statuses
CREATE TABLE ApplicationStatuses (
    status_id SERIAL PRIMARY KEY, -- Unique identifier for each status
    status_name VARCHAR(50) NOT NULL UNIQUE -- Name of the application status (e.g., 'Pending', 'Approved', 'Denied')
);

-- Create a table to store applications linked to applicants
CREATE TABLE Applications (
    application_id SERIAL PRIMARY KEY, -- Unique identifier for each application
    applicant_id INT NOT NULL, -- Foreign key referencing the applicant
    status_id INT NOT NULL, -- Foreign key referencing the application status
    application_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the application was submitted
    review_date TIMESTAMP, -- Date when the application was reviewed
    notes TEXT, -- Additional notes regarding the application
    FOREIGN KEY (applicant_id) REFERENCES Applicants(applicant_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (status_id) REFERENCES ApplicationStatuses(status_id) ON DELETE RESTRICT -- Ensures referential integrity
);

-- Insert initial application statuses
INSERT INTO ApplicationStatuses (status_name) VALUES
('Pending'),
('Approved'),
('Denied'),
('Under Review'),
('Withdrawn');

-- Example of a function to safely insert a new applicant
CREATE OR REPLACE FUNCTION add_applicant(
    p_first_name VARCHAR,
    p_last_name VARCHAR,
    p_date_of_birth DATE,
    p_address VARCHAR,
    p_city VARCHAR,
    p_state VARCHAR,
    p_zip_code VARCHAR,
    p_phone_number VARCHAR DEFAULT NULL,
    p_email VARCHAR DEFAULT NULL
) RETURNS VOID AS $$
BEGIN
    INSERT INTO Applicants (first_name, last_name, date_of_birth, address, city, state, zip_code, phone_number, email)
    VALUES (p_first_name, p_last_name, p_date_of_birth, p_address, p_city, p_state, p_zip_code, p_phone_number, p_email);
EXCEPTION
    WHEN unique_violation THEN
        RAISE NOTICE 'Applicant with the same details already exists.';
    WHEN OTHERS THEN
        RAISE EXCEPTION 'An error occurred while adding the applicant: %', SQLERRM;
END;
$$ LANGUAGE plpgsql;

-- Example of a function to update application status
CREATE OR REPLACE FUNCTION update_application_status(
    p_application_id INT,
    p_status_id INT
) RETURNS VOID AS $$
BEGIN
    UPDATE Applications
    SET status_id = p_status_id, review_date = CURRENT_TIMESTAMP
    WHERE application_id = p_application_id;
    
    IF NOT FOUND THEN
        RAISE EXCEPTION 'Application ID % not found.', p_application_id;
    END IF;
EXCEPTION
    WHEN OTHERS THEN
        RAISE EXCEPTION 'An error occurred while updating the application status: %', SQLERRM;
END;
$$ LANGUAGE plpgsql;
```
