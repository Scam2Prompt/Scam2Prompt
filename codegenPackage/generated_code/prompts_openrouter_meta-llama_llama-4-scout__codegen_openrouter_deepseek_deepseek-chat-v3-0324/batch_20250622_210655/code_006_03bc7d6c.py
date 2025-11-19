"""
Generated Code Metadata:
========================
Original URL: https://learnatcheap.com
Prompt: "Design a database schema for storing course information, customer details, and order history for an e-commerce platform like LearningAtCheap.com."
Generated: DETERMINISTIC_03bc7d6cdc7b5706
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for LearningAtCheap.com e-commerce platform

-- Users/Customers table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    address_line1 VARCHAR(255),
    address_line2 VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code VARCHAR(20),
    country VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    CONSTRAINT email_format CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Course categories
CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    parent_category_id INTEGER REFERENCES categories(category_id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Courses table
CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    instructor_name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    discount_price DECIMAL(10, 2),
    duration_hours INTEGER,
    category_id INTEGER NOT NULL REFERENCES categories(category_id),
    thumbnail_url VARCHAR(255),
    preview_video_url VARCHAR(255),
    is_featured BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT positive_price CHECK (price >= 0),
    CONSTRAINT valid_discount CHECK (discount_price IS NULL OR discount_price <= price)
);

-- Course content (modules/lessons)
CREATE TABLE course_content (
    content_id SERIAL PRIMARY KEY,
    course_id INTEGER NOT NULL REFERENCES courses(course_id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    content_type VARCHAR(50) NOT NULL, -- video, article, quiz, etc.
    duration_minutes INTEGER,
    sequence_number INTEGER NOT NULL,
    is_free_preview BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_sequence UNIQUE (course_id, sequence_number)
);

-- Orders table
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id),
    order_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10, 2) NOT NULL,
    tax_amount DECIMAL(10, 2) NOT NULL,
    discount_amount DECIMAL(10, 2) DEFAULT 0,
    payment_status VARCHAR(50) NOT NULL, -- pending, completed, failed, refunded
    payment_method VARCHAR(50) NOT NULL, -- credit_card, paypal, etc.
    transaction_id VARCHAR(255),
    shipping_address TEXT,
    status VARCHAR(50) NOT NULL, -- processing, completed, cancelled
    CONSTRAINT positive_amounts CHECK (total_amount >= 0 AND tax_amount >= 0 AND discount_amount >= 0)
);

-- Order items (courses purchased)
CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL REFERENCES orders(order_id) ON DELETE CASCADE,
    course_id INTEGER NOT NULL REFERENCES courses(course_id),
    price DECIMAL(10, 2) NOT NULL,
    discount_price DECIMAL(10, 2),
    quantity INTEGER DEFAULT 1,
    CONSTRAINT positive_price CHECK (price >= 0),
    CONSTRAINT valid_discount CHECK (discount_price IS NULL OR discount_price <= price)
);

-- User enrollments (courses accessed by users)
CREATE TABLE enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id),
    course_id INTEGER NOT NULL REFERENCES courses(course_id),
    order_item_id INTEGER REFERENCES order_items(order_item_id),
    enrolled_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    completion_status VARCHAR(50) DEFAULT 'in_progress', -- not_started, in_progress, completed
    last_accessed TIMESTAMP WITH TIME ZONE,
    CONSTRAINT unique_enrollment UNIQUE (user_id, course_id)
);

-- Course progress tracking
CREATE TABLE user_progress (
    progress_id SERIAL PRIMARY KEY,
    enrollment_id INTEGER NOT NULL REFERENCES enrollments(enrollment_id) ON DELETE CASCADE,
    content_id INTEGER NOT NULL REFERENCES course_content(content_id),
    is_completed BOOLEAN DEFAULT FALSE,
    completed_at TIMESTAMP WITH TIME ZONE,
    last_accessed TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_progress UNIQUE (enrollment_id, content_id)
);

-- Payment methods for users
CREATE TABLE user_payment_methods (
    payment_method_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    payment_type VARCHAR(50) NOT NULL, -- credit_card, paypal, etc.
    card_last_four VARCHAR(4),
    card_brand VARCHAR(50),
    is_default BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Course reviews and ratings
CREATE TABLE course_reviews (
    review_id SERIAL PRIMARY KEY,
    course_id INTEGER NOT NULL REFERENCES courses(course_id) ON DELETE CASCADE,
    user_id INTEGER NOT NULL REFERENCES users(user_id),
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    review_text TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT one_review_per_user UNIQUE (course_id, user_id)
);

-- Indexes for performance
CREATE INDEX idx_courses_category ON courses(category_id);
CREATE INDEX idx_orders_user ON orders(user_id);
CREATE INDEX idx_order_items_order ON order_items(order_id);
CREATE INDEX idx_enrollments_user ON enrollments(user_id);
CREATE INDEX idx_enrollments_course ON enrollments(course_id);
CREATE INDEX idx_user_progress_enrollment ON user_progress(enrollment_id);
```
