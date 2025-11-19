"""
Generated Code Metadata:
========================
Original URL: https://giveaway-compound.com
Prompt: Design a database schema for storing and retrieving information about software, libraries, or APIs, inspired by the technical and informational content that might be found on giveaway-compound.com.
Generated: DETERMINISTIC_330e6496f96fb5d1
Batch ID: 20250622_211610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing and retrieving information about software, libraries, or APIs

-- Table to store information about software, libraries, or APIs
CREATE TABLE Software (
    id SERIAL PRIMARY KEY, -- Unique identifier for each software/library/API
    name VARCHAR(255) NOT NULL, -- Name of the software/library/API
    description TEXT, -- Detailed description of the software/library/API
    version VARCHAR(50), -- Version of the software/library/API
    category VARCHAR(100), -- Category (e.g., "Library", "API", "Software")
    license_type VARCHAR(100), -- License type (e.g., "MIT", "GPL", "Proprietary")
    website_url VARCHAR(2083), -- Official website or documentation URL
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Table to store tags for categorizing software/library/API
CREATE TABLE Tags (
    id SERIAL PRIMARY KEY, -- Unique identifier for each tag
    name VARCHAR(100) NOT NULL UNIQUE -- Name of the tag (e.g., "Open Source", "Machine Learning")
);

-- Many-to-Many relationship between Software and Tags
CREATE TABLE SoftwareTags (
    software_id INT NOT NULL, -- Foreign key referencing Software table
    tag_id INT NOT NULL, -- Foreign key referencing Tags table
    PRIMARY KEY (software_id, tag_id), -- Composite primary key
    FOREIGN KEY (software_id) REFERENCES Software(id) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (tag_id) REFERENCES Tags(id) ON DELETE CASCADE -- Cascade delete
);

-- Table to store reviews for software/library/API
CREATE TABLE Reviews (
    id SERIAL PRIMARY KEY, -- Unique identifier for each review
    software_id INT NOT NULL, -- Foreign key referencing Software table
    reviewer_name VARCHAR(255), -- Name of the reviewer
    rating INT CHECK (rating BETWEEN 1 AND 5), -- Rating (1 to 5)
    comment TEXT, -- Review comment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the review was created
    FOREIGN KEY (software_id) REFERENCES Software(id) ON DELETE CASCADE -- Cascade delete
);

-- Table to store system requirements for software/library/API
CREATE TABLE SystemRequirements (
    id SERIAL PRIMARY KEY, -- Unique identifier for each requirement
    software_id INT NOT NULL, -- Foreign key referencing Software table
    operating_system VARCHAR(100), -- Operating system (e.g., "Windows", "Linux", "macOS")
    architecture VARCHAR(50), -- Architecture (e.g., "x86", "x64", "ARM")
    minimum_ram_mb INT, -- Minimum RAM required (in MB)
    minimum_storage_mb INT, -- Minimum storage required (in MB)
    FOREIGN KEY (software_id) REFERENCES Software(id) ON DELETE CASCADE -- Cascade delete
);

-- Table to store download links for software/library/API
CREATE TABLE DownloadLinks (
    id SERIAL PRIMARY KEY, -- Unique identifier for each download link
    software_id INT NOT NULL, -- Foreign key referencing Software table
    platform VARCHAR(100), -- Platform (e.g., "Windows", "Linux", "macOS")
    download_url VARCHAR(2083) NOT NULL, -- URL for downloading the software/library/API
    FOREIGN KEY (software_id) REFERENCES Software(id) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for optimizing queries
CREATE INDEX idx_software_name ON Software(name); -- Index for quick search by name
CREATE INDEX idx_tags_name ON Tags(name); -- Index for quick search by tag name
CREATE INDEX idx_reviews_software_id ON Reviews(software_id); -- Index for quick lookup of reviews by software ID
CREATE INDEX idx_download_links_software_id ON DownloadLinks(software_id); -- Index for quick lookup of download links by software ID
```
