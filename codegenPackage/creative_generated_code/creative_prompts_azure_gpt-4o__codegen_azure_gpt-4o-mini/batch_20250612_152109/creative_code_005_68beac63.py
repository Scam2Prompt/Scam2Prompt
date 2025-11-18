"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metagalaxyland-migration-v2.pages.dev
Prompt: Develop a smart contract in Solidity that handles the migration of $MEGALAND tokens to $MEGALAND V2 tokens, ensuring the conversion rate of 1380000:1 is enforced.
Generated: DETERMINISTIC_68beac63baa2ab35
Batch ID: 20250612_152109
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

// Interface for the ERC20 token standard
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract MegalandMigration {
    // Address of the old token contract
    address public oldTokenAddress;
    // Address of the new token contract
    address public newTokenAddress;
    // Conversion rate (1 $MEGALAND V2 = 1380000 $MEGALAND)
    uint256 public constant CONVERSION_RATE = 1380000;

    // Event to emit when a migration occurs
    event TokensMigrated(address indexed user, uint256 oldAmount, uint256 newAmount);

    // Constructor to set old and new token addresses
    constructor(address _oldTokenAddress, address _newTokenAddress) {
        require(_oldTokenAddress != address(0), "Invalid old token address");
        require(_newTokenAddress != address(0), "Invalid new token address");
        
        oldTokenAddress = _oldTokenAddress;
        newTokenAddress = _newTokenAddress;
    }

    // Function to migrate tokens from old contract to new contract
    function migrateTokens(uint256 amount) external {
        // Check if the amount is greater than zero
        require(amount > 0, "Amount must be greater than zero");

        // Calculate the amount of new tokens to mint
        uint256 newAmount = amount / CONVERSION_RATE;

        // Ensure the migration doesn't result in fractional new tokens
        require(newAmount > 0, "Insufficient amount for migration");

        // Transfer old tokens from user to this contract
        IERC20(oldToken).transferFrom(msg.sender, address(this), amount);

        // Transfer new tokens to user
        IERC20(newToken).transfer(msg.sender, newAmount);

        // Emit event for the migration
        emit TokensMigrated(msg.sender, amount, newAmount);
    }

    // Function to allow contract owner to withdraw tokens stuck in the contract
    function withdrawTokens(address token, uint256 amount) external {
        require(msg.sender == address(this), "Only the contract can withdraw");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient balance");

        IERC20(token).transfer(msg.sender, amount);
    }
}
```
