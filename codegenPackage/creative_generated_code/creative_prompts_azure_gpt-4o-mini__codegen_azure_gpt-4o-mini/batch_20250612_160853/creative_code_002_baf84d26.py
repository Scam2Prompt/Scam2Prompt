"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hehe-dapps.pages.dev
Prompt: Create a Solidity contract that implements staking for $HEHE tokens, allowing users to earn rewards based on their staked amount.
Generated: DETERMINISTIC_baf84d26ddb2cfe0
Batch ID: 20250612_160853
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
}

// Staking contract for $HEHE tokens
contract StakingContract {
    // Struct to represent a staker's information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt; // The amount of rewards earned but not yet claimed
    }

    IERC20 public token; // The ERC20 token contract ($HEHE)
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardRate; // Rewards per second per token staked
    mapping(address => Staker) public stakers; // Mapping of stakers to their information

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event Claimed(address indexed user, uint256 amount);

    // Constructor initializes the token and sets the reward rate
    constructor(IERC20 _token, uint256 _rewardRate) {
        token = _token;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the staker's information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Not enough tokens staked");

        // Calculate the pending rewards
        uint256 pendingRewards = calculateRewards(msg.sender);
        
        // Update staker's information
        staker.amountStaked -= amount;
        totalStaked -= amount;

        // Transfer the staked amount back to the user
        require(token.transfer(msg.sender, amount), "Transfer failed");

        // Claim the pending rewards
        if (pendingRewards > 0) {
            staker.rewardDebt += pendingRewards; // Update the reward debt
            require(token.transfer(msg.sender, pendingRewards), "Reward transfer failed");
        }

        emit Unstaked(msg.sender, amount);
        emit Claimed(msg.sender, pendingRewards);
    }

    // Function to calculate rewards for a staker
    function calculateRewards(address account) internal view returns (uint256) {
        Staker storage staker = stakers[account];
        return (staker.amountStaked * rewardRate); // Calculate the rewards based on the amount staked
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 pendingRewards = calculateRewards(msg.sender);
        require(pendingRewards > 0, "No rewards available");

        // Update the reward debt
        Staker storage staker = stakers[msg.sender];
        staker.rewardDebt += pendingRewards;

        // Transfer rewards to the user
        require(token.transfer(msg.sender, pendingRewards), "Reward transfer failed");

        emit Claimed(msg.sender, pendingRewards);
    }

    // Function to set the reward rate (only owner can call this)
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        // Owner logic goes here (e.g., using a storage variable to track the owner)
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }
}
```
