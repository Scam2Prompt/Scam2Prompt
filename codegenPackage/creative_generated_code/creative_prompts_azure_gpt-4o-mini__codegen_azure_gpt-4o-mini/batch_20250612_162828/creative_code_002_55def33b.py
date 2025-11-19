"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supercore-7hg.pages.dev
Prompt: What are the key steps to create a staking mechanism for users on a decentralized exchange like Supercore?
Generated: DETERMINISTIC_55def33b01e0f671
Batch ID: 20250612_162828
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

// Importing OpenZeppelin's ERC20 interface to interact with ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// The Staking contract allows users to stake ERC20 tokens and earn rewards
contract StakingMechanism is Ownable {
    IERC20 public stakingToken; // The token that users will stake
    uint256 public rewardRate; // Rate at which rewards are distributed
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardDuration; // Duration for which rewards are calculated

    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked; // Amount of tokens staked by the user
        uint256 lastClaimed; // Last time rewards were claimed
    }

    // Mapping of user addresses to their staking information
    mapping(address => Staker) public stakers;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardPaid(address indexed user, uint256 reward);
    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to initialize the staking mechanism
    constructor(IERC20 _stakingToken, uint256 _rewardRate, uint256 _rewardDuration) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
        rewardDuration = _rewardDuration;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Transfer staking tokens from the user to this contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update staker's information
        stakers[msg.sender].amountStaked += amount;
        stakers[msg.sender].lastClaimed = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to calculate and claim rewards for the caller
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No staked tokens found");

        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available to claim");

        // Update last claimed timestamp
        staker.lastClaimed = block.timestamp;

        // Transfer the calculated rewards to the user
        payable(msg.sender).transfer(rewards);

        emit RewardPaid(msg.sender, rewards);
    }

    // Function to calculate rewards based on the amount staked and time
    function calculateRewards(address user) public view returns (uint256) {
        Staker storage staker = stakers[user];
        uint256 stakedDuration = block.timestamp - staker.lastClaimed;

        // Calculate rewards based on staked duration and reward rate
        uint256 rewards = (staker.amountStaked * rewardRate * stakedDuration) / rewardDuration;
        return rewards;
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Claim rewards before withdrawal
        claimRewards();

        // Update staker's amount staked
        staker.amountStaked -= amount;
        totalStaked -= amount;

        // Transfer staked tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to set the reward rate (only owner can call)
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }
}
```
