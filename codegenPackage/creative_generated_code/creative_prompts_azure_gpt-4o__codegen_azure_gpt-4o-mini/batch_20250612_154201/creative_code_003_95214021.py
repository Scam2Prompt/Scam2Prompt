"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://njax.pages.dev
Prompt: Write a smart contract in Solidity for staking tokens on a decentralized platform, incorporating mechanisms to address high gas fees and slippage errors during trades.
Generated: DETERMINISTIC_95214021538d3e1f
Batch ID: 20250612_154201
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

// Interface for the ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

// Staking contract for token staking
contract TokenStaking {
    // State variables
    IERC20 public stakingToken; // Token to be staked
    uint256 public totalStaked;  // Total amount of tokens staked
    uint256 public rewardRate;    // Reward rate for staking
    uint256 public minStakeAmount; // Minimum amount required to stake
    mapping(address => uint256) public stakedAmounts; // Amount staked by each user
    mapping(address => uint256) public lastRewardClaimed; // Last block number when rewards were claimed

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract
    constructor(IERC20 _stakingToken, uint256 _rewardRate, uint256 _minStakeAmount) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
        minStakeAmount = _minStakeAmount;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount >= minStakeAmount, "Stake amount is less than minimum required");
        
        // Update user state
        stakedAmounts[msg.sender] += amount;
        totalStaked += amount;

        // Transfer tokens to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        lastRewardClaimed[msg.sender] = block.number; // Update last reward claimed

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(stakedAmounts[msg.sender] >= amount, "Insufficient staked balance");

        // Update user state
        stakedAmounts[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        require(stakingToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate pending rewards
    function calculateRewards(address user) public view returns (uint256) {
        uint256 blocksStaked = block.number - lastRewardClaimed[user]; 
        return stakedAmounts[user] * rewardRate * blocksStaked;
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Update last claimed block
        lastRewardClaimed[msg.sender] = block.number;

        // Transfer rewards (for simplicity, rewards are paid in the staked token)
        require(stakingToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to set a new reward rate (owner only)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    // Modifier to restrict access to owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Owner of the contract
    address public owner;

    // Set the contract deployer as the owner
    constructor() {
        owner = msg.sender;
    }
}
```
