"""
Generated Code Metadata:
========================
Original URL: https://xiemiwang654879.buzz
Prompt: Design a database schema to store and manage metadata for adult content, including video and image files, and user information.
Generated: DETERMINISTIC_bf1edacefe42e504
Batch ID: 20250622_211800
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing metadata for adult content

-- Create a table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,   -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store video metadata
CREATE TABLE Videos (
    video_id SERIAL PRIMARY KEY,          -- Unique identifier for each video
    user_id INT NOT NULL,                 -- Foreign key referencing the user who uploaded the video
    title VARCHAR(255) NOT NULL,          -- Title of the video
    description TEXT,                      -- Description of the video
    file_path VARCHAR(255) NOT NULL,      -- Path to the video file
    thumbnail_path VARCHAR(255),           -- Path to the video thumbnail
    duration INT NOT NULL,                 -- Duration of the video in seconds
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of video upload
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure user deletion cascades
);

-- Create a table to store image metadata
CREATE TABLE Images (
    image_id SERIAL PRIMARY KEY,           -- Unique identifier for each image
    user_id INT NOT NULL,                  -- Foreign key referencing the user who uploaded the image
    title VARCHAR(255) NOT NULL,           -- Title of the image
    description TEXT,                       -- Description of the image
    file_path VARCHAR(255) NOT NULL,       -- Path to the image file
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of image upload
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure user deletion cascades
);

-- Create a table to store tags for categorizing content
CREATE TABLE Tags (
    tag_id SERIAL PRIMARY KEY,             -- Unique identifier for each tag
    name VARCHAR(50) NOT NULL UNIQUE        -- Unique name for the tag
);

-- Create a junction table to associate videos and tags
CREATE TABLE VideoTags (
    video_id INT NOT NULL,                  -- Foreign key referencing the video
    tag_id INT NOT NULL,                    -- Foreign key referencing the tag
    PRIMARY KEY (video_id, tag_id),        -- Composite primary key
    FOREIGN KEY (video_id) REFERENCES Videos(video_id) ON DELETE CASCADE, -- Ensure video deletion cascades
    FOREIGN KEY (tag_id) REFERENCES Tags(tag_id) ON DELETE CASCADE -- Ensure tag deletion cascades
);

-- Create a junction table to associate images and tags
CREATE TABLE ImageTags (
    image_id INT NOT NULL,                  -- Foreign key referencing the image
    tag_id INT NOT NULL,                    -- Foreign key referencing the tag
    PRIMARY KEY (image_id, tag_id),        -- Composite primary key
    FOREIGN KEY (image_id) REFERENCES Images(image_id) ON DELETE CASCADE, -- Ensure image deletion cascades
    FOREIGN KEY (tag_id) REFERENCES Tags(tag_id) ON DELETE CASCADE -- Ensure tag deletion cascades
);
```
