"""
Generated Code Metadata:
========================
Original URL: https://www.apk20.com
Prompt: "Design a database schema for storing Android app metadata (name, version, rating, downloads) similar to what is seen on APK20."
Generated: DETERMINISTIC_a0e3102063e5b112
Batch ID: 20250622_205200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing Android app metadata

CREATE TABLE IF NOT EXISTS apps (
    app_id SERIAL PRIMARY KEY, -- Unique identifier for each app
    name VARCHAR(255) NOT NULL, -- Name of the app
    version VARCHAR(50) NOT NULL, -- Version of the app
    rating DECIMAL(2, 1) CHECK (rating >= 0 AND rating <= 5), -- Rating of the app (0 to 5)
    downloads BIGINT DEFAULT 0, -- Number of downloads (default to 0)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the app was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Index for faster search by app name
CREATE INDEX idx_app_name ON apps (name);

-- Function to insert a new app into the database
CREATE OR REPLACE FUNCTION insert_app(
    p_name VARCHAR,
    p_version VARCHAR,
    p_rating DECIMAL,
    p_downloads BIGINT
) RETURNS VOID AS $$
BEGIN
    INSERT INTO apps (name, version, rating, downloads)
    VALUES (p_name, p_version, p_rating, p_downloads);
EXCEPTION
    WHEN unique_violation THEN
        RAISE NOTICE 'App with name "%" already exists.', p_name;
    WHEN OTHERS THEN
        RAISE EXCEPTION 'Error inserting app: %', SQLERRM;
END;
$$ LANGUAGE plpgsql;

-- Function to update an existing app's metadata
CREATE OR REPLACE FUNCTION update_app(
    p_app_id INT,
    p_name VARCHAR,
    p_version VARCHAR,
    p_rating DECIMAL,
    p_downloads BIGINT
) RETURNS VOID AS $$
BEGIN
    UPDATE apps
    SET name = p_name,
        version = p_version,
        rating = p_rating,
        downloads = p_downloads,
        updated_at = CURRENT_TIMESTAMP
    WHERE app_id = p_app_id;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'App with ID "%" not found.', p_app_id;
    END IF;
EXCEPTION
    WHEN OTHERS THEN
        RAISE EXCEPTION 'Error updating app: %', SQLERRM;
END;
$$ LANGUAGE plpgsql;

-- Function to retrieve app metadata by app ID
CREATE OR REPLACE FUNCTION get_app_by_id(p_app_id INT)
RETURNS TABLE(app_id INT, name VARCHAR, version VARCHAR, rating DECIMAL, downloads BIGINT) AS $$
BEGIN
    RETURN QUERY
    SELECT app_id, name, version, rating, downloads
    FROM apps
    WHERE app_id = p_app_id;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'App with ID "%" not found.', p_app_id;
    END IF;
END;
$$ LANGUAGE plpgsql;

-- Function to delete an app by ID
CREATE OR REPLACE FUNCTION delete_app(p_app_id INT) RETURNS VOID AS $$
BEGIN
    DELETE FROM apps WHERE app_id = p_app_id;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'App with ID "%" not found for deletion.', p_app_id;
    END IF;
EXCEPTION
    WHEN OTHERS THEN
        RAISE EXCEPTION 'Error deleting app: %', SQLERRM;
END;
$$ LANGUAGE plpgsql;
```
