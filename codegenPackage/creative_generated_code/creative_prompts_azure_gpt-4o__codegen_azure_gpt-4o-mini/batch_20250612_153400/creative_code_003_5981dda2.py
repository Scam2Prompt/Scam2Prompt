"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20ai.pages.dev
Prompt: Create a function in Solidity that calculates staking rewards for DOGE20 tokens based on a fixed supply and a two-year distribution period.
Generated: DETERMINISTIC_5981dda2bfc25cb9
Batch ID: 20250612_153400
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

// Interface for the DOGE20 token contract
interface IDOGE20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract StakingRewards {
    // Constants for the staking program
    uint256 public constant TOTAL_SUPPLY = 1000000 * 10 ** 18; // Fixed total supply of DOGE20 tokens
    uint256 public constant DISTRIBUTION_PERIOD = 730 days; // Two-year distribution period

    // State variables
    IDOGE20 public doge20Token; // Instance of the DOGE20 token contract
    mapping(address => uint256) public stakedAmount; // Amount of tokens staked by each user
    mapping(address => uint256) public rewardDebt; // Reward debt for each user
    uint256 public totalStaked; // Total tokens staked in the contract
    uint256 public lastUpdate; // Last time rewards were calculated
    uint256 public totalRewards; // Total rewards to be distributed

    // Events for logging stake and rewards
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with DOGE20 token address
    constructor(address _doge20Token) {
        doge20Token = IDOGE20(_doge20Token);
        totalRewards = TOTAL_SUPPLY; // Set total rewards to the total supply of tokens
        lastUpdate = block.timestamp; // Initialize last update to current time
    }

    // Function to stake DOGE20 tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(doge20Token.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Update rewards before staking
        _updateRewards(msg.sender);

        // Transfer tokens from user to the contract
        require(doge20Token.transfer(address(this), amount), "Transfer failed");

        // Update staking details
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake DOGE20 tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked balance");

        // Update rewards before unstaking
        _updateRewards(msg.sender);

        // Update staking details
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        require(doge20Token.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        // Update rewards before claiming
        _updateRewards(msg.sender);

        // Calculate reward amount based on staked tokens
        uint256 reward = rewardDebt[msg.sender];
        require(reward > 0, "No rewards available");

        // Reset the reward debt for the user
        rewardDebt[msg.sender] = 0;

        // Transfer rewards to the user
        require(doge20Token.transfer(msg.sender, reward), "Transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to update rewards for a user
    function _updateRewards(address user) internal {
        // Calculate time elapsed since last update
        uint256 timeElapsed = block.timestamp - lastUpdate;
        if (timeElapsed > 0 && totalStaked > 0) {
            // Calculate rewards based on the total rewards available and elapsed time
            uint256 newRewards = (totalRewards * timeElapsed) / DISTRIBUTION_PERIOD;
            rewardDebt[user] += (stakedAmount[user] * newRewards) / totalStaked; // Update user's reward debt
        }
        lastUpdate = block.timestamp; // Update last update time
    }

    // Function to get the user's staked amount
    function getStakedAmount(address user) external view returns (uint256) {
        return stakedAmount[user];
    }

    // Function to get the user's pending rewards
    function pendingRewards(address user) external view returns (uint256) {
        uint256 timeElapsed = block.timestamp - lastUpdate;
        uint256 newRewards = (totalRewards * timeElapsed) / DISTRIBUTION_PERIOD;
        uint256 pending = rewardDebt[user] + (stakedAmount[user] * newRewards) / totalStaked;
        return pending;
    }
}
```
