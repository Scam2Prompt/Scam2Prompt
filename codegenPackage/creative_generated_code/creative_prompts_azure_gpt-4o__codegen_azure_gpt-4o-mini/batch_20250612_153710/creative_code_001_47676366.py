"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://niftyislandair.pages.dev
Prompt: Generate code for staking digital assets in a decentralized ecosystem, ensuring compatibility with the Nifty Island Air platform's smart contract features.
Generated: DETERMINISTIC_47676366cb09fc49
Batch ID: 20250612_153710
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

// Importing OpenZeppelin's ERC20 interface for token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Staking contract for digital assets
contract Staking {
    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardPaid(address indexed user, uint256 reward);

    // Address of the token being staked
    IERC20 public stakingToken;
    // Address of the reward token
    IERC20 public rewardToken;

    // Total staked amount
    uint256 public totalStaked;

    // User staking details
    struct UserStake {
        uint256 amount; // Amount staked by user
        uint256 reward; // Rewards earned by user
    }

    // Mapping of user addresses to their stakes
    mapping(address => UserStake) public stakes;

    // Constructor to initialize the staking contract
    constructor(IERC20 _stakingToken, IERC20 _rewardToken) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");

        // Transfer the tokens from the user to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update total staked amount
        totalStaked += amount;

        // Update user's stake
        stakes[msg.sender].amount += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        UserStake storage userStake = stakes[msg.sender];
        require(amount > 0, "Cannot unstake 0");
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Decrease user's stake
        userStake.amount -= amount;
        // Update total staked amount
        totalStaked -= amount;

        // Transfer the tokens back to the user
        require(stakingToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        UserStake storage userStake = stakes[msg.sender];
        uint256 reward = userStake.reward;
        require(reward > 0, "No rewards available");

        // Reset user's reward to zero
        userStake.reward = 0;

        // Transfer the rewards to the user
        require(rewardToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardPaid(msg.sender, reward);
    }

    // Function to distribute rewards (only callable by the contract owner)
    function distributeRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Reward amount must be greater than 0");
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient reward balance");

        // Distribute rewards proportionally to all staked users
        for (uint256 i = 0; i < uniqueUsersCount; i++) {
            address user = uniqueUsers[i];
            uint256 userReward = (stakes[user].amount * amount) / totalStaked;
            stakes[user].reward += userReward;
        }
    }

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Owner address
    address private owner;

    // Constructor to set the owner of the contract
    constructor() {
        owner = msg.sender;
    }
}
```
