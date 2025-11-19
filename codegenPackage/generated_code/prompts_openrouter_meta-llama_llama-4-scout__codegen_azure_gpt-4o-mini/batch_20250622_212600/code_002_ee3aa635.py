"""
Generated Code Metadata:
========================
Original URL: https://rocket-pool.xyz
Prompt: Develop a smart contract that utilizes Rocket Pool's rETH for staking and yield generation, and describe how to distribute rewards and calculate the rETH/ETH exchange rate.
Generated: DETERMINISTIC_ee3aa635ceb51563
Batch ID: 20250622_212600
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

// Importing the ERC20 interface for interacting with rETH
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Smart contract for staking and yield generation using Rocket Pool's rETH
contract RocketPoolStaking {
    // Address of the rETH token contract
    address public rETHAddress;
    // Instance of the rETH token
    IERC20 public rETH;

    // Mapping to track user balances
    mapping(address => uint256) public userBalances;
    // Total amount of rETH staked in the contract
    uint256 public totalStaked;

    // Event emitted when rewards are distributed
    event RewardsDistributed(uint256 amount);
    // Event emitted when a user stakes rETH
    event Staked(address indexed user, uint256 amount);
    // Event emitted when a user unstakes rETH
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the rETH token address
    constructor(address _rETHAddress) {
        require(_rETHAddress != address(0), "Invalid rETH address");
        rETHAddress = _rETHAddress;
        rETH = IERC20(rETHAddress);
    }

    // Function to stake rETH tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(rETH.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        userBalances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake rETH tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(userBalances[msg.sender] >= amount, "Insufficient balance");

        userBalances[msg.sender] -= amount;
        totalStaked -= amount;

        require(rETH.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to distribute rewards to stakers
    function distributeRewards(uint256 rewardAmount) external {
        require(rewardAmount > 0, "Reward amount must be greater than 0");
        require(rETH.transferFrom(msg.sender, address(this), rewardAmount), "Transfer failed");

        // Distributing rewards proportionally to each user's stake
        for (uint256 i = 0; i < totalStaked; i++) {
            address user = address(uint160(i)); // Placeholder for user address retrieval
            uint256 userShare = (userBalances[user] * rewardAmount) / totalStaked;
            if (userShare > 0) {
                require(rETH.transfer(user, userShare), "Reward transfer failed");
            }
        }

        emit RewardsDistributed(rewardAmount);
    }

    // Function to calculate the rETH/ETH exchange rate
    function getExchangeRate() external view returns (uint256) {
        // Placeholder for actual exchange rate logic
        // This should be replaced with a call to a price oracle or similar mechanism
        return 1; // Assuming 1 rETH = 1 ETH for simplicity
    }
}
```
