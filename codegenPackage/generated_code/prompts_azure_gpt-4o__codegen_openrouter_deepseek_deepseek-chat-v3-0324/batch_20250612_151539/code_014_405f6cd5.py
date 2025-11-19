"""
Generated Code Metadata:
========================
Original URL: https://casinouniswap.com
Prompt: Create a database schema to store information about casinos, including bonuses, free spins, wagering requirements, and user ratings, as structured on Santa Claus Casino.
Generated: DETERMINISTIC_405f6cd5305aa7d4
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Santa Claus Casino information system

-- Enable UUID extension for unique identifiers
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Casinos table
CREATE TABLE casinos (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    website_url VARCHAR(255) NOT NULL,
    logo_url VARCHAR(255),
    license VARCHAR(100),
    established_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_casino_name UNIQUE (name)
);

-- Casino features table
CREATE TABLE casino_features (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    casino_id UUID NOT NULL,
    has_live_casino BOOLEAN DEFAULT FALSE,
    has_sports_betting BOOLEAN DEFAULT FALSE,
    has_mobile_app BOOLEAN DEFAULT FALSE,
    languages_supported VARCHAR(255)[],
    currencies_supported VARCHAR(255)[],
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_casino FOREIGN KEY (casino_id) REFERENCES casinos(id) ON DELETE CASCADE
);

-- Bonus types table
CREATE TABLE bonus_types (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(50) NOT NULL,
    description TEXT,
    CONSTRAINT unique_bonus_type UNIQUE (name)
);

-- Bonuses table
CREATE TABLE bonuses (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    casino_id UUID NOT NULL,
    bonus_type_id UUID NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    amount VARCHAR(50),
    is_exclusive BOOLEAN DEFAULT FALSE,
    min_deposit DECIMAL(10, 2),
    max_bonus DECIMAL(10, 2),
    valid_from TIMESTAMP WITH TIME ZONE,
    valid_to TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_casino FOREIGN KEY (casino_id) REFERENCES casinos(id) ON DELETE CASCADE,
    CONSTRAINT fk_bonus_type FOREIGN KEY (bonus_type_id) REFERENCES bonus_types(id)
);

-- Free spins table
CREATE TABLE free_spins (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    bonus_id UUID NOT NULL,
    amount INTEGER NOT NULL,
    slot_game VARCHAR(100),
    value_per_spin DECIMAL(10, 2),
    max_win DECIMAL(10, 2),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_bonus FOREIGN KEY (bonus_id) REFERENCES bonuses(id) ON DELETE CASCADE
);

-- Wagering requirements table
CREATE TABLE wagering_requirements (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    bonus_id UUID NOT NULL,
    multiplier DECIMAL(10, 2) NOT NULL,
    game_contribution JSONB, -- Stores game type contributions (e.g., slots:100%, table games:10%)
    max_bet DECIMAL(10, 2),
    time_limit_days INTEGER,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_bonus FOREIGN KEY (bonus_id) REFERENCES bonuses(id) ON DELETE CASCADE
);

-- User ratings table
CREATE TABLE user_ratings (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    casino_id UUID NOT NULL,
    user_id UUID NOT NULL, -- Assuming users are identified by UUID
    rating DECIMAL(2, 1) NOT NULL CHECK (rating >= 1 AND rating <= 5),
    review TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_casino FOREIGN KEY (casino_id) REFERENCES casinos(id) ON DELETE CASCADE,
    CONSTRAINT unique_user_rating UNIQUE (casino_id, user_id)
);

-- Payment methods table
CREATE TABLE payment_methods (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(50) NOT NULL,
    type VARCHAR(20) NOT NULL, -- e.g., 'ewallet', 'credit_card', 'crypto'
    CONSTRAINT unique_payment_method UNIQUE (name)
);

-- Casino payment methods junction table
CREATE TABLE casino_payment_methods (
    casino_id UUID NOT NULL,
    payment_method_id UUID NOT NULL,
    deposit_fee DECIMAL(5, 2) DEFAULT 0,
    withdrawal_fee DECIMAL(5, 2) DEFAULT 0,
    withdrawal_time VARCHAR(50),
    min_deposit DECIMAL(10, 2),
    min_withdrawal DECIMAL(10, 2),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (casino_id, payment_method_id),
    CONSTRAINT fk_casino FOREIGN KEY (casino_id) REFERENCES casinos(id) ON DELETE CASCADE,
    CONSTRAINT fk_payment_method FOREIGN KEY (payment_method_id) REFERENCES payment_methods(id)
);

-- Trigger to update the updated_at timestamp on row modification
CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create triggers for tables with updated_at columns
CREATE TRIGGER update_casinos_modtime
BEFORE UPDATE ON casinos
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_casino_features_modtime
BEFORE UPDATE ON casino_features
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_bonuses_modtime
BEFORE UPDATE ON bonuses
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_user_ratings_modtime
BEFORE UPDATE ON user_ratings
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_casino_payment_methods_modtime
BEFORE UPDATE ON casino_payment_methods
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

-- Insert common bonus types
INSERT INTO bonus_types (name, description) VALUES 
('Welcome Bonus', 'Bonus offered to new players upon registration or first deposit'),
('No Deposit Bonus', 'Bonus awarded without requiring a deposit'),
('Free Spins', 'Free spins on slot games'),
('Reload Bonus', 'Bonus offered on subsequent deposits'),
('Cashback', 'Percentage of losses returned to the player'),
('Loyalty Bonus', 'Bonus awarded to loyal players');

-- Insert common payment methods
INSERT INTO payment_methods (name, type) VALUES 
('Visa', 'credit_card'),
('Mastercard', 'credit_card'),
('Skrill', 'ewallet'),
('Neteller', 'ewallet'),
('PayPal', 'ewallet'),
('Bank Transfer', 'bank_transfer'),
('Bitcoin', 'crypto'),
('Ethereum', 'crypto'),
('Litecoin', 'crypto');
```
