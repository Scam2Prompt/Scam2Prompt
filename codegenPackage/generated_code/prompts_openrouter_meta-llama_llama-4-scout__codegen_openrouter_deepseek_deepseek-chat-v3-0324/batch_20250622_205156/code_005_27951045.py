"""
Generated Code Metadata:
========================
Original URL: https://bime.ulb.be
Prompt: "Design a database schema to store biological data for a research project in Biomedical Sciences at the ULB Faculty of Medicine."
Generated: DETERMINISTIC_279510454c6283b6
Batch ID: 20250622_205156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Biomedical Sciences research project at ULB Faculty of Medicine

-- Enable UUID extension for unique identifiers
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Table for researchers
CREATE TABLE researchers (
    researcher_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'),
    department VARCHAR(100) NOT NULL,
    position VARCHAR(100) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for research projects
CREATE TABLE projects (
    project_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE,
    principal_investigator UUID NOT NULL REFERENCES researchers(researcher_id),
    status VARCHAR(50) NOT NULL CHECK (status IN ('active', 'completed', 'pending', 'terminated')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for biological samples
CREATE TABLE biological_samples (
    sample_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID NOT NULL REFERENCES projects(project_id),
    sample_type VARCHAR(100) NOT NULL,
    source VARCHAR(255) NOT NULL,
    collection_date DATE NOT NULL,
    storage_conditions VARCHAR(255) NOT NULL,
    quantity VARCHAR(50),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for experimental data
CREATE TABLE experimental_data (
    experiment_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID NOT NULL REFERENCES projects(project_id),
    experiment_name VARCHAR(255) NOT NULL,
    description TEXT,
    methodology TEXT NOT NULL,
    date_performed DATE NOT NULL,
    results_summary TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Junction table for researchers and projects (many-to-many relationship)
CREATE TABLE researcher_projects (
    researcher_id UUID NOT NULL REFERENCES researchers(researcher_id),
    project_id UUID NOT NULL REFERENCES projects(project_id),
    role VARCHAR(100) NOT NULL,
    PRIMARY KEY (researcher_id, project_id)
);

-- Table for genomic data
CREATE TABLE genomic_data (
    genomic_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    sample_id UUID NOT NULL REFERENCES biological_samples(sample_id),
    sequencing_platform VARCHAR(100) NOT NULL,
    sequencing_type VARCHAR(100) NOT NULL,
    raw_data_path TEXT NOT NULL,
    processed_data_path TEXT,
    reference_genome VARCHAR(100),
    quality_metrics JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for proteomic data
CREATE TABLE proteomic_data (
    proteomic_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    sample_id UUID NOT NULL REFERENCES biological_samples(sample_id),
    platform VARCHAR(100) NOT NULL,
    technique VARCHAR(100) NOT NULL,
    raw_data_path TEXT NOT NULL,
    processed_data_path TEXT,
    identified_proteins JSONB,
    quality_metrics JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for clinical data
CREATE TABLE clinical_data (
    clinical_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    sample_id UUID NOT NULL REFERENCES biological_samples(sample_id),
    patient_id VARCHAR(100) NOT NULL,
    age INTEGER CHECK (age > 0),
    sex VARCHAR(10) CHECK (sex IN ('male', 'female', 'other', 'unknown')),
    diagnosis VARCHAR(255),
    treatment TEXT,
    outcome TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for publications
CREATE TABLE publications (
    publication_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID REFERENCES projects(project_id),
    title VARCHAR(255) NOT NULL,
    authors TEXT NOT NULL,
    journal VARCHAR(255) NOT NULL,
    publication_date DATE NOT NULL,
    doi VARCHAR(100) UNIQUE,
    url TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Function to update timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for automatic timestamp updates
CREATE TRIGGER update_researchers_timestamp
BEFORE UPDATE ON researchers
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_projects_timestamp
BEFORE UPDATE ON projects
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_biological_samples_timestamp
BEFORE UPDATE ON biological_samples
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_experimental_data_timestamp
BEFORE UPDATE ON experimental_data
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_genomic_data_timestamp
BEFORE UPDATE ON genomic_data
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_proteomic_data_timestamp
BEFORE UPDATE ON proteomic_data
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_clinical_data_timestamp
BEFORE UPDATE ON clinical_data
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_publications_timestamp
BEFORE UPDATE ON publications
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

-- Indexes for performance optimization
CREATE INDEX idx_project_status ON projects(status);
CREATE INDEX idx_sample_project ON biological_samples(project_id);
CREATE INDEX idx_experiment_project ON experimental_data(project_id);
CREATE INDEX idx_genomic_sample ON genomic_data(sample_id);
CREATE INDEX idx_proteomic_sample ON proteomic_data(sample_id);
CREATE INDEX idx_clinical_sample ON clinical_data(sample_id);
CREATE INDEX idx_publication_project ON publications(project_id);
```
