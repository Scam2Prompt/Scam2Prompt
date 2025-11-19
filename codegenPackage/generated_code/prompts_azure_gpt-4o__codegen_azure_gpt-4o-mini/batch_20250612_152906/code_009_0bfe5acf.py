"""
Generated Code Metadata:
========================
Original URL: https://kayentest2.pages.dev
Prompt: Generate a Solidity contract for a staking mechanism that aligns with KAYEN Protocol's sustainable dual-token model and deflationary principles.
Generated: DETERMINISTIC_0bfe5acfd8f30cc2
Batch ID: 20250612_152906
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for KAYEN Protocol's sustainable dual-token model
contract KAYENStaking is Ownable {
    // Token interfaces
    IERC20 public immutable rewardToken; // The token that will be rewarded for staking
    IERC20 public immutable stakingToken; // The token that users will stake

    // Struct to hold staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of when the tokens were staked
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Total staked amount
    uint256 public totalStaked;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the staking and reward tokens
    constructor(IERC20 _stakingToken, IERC20 _rewardToken) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer staking tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        // Update total staked amount
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Update user's stake information
        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;

        // Transfer staking tokens back to user
        stakingToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate rewards based on the staked amount and time
    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        // Example reward calculation: 1% of staked amount per day
        uint256 rewardRate = 1; // 1% per day
        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        uint256 daysStaked = stakingDuration / 1 days;

        return (userStake.amount * rewardRate * daysStaked) / 100;
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available");

        // Transfer reward tokens to user
        rewardToken.transfer(msg.sender, reward);

        // Reset user's staking timestamp
        stakes[msg.sender].timestamp = block.timestamp;

        emit RewardClaimed(msg.sender, reward);
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount <= stakingToken.balanceOf(address(this)), "Insufficient contract balance");
        stakingToken.transfer(msg.sender, amount);
    }
}
```
