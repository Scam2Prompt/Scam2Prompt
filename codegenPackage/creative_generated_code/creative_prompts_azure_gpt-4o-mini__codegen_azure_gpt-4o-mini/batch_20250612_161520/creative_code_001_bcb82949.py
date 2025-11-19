"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mememoguls-de.web.app
Prompt: How can I implement a staking mechanism for $MGLS tokens that rewards users based on their share of the staking pool?
Generated: DETERMINISTIC_bcb82949f85c0dcf
Batch ID: 20250612_161520
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

// Importing the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $MGLS tokens
contract MGLSStaking is Ownable {
    IERC20 public mglsToken; // The $MGLS token contract
    uint256 public totalStaked; // Total amount of tokens staked
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public rewards; // Rewards earned by each user
    uint256 public rewardRate; // Reward rate in tokens per staked token

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted when rewards are harvested
    event RewardsHarvested(address indexed user, uint256 amount);

    // Constructor to initialize the staking contract
    constructor(IERC20 _mglsToken, uint256 _rewardRate) {
        mglsToken = _mglsToken;
        rewardRate = _rewardRate;
    }

    // Modifier to check if the user has staked tokens
    modifier hasStaked() {
        require(stakedAmount[msg.sender] > 0, "You have not staked any tokens");
        _;
    }

    // Function to stake $MGLS tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(mglsToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update total staked and user's staked amount
        totalStaked += amount;
        stakedAmount[msg.sender] += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake $MGLS tokens
    function unstake(uint256 amount) external hasStaked {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Update total staked and user's staked amount
        totalStaked -= amount;
        stakedAmount[msg.sender] -= amount;

        // Transfer tokens back to the user
        require(mglsToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate and harvest rewards
    function harvestRewards() external hasStaked {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards to harvest");

        // Reset the user's rewards before transferring
        rewards[msg.sender] = 0;

        // Transfer rewards to the user
        require(mglsToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardsHarvested(msg.sender, reward);
    }

    // Internal function to calculate rewards for a user
    function calculateRewards(address user) internal view returns (uint256) {
        // Calculate the user's share of the staking pool
        uint256 userShare = (stakedAmount[user] * rewardRate * totalStaked) / totalStaked;
        return userShare + rewards[user]; // Add any previously accumulated rewards
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to view the user's staked amount
    function getStakedAmount(address user) external view returns (uint256) {
        return stakedAmount[user];
    }

    // Function to view the user's earned rewards
    function getRewards(address user) external view returns (uint256) {
        return calculateRewards(user);
    }
}
```
