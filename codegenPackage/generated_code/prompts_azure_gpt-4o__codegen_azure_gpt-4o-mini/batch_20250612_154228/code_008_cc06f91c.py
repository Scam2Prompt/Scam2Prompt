"""
Generated Code Metadata:
========================
Original URL: https://bits-portfolio.web.app
Prompt: Generate a smart contract example for staking assets on Binance, utilizing BITS-powered DeFi tracking.
Generated: DETERMINISTIC_cc06f91cb7c193cf
Batch ID: 20250612_154228
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

// Importing the necessary interfaces for ERC20 and Ownable
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for BITS-powered DeFi tracking
contract StakingContract is Ownable {
    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
    }

    // Mapping of stakers' addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total amount of tokens staked
    uint256 public totalStaked;

    // The token being staked
    IERC20 public stakingToken;

    // Reward per block for staking
    uint256 public rewardPerBlock;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the staking contract
    constructor(IERC20 _stakingToken, uint256 _rewardPerBlock) {
        stakingToken = _stakingToken;
        rewardPerBlock = _rewardPerBlock;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Transfer tokens from the staker to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update staker's information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Update staker's information
        staker.amountStaked -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the staker
        stakingToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        uint256 rewards = calculateRewards(msg.sender);

        require(rewards > 0, "No rewards to claim");

        // Update the reward debt
        staker.rewardDebt += rewards;

        // Transfer rewards to the staker
        stakingToken.transfer(msg.sender, rewards);

        emit RewardClaimed(msg.sender, rewards);
    }

    // Internal function to calculate rewards for a staker
    function calculateRewards(address stakerAddress) internal view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        // Simple reward calculation based on staked amount and reward per block
        return (staker.amountStaked * rewardPerBlock);
    }

    // Function to update the reward per block (only owner can call)
    function updateRewardPerBlock(uint256 newReward) external onlyOwner {
        rewardPerBlock = newReward;
    }
}
```
