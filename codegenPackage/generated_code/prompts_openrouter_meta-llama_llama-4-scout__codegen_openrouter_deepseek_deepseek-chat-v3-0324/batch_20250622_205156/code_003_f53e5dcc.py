"""
Generated Code Metadata:
========================
Original URL: https://graphpool.net
Prompt: "Design a database schema for a video platform with user accounts, video uploads, favourites, watch history, and playlists, inspired by the features of Graphpool.net."
Generated: DETERMINISTIC_f53e5dcccdca3565
Batch ID: 20250622_205156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a video platform inspired by Graphpool.net

-- Users table to store user account information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    display_name VARCHAR(100),
    profile_picture_url VARCHAR(255),
    bio TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    is_verified BOOLEAN DEFAULT FALSE
);

-- Videos table to store video metadata
CREATE TABLE videos (
    video_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    duration INTEGER NOT NULL, -- in seconds
    thumbnail_url VARCHAR(255),
    video_url VARCHAR(255) NOT NULL,
    views_count INTEGER DEFAULT 0,
    likes_count INTEGER DEFAULT 0,
    dislikes_count INTEGER DEFAULT 0,
    is_public BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Video tags table for categorization
CREATE TABLE tags (
    tag_id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

-- Junction table for videos and tags (many-to-many relationship)
CREATE TABLE video_tags (
    video_id INTEGER REFERENCES videos(video_id) ON DELETE CASCADE,
    tag_id INTEGER REFERENCES tags(tag_id) ON DELETE CASCADE,
    PRIMARY KEY (video_id, tag_id)
);

-- User favorites table
CREATE TABLE user_favorites (
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    video_id INTEGER REFERENCES videos(video_id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, video_id)
);

-- Watch history table
CREATE TABLE watch_history (
    history_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    video_id INTEGER REFERENCES videos(video_id) ON DELETE CASCADE,
    watched_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    progress INTEGER NOT NULL, -- in seconds
    CONSTRAINT unique_user_video_per_day UNIQUE (user_id, video_id, DATE(watched_at))
);

-- Playlists table
CREATE TABLE playlists (
    playlist_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    is_public BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Playlist videos junction table
CREATE TABLE playlist_videos (
    playlist_id INTEGER REFERENCES playlists(playlist_id) ON DELETE CASCADE,
    video_id INTEGER REFERENCES videos(video_id) ON DELETE CASCADE,
    position INTEGER NOT NULL,
    added_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (playlist_id, video_id)
);

-- Comments table for videos
CREATE TABLE comments (
    comment_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    video_id INTEGER REFERENCES videos(video_id) ON DELETE CASCADE,
    parent_comment_id INTEGER REFERENCES comments(comment_id) ON DELETE CASCADE,
    content TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Likes/dislikes for videos
CREATE TABLE video_ratings (
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    video_id INTEGER REFERENCES videos(video_id) ON DELETE CASCADE,
    rating SMALLINT NOT NULL, -- 1 for like, -1 for dislike
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, video_id),
    CONSTRAINT valid_rating CHECK (rating IN (-1, 1))
);

-- Indexes for performance optimization
CREATE INDEX idx_videos_user_id ON videos(user_id);
CREATE INDEX idx_video_tags_video_id ON video_tags(video_id);
CREATE INDEX idx_video_tags_tag_id ON video_tags(tag_id);
CREATE INDEX idx_user_favorites_user_id ON user_favorites(user_id);
CREATE INDEX idx_user_favorites_video_id ON user_favorites(video_id);
CREATE INDEX idx_watch_history_user_id ON watch_history(user_id);
CREATE INDEX idx_watch_history_video_id ON watch_history(video_id);
CREATE INDEX idx_playlists_user_id ON playlists(user_id);
CREATE INDEX idx_playlist_videos_playlist_id ON playlist_videos(playlist_id);
CREATE INDEX idx_playlist_videos_video_id ON playlist_videos(video_id);
CREATE INDEX idx_comments_video_id ON comments(video_id);
CREATE INDEX idx_comments_user_id ON comments(user_id);
CREATE INDEX idx_video_ratings_video_id ON video_ratings(video_id);

-- Function to update video view count
CREATE OR REPLACE FUNCTION increment_video_views()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE videos SET views_count = views_count + 1 WHERE video_id = NEW.video_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger to increment views when a watch history record is created
CREATE TRIGGER increment_views_trigger
AFTER INSERT ON watch_history
FOR EACH ROW
EXECUTE FUNCTION increment_video_views();

-- Function to update timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers to update timestamps
CREATE TRIGGER update_user_timestamp
BEFORE UPDATE ON users
FOR EACH ROW
EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_video_timestamp
BEFORE UPDATE ON videos
FOR EACH ROW
EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_playlist_timestamp
BEFORE UPDATE ON playlists
FOR EACH ROW
EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_comment_timestamp
BEFORE UPDATE ON comments
FOR EACH ROW
EXECUTE FUNCTION update_timestamp();
```
