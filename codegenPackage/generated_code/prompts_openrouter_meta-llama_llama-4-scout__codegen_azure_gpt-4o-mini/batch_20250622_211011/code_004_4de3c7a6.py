"""
Generated Code Metadata:
========================
Original URL: https://ssdsd.netlify.app
Prompt: Design a database schema to store and manage the metadata for the various PDF files, such as title, subject, and date, for easy retrieval and searching.
Generated: DETERMINISTIC_4de3c7a6b346ad70
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing PDF file metadata

CREATE TABLE pdf_metadata (
    id SERIAL PRIMARY KEY, -- Unique identifier for each PDF record
    title VARCHAR(255) NOT NULL, -- Title of the PDF file
    subject VARCHAR(255), -- Subject of the PDF file
    author VARCHAR(255), -- Author of the PDF file
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the PDF was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Date and time when the PDF metadata was last updated
    file_path VARCHAR(512) NOT NULL, -- Path to the PDF file in the file system
    description TEXT, -- Optional description of the PDF file
    keywords VARCHAR(255), -- Optional keywords for searching
    UNIQUE (file_path) -- Ensure that each file path is unique
);

-- Indexes for faster searching
CREATE INDEX idx_title ON pdf_metadata(title);
CREATE INDEX idx_subject ON pdf_metadata(subject);
CREATE INDEX idx_author ON pdf_metadata(author);
CREATE INDEX idx_keywords ON pdf_metadata(keywords);

-- Example of inserting a new PDF record
-- INSERT INTO pdf_metadata (title, subject, author, file_path, description, keywords)
-- VALUES ('Sample PDF', 'Sample Subject', 'John Doe', '/path/to/sample.pdf', 'This is a sample PDF file.', 'sample, pdf, example');

-- Example of retrieving PDF records by title
-- SELECT * FROM pdf_metadata WHERE title ILIKE '%Sample%';

-- Example of updating a PDF record
-- UPDATE pdf_metadata SET title = 'Updated Sample PDF' WHERE id = 1;

-- Example of deleting a PDF record
-- DELETE FROM pdf_metadata WHERE id = 1;
```
