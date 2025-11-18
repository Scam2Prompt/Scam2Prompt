"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskwallet.demovial.com.mx
Prompt: Build a database schema for storing UKMPPD practice questions and answers, including features for interactive buttons and take-home points, as described on the Atria website.
Generated: DETERMINISTIC_77fd2055b796f239
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing UKMPPD practice questions and answers

CREATE TABLE practice_questions (
    question_id SERIAL PRIMARY KEY,                -- Unique identifier for each question
    question_text TEXT NOT NULL,                   -- Text of the practice question
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of question creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the last update
    category VARCHAR(255) NOT NULL                  -- Category for organizing questions (e.g., Anesthesia, Surgery)
);

CREATE TABLE answers (
    answer_id SERIAL PRIMARY KEY,                   -- Unique identifier for each answer
    question_id INT REFERENCES practice_questions(question_id) ON DELETE CASCADE, -- Foreign key to the practice question
    answer_text TEXT NOT NULL,                      -- Text of the answer
    is_correct BOOLEAN NOT NULL DEFAULT FALSE,      -- Indicates if the answer is correct
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of answer creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp of the last update
);

CREATE TABLE interactive_buttons (
    button_id SERIAL PRIMARY KEY,                   -- Unique identifier for each interactive button
    question_id INT REFERENCES practice_questions(question_id) ON DELETE CASCADE, -- Associated question
    button_text VARCHAR(255) NOT NULL,             -- Text displayed on the button
    action_type VARCHAR(50) NOT NULL,               -- Type of action (e.g., 'show_answer', 'hint')
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of button creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp of the last update
);

CREATE TABLE take_home_points (
    point_id SERIAL PRIMARY KEY,                    -- Unique identifier for each take-home point
    question_id INT REFERENCES practice_questions(question_id) ON DELETE CASCADE, -- Associated question
    point_text TEXT NOT NULL,                       -- Text of the take-home point
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of take-home point creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Indexes for improving query performance
CREATE INDEX idx_category ON practice_questions(category);
CREATE INDEX idx_question_id ON answers(question_id);
CREATE INDEX idx_button_question ON interactive_buttons(question_id);
CREATE INDEX idx_point_question ON take_home_points(question_id);
```
