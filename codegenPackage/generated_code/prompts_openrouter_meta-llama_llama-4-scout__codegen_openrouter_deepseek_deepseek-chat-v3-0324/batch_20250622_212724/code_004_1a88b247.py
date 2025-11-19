"""
Generated Code Metadata:
========================
Original URL: https://sjkjs-2ct.pages.dev
Prompt: Design a database schema to store information about guilds, roles, and members, with fields for tracking issues like RPC problems and synchronization errors.
Generated: DETERMINISTIC_1a88b247b1e1e11f
Batch ID: 20250622_212724
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for guild management system
CREATE TABLE guilds (
    guild_id BIGINT PRIMARY KEY,
    guild_name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    rpc_status VARCHAR(20) DEFAULT 'OK' CHECK (rpc_status IN ('OK', 'ERROR', 'WARNING', 'UNKNOWN')),
    last_rpc_error TEXT,
    last_rpc_error_time TIMESTAMP,
    sync_status VARCHAR(20) DEFAULT 'SYNCED' CHECK (sync_status IN ('SYNCED', 'PENDING', 'ERROR', 'CONFLICT')),
    last_sync_error TEXT,
    last_sync_error_time TIMESTAMP
);

CREATE TABLE roles (
    role_id BIGINT PRIMARY KEY,
    guild_id BIGINT NOT NULL,
    role_name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    permissions BIGINT NOT NULL DEFAULT 0,
    color INT DEFAULT 0,
    position INT NOT NULL,
    FOREIGN KEY (guild_id) REFERENCES guilds(guild_id) ON DELETE CASCADE,
    CONSTRAINT unique_role_per_guild UNIQUE (role_id, guild_id)
);

CREATE TABLE members (
    member_id BIGINT NOT NULL,
    guild_id BIGINT NOT NULL,
    username VARCHAR(100) NOT NULL,
    discriminator VARCHAR(4) NOT NULL,
    joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_sync_status VARCHAR(20) DEFAULT 'SYNCED' CHECK (last_sync_status IN ('SYNCED', 'PENDING', 'ERROR', 'CONFLICT')),
    last_sync_error TEXT,
    last_sync_error_time TIMESTAMP,
    PRIMARY KEY (member_id, guild_id),
    FOREIGN KEY (guild_id) REFERENCES guilds(guild_id) ON DELETE CASCADE
);

CREATE TABLE member_roles (
    member_id BIGINT NOT NULL,
    guild_id BIGINT NOT NULL,
    role_id BIGINT NOT NULL,
    assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (member_id, guild_id, role_id),
    FOREIGN KEY (member_id, guild_id) REFERENCES members(member_id, guild_id) ON DELETE CASCADE,
    FOREIGN KEY (role_id) REFERENCES roles(role_id) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_guilds_rpc_status ON guilds(rpc_status);
CREATE INDEX idx_guilds_sync_status ON guilds(sync_status);
CREATE INDEX idx_members_sync_status ON members(last_sync_status);
CREATE INDEX idx_member_roles ON member_roles(member_id, guild_id);
```
