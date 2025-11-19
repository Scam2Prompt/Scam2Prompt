"""
Generated Code Metadata:
========================
Original URL: https://mememoguls-de.web.app
Prompt: Develop a staking pool smart contract in Solidity that allows users to stake $MGLS tokens and earn rewards based on their share of the pool.
Generated: DETERMINISTIC_2429d41ecd2e9e55
Batch ID: 20250612_152739
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

// Importing the ERC20 interface for the $MGLS token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// StakingPool contract allows users to stake $MGLS tokens and earn rewards
contract StakingPool is Ownable {
    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
    }

    // Mapping of staker addresses to their information
    mapping(address => Staker) public stakers;

    // Total amount of tokens staked in the pool
    uint256 public totalStaked;

    // The $MGLS token contract
    IERC20 public mglsToken;

    // Reward per token staked (in wei)
    uint256 public rewardPerToken;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the staking pool with the $MGLS token address
    constructor(IERC20 _mglsToken) {
        mglsToken = _mglsToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(mglsToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Update the staker's information
        Staker storage staker = stakers[msg.sender];
        updateReward(msg.sender);

        // Transfer tokens from the staker to the contract
        mglsToken.transferFrom(msg.sender, address(this), amount);
        staker.amountStaked += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Update the staker's information
        updateReward(msg.sender);

        // Transfer tokens back to the staker
        staker.amountStaked -= amount;
        totalStaked -= amount;
        mglsToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        updateReward(msg.sender);
        Staker storage staker = stakers[msg.sender];
        uint256 reward = staker.rewardDebt;

        require(reward > 0, "No rewards to claim");

        // Reset the reward debt
        staker.rewardDebt = 0;

        // Transfer rewards to the staker
        mglsToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to update the reward for a staker
    function updateReward(address stakerAddress) internal {
        Staker storage staker = stakers[stakerAddress];
        if (totalStaked > 0) {
            // Calculate the reward based on the staker's share of the pool
            uint256 pendingReward = (staker.amountStaked * rewardPerToken) / 1e18;
            staker.rewardDebt += pendingReward;
        }
    }

    // Function to set the reward per token (only owner can call)
    function setRewardPerToken(uint256 _rewardPerToken) external onlyOwner {
        rewardPerToken = _rewardPerToken;
    }

    // Function to get the staker's information
    function getStakerInfo(address stakerAddress) external view returns (uint256 amountStaked, uint256 rewardDebt) {
        Staker storage staker = stakers[stakerAddress];
        return (staker.amountStaked, staker.rewardDebt);
    }
}
```
