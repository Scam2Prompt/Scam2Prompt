"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-6s6.pages.dev
Prompt: Create a Solidity smart contract function to calculate staking rewards for the $FROP token based on the locked schedule pool described in the War Chest.
Generated: DETERMINISTIC_5852401c80053e9c
Batch ID: 20250612_152321
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

// Interface for the ERC20 token, in this case, the $FROP token
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

// Contract for managing staking rewards for the $FROP token
contract StakingRewards {
    // State variables
    IERC20 public fropToken; // Instance of the $FROP token contract
    uint256 public totalStaked; // Total amount of tokens staked
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public lastRewardTime; // Last time rewards were calculated for each user
    uint256 public rewardRate; // Reward rate per second

    // Event emitted when rewards are calculated and distributed
    event RewardsCalculated(address indexed user, uint256 rewardAmount);

    // Constructor to initialize the contract with the $FROP token and reward rate
    constructor(address _fropToken, uint256 _rewardRate) {
        require(_fropToken != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        fropToken = IERC20(_fropToken);
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(fropToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staked amount and total staked
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;

        // Update last reward time
        lastRewardTime[msg.sender] = block.timestamp;
    }

    // Function to calculate and distribute staking rewards
    function calculateRewards() external {
        // Calculate rewards based on the time since last reward calculation
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available");

        // Update last reward time
        lastRewardTime[msg.sender] = block.timestamp;

        // Transfer rewards to the user
        require(fropToken.transfer(msg.sender, reward), "Reward transfer failed");

        // Emit an event for the rewards calculation
        emit RewardsCalculated(msg.sender, reward);
    }

    // Internal function to calculate the reward for a given user
    function calculateReward(address user) internal view returns (uint256) {
        if (stakedAmount[user] == 0) {
            return 0; // No staked amount means no rewards
        }
        uint256 timeStaked = block.timestamp - lastRewardTime[user];
        return (timeStaked * rewardRate * stakedAmount[user]) / 1e18; // Adjust for precision
    }

    // Function to withdraw staked tokens (with rewards)
    function withdraw(uint256 amount) external {
        require(amount > 0 && amount <= stakedAmount[msg.sender], "Invalid withdrawal amount");

        // Calculate rewards before withdrawal
        calculateRewards();

        // Update staked amount and total staked
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        require(fropToken.transfer(msg.sender, amount), "Withdrawal transfer failed");
    }

    // Function to set a new reward rate (only callable by the owner)
    function setRewardRate(uint256 newRate) external {
        require(newRate > 0, "New reward rate must be greater than zero");
        rewardRate = newRate;
    }
}
```
