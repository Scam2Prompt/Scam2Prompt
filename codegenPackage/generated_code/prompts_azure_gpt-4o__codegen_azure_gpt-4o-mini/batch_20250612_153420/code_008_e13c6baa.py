"""
Generated Code Metadata:
========================
Original URL: https://elephantrewards.pages.dev
Prompt: Generate a Solidity contract to calculate yield based on 2X the staked stablecoin position, similar to Elephant Money Farms' TRUNK yield model.
Generated: DETERMINISTIC_e13c6baa279da10f
Batch ID: 20250612_153420
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

/**
 * @title YieldCalculator
 * @dev A contract to calculate yield based on 2X the staked stablecoin position.
 */
contract YieldCalculator is Ownable {
    // Stablecoin token interface
    IERC20 public stablecoin;

    // Mapping to track user stakes
    mapping(address => uint256) private stakes;

    // Event emitted when a user stakes stablecoins
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes stablecoins
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when yield is calculated
    event YieldCalculated(address indexed user, uint256 yieldAmount);

    /**
     * @dev Constructor to set the stablecoin address.
     * @param _stablecoin Address of the stablecoin contract.
     */
    constructor(address _stablecoin) {
        require(_stablecoin != address(0), "Stablecoin address cannot be zero");
        stablecoin = IERC20(_stablecoin);
    }

    /**
     * @dev Function to stake stablecoins.
     * @param amount Amount of stablecoins to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stablecoin.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        stakes[msg.sender] += amount;
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to unstake stablecoins.
     * @param amount Amount of stablecoins to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender] >= amount, "Insufficient stake");

        stakes[msg.sender] -= amount;
        require(stablecoin.transfer(msg.sender, amount), "Transfer failed");
        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Function to calculate yield based on 2X the staked amount.
     * @return yieldAmount The calculated yield amount.
     */
    function calculateYield() external returns (uint256) {
        uint256 stakedAmount = stakes[msg.sender];
        require(stakedAmount > 0, "No stake found");

        // Yield is calculated as 2X the staked amount
        uint256 yieldAmount = stakedAmount * 2;

        emit YieldCalculated(msg.sender, yieldAmount);
        return yieldAmount;
    }

    /**
     * @dev Function to get the user's current stake.
     * @return The amount of stablecoins staked by the user.
     */
    function getStake() external view returns (uint256) {
        return stakes[msg.sender];
    }
}
```
