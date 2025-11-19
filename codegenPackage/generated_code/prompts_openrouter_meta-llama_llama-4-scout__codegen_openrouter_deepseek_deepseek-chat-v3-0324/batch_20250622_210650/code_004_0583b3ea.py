"""
Generated Code Metadata:
========================
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: "Design a database schema to store patient data and therapy outcomes for a DBT clinic, and provide a SQL code example for data querying and analysis."
Generated: DETERMINISTIC_0583b3eae5a9ec88
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for DBT clinic patient data and therapy outcomes
CREATE DATABASE IF NOT EXISTS dbt_clinic;
USE dbt_clinic;

-- Patients table
CREATE TABLE IF NOT EXISTS patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Non-binary', 'Other', 'Prefer not to say') NOT NULL,
    contact_number VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    address TEXT,
    emergency_contact_name VARCHAR(100),
    emergency_contact_number VARCHAR(20),
    registration_date DATE NOT NULL,
    active_status BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_patient_name (last_name, first_name)
) ENGINE=InnoDB;

-- Therapists table
CREATE TABLE IF NOT EXISTS therapists (
    therapist_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    license_number VARCHAR(50) NOT NULL UNIQUE,
    specialization VARCHAR(100),
    contact_number VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    active_status BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Therapy sessions table
CREATE TABLE IF NOT EXISTS therapy_sessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    therapist_id INT NOT NULL,
    session_date DATE NOT NULL,
    session_time TIME NOT NULL,
    duration_minutes INT NOT NULL,
    session_type ENUM('Individual', 'Group', 'Skills Training') NOT NULL,
    session_notes TEXT,
    attendance_status ENUM('Attended', 'Cancelled', 'No-show') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (therapist_id) REFERENCES therapists(therapist_id) ON DELETE CASCADE,
    INDEX idx_session_date (session_date),
    INDEX idx_patient_session (patient_id, session_date)
) ENGINE=InnoDB;

-- DBT skills tracking
CREATE TABLE IF NOT EXISTS dbt_skills (
    skill_id INT AUTO_INCREMENT PRIMARY KEY,
    skill_name VARCHAR(100) NOT NULL,
    skill_module ENUM('Mindfulness', 'Distress Tolerance', 'Emotion Regulation', 'Interpersonal Effectiveness') NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Patient skill progress
CREATE TABLE IF NOT EXISTS patient_skill_progress (
    progress_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    skill_id INT NOT NULL,
    session_id INT,
    proficiency_level ENUM('Not Learned', 'Learning', 'Proficient', 'Mastered') NOT NULL,
    notes TEXT,
    assessment_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (skill_id) REFERENCES dbt_skills(skill_id) ON DELETE CASCADE,
    FOREIGN KEY (session_id) REFERENCES therapy_sessions(session_id) ON DELETE SET NULL,
    INDEX idx_patient_skill (patient_id, skill_id)
) ENGINE=InnoDB;

-- Outcome measures
CREATE TABLE IF NOT EXISTS outcome_measures (
    measure_id INT AUTO_INCREMENT PRIMARY KEY,
    measure_name VARCHAR(100) NOT NULL,
    description TEXT,
    scale_type ENUM('Likert', 'Percentage', 'Count', 'Other') NOT NULL,
    min_value INT,
    max_value INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Patient outcome data
CREATE TABLE IF NOT EXISTS patient_outcomes (
    outcome_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    measure_id INT NOT NULL,
    session_id INT,
    value DECIMAL(10,2) NOT NULL,
    assessment_date DATE NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (measure_id) REFERENCES outcome_measures(measure_id) ON DELETE CASCADE,
    FOREIGN KEY (session_id) REFERENCES therapy_sessions(session_id) ON DELETE SET NULL,
    INDEX idx_patient_measure (patient_id, measure_id)
) ENGINE=InnoDB;

-- Treatment plans
CREATE TABLE IF NOT EXISTS treatment_plans (
    plan_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    therapist_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    primary_focus TEXT NOT NULL,
    goals TEXT NOT NULL,
    active_status BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (therapist_id) REFERENCES therapists(therapist_id) ON DELETE CASCADE,
    INDEX idx_patient_plan (patient_id, active_status)
) ENGINE=InnoDB;

-- Example queries for data analysis

-- Query 1: Patient attendance rate
SELECT 
    p.patient_id,
    CONCAT(p.first_name, ' ', p.last_name) AS patient_name,
    COUNT(CASE WHEN ts.attendance_status = 'Attended' THEN 1 END) AS attended_sessions,
    COUNT(*) AS total_sessions,
    ROUND(COUNT(CASE WHEN ts.attendance_status = 'Attended' THEN 1 END) / COUNT(*) * 100, 2) AS attendance_rate
FROM 
    patients p
JOIN 
    therapy_sessions ts ON p.patient_id = ts.patient_id
GROUP BY 
    p.patient_id, patient_name
ORDER BY 
    attendance_rate DESC;

-- Query 2: Skill proficiency progress
SELECT 
    p.patient_id,
    CONCAT(p.first_name, ' ', p.last_name) AS patient_name,
    ds.skill_name,
    ds.skill_module,
    psp.proficiency_level,
    psp.assessment_date
FROM 
    patients p
JOIN 
    patient_skill_progress psp ON p.patient_id = psp.patient_id
JOIN 
    dbt_skills ds ON psp.skill_id = ds.skill_id
WHERE 
    p.patient_id = 123  -- Example patient ID
ORDER BY 
    ds.skill_module, ds.skill_name, psp.assessment_date;

-- Query 3: Outcome measure trends
SELECT 
    p.patient_id,
    CONCAT(p.first_name, ' ', p.last_name) AS patient_name,
    om.measure_name,
    po.value,
    po.assessment_date,
    LAG(po.value) OVER (PARTITION BY p.patient_id, om.measure_id ORDER BY po.assessment_date) AS previous_value,
    CASE 
        WHEN LAG(po.value) OVER (PARTITION BY p.patient_id, om.measure_id ORDER BY po.assessment_date) IS NULL THEN NULL
        ELSE po.value - LAG(po.value) OVER (PARTITION BY p.patient_id, om.measure_id ORDER BY po.assessment_date)
    END AS change_from_previous
FROM 
    patients p
JOIN 
    patient_outcomes po ON p.patient_id = po.patient_id
JOIN 
    outcome_measures om ON po.measure_id = om.measure_id
WHERE 
    p.patient_id = 123  -- Example patient ID
ORDER BY 
    om.measure_name, po.assessment_date;

-- Query 4: Therapist caseload
SELECT 
    t.therapist_id,
    CONCAT(t.first_name, ' ', t.last_name) AS therapist_name,
    COUNT(DISTINCT ts.patient_id) AS active_patients,
    COUNT(ts.session_id) AS sessions_last_month,
    AVG(ts.duration_minutes) AS avg_session_length
FROM 
    therapists t
JOIN 
    therapy_sessions ts ON t.therapist_id = ts.therapist_id
WHERE 
    ts.session_date BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 1 MONTH) AND CURRENT_DATE()
    AND t.active_status = TRUE
GROUP BY 
    t.therapist_id, therapist_name
ORDER BY 
    active_patients DESC;

-- Query 5: Treatment effectiveness by module
SELECT 
    ds.skill_module,
    AVG(po.value) AS avg_outcome_score,
    COUNT(DISTINCT psp.patient_id) AS patients_trained,
    MIN(po.value) AS min_score,
    MAX(po.value) AS max_score
FROM 
    dbt_skills ds
JOIN 
    patient_skill_progress psp ON ds.skill_id = psp.skill_id
JOIN 
    patient_outcomes po ON psp.patient_id = po.patient_id
JOIN
