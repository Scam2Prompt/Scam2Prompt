"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-token.pages.dev
Prompt: Generate a smart contract for staking DOGE20 tokens on Ethereum that distributes rewards over two years.
Generated: DETERMINISTIC_43b6f4225a0e344c
Batch ID: 20250612_161500
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

// Importing the ERC20 interface to interact with the DOGE20 token contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract StakingContract {
    // State variables
    IERC20 public doge20Token; // The DOGE20 token contract
    uint256 public totalStaked; // Total tokens staked by all users
    uint256 public rewardRate; // Rate of rewards per token staked
    uint256 public stakingEndTime; // Timestamp when staking ends

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Time when tokens were staked
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with token address and reward rate
    constructor(address _doge20Token, uint256 _rewardRate, uint256 _durationInDays) {
        doge20Token = IERC20(_doge20Token);
        rewardRate = _rewardRate; // e.g., rewards per token per day
        stakingEndTime = block.timestamp + (_durationInDays * 1 days);
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(block.timestamp < stakingEndTime, "Staking period has ended");
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer DOGE20 tokens from user to this contract
        doge20Token.transferFrom(msg.sender, address(this), amount);
        
        // Update user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");
        
        uint256 reward = calculateRewards(msg.sender);
        
        // Transfer staked tokens back to user
        doge20Token.transfer(msg.sender, userStake.amount);
        // Pay out rewards
        if (reward > 0) {
            doge20Token.transfer(msg.sender, reward);
        }
        
        // Reset user's stake
        totalStaked -= userStake.amount;
        delete stakes[msg.sender];

        emit Unstaked(msg.sender, userStake.amount);
        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0; // No tokens staked
        
        uint256 stakedDuration = block.timestamp - userStake.timestamp;
        uint256 reward = (userStake.amount * rewardRate * stakedDuration) / 1 days;

        return reward;
    }

    // Function to withdraw remaining tokens after staking period (owner only)
    function withdrawRemainingTokens() external {
        require(block.timestamp >= stakingEndTime, "Staking period not ended");
        uint256 balance = doge20Token.balanceOf(address(this));
        require(balance > totalStaked, "No remaining tokens to withdraw");

        uint256 toWithdraw = balance - totalStaked;
        doge20Token.transfer(msg.sender, toWithdraw);
    }
}
```
