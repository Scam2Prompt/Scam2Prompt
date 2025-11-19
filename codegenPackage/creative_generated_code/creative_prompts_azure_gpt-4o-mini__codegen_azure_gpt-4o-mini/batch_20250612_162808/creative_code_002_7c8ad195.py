"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yieldeth.org
Prompt: Explain how to use yieldETH's smart contracts for staking ETH and minimizing penalty risks.
Generated: DETERMINISTIC_7c8ad1950138576e
Batch ID: 20250612_162808
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

// Import the necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Yield ETH Staking Contract
interface IYieldETH {
    function stake(uint256 amount) external;
    function unstake(uint256 amount) external;
    function getStakedAmount(address user) external view returns (uint256);
    function getRewards(address user) external view returns (uint256);
}

contract YieldETHStaking is Ownable {
    // Address of the Yield ETH contract
    IYieldETH public yieldETH;

    // Event emitted when ETH is staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when ETH is unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Error codes
    error InsufficientBalance(uint256 requested, uint256 available);
    error InvalidAmount(uint256 amount);

    // Constructor to set the Yield ETH contract address
    constructor(address _yieldETHAddress) {
        yieldETH = IYieldETH(_yieldETHAddress);
    }

    // Function to stake ETH
    function stakeETH(uint256 amount) external {
        // Check if amount is greater than zero
        if (amount <= 0) revert InvalidAmount(amount);

        // Check if the sender has enough ETH
        uint256 balance = address(this).balance;
        if (amount > balance) revert InsufficientBalance(amount, balance);

        // Stake the provided amount
        yieldETH.stake(amount);

        // Emit the Staked event
        emit Staked(msg.sender, amount);
    }

    // Function to unstake ETH
    function unstakeETH(uint256 amount) external {
        // Check if amount is greater than zero
        if (amount <= 0) revert InvalidAmount(amount);

        // Get the user's staked amount
        uint256 stakedAmount = yieldETH.getStakedAmount(msg.sender);
        if (amount > stakedAmount) revert InsufficientBalance(amount, stakedAmount);

        // Unstake the provided amount
        yieldETH.unstake(amount);

        // Emit the Unstaked event
        emit Unstaked(msg.sender, amount);
    }

    // Function to check staked amount
    function checkStakedAmount() external view returns (uint256) {
        return yieldETH.getStakedAmount(msg.sender);
    }

    // Function to check rewards
    function checkRewards() external view returns (uint256) {
        return yieldETH.getRewards(msg.sender);
    }

    // Fallback function to accept ETH
    receive() external payable {}
}
```
