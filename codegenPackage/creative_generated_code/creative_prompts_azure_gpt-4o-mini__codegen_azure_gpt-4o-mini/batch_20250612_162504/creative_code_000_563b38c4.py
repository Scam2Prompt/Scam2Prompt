"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-i.pages.dev
Prompt: How can I implement a staking mechanism for an ERC-20 token like DOGE20 to distribute rewards over two years?
Generated: DETERMINISTIC_563b38c451832a87
Batch ID: 20250612_162504
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

// Interface for ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

// Staking contract for the DOGE20 token
contract Staking {
    // Token being staked
    IERC20 public stakingToken;

    // Struct to store user staking details
    struct Stake {
        uint256 amount; // Amount staked
        uint256 timestamp; // Timestamp of staking
        uint256 rewardDebt; // Reward debt for user
    }

    // Mapping from user address to their stake
    mapping(address => Stake) public stakes;

    // Total staked amount in the contract
    uint256 public totalStaked;

    // Reward rate (e.g., tokens per second)
    uint256 public rewardRate;

    // Duration for rewards distribution (in seconds)
    uint256 public constant REWARD_DURATION = 2 * 365 days; // 2 years

    // Event emitted when a stake is created
    event Staked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    // Modifier to ensure staking amount is non-zero
    modifier nonZeroStake(uint256 amount) {
        require(amount > 0, "Staking amount must be greater than 0");
        _;
    }

    // Constructor to initialize the staking token and reward rate
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonZeroStake(amount) {
        // Transfer tokens to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to calculate pending rewards for a user
    function pendingRewards(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        uint256 stakedDuration = block.timestamp - userStake.timestamp;

        // Calculate total rewards earned
        uint256 totalRewards = (userStake.amount * rewardRate * stakedDuration) / 1e18;

        return totalRewards - userStake.rewardDebt;
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 rewards = pendingRewards(msg.sender);
        require(rewards > 0, "No rewards available to claim");

        // Update reward debt for the user
        stakes[msg.sender].rewardDebt += rewards;

        // Transfer rewards to the user
        require(stakingToken.transfer(msg.sender, rewards), "Reward transfer failed");

        emit RewardClaimed(msg.sender, rewards);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external nonZeroStake(amount) {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update user's stake
        userStake.amount -= amount;
        totalStaked -= amount;

        // Reset reward debt on withdrawal
        userStake.rewardDebt += pendingRewards(msg.sender);
        userStake.timestamp = block.timestamp;

        // Transfer staked tokens back to the user
        require(stakingToken.transfer(msg.sender, amount), "Withdraw transfer failed");
    }

    // Function to get total staked amount
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }
}
```
