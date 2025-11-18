"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elephantrewards.pages.dev
Prompt: Generate a Solidity contract to calculate yield based on 2X the staked stablecoin position, similar to Elephant Money Farms' TRUNK yield model.
Generated: DETERMINISTIC_e13c6baa279da10f
Batch ID: 20250612_153420
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

// Interface for the yield calculation
interface IYieldCalculator {
    function calculateYield(uint256 stakedAmount) external view returns (uint256);
}

// Main contract for yield calculation
contract YieldFarming is Ownable {
    // State variables
    IERC20 public stablecoin;  // The stablecoin used for staking
    uint256 public constant YIELD_MULTIPLIER = 2; // Yield multiplier constant

    // Event emitted when yield is calculated
    event YieldCalculated(address indexed user, uint256 yield);

    // Constructor to initialize the stablecoin address
    constructor(address _stablecoin) {
        require(_stablecoin != address(0), "Invalid stablecoin address");
        stablecoin = IERC20(_stablecoin);
    }

    // Function to stake stablecoin
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stablecoin.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer stablecoin from user to this contract
        stablecoin.transferFrom(msg.sender, address(this), amount);
    }

    // Function to calculate yield based on staked amount
    function calculateYield(uint256 stakedAmount) external view returns (uint256) {
        require(stakedAmount > 0, "Staked amount must be greater than 0");
        return stakedAmount * YIELD_MULTIPLIER; // Yield is calculated as 2X the staked amount
    }

    // Function to withdraw yield for a user
    function withdrawYield(uint256 stakedAmount) external {
        uint256 yield = calculateYield(stakedAmount);
        require(yield > 0, "Yield must be greater than 0");

        // Transfer yield to user
        stablecoin.transfer(msg.sender, yield);

        emit YieldCalculated(msg.sender, yield);
    }

    // Function to change the stablecoin address if needed
    function setStablecoin(address _stablecoin) external onlyOwner {
        require(_stablecoin != address(0), "Invalid stablecoin address");
        stablecoin = IERC20(_stablecoin);
    }
}
```
