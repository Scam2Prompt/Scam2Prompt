"""
Generated Code Metadata:
========================
Original URL: https://oraclememe-com.pages.dev
Prompt: Design a simple staking system using Solidity for the Oracle Meme token (OMEME) on the Binance Smart Chain, offering a 652% reward based on dynamic percentage.
Generated: DETERMINISTIC_2ebce7eaa8a2fd41
Batch ID: 20250622_205836
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

// Importing OpenZeppelin's SafeMath library for safe arithmetic operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for the Oracle Meme token (OMEME)
contract StakingSystem is Ownable {
    using SafeMath for uint256;

    // Token to be staked
    IERC20 public immutable token;

    // Struct to hold staking information
    struct Stake {
        uint256 amount; // Amount staked
        uint256 timestamp; // Timestamp of the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate (dynamic percentage)
    uint256 public rewardRate = 652; // 652%

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Constructor to set the token address
    constructor(IERC20 _token) {
        token = _token;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(token.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        token.transferFrom(msg.sender, address(this), _amount);

        // Update user's stake information
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(_amount);
        stakes[msg.sender].timestamp = block.timestamp;

        // Update total staked amount
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate reward based on the time staked
        uint256 reward = calculateReward(userStake.amount, userStake.timestamp);
        
        // Update total staked amount
        totalStaked = totalStaked.sub(userStake.amount);

        // Reset user's stake
        delete stakes[msg.sender];

        // Transfer staked tokens and reward to user
        token.transfer(msg.sender, userStake.amount);
        token.transfer(msg.sender, reward);

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    // Function to calculate reward based on staked amount and time
    function calculateReward(uint256 _amount, uint256 _timestamp) internal view returns (uint256) {
        uint256 stakingDuration = block.timestamp.sub(_timestamp);
        uint256 reward = _amount.mul(rewardRate).div(100).mul(stakingDuration).div(365 days); // Annualized reward
        return reward;
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(_amount <= token.balanceOf(address(this)), "Insufficient contract balance");
        token.transfer(msg.sender, _amount);
    }
}
```
