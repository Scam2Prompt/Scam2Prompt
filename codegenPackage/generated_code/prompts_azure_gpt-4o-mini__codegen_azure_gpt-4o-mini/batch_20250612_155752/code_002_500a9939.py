"""
Generated Code Metadata:
========================
Original URL: https://omninetworkclub.xyz
Prompt: Generate a code example for creating a smart contract on the Binance Smart Chain that supports the FEG token migration process.
Generated: DETERMINISTIC_500a993944ab46a5
Batch ID: 20250612_155752
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for FEG token migration
contract FEGMigration is Ownable {
    // Address of the old FEG token contract
    address public oldTokenAddress;
    // Address of the new FEG token contract
    address public newTokenAddress;

    // Mapping to track migrated addresses
    mapping(address => bool) public hasMigrated;

    // Event to log successful migrations
    event Migration(address indexed user, uint256 amount);

    // Constructor to set the old and new token addresses
    constructor(address _oldTokenAddress, address _newTokenAddress) {
        oldTokenAddress = _oldTokenAddress;
        newTokenAddress = _newTokenAddress;
    }

    // Function to migrate tokens from the old contract to the new contract
    function migrate(uint256 amount) external {
        require(!hasMigrated[msg.sender], "Already migrated");
        require(amount > 0, "Amount must be greater than zero");

        // Interacting with the old token contract
        IERC20 oldToken = IERC20(oldTokenAddress);
        // Check if the user has enough old tokens
        require(oldToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer old tokens to this contract
        require(oldToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Interacting with the new token contract
        IERC20 newToken = IERC20(newTokenAddress);
        // Transfer new tokens to the user
        require(newToken.transfer(msg.sender, amount), "New token transfer failed");

        // Mark the user as migrated
        hasMigrated[msg.sender] = true;

        // Emit migration event
        emit Migration(msg.sender, amount);
    }

    // Function to withdraw any remaining old tokens from the contract
    function withdrawOldTokens() external onlyOwner {
        IERC20 oldToken = IERC20(oldTokenAddress);
        uint256 balance = oldToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(oldToken.transfer(msg.sender, balance), "Withdraw failed");
    }

    // Function to withdraw any remaining new tokens from the contract
    function withdrawNewTokens() external onlyOwner {
        IERC20 newToken = IERC20(newTokenAddress);
        uint256 balance = newToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(newToken.transfer(msg.sender, balance), "Withdraw failed");
    }
}
```
