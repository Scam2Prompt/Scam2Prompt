"""
Generated Code Metadata:
========================
Original URL: https://grandbase.co
Prompt: Write code for a DApp feature that verifies user balances before migration, inspired by Grandbase's safety measures.
Generated: DETERMINISTIC_8483431dc2047a4d
Batch ID: 20250612_151343
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

contract BalanceVerifier is Ownable, ReentrancyGuard {
    IERC20 public token;
    uint256 public migrationThreshold;
    bool public migrationActive;

    mapping(address => bool) public hasMigrated;
    mapping(address => uint256) public verifiedBalances;

    event BalanceVerified(address indexed user, uint256 balance);
    event MigrationCompleted(address indexed user, uint256 amount);
    event ThresholdUpdated(uint256 newThreshold);
    event MigrationStatusChanged(bool active);

    constructor(address _tokenAddress, uint256 _migrationThreshold) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
        migrationThreshold = _migrationThreshold;
        migrationActive = false;
    }

    modifier whenMigrationActive() {
        require(migrationActive, "Migration is not active");
        _;
    }

    function verifyBalance() external nonReentrant {
        require(!hasMigrated[msg.sender], "Already migrated");
        
        uint256 balance = token.balanceOf(msg.sender);
        require(balance >= migrationThreshold, "Balance below threshold");
        
        verifiedBalances[msg.sender] = balance;
        emit BalanceVerified(msg.sender, balance);
    }

    function migrate() external nonReentrant whenMigrationActive {
        require(!hasMigrated[msg.sender], "Already migrated");
        require(verifiedBalances[msg.sender] > 0, "Balance not verified");
        
        uint256 amount = verifiedBalances[msg.sender];
        hasMigrated[msg.sender] = true;
        
        bool success = token.transferFrom(msg.sender, address(this), amount);
        require(success, "Transfer failed");
        
        emit MigrationCompleted(msg.sender, amount);
    }

    function setMigrationThreshold(uint256 _newThreshold) external onlyOwner {
        require(_newThreshold > 0, "Threshold must be > 0");
        migrationThreshold = _newThreshold;
        emit ThresholdUpdated(_newThreshold);
    }

    function toggleMigrationStatus(bool _active) external onlyOwner {
        migrationActive = _active;
        emit MigrationStatusChanged(_active);
    }

    function withdrawTokens(address _to) external onlyOwner {
        uint256 contractBalance = token.balanceOf(address(this));
        require(contractBalance > 0, "No tokens to withdraw");
        
        bool success = token.transfer(_to, contractBalance);
        require(success, "Withdrawal failed");
    }
}
```
