"""
Generated Code Metadata:
========================
Original URL: https://techsavvy3.pages.dev
Prompt: Generate code to implement a token migration feature using a blockchain and DeFi, referencing the need for a recovery wallet and TATs.
Generated: DETERMINISTIC_549e0d031470a506
Batch ID: 20250622_210806
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title TokenMigration
 * @dev Contract for migrating tokens from an old token to a new token
 * with recovery wallet functionality and TAT (Time-Action Triggers)
 */
contract TokenMigration is Ownable, ReentrancyGuard {
    IERC20 public oldToken;
    IERC20 public newToken;
    address public recoveryWallet;
    
    uint256 public migrationRate; // e.g., 1000 = 1:1 migration
    uint256 public migrationStartTime;
    uint256 public migrationEndTime;
    
    bool public migrationPaused;
    bool public recoveryMode;
    
    mapping(address => bool) public hasMigrated;
    mapping(address => uint256) public migrationTimestamps;
    
    event MigrationStarted(uint256 startTime, uint256 endTime);
    event TokensMigrated(address indexed user, uint256 oldAmount, uint256 newAmount);
    event MigrationPaused(bool paused);
    event RecoveryModeActivated();
    event RecoveryWalletChanged(address newWallet);
    event TokensRecovered(address token, uint256 amount);
    
    modifier duringMigrationPeriod() {
        require(block.timestamp >= migrationStartTime, "Migration not started");
        require(block.timestamp <= migrationEndTime, "Migration ended");
        _;
    }
    
    modifier whenNotPaused() {
        require(!migrationPaused, "Migration is paused");
        _;
    }
    
    constructor(
        address _oldToken,
        address _newToken,
        address _recoveryWallet,
        uint256 _migrationRate
    ) {
        require(_oldToken != address(0), "Invalid old token address");
        require(_newToken != address(0), "Invalid new token address");
        require(_recoveryWallet != address(0), "Invalid recovery wallet");
        
        oldToken = IERC20(_oldToken);
        newToken = IERC20(_newToken);
        recoveryWallet = _recoveryWallet;
        migrationRate = _migrationRate;
    }
    
    /**
     * @dev Start the migration process with specified duration
     * @param duration Duration of migration period in seconds
     */
    function startMigration(uint256 duration) external onlyOwner {
        require(migrationStartTime == 0, "Migration already started");
        migrationStartTime = block.timestamp;
        migrationEndTime = block.timestamp + duration;
        
        emit MigrationStarted(migrationStartTime, migrationEndTime);
    }
    
    /**
     * @dev Migrate old tokens to new tokens
     * @param amount Amount of old tokens to migrate
     */
    function migrateTokens(uint256 amount) external nonReentrant duringMigrationPeriod whenNotPaused {
        require(amount > 0, "Amount must be greater than 0");
        require(!hasMigrated[msg.sender], "Already migrated");
        
        uint256 allowance = oldToken.allowance(msg.sender, address(this));
        require(allowance >= amount, "Insufficient allowance");
        
        uint256 newTokenAmount = (amount * migrationRate) / 1000;
        require(newToken.balanceOf(address(this)) >= newTokenAmount, "Insufficient new token balance");
        
        hasMigrated[msg.sender] = true;
        migrationTimestamps[msg.sender] = block.timestamp;
        
        oldToken.transferFrom(msg.sender, address(this), amount);
        newToken.transfer(msg.sender, newTokenAmount);
        
        emit TokensMigrated(msg.sender, amount, newTokenAmount);
    }
    
    /**
     * @dev Pause or unpause the migration
     * @param paused Boolean indicating whether to pause or unpause
     */
    function setMigrationPaused(bool paused) external onlyOwner {
        migrationPaused = paused;
        emit MigrationPaused(paused);
    }
    
    /**
     * @dev Activate recovery mode (emergency only)
     */
    function activateRecoveryMode() external onlyOwner {
        recoveryMode = true;
        emit RecoveryModeActivated();
    }
    
    /**
     * @dev Change the recovery wallet address
     * @param newWallet New recovery wallet address
     */
    function changeRecoveryWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "Invalid wallet address");
        recoveryWallet = newWallet;
        emit RecoveryWalletChanged(newWallet);
    }
    
    /**
     * @dev Recover tokens in case of emergency
     * @param tokenAddress Address of token to recover
     */
    function recoverTokens(address tokenAddress) external onlyOwner {
        require(recoveryMode, "Recovery mode not active");
        
        IERC20 token = IERC20(tokenAddress);
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to recover");
        
        token.transfer(recoveryWallet, balance);
        emit TokensRecovered(tokenAddress, balance);
    }
    
    /**
     * @dev Extend migration period
     * @param additionalTime Additional time in seconds
     */
    function extendMigrationPeriod(uint256 additionalTime) external onlyOwner {
        require(block.timestamp <= migrationEndTime, "Migration already ended");
        migrationEndTime += additionalTime;
    }
    
    /**
     * @dev Get migration status for a user
     * @param user Address to check
     * @return hasMigrated Whether user has migrated
     * @return timestamp When user migrated (0 if not migrated)
     */
    function getUserMigrationStatus(address user) external view returns (bool, uint256) {
        return (hasMigrated[user], migrationTimestamps[user]);
    }
}
```
