"""
Generated Code Metadata:
========================
Original URL: https://bodegajeanbousquet.com.ar
Prompt: Design a database schema to store menu and wine information for a restaurant and winery like Bodega Jean Bousquet, including tables for menu items, wine varieties, and customer reservations.
Generated: DETERMINISTIC_ea50fe1a931b9de1
Batch ID: 20250622_212059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for restaurant and winery management system

-- Table to store wine varieties
CREATE TABLE wine_varieties (
    wine_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    type VARCHAR(50) NOT NULL CHECK (type IN ('Red', 'White', 'Rosé', 'Sparkling', 'Dessert')),
    vintage INTEGER NOT NULL,
    region VARCHAR(100) NOT NULL,
    description TEXT,
    alcohol_content DECIMAL(4, 2),
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INTEGER NOT NULL DEFAULT 0,
    is_available BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table to store food categories
CREATE TABLE food_categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    display_order INTEGER NOT NULL
);

-- Table to store menu items
CREATE TABLE menu_items (
    item_id SERIAL PRIMARY KEY,
    category_id INTEGER REFERENCES food_categories(category_id),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    is_vegetarian BOOLEAN NOT NULL DEFAULT FALSE,
    is_vegan BOOLEAN NOT NULL DEFAULT FALSE,
    is_gluten_free BOOLEAN NOT NULL DEFAULT FALSE,
    is_available BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table to store wine and food pairings
CREATE TABLE wine_pairings (
    pairing_id SERIAL PRIMARY KEY,
    wine_id INTEGER REFERENCES wine_varieties(wine_id),
    item_id INTEGER REFERENCES menu_items(item_id),
    pairing_description TEXT,
    strength VARCHAR(20) CHECK (strength IN ('Strong', 'Medium', 'Weak')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table to store customers
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table to store reservations
CREATE TABLE reservations (
    reservation_id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id),
    reservation_date DATE NOT NULL,
    reservation_time TIME NOT NULL,
    party_size INTEGER NOT NULL CHECK (party_size > 0),
    table_number VARCHAR(20),
    special_requests TEXT,
    status VARCHAR(20) NOT NULL DEFAULT 'Confirmed' CHECK (status IN ('Confirmed', 'Cancelled', 'No-show', 'Completed')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table to store orders (for both food and wine)
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    reservation_id INTEGER REFERENCES reservations(reservation_id),
    order_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) NOT NULL DEFAULT 'Pending' CHECK (status IN ('Pending', 'In Progress', 'Completed', 'Cancelled')),
    total_amount DECIMAL(10, 2) NOT NULL,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table to store order items (both food and wine)
CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(order_id),
    item_id INTEGER REFERENCES menu_items(item_id),
    wine_id INTEGER REFERENCES wine_varieties(wine_id),
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    special_instructions TEXT,
    price_at_order DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table to store staff members
CREATE TABLE staff (
    staff_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    role VARCHAR(50) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table to store inventory of wine bottles
CREATE TABLE wine_inventory (
    inventory_id SERIAL PRIMARY KEY,
    wine_id INTEGER REFERENCES wine_varieties(wine_id),
    quantity INTEGER NOT NULL CHECK (quantity >= 0),
    location VARCHAR(100),
    last_updated TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table to store wine tasting events
CREATE TABLE tasting_events (
    event_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    event_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    max_attendees INTEGER NOT NULL,
    price_per_person DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table to store tasting event registrations
CREATE TABLE tasting_registrations (
    registration_id SERIAL PRIMARY KEY,
    event_id INTEGER REFERENCES tasting_events(event_id),
    customer_id INTEGER REFERENCES customers(customer_id),
    num_attendees INTEGER NOT NULL CHECK (num_attendees > 0),
    total_amount DECIMAL(10, 2) NOT NULL,
    payment_status VARCHAR(20) NOT NULL DEFAULT 'Pending' CHECK (payment_status IN ('Pending', 'Paid', 'Cancelled', 'Refunded')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Function to update timestamp on record update
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers to update timestamps
CREATE TRIGGER update_wine_varieties_timestamp
BEFORE UPDATE ON wine_varieties
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_menu_items_timestamp
BEFORE UPDATE ON menu_items
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_customers_timestamp
BEFORE UPDATE ON customers
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_reservations_timestamp
BEFORE UPDATE ON reservations
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_orders_timestamp
BEFORE UPDATE ON orders
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_staff_timestamp
BEFORE UPDATE ON staff
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_tasting_events_timestamp
BEFORE UPDATE ON tasting_events
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_tasting_registrations_timestamp
BEFORE UPDATE ON tasting_registrations
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
