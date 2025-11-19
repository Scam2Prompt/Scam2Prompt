"""
Generated Code Metadata:
========================
Original URL: https://godcoin.world
Prompt: Develop a simple staking program for God Token using Solidity and OpenZeppelin libraries.
Generated: DETERMINISTIC_ccb296cc6de63b14
Batch ID: 20250622_211614
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

// Import OpenZeppelin libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract GodTokenStaking is Ownable, ReentrancyGuard {
    // Struct to store staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp when the stake was created
    }

    // Mapping to store stakes for each user
    mapping(address => Stake) public stakes;

    // Token to be staked
    IERC20 public godToken;

    // Reward rate (e.g., 10% annual reward rate)
    uint256 public rewardRate; // Reward rate in percentage (e.g., 10 for 10%)

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event RewardRateUpdated(uint256 newRewardRate);

    // Constructor to initialize the staking contract
    constructor(IERC20 _godToken, uint256 _rewardRate) {
        require(address(_godToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        godToken = _godToken;
        rewardRate = _rewardRate;
    }

    // Function to update the reward rate (only owner can call)
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _newRewardRate;
        emit RewardRateUpdated(_newRewardRate);
    }

    // Function to stake tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(godToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update the user's stake
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to calculate rewards
    function calculateReward(address _user) public view returns (uint256) {
        Stake memory userStake = stakes[_user];
        if (userStake.amount == 0) {
            return 0;
        }

        // Calculate the staking duration in seconds
        uint256 stakingDuration = block.timestamp - userStake.timestamp;

        // Calculate the reward based on the reward rate and staking duration
        // Reward formula: (amount * rewardRate * duration) / (100 * 365 * 24 * 60 * 60)
        uint256 reward = (userStake.amount * rewardRate * stakingDuration) / (100 * 365 * 24 * 60 * 60);
        return reward;
    }

    // Function to unstake tokens and claim rewards
    function unstake() external nonReentrant {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate the reward
        uint256 reward = calculateReward(msg.sender);

        // Reset the user's stake
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].timestamp = 0;

        // Transfer the staked tokens and reward to the user
        require(godToken.transfer(msg.sender, userStake.amount), "Token transfer failed");
        if (reward > 0) {
            require(godToken.transfer(msg.sender, reward), "Reward transfer failed");
        }

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    // Function to check the staked amount of a user
    function stakedAmount(address _user) external view returns (uint256) {
        return stakes[_user].amount;
    }
}
```
