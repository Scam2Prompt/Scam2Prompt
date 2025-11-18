"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copycoden.pages.dev
Prompt: Write a Solidity contract that receives Ether payments and stores liquidity information, following the structure of the Oneinch Slippage Bot.
Generated: DETERMINISTIC_834aec60144e459d
Batch ID: 20250612_145917
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

// A contract for managing liquidity and receiving Ether payments
contract LiquidityManager {
    // State variable to store the total liquidity
    uint256 public totalLiquidity;

    // Event to log the liquidity added
    event LiquidityAdded(address indexed user, uint256 amount);
    
    // Event to log the liquidity withdrawn
    event LiquidityWithdrawn(address indexed user, uint256 amount);
    
    // Mapping to track user liquidity contributions
    mapping(address => uint256) public userLiquidity;

    // Modifier to check if the sender has sufficient liquidity
    modifier hasLiquidity(uint256 amount) {
        require(userLiquidity[msg.sender] >= amount, "Insufficient liquidity");
        _;
    }

    // Function to receive Ether. This function is called when the contract receives Ether.
    receive() external payable {
        require(msg.value > 0, "Must send non-zero Ether");
        _addLiquidity(msg.sender, msg.value);
    }

    // Internal function to add liquidity to the user's balance and update total liquidity
    function _addLiquidity(address user, uint256 amount) internal {
        totalLiquidity += amount;
        userLiquidity[user] += amount;

        emit LiquidityAdded(user, amount);
    }

    // Function to withdraw liquidity
    function withdrawLiquidity(uint256 amount) external hasLiquidity(amount) {
        userLiquidity[msg.sender] -= amount;
        totalLiquidity -= amount;

        // Transfer Ether back to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        emit LiquidityWithdrawn(msg.sender, amount);
    }

    // Function to get user liquidity
    function getUserLiquidity(address user) external view returns (uint256) {
        return userLiquidity[user];
    }

    // Function to get total contract liquidity
    function getTotalLiquidity() external view returns (uint256) {
        return totalLiquidity;
    }
}
```
