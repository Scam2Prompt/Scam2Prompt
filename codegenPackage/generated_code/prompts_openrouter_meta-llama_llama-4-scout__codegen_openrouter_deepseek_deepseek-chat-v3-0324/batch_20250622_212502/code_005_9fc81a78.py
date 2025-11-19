"""
Generated Code Metadata:
========================
Original URL: https://bincoin-rew.com
Prompt: "Design a database schema for storing and retrieving recipes for plant-based cooking, including fields for nutritional information."
Generated: DETERMINISTIC_9fc81a782f3e0d16
Batch ID: 20250622_212502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for plant-based recipe management system

CREATE TABLE ingredients (
    ingredient_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    category VARCHAR(50),
    is_vegan BOOLEAN DEFAULT TRUE,
    is_gluten_free BOOLEAN DEFAULT FALSE,
    is_organic BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE nutritional_info (
    nutritional_info_id SERIAL PRIMARY KEY,
    ingredient_id INTEGER REFERENCES ingredients(ingredient_id) ON DELETE CASCADE,
    calories_per_100g DECIMAL(10,2),
    protein_g DECIMAL(10,2),
    carbs_g DECIMAL(10,2),
    fat_g DECIMAL(10,2),
    fiber_g DECIMAL(10,2),
    sugar_g DECIMAL(10,2),
    sodium_mg DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE recipes (
    recipe_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    preparation_time_minutes INTEGER,
    cooking_time_minutes INTEGER,
    servings INTEGER,
    difficulty_level VARCHAR(20) CHECK (difficulty_level IN ('Easy', 'Medium', 'Hard')),
    meal_type VARCHAR(50),
    cuisine_type VARCHAR(50),
    is_gluten_free BOOLEAN DEFAULT FALSE,
    is_soy_free BOOLEAN DEFAULT FALSE,
    is_nut_free BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE recipe_ingredients (
    recipe_ingredient_id SERIAL PRIMARY KEY,
    recipe_id INTEGER REFERENCES recipes(recipe_id) ON DELETE CASCADE,
    ingredient_id INTEGER REFERENCES ingredients(ingredient_id) ON DELETE CASCADE,
    quantity DECIMAL(10,2),
    unit VARCHAR(20),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE recipe_steps (
    step_id SERIAL PRIMARY KEY,
    recipe_id INTEGER REFERENCES recipes(recipe_id) ON DELETE CASCADE,
    step_number INTEGER NOT NULL,
    instruction TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE recipe_nutritional_summary (
    summary_id SERIAL PRIMARY KEY,
    recipe_id INTEGER REFERENCES recipes(recipe_id) ON DELETE CASCADE,
    total_calories DECIMAL(10,2),
    total_protein_g DECIMAL(10,2),
    total_carbs_g DECIMAL(10,2),
    total_fat_g DECIMAL(10,2),
    total_fiber_g DECIMAL(10,2),
    total_sugar_g DECIMAL(10,2),
    total_sodium_mg DECIMAL(10,2),
    calories_per_serving DECIMAL(10,2),
    protein_per_serving DECIMAL(10,2),
    carbs_per_serving DECIMAL(10,2),
    fat_per_serving DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE tags (
    tag_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE recipe_tags (
    recipe_tag_id SERIAL PRIMARY KEY,
    recipe_id INTEGER REFERENCES recipes(recipe_id) ON DELETE CASCADE,
    tag_id INTEGER REFERENCES tags(tag_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(recipe_id, tag_id)
);

-- Indexes for performance optimization
CREATE INDEX idx_ingredients_name ON ingredients(name);
CREATE INDEX idx_recipes_title ON recipes(title);
CREATE INDEX idx_recipe_ingredients_recipe ON recipe_ingredients(recipe_id);
CREATE INDEX idx_recipe_ingredients_ingredient ON recipe_ingredients(ingredient_id);
CREATE INDEX idx_recipe_steps_recipe ON recipe_steps(recipe_id);
CREATE INDEX idx_recipe_tags_recipe ON recipe_tags(recipe_id);
CREATE INDEX idx_recipe_tags_tag ON recipe_tags(tag_id);

-- Trigger to update timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_ingredients_timestamp
BEFORE UPDATE ON ingredients
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_nutritional_info_timestamp
BEFORE UPDATE ON nutritional_info
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_recipes_timestamp
BEFORE UPDATE ON recipes
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_recipe_nutritional_summary_timestamp
BEFORE UPDATE ON recipe_nutritional_summary
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
