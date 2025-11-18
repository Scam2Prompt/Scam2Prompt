"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memegames-web.pages.dev
Prompt: Write a smart contract in Solidity for staking $MGMES tokens, ensuring compatibility with the blockchain-based leaderboard system described in The Meme Games Token documentation.
Generated: DETERMINISTIC_bdcab18531a17156
Batch ID: 20250612_151246
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Staking contract for $MGMES tokens
contract MGMESStaking is Ownable, ReentrancyGuard {
    // Token being staked
    IERC20 public immutable mgmesToken;

    // Struct to hold staking details
    struct Staker {
        uint256 amount; // Amount staked
        uint256 reward; // Accumulated rewards
        uint256 lastStakedTime; // Last time the user staked tokens
    }

    // Mapping of staker addresses to their details
    mapping(address => Staker) public stakers;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate per token per second
    uint256 public rewardRate;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the token address and reward rate
    constructor(IERC20 _mgmesToken, uint256 _rewardRate) {
        require(address(_mgmesToken) != address(0), "Invalid token address");
        mgmesToken = _mgmesToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Cannot stake 0 tokens");
        
        // Update staker's state before transferring tokens
        Staker storage staker = stakers[msg.sender];
        _updateReward(msg.sender);

        // Transfer the tokens from the staker to the contract
        mgmesToken.transferFrom(msg.sender, address(this), _amount);
        
        // Update total staked and staker's amount
        totalStaked += _amount;
        staker.amount += _amount;
        staker.lastStakedTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= _amount, "Insufficient staked amount");

        // Update staker's state before transferring tokens
        _updateReward(msg.sender);

        // Update total staked and staker's amount
        totalStaked -= _amount;
        staker.amount -= _amount;

        // Transfer the tokens back to the staker
        mgmesToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant {
        _updateReward(msg.sender);
        Staker storage staker = stakers[msg.sender];
        uint256 reward = staker.reward;

        require(reward > 0, "No rewards to claim");
        
        // Reset the staker's reward to zero
        staker.reward = 0;

        // Transfer the reward to the staker
        mgmesToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to update rewards for a staker
    function _updateReward(address _staker) internal {
        Staker storage staker = stakers[_staker];
        uint256 timeStaked = block.timestamp - staker.lastStakedTime;
        staker.reward += (staker.amount * rewardRate * timeStaked) / 1e18;
        staker.lastStakedTime = block.timestamp;
    }

    // Function to set the reward rate (only owner)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }
}
```
