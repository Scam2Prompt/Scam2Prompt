"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webbridge.pages.dev
Prompt: How can I implement token migration functionality in a DeFi application using the features described on the Tigris trading platform?
Generated: DETERMINISTIC_e34202d1de5ef2df
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TokenMigration is Ownable {
    // Event emitted when tokens are migrated
    event TokensMigrated(address indexed user, uint256 amount);

    // Old token contract address
    address public oldTokenAddress;

    // New token contract
    IERC20 public newToken;

    // Mapping to keep track of migrated users
    mapping(address => bool) public hasMigrated;

    // Constructor to set the old token address and new token
    constructor(address _oldTokenAddress, address _newTokenAddress) {
        oldTokenAddress = _oldTokenAddress;
        newToken = IERC20(_newTokenAddress);
    }

    // Function to migrate tokens
    function migrateTokens(uint256 amount) external {
        require(!hasMigrated[msg.sender], "Tokens already migrated");
        require(amount > 0, "Amount must be greater than zero");
        
        // Interact with the old token contract to transfer tokens to this contract
        IERC20 oldToken = IERC20(oldTokenAddress);
        require(oldToken.balanceOf(msg.sender) >= amount, "Insufficient balance");
        require(oldToken.allowance(msg.sender, address(this)) >= amount, "Allowance not set");

        // Transfer old tokens to this contract
        oldToken.transferFrom(msg.sender, address(this), amount);
        
        // Mint or transfer new tokens to the user
        // Here we assume newToken has a fixed supply and we are just transferring
        newToken.transfer(msg.sender, amount);

        // Mark the user as having migrated
        hasMigrated[msg.sender] = true;

        // Emit an event for tracking
        emit TokensMigrated(msg.sender, amount);
    }

    // Function for the owner to withdraw old tokens and new tokens
    function withdrawOldTokens() external onlyOwner {
        IERC20 oldToken = IERC20(oldTokenAddress);
        uint256 balance = oldToken.balanceOf(address(this));
        require(balance > 0, "No old tokens to withdraw");
        oldToken.transfer(owner(), balance);
    }

    function withdrawNewTokens() external onlyOwner {
        uint256 balance = newToken.balanceOf(address(this));
        require(balance > 0, "No new tokens to withdraw");
        newToken.transfer(owner(), balance);
    }
}
```
