"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-reward.web.app
Prompt: Create a Solidity contract that supports staking rewards for multiple meme coins, with a mechanism to incentivize holding a specific token like $STARS.
Generated: DETERMINISTIC_8c1ebe0345dbfefc
Batch ID: 20250612_154133
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

// Importing necessary OpenZeppelin contracts for security and efficiency
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract StakingRewards is Ownable, ReentrancyGuard {
    // Struct to store information for each staker
    struct Stake {
        uint256 amount;       // Amount of tokens staked
        uint256 rewardDebt;   // Reward debt for the staker
    }

    // Mapping to track stakes for each user
    mapping(address => Stake) public stakes;

    // Mapping to track the total staked per token
    mapping(address => uint256) public totalStaked;
    
    // Reward token and the token to stake
    IERC20 public rewardToken;  
    IERC20 public stakedToken;  

    // Reward rate per token staked
    uint256 public rewardRate;  

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    
    // Event emitted when a user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount);
    
    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with required tokens and reward rate
    constructor(IERC20 _stakedToken, IERC20 _rewardToken, uint256 _rewardRate) {
        stakedToken = _stakedToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0");
        require(stakedToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        Stake storage stakeData = stakes[msg.sender];

        // Update the user's reward debt and the total staked amount
        updateReward(msg.sender);
        stakeData.amount += amount;
        totalStaked[address(stakedToken)] += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external nonReentrant {
        Stake storage stakeData = stakes[msg.sender];
        require(stakeData.amount >= amount, "Insufficient staked amount");

        updateReward(msg.sender);
        stakeData.amount -= amount;
        totalStaked[address(stakedToken)] -= amount;

        require(stakedToken.transfer(msg.sender, amount), "Transfer failed");
        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant {
        updateReward(msg.sender);
        uint256 reward = stakes[msg.sender].rewardDebt;
        require(reward > 0, "No rewards available");

        stakes[msg.sender].rewardDebt = 0; // Reset reward debt
        require(rewardToken.transfer(msg.sender, reward), "Transfer failed");
        emit RewardClaimed(msg.sender, reward);
    }

    // Function to update rewards for a user
    function updateReward(address user) internal {
        Stake storage stakeData = stakes[user];
        // Calculate pending rewards
        uint256 pendingReward = (stakeData.amount * rewardRate) / 1e18;
        stakeData.rewardDebt += pendingReward; // Update user's reward debt
    }

    // Function to set a new reward rate, only callable by the owner
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw tokens in case of emergency
    function emergencyWithdraw(IERC20 token, uint256 amount) external onlyOwner {
        require(token != stakedToken, "Cannot withdraw staked tokens");
        require(token.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
