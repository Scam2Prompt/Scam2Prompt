"""
Generated Code Metadata:
========================
Original URL: https://cryptomaniaapp.com
Prompt: Design a database schema to store and manage user data, trading history, and market data for a cryptocurrency trading platform like Crypto Mania, ensuring data security and scalability.
Generated: DETERMINISTIC_4ee5eeb6981504dd
Batch ID: 20250622_211850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Crypto Mania trading platform

-- Enable UUID extension for unique identifiers
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Users table to store user information
CREATE TABLE users (
    user_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    salt VARCHAR(255) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    phone_number VARCHAR(20),
    is_verified BOOLEAN DEFAULT FALSE,
    verification_token VARCHAR(255),
    verification_expires TIMESTAMP,
    two_factor_enabled BOOLEAN DEFAULT FALSE,
    two_factor_secret VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE,
    status VARCHAR(20) DEFAULT 'active' CHECK (status IN ('active', 'suspended', 'banned'))
);

-- User security logs for audit purposes
CREATE TABLE user_security_logs (
    log_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(user_id) ON DELETE CASCADE,
    action VARCHAR(50) NOT NULL,
    ip_address VARCHAR(45),
    user_agent TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- User wallets to store cryptocurrency balances
CREATE TABLE user_wallets (
    wallet_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(user_id) ON DELETE CASCADE,
    currency_symbol VARCHAR(10) NOT NULL,
    balance DECIMAL(30, 18) NOT NULL DEFAULT 0,
    locked_balance DECIMAL(30, 18) NOT NULL DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, currency_symbol)
);

-- Supported cryptocurrencies
CREATE TABLE currencies (
    currency_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    symbol VARCHAR(10) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    min_trade_amount DECIMAL(30, 18) NOT NULL,
    precision INTEGER NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Trading pairs
CREATE TABLE trading_pairs (
    pair_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    base_currency VARCHAR(10) NOT NULL REFERENCES currencies(symbol),
    quote_currency VARCHAR(10) NOT NULL REFERENCES currencies(symbol),
    is_active BOOLEAN DEFAULT TRUE,
    min_trade_amount DECIMAL(30, 18) NOT NULL,
    price_precision INTEGER NOT NULL,
    amount_precision INTEGER NOT NULL,
    fee_percent DECIMAL(10, 8) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(base_currency, quote_currency)
);

-- Orders table
CREATE TABLE orders (
    order_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(user_id) ON DELETE CASCADE,
    pair_id UUID REFERENCES trading_pairs(pair_id),
    order_type VARCHAR(10) NOT NULL CHECK (order_type IN ('limit', 'market', 'stop_limit')),
    side VARCHAR(4) NOT NULL CHECK (side IN ('buy', 'sell')),
    price DECIMAL(30, 18),
    amount DECIMAL(30, 18) NOT NULL,
    filled_amount DECIMAL(30, 18) DEFAULT 0,
    status VARCHAR(20) NOT NULL DEFAULT 'open' CHECK (status IN ('open', 'filled', 'partially_filled', 'cancelled', 'rejected')),
    time_in_force VARCHAR(20) DEFAULT 'GTC' CHECK (time_in_force IN ('GTC', 'IOC', 'FOK')),
    stop_price DECIMAL(30, 18),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Trades table (executed orders)
CREATE TABLE trades (
    trade_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    order_id UUID REFERENCES orders(order_id),
    pair_id UUID REFERENCES trading_pairs(pair_id),
    maker_order_id UUID REFERENCES orders(order_id),
    taker_order_id UUID REFERENCES orders(order_id),
    price DECIMAL(30, 18) NOT NULL,
    amount DECIMAL(30, 18) NOT NULL,
    fee DECIMAL(30, 18) NOT NULL,
    fee_currency VARCHAR(10) NOT NULL,
    side VARCHAR(4) NOT NULL CHECK (side IN ('buy', 'sell')),
    executed_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Deposits table
CREATE TABLE deposits (
    deposit_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(user_id) ON DELETE CASCADE,
    currency_symbol VARCHAR(10) NOT NULL REFERENCES currencies(symbol),
    amount DECIMAL(30, 18) NOT NULL,
    tx_hash VARCHAR(255) UNIQUE,
    address VARCHAR(255),
    status VARCHAR(20) NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'completed', 'failed')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP WITH TIME ZONE
);

-- Withdrawals table
CREATE TABLE withdrawals (
    withdrawal_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(user_id) ON DELETE CASCADE,
    currency_symbol VARCHAR(10) NOT NULL REFERENCES currencies(symbol),
    amount DECIMAL(30, 18) NOT NULL,
    fee DECIMAL(30, 18) NOT NULL,
    address VARCHAR(255) NOT NULL,
    tx_hash VARCHAR(255),
    status VARCHAR(20) NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'processing', 'completed', 'failed', 'cancelled')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP WITH TIME ZONE
);

-- Market data (OHLCV)
CREATE TABLE ohlcv_data (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    pair_id UUID REFERENCES trading_pairs(pair_id),
    timeframe VARCHAR(10) NOT NULL CHECK (timeframe IN ('1m', '5m', '15m', '30m', '1h', '4h', '1d', '1w')),
    timestamp TIMESTAMP WITH TIME ZONE NOT NULL,
    open DECIMAL(30, 18) NOT NULL,
    high DECIMAL(30, 18) NOT NULL,
    low DECIMAL(30, 18) NOT NULL,
    close DECIMAL(30, 18) NOT NULL,
    volume DECIMAL(30, 18) NOT NULL,
    UNIQUE(pair_id, timeframe, timestamp)
);

-- Indexes for performance
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_orders_pair_id ON orders(pair_id);
CREATE INDEX idx_orders_status ON orders(status);
CREATE INDEX idx_trades_pair_id ON trades(pair_id);
CREATE INDEX idx_trades_executed_at ON trades(executed_at);
CREATE INDEX idx_ohlcv_data_pair_id ON ohlcv_data(pair_id);
CREATE INDEX idx_ohlcv_data_timestamp ON ohlcv_data(timestamp);
CREATE INDEX idx_user_wallets_user_id ON user_wallets(user_id);

-- Function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for automatic updated_at
CREATE TRIGGER update_users_modtime
BEFORE UPDATE ON users
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_user_wallets_modtime
BEFORE UPDATE ON user_wallets
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_orders_modtime
BEFORE UPDATE ON orders
FOR EACH ROW EXECUTE FUNCTION update_modified_column();
```
