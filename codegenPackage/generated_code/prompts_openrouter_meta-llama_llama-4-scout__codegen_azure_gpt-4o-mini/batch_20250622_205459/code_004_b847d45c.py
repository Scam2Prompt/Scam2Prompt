"""
Generated Code Metadata:
========================
Original URL: https://nicerfoundation.org.ng
Prompt: Design a database schema to store information about donors, volunteers, and programs for an organization like the NICER Foundation, including fields for tracking engagement and impact.
Generated: DETERMINISTIC_b847d45c4338ca27
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for NICER Foundation

-- Table to store information about donors
CREATE TABLE Donors (
    donor_id SERIAL PRIMARY KEY, -- Unique identifier for each donor
    first_name VARCHAR(100) NOT NULL, -- Donor's first name
    last_name VARCHAR(100) NOT NULL, -- Donor's last name
    email VARCHAR(255) UNIQUE NOT NULL, -- Donor's email address
    phone VARCHAR(15), -- Donor's phone number
    address TEXT, -- Donor's address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about volunteers
CREATE TABLE Volunteers (
    volunteer_id SERIAL PRIMARY KEY, -- Unique identifier for each volunteer
    first_name VARCHAR(100) NOT NULL, -- Volunteer’s first name
    last_name VARCHAR(100) NOT NULL, -- Volunteer’s last name
    email VARCHAR(255) UNIQUE NOT NULL, -- Volunteer’s email address
    phone VARCHAR(15), -- Volunteer’s phone number
    skills TEXT, -- Skills of the volunteer
    availability TEXT, -- Availability of the volunteer
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about programs
CREATE TABLE Programs (
    program_id SERIAL PRIMARY KEY, -- Unique identifier for each program
    name VARCHAR(255) NOT NULL, -- Name of the program
    description TEXT, -- Description of the program
    start_date DATE NOT NULL, -- Start date of the program
    end_date DATE NOT NULL, -- End date of the program
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to track donor engagement with programs
CREATE TABLE DonorEngagement (
    engagement_id SERIAL PRIMARY KEY, -- Unique identifier for each engagement
    donor_id INT NOT NULL, -- Foreign key referencing Donors
    program_id INT NOT NULL, -- Foreign key referencing Programs
    donation_amount DECIMAL(10, 2) NOT NULL, -- Amount donated
    engagement_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of engagement
    FOREIGN KEY (donor_id) REFERENCES Donors(donor_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (program_id) REFERENCES Programs(program_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to track volunteer participation in programs
CREATE TABLE VolunteerParticipation (
    participation_id SERIAL PRIMARY KEY, -- Unique identifier for each participation
    volunteer_id INT NOT NULL, -- Foreign key referencing Volunteers
    program_id INT NOT NULL, -- Foreign key referencing Programs
    hours_contributed DECIMAL(5, 2) NOT NULL, -- Hours contributed by the volunteer
    participation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of participation
    FOREIGN KEY (volunteer_id) REFERENCES Volunteers(volunteer_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (program_id) REFERENCES Programs(program_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to track the impact of programs
CREATE TABLE ProgramImpact (
    impact_id SERIAL PRIMARY KEY, -- Unique identifier for each impact record
    program_id INT NOT NULL, -- Foreign key referencing Programs
    impact_description TEXT, -- Description of the impact
    impact_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of impact assessment
    FOREIGN KEY (program_id) REFERENCES Programs(program_id) ON DELETE CASCADE -- Ensures referential integrity
);
```
