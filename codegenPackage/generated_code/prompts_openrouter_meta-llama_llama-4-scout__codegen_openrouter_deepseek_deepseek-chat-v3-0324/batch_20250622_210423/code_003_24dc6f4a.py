"""
Generated Code Metadata:
========================
Original URL: https://sapt.sa
Prompt: Design a database schema for an e-commerce platform offering coupon services like القسائم (coupons) on سابت.
Generated: DETERMINISTIC_24dc6f4a70701d96
Batch ID: 20250622_210423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for e-commerce coupon platform

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    is_verified BOOLEAN DEFAULT FALSE
);

CREATE TABLE merchants (
    merchant_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    business_name VARCHAR(100) NOT NULL,
    business_description TEXT,
    logo_url VARCHAR(255),
    website_url VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    parent_category_id INTEGER REFERENCES categories(category_id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE coupons (
    coupon_id SERIAL PRIMARY KEY,
    merchant_id INTEGER REFERENCES merchants(merchant_id),
    category_id INTEGER REFERENCES categories(category_id),
    title VARCHAR(100) NOT NULL,
    description TEXT,
    code VARCHAR(50) NOT NULL UNIQUE,
    discount_amount DECIMAL(10, 2),
    discount_percentage DECIMAL(5, 2),
    min_purchase_amount DECIMAL(10, 2) DEFAULT 0,
    max_discount_amount DECIMAL(10, 2),
    start_date TIMESTAMP WITH TIME ZONE NOT NULL,
    end_date TIMESTAMP WITH TIME ZONE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    total_quantity INTEGER,
    remaining_quantity INTEGER,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_discount CHECK (
        (discount_amount IS NOT NULL AND discount_percentage IS NULL) OR
        (discount_amount IS NULL AND discount_percentage IS NOT NULL)
    ),
    CONSTRAINT valid_dates CHECK (end_date > start_date)
);

CREATE TABLE user_coupons (
    user_coupon_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    coupon_id INTEGER REFERENCES coupons(coupon_id),
    redeemed_at TIMESTAMP WITH TIME ZONE,
    is_used BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (user_id, coupon_id)
);

CREATE TABLE coupon_views (
    view_id SERIAL PRIMARY KEY,
    coupon_id INTEGER REFERENCES coupons(coupon_id),
    user_id INTEGER REFERENCES users(user_id),
    viewed_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    ip_address VARCHAR(45)
);

CREATE TABLE coupon_clicks (
    click_id SERIAL PRIMARY KEY,
    coupon_id INTEGER REFERENCES coupons(coupon_id),
    user_id INTEGER REFERENCES users(user_id),
    clicked_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    ip_address VARCHAR(45),
    referrer_url VARCHAR(255)
);

CREATE TABLE favorites (
    favorite_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    coupon_id INTEGER REFERENCES coupons(coupon_id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (user_id, coupon_id)
);

CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    coupon_id INTEGER REFERENCES coupons(coupon_id),
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (user_id, coupon_id)
);

CREATE TABLE notifications (
    notification_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    title VARCHAR(100) NOT NULL,
    message TEXT NOT NULL,
    is_read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    link_url VARCHAR(255)
);

-- Indexes for performance optimization
CREATE INDEX idx_coupons_merchant ON coupons(merchant_id);
CREATE INDEX idx_coupons_category ON coupons(category_id);
CREATE INDEX idx_coupons_active ON coupons(is_active);
CREATE INDEX idx_coupons_dates ON coupons(start_date, end_date);
CREATE INDEX idx_user_coupons_user ON user_coupons(user_id);
CREATE INDEX idx_user_coupons_coupon ON user_coupons(coupon_id);
CREATE INDEX idx_favorites_user ON favorites(user_id);
CREATE INDEX idx_reviews_coupon ON reviews(coupon_id);
```
