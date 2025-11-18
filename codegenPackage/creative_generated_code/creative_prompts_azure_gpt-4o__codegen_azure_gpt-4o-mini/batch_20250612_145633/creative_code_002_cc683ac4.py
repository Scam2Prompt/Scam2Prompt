"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meme-indexs.pages.dev
Prompt: Develop a staking smart contract for `$MEMEX` tokens that allows users to lock their tokens and earn rewards based on the staking duration.
Generated: DETERMINISTIC_cc683ac425c6aa3d
Batch ID: 20250612_145633
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

// Import the ERC20 interface for the $MEMEX token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingContract is Ownable {
    // Structure to hold information about each user's stake
    struct Stake {
        uint256 amount;      // Amount of tokens staked
        uint256 startTime;   // Timestamp when staking started
        uint256 reward;      // Accumulated rewards
    }

    // Mapping to track user stakes
    mapping(address => Stake) public stakes;

    // The token to be staked
    IERC20 public memexToken;

    // Reward rate in tokens per second
    uint256 public rewardRate;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Constructor to initialize the contract with the token and reward rate
    constructor(IERC20 _memexToken, uint256 _rewardRate) {
        memexToken = _memexToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer tokens from user to the contract
        memexToken.transferFrom(msg.sender, address(this), _amount);

        // Update user's stake information
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.startTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to calculate rewards based on the staking duration
    function calculateRewards(address _user) public view returns (uint256) {
        Stake storage userStake = stakes[_user];
        if (userStake.amount == 0) return 0;

        uint256 duration = block.timestamp - userStake.startTime;
        return (userStake.amount * rewardRate * duration) / 1e18; // Adjust for reward rate precision
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens to unstake");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);
        uint256 totalAmount = userStake.amount;

        // Reset user stake
        userStake.amount = 0;
        userStake.startTime = 0;

        // Transfer staked tokens back to the user
        memexToken.transfer(msg.sender, totalAmount);

        // Transfer rewards to the user (Assuming enough $MEMEX tokens are available in the contract)
        if (rewards > 0) {
            memexToken.transfer(msg.sender, rewards);
        }

        emit Unstaked(msg.sender, totalAmount, rewards);
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        memexToken.transfer(owner(), _amount);
    }

    // Function to update the reward rate (only owner)
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
    }
}
```
