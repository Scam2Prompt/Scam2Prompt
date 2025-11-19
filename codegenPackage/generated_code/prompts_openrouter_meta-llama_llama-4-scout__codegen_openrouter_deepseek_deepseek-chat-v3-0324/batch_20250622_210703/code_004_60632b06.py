"""
Generated Code Metadata:
========================
Original URL: https://bekon.rs
Prompt: Design a database schema to store information about meat products, including types (e.g., fresh meat, sausages, dry products) and recipes, inspired by Bekon Promet's product offerings.
Generated: DETERMINISTIC_60632b0620af7fba
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for meat products management system

-- Enable UUID extension if not already enabled
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Product categories table
CREATE TABLE product_categories (
    category_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_category_name UNIQUE (name)
);

-- Product types table
CREATE TABLE product_types (
    type_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    category_id UUID NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    storage_requirements TEXT,
    shelf_life_days INTEGER,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_category FOREIGN KEY (category_id) REFERENCES product_categories(category_id) ON DELETE CASCADE,
    CONSTRAINT unique_type_name_per_category UNIQUE (category_id, name)
);

-- Ingredients table
CREATE TABLE ingredients (
    ingredient_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    is_allergen BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_ingredient_name UNIQUE (name)
);

-- Products table
CREATE TABLE products (
    product_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    type_id UUID NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    weight_grams INTEGER,
    price DECIMAL(10, 2),
    is_available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_type FOREIGN KEY (type_id) REFERENCES product_types(type_id) ON DELETE CASCADE,
    CONSTRAINT unique_product_name_per_type UNIQUE (type_id, name)
);

-- Recipes table
CREATE TABLE recipes (
    recipe_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    product_id UUID NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    preparation_time_minutes INTEGER,
    cooking_time_minutes INTEGER,
    difficulty_level VARCHAR(20) CHECK (difficulty_level IN ('easy', 'medium', 'hard')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    CONSTRAINT unique_recipe_name_per_product UNIQUE (product_id, name)
);

-- Recipe ingredients junction table
CREATE TABLE recipe_ingredients (
    recipe_ingredient_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    recipe_id UUID NOT NULL,
    ingredient_id UUID NOT NULL,
    quantity DECIMAL(10, 2),
    unit VARCHAR(20) NOT NULL,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_recipe FOREIGN KEY (recipe_id) REFERENCES recipes(recipe_id) ON DELETE CASCADE,
    CONSTRAINT fk_ingredient FOREIGN KEY (ingredient_id) REFERENCES ingredients(ingredient_id) ON DELETE CASCADE,
    CONSTRAINT unique_ingredient_per_recipe UNIQUE (recipe_id, ingredient_id)
);

-- Nutritional information table
CREATE TABLE nutritional_info (
    nutritional_info_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    product_id UUID NOT NULL,
    calories_kcal DECIMAL(10, 2),
    protein_g DECIMAL(10, 2),
    fat_g DECIMAL(10, 2),
    carbohydrates_g DECIMAL(10, 2),
    sodium_mg DECIMAL(10, 2),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    CONSTRAINT unique_nutritional_info_per_product UNIQUE (product_id)
);

-- Product images table
CREATE TABLE product_images (
    image_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    product_id UUID NOT NULL,
    image_url TEXT NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    alt_text VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX idx_product_type ON products(type_id);
CREATE INDEX idx_recipe_product ON recipes(product_id);
CREATE INDEX idx_recipe_ingredient_recipe ON recipe_ingredients(recipe_id);
CREATE INDEX idx_recipe_ingredient_ingredient ON recipe_ingredients(ingredient_id);
CREATE INDEX idx_nutritional_info_product ON nutritional_info(product_id);
CREATE INDEX idx_product_images_product ON product_images(product_id);

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create triggers for all tables with updated_at field
DO $$
DECLARE
    t record;
BEGIN
    FOR t IN 
        SELECT table_name 
        FROM information_schema.columns 
        WHERE column_name = 'updated_at' 
        AND table_schema = 'public'
    LOOP
        EXECUTE format('DROP TRIGGER IF EXISTS update_%s_timestamp ON %I', t.table_name, t.table_name);
        EXECUTE format('CREATE TRIGGER update_%s_timestamp
                        BEFORE UPDATE ON %I
                        FOR EACH ROW EXECUTE FUNCTION update_timestamp()', 
                        t.table_name, t.table_name);
    END LOOP;
END;
$$ LANGUAGE plpgsql;
```
