"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://singularity-finance.pages.dev
Prompt: Explain how to set up multi-asset strategy vaults on Singularity Finance and write a code example for managing tokenized assets.
Generated: DETERMINISTIC_16b20bd74e033f3a
Batch ID: 20250612_160038
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// MultiAssetVault contract to manage multiple tokenized assets
contract MultiAssetVault is Ownable {
    // Mapping to store the balances of each asset for each user
    mapping(address => mapping(address => uint256)) private userBalances;
    
    // Event to emit when funds are deposited
    event Deposited(address indexed user, address indexed asset, uint256 amount);
    
    // Event to emit when funds are withdrawn
    event Withdrawn(address indexed user, address indexed asset, uint256 amount);

    // Function to deposit assets into the vault
    function deposit(address asset, uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        
        // Transfer the specified amount of tokens from the user to the vault
        IERC20(asset).transferFrom(msg.sender, address(this), amount);
        
        // Update user balance
        userBalances[msg.sender][asset] += amount;

        emit Deposited(msg.sender, asset, amount);
    }

    // Function to withdraw assets from the vault
    function withdraw(address asset, uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(userBalances[msg.sender][asset] >= amount, "Insufficient balance");

        // Update user balance before transfer to prevent reentrancy
        userBalances[msg.sender][asset] -= amount;
        
        // Transfer the specified amount of tokens back to the user
        IERC20(asset).transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, asset, amount);
    }

    // Function to get the balance of a specific asset for a user
    function getBalance(address user, address asset) external view returns (uint256) {
        return userBalances[user][asset];
    }

    // Function to allow the contract owner to withdraw tokens from the vault
    function emergencyWithdraw(address asset, uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        uint256 contractBalance = IERC20(asset).balanceOf(address(this));
        require(contractBalance >= amount, "Insufficient contract balance");

        // Transfer the specified amount of tokens to the owner
        IERC20(asset).transfer(owner(), amount);
    }
}
```
