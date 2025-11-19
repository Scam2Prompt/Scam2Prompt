"""
Generated Code Metadata:
========================
Original URL: https://meme-indexs.pages.dev
Prompt: Develop a smart contract using Solidity to create a decentralized meme coin index, including functions for buying, staking, and claiming rewards.
Generated: DETERMINISTIC_5846784f2346b2c5
Batch ID: 20250622_211639
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract MemeCoinIndex is ERC20Burnable, Ownable {
    using SafeMath for uint256;

    // Reward token
    IERC20 public rewardToken;

    // Staking structure
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the token and reward token
    constructor(string memory name, string memory symbol, address _rewardToken) 
        ERC20(name, symbol) 
    {
        rewardToken = IERC20(_rewardToken);
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens from user to contract
        _transfer(msg.sender, address(this), amount);

        // Update user's stake
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Update user's stake
        stakes[msg.sender].amount = stakes[msg.sender].amount.sub(amount);

        // Transfer tokens back to user
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available");

        // Update user's stake timestamp
        stakes[msg.sender].timestamp = block.timestamp;

        // Transfer reward tokens to user
        rewardToken.transfer(msg.sender, reward);

        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to calculate rewards based on staked amount and time
    function calculateRewards(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        // Example reward calculation: 1% of staked amount per day
        uint256 stakingDuration = block.timestamp.sub(userStake.timestamp);
        uint256 daysStaked = stakingDuration.div(1 days);
        return userStake.amount.mul(daysStaked).div(100); // 1% reward
    }

    // Function to withdraw tokens in case of emergency
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to owner
        _transfer(address(this), owner(), amount);
    }
}
```
