"""
Generated Code Metadata:
========================
Original URL: https://eursj.com
Prompt: Generate a Solidity smart contract compatible with Ethereum 2.0 that implements a basic staking mechanism with reward distribution.
Generated: DETERMINISTIC_27dcfc15d2f1bfa7
Batch ID: 20250612_151207
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

// Importing OpenZeppelin's SafeMath library for safe arithmetic operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract interface
interface IStaking {
    function stake(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function claimRewards() external;
}

// Basic Staking Contract
contract StakingContract is IStaking, Ownable {
    using SafeMath for uint256;

    // Struct to hold user staking information
    struct Staker {
        uint256 amountStaked;
        uint256 rewards;
        uint256 lastStakedTime;
    }

    // Mapping of user addresses to their staking information
    mapping(address => Staker) private stakers;

    // Total staked amount in the contract
    uint256 public totalStaked;

    // Reward rate per second (in wei)
    uint256 public rewardRate = 1e18; // 1 token per second for simplicity

    // Event emitted when a user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Function to stake tokens
    function stake(uint256 amount) external override {
        require(amount > 0, "Amount must be greater than 0");
        
        // Update the staker's rewards before staking
        updateRewards(msg.sender);

        // Transfer tokens from the user to the contract
        // Assuming the contract has been approved to spend the tokens
        // Replace `IERC20(tokenAddress).transferFrom` with actual token transfer logic
        // IERC20(tokenAddress).transferFrom(msg.sender, address(this), amount);

        // Update staker's information
        stakers[msg.sender].amountStaked = stakers[msg.sender].amountStaked.add(amount);
        stakers[msg.sender].lastStakedTime = block.timestamp;
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external override {
        require(amount > 0, "Amount must be greater than 0");
        require(stakers[msg.sender].amountStaked >= amount, "Insufficient staked amount");

        // Update the staker's rewards before withdrawing
        updateRewards(msg.sender);

        // Transfer tokens back to the user
        // Replace `IERC20(tokenAddress).transfer` with actual token transfer logic
        // IERC20(tokenAddress).transfer(msg.sender, amount);

        // Update staker's information
        stakers[msg.sender].amountStaked = stakers[msg.sender].amountStaked.sub(amount);
        totalStaked = totalStaked.sub(amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external override {
        updateRewards(msg.sender);
        uint256 rewardAmount = stakers[msg.sender].rewards;
        require(rewardAmount > 0, "No rewards to claim");

        // Reset rewards to zero after claiming
        stakers[msg.sender].rewards = 0;

        // Transfer rewards to the user
        // Replace `IERC20(tokenAddress).transfer` with actual token transfer logic
        // IERC20(tokenAddress).transfer(msg.sender, rewardAmount);

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    // Internal function to update rewards for a staker
    function updateRewards(address stakerAddress) internal {
        Staker storage staker = stakers[stakerAddress];
        uint256 timeStaked = block.timestamp.sub(staker.lastStakedTime);
        uint256 earnedRewards = timeStaked.mul(staker.amountStaked).mul(rewardRate).div(1e18);
        staker.rewards = staker.rewards.add(earnedRewards);
        staker.lastStakedTime = block.timestamp;
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to get the staker's information
    function getStakerInfo(address stakerAddress) external view returns (uint256, uint256, uint256) {
        Staker memory staker = stakers[stakerAddress];
        return (staker.amountStaked, staker.rewards, staker.lastStakedTime);
    }
}
```
