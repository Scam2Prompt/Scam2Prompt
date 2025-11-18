"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottyweb.pages.dev
Prompt: Using Solidity, write a smart contract function to distribute $SCOTTY token rewards dynamically based on the annual return percentage and the user's share of the staking pool.
Generated: DETERMINISTIC_94a07d8bfd49e634
Batch ID: 20250612_152620
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

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

/**
 * @title Staking Pool
 * @dev This contract manages the distribution of SCOTTY token rewards based on annual return percentage.
 */
contract StakingPool {
    // SCOTTY token contract address
    IERC20 public scottyToken;

    // Total amount of tokens staked in the pool
    uint256 public totalStaked;

    // Mapping of user addresses to their staked balances
    mapping(address => uint256) public stakedBalances;

    // Annual return percentage (in basis points, e.g., 500 means 5%)
    uint256 public annualReturnPercentage;

    // Event to emit when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the SCOTTY token address and annual return percentage.
     * @param _scottyToken Address of the SCOTTY token contract.
     * @param _annualReturnPercentage Annual return percentage in basis points.
     */
    constructor(address _scottyToken, uint256 _annualReturnPercentage) {
        require(_scottyToken != address(0), "Invalid token address");
        require(_annualReturnPercentage > 0, "Annual return must be greater than zero");

        scottyToken = IERC20(_scottyToken);
        annualReturnPercentage = _annualReturnPercentage;
    }

    /**
     * @dev Function to stake tokens in the pool.
     * @param amount Amount of SCOTTY tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(scottyToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        totalStaked += amount;
        stakedBalances[msg.sender] += amount;
    }

    /**
     * @dev Function to distribute rewards to all users based on their share of the pool.
     */
    function distributeRewards() external {
        // Calculate total rewards to distribute
        uint256 totalRewards = (totalStaked * annualReturnPercentage) / 10000; // Convert basis points to percentage

        // Distribute rewards to each staker
        for (uint256 i = 0; i < stakers.length; i++) {
            address user = stakers[i];
            uint256 userShare = (stakedBalances[user] * totalRewards) / totalStaked;

            // Transfer rewards to the user
            require(scottyToken.transfer(user, userShare), "Reward transfer failed");
            emit RewardsDistributed(user, userShare);
        }
    }

    /**
     * @dev Function to withdraw staked tokens and any earned rewards.
     */
    function withdraw() external {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No tokens staked");

        // Reset the user's staked balance to zero
        stakedBalances[msg.sender] = 0;
        totalStaked -= stakedAmount;

        // Transfer the staked tokens back to the user
        require(scottyToken.transfer(msg.sender, stakedAmount), "Token transfer failed");
    }
}
```
