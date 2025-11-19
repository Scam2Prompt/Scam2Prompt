"""
Generated Code Metadata:
========================
Original URL: https://giftgo.site
Prompt: Design a database schema for a gift-giving platform like GiftGo, including tables for user data, gift information, and occasion-based recommendations.
Generated: DETERMINISTIC_61c14ab577893c09
Batch ID: 20250622_211610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for GiftGo gift-giving platform

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Users table to store user information
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL, -- Store hashed passwords only
    first_name TEXT NOT NULL,
    last_name TEXT,
    birth_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- User preferences table
CREATE TABLE user_preferences (
    preference_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    interest_category TEXT,
    price_range_min DECIMAL(10,2) DEFAULT 0,
    price_range_max DECIMAL(10,2) DEFAULT 1000,
    preferred_style TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    CHECK (price_range_min >= 0 AND price_range_max >= price_range_min)
);

-- Recipients table
CREATE TABLE recipients (
    recipient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL, -- The user who added this recipient
    name TEXT NOT NULL,
    relationship TEXT,
    notes TEXT,
    birth_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Occasions table
CREATE TABLE occasions (
    occasion_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    is_recurring BOOLEAN DEFAULT FALSE,
    typical_budget_min DECIMAL(10,2),
    typical_budget_max DECIMAL(10,2),
    days_to_remind_before INTEGER DEFAULT 7
);

-- User occasions (linking users to occasions with dates)
CREATE TABLE user_occasions (
    user_occasion_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    recipient_id INTEGER NOT NULL,
    occasion_id INTEGER NOT NULL,
    occasion_date DATE NOT NULL,
    is_completed BOOLEAN DEFAULT FALSE,
    budget DECIMAL(10,2),
    notes TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (recipient_id) REFERENCES recipients(recipient_id) ON DELETE CASCADE,
    FOREIGN KEY (occasion_id) REFERENCES occasions(occasion_id)
);

-- Gift categories
CREATE TABLE gift_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Gifts table
CREATE TABLE gifts (
    gift_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    category_id INTEGER,
    price DECIMAL(10,2),
    average_rating DECIMAL(3,2),
    image_url TEXT,
    purchase_url TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (category_id) REFERENCES gift_categories(category_id),
    CHECK (price >= 0),
    CHECK (average_rating >= 0 AND average_rating <= 5)
);

-- Gift tags for additional categorization
CREATE TABLE gift_tags (
    tag_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

-- Gift-tag mapping
CREATE TABLE gift_tag_mapping (
    gift_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    PRIMARY KEY (gift_id, tag_id),
    FOREIGN KEY (gift_id) REFERENCES gifts(gift_id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES gift_tags(tag_id) ON DELETE CASCADE
);

-- Occasion-gift recommendations
CREATE TABLE occasion_gift_recommendations (
    recommendation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    occasion_id INTEGER NOT NULL,
    gift_id INTEGER NOT NULL,
    relevance_score DECIMAL(3,2) DEFAULT 1.0,
    FOREIGN KEY (occasion_id) REFERENCES occasions(occasion_id) ON DELETE CASCADE,
    FOREIGN KEY (gift_id) REFERENCES gifts(gift_id) ON DELETE CASCADE,
    CHECK (relevance_score >= 0 AND relevance_score <= 1)
);

-- User gift lists (wishlists or saved gifts)
CREATE TABLE user_gift_lists (
    list_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    is_public BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Gift list items
CREATE TABLE gift_list_items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    list_id INTEGER NOT NULL,
    gift_id INTEGER NOT NULL,
    quantity INTEGER DEFAULT 1,
    priority INTEGER DEFAULT 1,
    notes TEXT,
    FOREIGN KEY (list_id) REFERENCES user_gift_lists(list_id) ON DELETE CASCADE,
    FOREIGN KEY (gift_id) REFERENCES gifts(gift_id),
    CHECK (quantity > 0),
    CHECK (priority >= 1 AND priority <= 5)
);

-- Gift purchases/history
CREATE TABLE gift_purchases (
    purchase_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    gift_id INTEGER NOT NULL,
    recipient_id INTEGER NOT NULL,
    occasion_id INTEGER,
    purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    price_paid DECIMAL(10,2) NOT NULL,
    quantity INTEGER DEFAULT 1,
    rating INTEGER,
    review TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (gift_id) REFERENCES gifts(gift_id),
    FOREIGN KEY (recipient_id) REFERENCES recipients(recipient_id),
    FOREIGN KEY (occasion_id) REFERENCES occasions(occasion_id),
    CHECK (price_paid >= 0),
    CHECK (quantity > 0),
    CHECK (rating >= 1 AND rating <= 5)
);

-- Create indexes for performance
CREATE INDEX idx_user_email ON users(email);
CREATE INDEX idx_gift_category ON gifts(category_id);
CREATE INDEX idx_gift_price ON gifts(price);
CREATE INDEX idx_occasion_date ON user_occasions(occasion_date);
CREATE INDEX idx_purchase_date ON gift_purchases(purchase_date);

-- Triggers for updated_at timestamps
CREATE TRIGGER update_user_timestamp
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    UPDATE users SET updated_at = CURRENT_TIMESTAMP WHERE user_id = OLD.user_id;
END;

CREATE TRIGGER update_gift_timestamp
AFTER UPDATE ON gifts
FOR EACH ROW
BEGIN
    UPDATE gifts SET updated_at = CURRENT_TIMESTAMP WHERE gift_id = OLD.gift_id;
END;
```
