"""
Generated Code Metadata:
========================
Original URL: https://enafo.cl
Prompt: Create a database schema for storing information about ENAFO's academic programs, including monitorías, modules, and seasonal offerings, along with student enrollment details.
Generated: DETERMINISTIC_af057e70c64c2fc8
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for ENAFO academic programs

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Programs table
CREATE TABLE programs (
    program_id INTEGER PRIMARY KEY AUTOINCREMENT,
    program_name TEXT NOT NULL,
    description TEXT,
    duration_months INTEGER,
    degree_awarded TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Modules table
CREATE TABLE modules (
    module_id INTEGER PRIMARY KEY AUTOINCREMENT,
    program_id INTEGER NOT NULL,
    module_name TEXT NOT NULL,
    module_code TEXT UNIQUE NOT NULL,
    description TEXT,
    credits INTEGER,
    duration_weeks INTEGER,
    is_core BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE
);

-- Seasons table (e.g., Fall 2023, Spring 2024)
CREATE TABLE seasons (
    season_id INTEGER PRIMARY KEY AUTOINCREMENT,
    season_name TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    is_current BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_dates CHECK (start_date < end_date)
);

-- Module offerings per season
CREATE TABLE module_offerings (
    offering_id INTEGER PRIMARY KEY AUTOINCREMENT,
    module_id INTEGER NOT NULL,
    season_id INTEGER NOT NULL,
    instructor_name TEXT,
    schedule_info TEXT,
    classroom TEXT,
    max_capacity INTEGER,
    current_enrollment INTEGER DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (module_id) REFERENCES modules(module_id) ON DELETE CASCADE,
    FOREIGN KEY (season_id) REFERENCES seasons(season_id) ON DELETE CASCADE,
    CONSTRAINT unique_offering UNIQUE (module_id, season_id),
    CONSTRAINT valid_capacity CHECK (current_enrollment <= max_capacity)
);

-- Monitorías (tutoring sessions) table
CREATE TABLE monitorias (
    monitoria_id INTEGER PRIMARY KEY AUTOINCREMENT,
    offering_id INTEGER NOT NULL,
    monitor_name TEXT NOT NULL,
    schedule_info TEXT NOT NULL,
    location TEXT,
    max_attendees INTEGER,
    current_attendees INTEGER DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (offering_id) REFERENCES module_offerings(offering_id) ON DELETE CASCADE,
    CONSTRAINT valid_attendees CHECK (current_attendees <= max_attendees)
);

-- Students table
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    enrollment_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Student enrollments in programs
CREATE TABLE program_enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    program_id INTEGER NOT NULL,
    enrollment_date DATE NOT NULL,
    completion_date DATE,
    status TEXT CHECK(status IN ('active', 'completed', 'withdrawn', 'suspended')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE,
    CONSTRAINT unique_enrollment UNIQUE (student_id, program_id)
);

-- Student registrations for module offerings
CREATE TABLE module_registrations (
    registration_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    offering_id INTEGER NOT NULL,
    registration_date DATE NOT NULL,
    grade TEXT,
    status TEXT CHECK(status IN ('registered', 'completed', 'dropped', 'failed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (offering_id) REFERENCES module_offerings(offering_id) ON DELETE CASCADE,
    CONSTRAINT unique_registration UNIQUE (student_id, offering_id)
);

-- Student attendance at monitorías
CREATE TABLE monitoria_attendance (
    attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    monitoria_id INTEGER NOT NULL,
    attendance_date DATE NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (monitoria_id) REFERENCES monitorias(monitoria_id) ON DELETE CASCADE,
    CONSTRAINT unique_attendance UNIQUE (student_id, monitoria_id, attendance_date)
);

-- Triggers for automatic timestamp updates
CREATE TRIGGER update_program_timestamp
AFTER UPDATE ON programs
FOR EACH ROW
BEGIN
    UPDATE programs SET updated_at = CURRENT_TIMESTAMP WHERE program_id = OLD.program_id;
END;

CREATE TRIGGER update_module_timestamp
AFTER UPDATE ON modules
FOR EACH ROW
BEGIN
    UPDATE modules SET updated_at = CURRENT_TIMESTAMP WHERE module_id = OLD.module_id;
END;

CREATE TRIGGER update_season_timestamp
AFTER UPDATE ON seasons
FOR EACH ROW
BEGIN
    UPDATE seasons SET updated_at = CURRENT_TIMESTAMP WHERE season_id = OLD.season_id;
END;

CREATE TRIGGER update_offering_timestamp
AFTER UPDATE ON module_offerings
FOR EACH ROW
BEGIN
    UPDATE module_offerings SET updated_at = CURRENT_TIMESTAMP WHERE offering_id = OLD.offering_id;
END;

CREATE TRIGGER update_monitoria_timestamp
AFTER UPDATE ON monitorias
FOR EACH ROW
BEGIN
    UPDATE monitorias SET updated_at = CURRENT_TIMESTAMP WHERE monitoria_id = OLD.monitoria_id;
END;

CREATE TRIGGER update_student_timestamp
AFTER UPDATE ON students
FOR EACH ROW
BEGIN
    UPDATE students SET updated_at = CURRENT_TIMESTAMP WHERE student_id = OLD.student_id;
END;

CREATE TRIGGER update_enrollment_timestamp
AFTER UPDATE ON program_enrollments
FOR EACH ROW
BEGIN
    UPDATE program_enrollments SET updated_at = CURRENT_TIMESTAMP WHERE enrollment_id = OLD.enrollment_id;
END;

CREATE TRIGGER update_registration_timestamp
AFTER UPDATE ON module_registrations
FOR EACH ROW
BEGIN
    UPDATE module_registrations SET updated_at = CURRENT_TIMESTAMP WHERE registration_id = OLD.registration_id;
END;

-- Trigger to update enrollment count when a student registers for a module
CREATE TRIGGER update_offering_enrollment
AFTER INSERT ON module_registrations
FOR EACH ROW
BEGIN
    UPDATE module_offerings 
    SET current_enrollment = current_enrollment + 1 
    WHERE offering_id = NEW.offering_id;
END;

-- Trigger to update enrollment count when a student drops a module
CREATE TRIGGER update_offering_drop
AFTER UPDATE OF status ON module_registrations
FOR EACH ROW
WHEN NEW.status = 'dropped' AND OLD.status != 'dropped'
BEGIN
    UPDATE module_offerings 
    SET current_enrollment = current_enrollment - 1 
    WHERE offering_id = NEW.offering_id;
END;

-- Trigger to update monitoria attendance count
CREATE TRIGGER update_monitoria_attendance
AFTER INSERT ON monitoria_attendance
FOR EACH ROW
BEGIN
    UPDATE monitorias 
    SET current_attendees = current_attendees + 1 
    WHERE monitoria_id = NEW.monitoria_id;
END;
```
