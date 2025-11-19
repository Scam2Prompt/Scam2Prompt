"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omninetworkclub.xyz
Prompt: Generate a code example for creating a smart contract on the Binance Smart Chain that supports the FEG token migration process.
Generated: DETERMINISTIC_500a993944ab46a5
Batch ID: 20250612_155752
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

// Importing the necessary interfaces for ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// FEGTokenMigration contract allows users to migrate their FEG tokens to a new contract
contract FEGTokenMigration is Ownable {
    // Address of the old FEG token contract
    address public oldTokenAddress;
    
    // Address of the new FEG token contract
    address public newTokenAddress;

    // Mapping to track if an address has migrated their tokens
    mapping(address => bool) public hasMigrated;

    // Event emitted when tokens are migrated
    event TokensMigrated(address indexed user, uint256 amount);

    // Constructor to initialize the old and new token addresses
    constructor(address _oldTokenAddress, address _newTokenAddress) {
        oldTokenAddress = _oldTokenAddress;
        newTokenAddress = _newTokenAddress;
    }

    // Function to migrate tokens from the old contract to the new contract
    function migrateTokens() external {
        require(!hasMigrated[msg.sender], "Tokens have already been migrated");
        
        // Fetching balance from the old token contract
        IERC20 oldToken = IERC20(oldTokenAddress);
        uint256 amount = oldToken.balanceOf(msg.sender);
        require(amount > 0, "No tokens to migrate");

        // Transfer old tokens to this contract
        bool success = oldToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Mint new tokens to the user (in a real contract, you would handle minting in a safe manner)
        IERC20 newToken = IERC20(newTokenAddress);
        // Assuming the new token contract has an appropriate mint function
        // This would typically require the newToken contract to inherit from a Mintable ERC20 contract
        // newToken.mint(msg.sender, amount); // Uncomment if mint function exists 

        // Mark the user as migrated
        hasMigrated[msg.sender] = true;

        // Emit an event for logging
        emit TokensMigrated(msg.sender, amount);
    }

    // Function for the contract owner to withdraw old tokens from the contract
    function withdrawOldTokens() external onlyOwner {
        IERC20 oldToken = IERC20(oldTokenAddress);
        uint256 balance = oldToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        // Transfer all old tokens to the owner
        bool success = oldToken.transfer(msg.sender, balance);
        require(success, "Withdraw failed");
    }
    
    // Function for the contract owner to withdraw new tokens from the contract
    function withdrawNewTokens() external onlyOwner {
        IERC20 newToken = IERC20(newTokenAddress);
        uint256 balance = newToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        // Transfer all new tokens to the owner
        bool success = newToken.transfer(msg.sender, balance);
        require(success, "Withdraw failed");
    }
}
```
