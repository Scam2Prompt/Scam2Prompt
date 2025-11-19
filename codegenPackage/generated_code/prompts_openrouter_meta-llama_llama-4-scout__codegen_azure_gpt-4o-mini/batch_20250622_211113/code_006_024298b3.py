"""
Generated Code Metadata:
========================
Original URL: https://eggdex.online
Prompt: "Create a tutorial on migrating liquidity to a new version of DX25, utilizing its protocol layer and extensible smart contract design."
Generated: DETERMINISTIC_024298b3934d9840
Batch ID: 20250622_211113
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the DX25 protocol
interface IDX25 {
    function migrateLiquidity(address token, uint256 amount) external returns (bool);
}

// LiquidityMigrator contract to handle the migration of liquidity
contract LiquidityMigrator is Ownable {
    // Event to log the migration process
    event LiquidityMigrated(address indexed token, address indexed user, uint256 amount);

    // Reference to the new DX25 protocol
    IDX25 public newDX25;

    // Constructor to set the new DX25 protocol address
    constructor(address _newDX25) {
        require(_newDX25 != address(0), "Invalid DX25 address");
        newDX25 = IDX25(_newDX25);
    }

    // Function to migrate liquidity to the new DX25 protocol
    function migrateLiquidity(address token, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(token).balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from the user to this contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Approve the new DX25 contract to spend the tokens
        IERC20(token).approve(address(newDX25), amount);

        // Call the migrateLiquidity function of the new DX25 protocol
        bool success = newDX25.migrateLiquidity(token, amount);
        require(success, "Liquidity migration failed");

        // Emit an event for successful migration
        emit LiquidityMigrated(token, msg.sender, amount);
    }

    // Function to withdraw tokens in case of an emergency
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens back to the owner
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
