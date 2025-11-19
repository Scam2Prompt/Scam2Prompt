"""
Generated Code Metadata:
========================
Original URL: https://revolt-cultdaoio-migrate.vercel.app
Prompt: "Generate a smart contract code snippet for migrating RVLT tokens to uRVLT, considering the opt-in pool and APR of 6.31%."
Generated: DETERMINISTIC_abcd57d5d209a675
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title TokenMigration
 * @dev Smart contract for migrating RVLT tokens to uRVLT tokens with an opt-in pool and APR of 6.31%.
 */
contract TokenMigration {
    // State variables
    address public owner; // Contract owner
    address public rvltToken; // Address of RVLT token contract
    address public urvltToken; // Address of uRVLT token contract
    uint256 public apr; // Annual Percentage Rate (APR) for opt-in pool
    uint256 public constant APR_MULTIPLIER = 10000; // Multiplier for APR calculation

    mapping(address => uint256) public optInBalances; // Tracks balances of users in the opt-in pool
    mapping(address => uint256) public optInTimestamps; // Tracks timestamps of opt-in for users

    // Events
    event TokensMigrated(address indexed user, uint256 rvltAmount, uint256 urvltAmount);
    event OptedIn(address indexed user, uint256 amount);
    event OptedOut(address indexed user, uint256 amount, uint256 rewards);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier validAddress(address _address) {
        require(_address != address(0), "Invalid address");
        _;
    }

    // Constructor
    constructor(address _rvltToken, address _urvltToken) validAddress(_rvltToken) validAddress(_urvltToken) {
        owner = msg.sender;
        rvltToken = _rvltToken;
        urvltToken = _urvltToken;
        apr = 631; // APR of 6.31% (scaled by APR_MULTIPLIER)
    }

    /**
     * @dev Migrate RVLT tokens to uRVLT tokens.
     * @param amount Amount of RVLT tokens to migrate.
     */
    function migrateTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer RVLT tokens from user to contract
        require(IERC20(rvltToken).transferFrom(msg.sender, address(this), amount), "RVLT transfer failed");

        // Mint equivalent uRVLT tokens to user
        require(IERC20(urvltToken).transfer(msg.sender, amount), "uRVLT transfer failed");

        emit TokensMigrated(msg.sender, amount, amount);
    }

    /**
     * @dev Opt-in to the pool for APR rewards.
     * @param amount Amount of uRVLT tokens to opt-in.
     */
    function optIn(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer uRVLT tokens from user to contract
        require(IERC20(urvltToken).transferFrom(msg.sender, address(this), amount), "uRVLT transfer failed");

        // Update opt-in balances and timestamps
        optInBalances[msg.sender] += amount;
        optInTimestamps[msg.sender] = block.timestamp;

        emit OptedIn(msg.sender, amount);
    }

    /**
     * @dev Opt-out of the pool and claim rewards.
     */
    function optOut() external {
        uint256 balance = optInBalances[msg.sender];
        require(balance > 0, "No balance in opt-in pool");

        // Calculate rewards based on APR and time in pool
        uint256 timeInPool = block.timestamp - optInTimestamps[msg.sender];
        uint256 rewards = (balance * apr * timeInPool) / (365 days * APR_MULTIPLIER);

        // Reset opt-in balances and timestamps
        optInBalances[msg.sender] = 0;
        optInTimestamps[msg.sender] = 0;

        // Transfer original balance and rewards to user
        require(IERC20(urvltToken).transfer(msg.sender, balance + rewards), "uRVLT transfer failed");

        emit OptedOut(msg.sender, balance, rewards);
    }

    /**
     * @dev Update APR value. Only callable by the owner.
     * @param newApr New APR value (scaled by APR_MULTIPLIER).
     */
    function updateApr(uint256 newApr) external onlyOwner {
        require(newApr > 0, "APR must be greater than zero");
        apr = newApr;
    }

    /**
     * @dev Emergency withdrawal of tokens from the contract. Only callable by the owner.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner validAddress(token) {
        require(IERC20(token).transfer(owner, amount), "Token transfer failed");
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
