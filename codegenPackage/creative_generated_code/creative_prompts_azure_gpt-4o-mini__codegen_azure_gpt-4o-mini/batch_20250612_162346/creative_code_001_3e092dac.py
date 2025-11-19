"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimdogecoin20-portal.pages.dev
Prompt: Write a smart contract code snippet for staking DOGE20 tokens on the Ethereum blockchain that distributes rewards based on the percentage of the staking pool.
Generated: DETERMINISTIC_3e092dac493b8376
Batch ID: 20250612_162346
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract Staking {
    using SafeMath for uint256;

    // Token being staked
    IERC20 public stakingToken;

    // Structure to hold user staking information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardsEarned;
        uint256 lastUpdate;
    }

    // Mapping to track each staker's information
    mapping(address => Staker) public stakers;

    // Total amount of tokens staked in the contract
    uint256 public totalStaked;

    // Rewards rate per token staked per second (in wei)
    uint256 public rewardsRate;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    
    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);
    
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the staking contract with the token address and rewards rate
    constructor(IERC20 _stakingToken, uint256 _rewardsRate) {
        stakingToken = _stakingToken;
        rewardsRate = _rewardsRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Update staker's rewards before staking new tokens
        _updateRewards(msg.sender);

        // Transfer tokens from the staker to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);
        
        // Update staker's information
        stakers[msg.sender].amountStaked = stakers[msg.sender].amountStaked.add(amount);
        totalStaked = totalStaked.add(amount);
        
        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakers[msg.sender].amountStaked >= amount, "Insufficient staked amount");

        // Update staker's rewards before withdrawing
        _updateRewards(msg.sender);

        // Transfer staked tokens back to the staker
        stakingToken.transfer(msg.sender, amount);
        
        // Update staker's information
        stakers[msg.sender].amountStaked = stakers[msg.sender].amountStaked.sub(amount);
        totalStaked = totalStaked.sub(amount);
        
        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        // Update staker's rewards before claiming
        _updateRewards(msg.sender);
        
        uint256 rewards = stakers[msg.sender].rewardsEarned;
        require(rewards > 0, "No rewards to claim");

        // Reset earned rewards and transfer to the staker
        stakers[msg.sender].rewardsEarned = 0;
        stakingToken.transfer(msg.sender, rewards);
        
        emit RewardsClaimed(msg.sender, rewards);
    }

    // Internal function to update rewards based on the staked amount and time
    function _updateRewards(address user) internal {
        Staker storage staker = stakers[user];
        if (staker.amountStaked > 0) {
            uint256 timeStaked = block.timestamp.sub(staker.lastUpdate);
            uint256 earnedRewards = timeStaked.mul(staker.amountStaked).mul(rewardsRate).div(1 ether);
            staker.rewardsEarned = staker.rewardsEarned.add(earnedRewards);
        }
        // Update the last updated time
        staker.lastUpdate = block.timestamp;
    }
}
```
