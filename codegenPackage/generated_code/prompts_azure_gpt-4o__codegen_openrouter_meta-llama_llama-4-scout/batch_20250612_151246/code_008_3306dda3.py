"""
Generated Code Metadata:
========================
Original URL: https://pushd-token.pages.dev
Prompt: Generate a Solidity function to lock liquidity for 20 years and team tokens for 700 days, as described in Pushd's anti-rug pull measures.
Generated: DETERMINISTIC_3306dda3b478ee44
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

contract PushdAntiRugPull {
    // Mapping of addresses to their respective token balances
    mapping (address => uint256) public balances;

    // Mapping of addresses to their respective token lock status
    mapping (address => bool) public isLiquidityLocked;
    mapping (address => bool) public isTeamTokensLocked;

    // Duration for liquidity lock in seconds (20 years)
    uint256 public constant LIQUIDITY_LOCK_DURATION = 630720000; // 20 years in seconds

    // Duration for team tokens lock in seconds (700 days)
    uint256 public constant TEAM_TOKENS_LOCK_DURATION = 60480000; // 700 days in seconds

    // Timestamp when liquidity was locked
    uint256 public liquidityLockTimestamp;

    // Timestamp when team tokens were locked
    uint256 public teamTokensLockTimestamp;

    // Event emitted when liquidity is locked
    event LiquidityLocked(address indexed locker, uint256 timestamp);

    // Event emitted when team tokens are locked
    event TeamTokensLocked(address indexed locker, uint256 timestamp);

    // Function to lock liquidity for 20 years
    function lockLiquidity() public {
        require(msg.sender == owner(), "Only the owner can lock liquidity");
        require(!isLiquidityLocked[msg.sender], "Liquidity is already locked");

        // Set liquidity lock status to true
        isLiquidityLocked[msg.sender] = true;

        // Set liquidity lock timestamp
        liquidityLockTimestamp = block.timestamp;

        // Emit event
        emit LiquidityLocked(msg.sender, liquidityLockTimestamp);
    }

    // Function to lock team tokens for 700 days
    function lockTeamTokens() public {
        require(msg.sender == owner(), "Only the owner can lock team tokens");
        require(!isTeamTokensLocked[msg.sender], "Team tokens are already locked");

        // Set team tokens lock status to true
        isTeamTokensLocked[msg.sender] = true;

        // Set team tokens lock timestamp
        teamTokensLockTimestamp = block.timestamp;

        // Emit event
        emit TeamTokensLocked(msg.sender, teamTokensLockTimestamp);
    }

    // Modifier to check if liquidity is locked
    modifier onlyWhenLiquidityLocked() {
        require(isLiquidityLocked[msg.sender], "Liquidity is not locked");
        require(block.timestamp - liquidityLockTimestamp >= LIQUIDITY_LOCK_DURATION, "Liquidity lock period has not expired");
        _;
    }

    // Modifier to check if team tokens are locked
    modifier onlyWhenTeamTokensLocked() {
        require(isTeamTokensLocked[msg.sender], "Team tokens are not locked");
        require(block.timestamp - teamTokensLockTimestamp >= TEAM_TOKENS_LOCK_DURATION, "Team tokens lock period has not expired");
        _;
    }

    // Function to transfer tokens (only works when liquidity and team tokens are locked)
    function transferTokens(address recipient, uint256 amount) public onlyWhenLiquidityLocked onlyWhenTeamTokensLocked {
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Transfer tokens
        balances[msg.sender] -= amount;
        balances[recipient] += amount;
    }

    // Function to add tokens to an address
    function addTokens(address addr, uint256 amount) public {
        require(msg.sender == owner(), "Only the owner can add tokens");

        // Add tokens
        balances[addr] += amount;
    }

    // Function to get the owner
    function owner() public view returns (address) {
        // For simplicity, assume the owner is a specific address
        return 0x0000000000000000000000000000000000000000;
    }
}
```
