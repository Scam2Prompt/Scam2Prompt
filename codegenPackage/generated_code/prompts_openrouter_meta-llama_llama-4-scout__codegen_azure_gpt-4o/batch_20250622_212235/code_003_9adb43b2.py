"""
Generated Code Metadata:
========================
Original URL: https://timcheese.pages.dev
Prompt: "Design a community platform database schema to track NFT ownership and access levels, similar to The Park mentioned in Tim Cheese."
Generated: DETERMINISTIC_9adb43b2f9c4db87
Batch ID: 20250622_212235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a community platform to track NFT ownership and access levels

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email for the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store NFT information
CREATE TABLE NFTs (
    NFTID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each NFT
    TokenID VARCHAR(100) NOT NULL UNIQUE, -- Unique token ID of the NFT
    ContractAddress VARCHAR(100) NOT NULL, -- Address of the smart contract
    MetadataURL VARCHAR(255),             -- URL pointing to the metadata of the NFT
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the NFT was added to the system
);

-- Table to track ownership of NFTs
CREATE TABLE NFTOwnership (
    OwnershipID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each ownership record
    UserID INT NOT NULL,                        -- Foreign key referencing Users table
    NFTID INT NOT NULL,                         -- Foreign key referencing NFTs table
    OwnershipStart TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when ownership started
    OwnershipEnd TIMESTAMP NULL,               -- Timestamp when ownership ended (NULL if still owned)
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is removed
    FOREIGN KEY (NFTID) REFERENCES NFTs(NFTID) ON DELETE CASCADE     -- Cascade delete if NFT is removed
);

-- Table to define access levels for users based on their NFT ownership
CREATE TABLE AccessLevels (
    AccessLevelID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each access level
    LevelName VARCHAR(50) NOT NULL UNIQUE,        -- Name of the access level (e.g., "Basic", "VIP")
    Description TEXT,                             -- Description of the access level
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the access level was created
);

-- Table to assign access levels to users based on their NFT ownership
CREATE TABLE UserAccess (
    UserAccessID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user access record
    UserID INT NOT NULL,                         -- Foreign key referencing Users table
    AccessLevelID INT NOT NULL,                  -- Foreign key referencing AccessLevels table
    NFTID INT NOT NULL,                          -- Foreign key referencing NFTs table
    GrantedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when access was granted
    RevokedAt TIMESTAMP NULL,                    -- Timestamp when access was revoked (NULL if still active)
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is removed
    FOREIGN KEY (AccessLevelID) REFERENCES AccessLevels(AccessLevelID) ON DELETE CASCADE, -- Cascade delete if access level is removed
    FOREIGN KEY (NFTID) REFERENCES NFTs(NFTID) ON DELETE CASCADE -- Cascade delete if NFT is removed
);

-- Indexes for performance optimization
CREATE INDEX idx_UserNFT ON NFTOwnership(UserID, NFTID); -- Index for quick lookup of user-NFT relationships
CREATE INDEX idx_UserAccess ON UserAccess(UserID, AccessLevelID); -- Index for quick lookup of user access levels
```
