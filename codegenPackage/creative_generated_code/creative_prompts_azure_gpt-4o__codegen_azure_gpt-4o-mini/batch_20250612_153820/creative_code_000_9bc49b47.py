"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://good-games-guild.gitbook.io
Prompt: Write a smart contract in Solidity for staking $GGG tokens, referencing the staking platform details from Good Games Guild documentation.
Generated: DETERMINISTIC_9bc49b47b0c0c857
Batch ID: 20250612_153820
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Good Games Guild Staking Contract
 * @notice This contract allows users to stake their $GGG tokens and earn rewards.
 */
contract GGGPStaking is ReentrancyGuard, Ownable {
    
    // State variables
    IERC20 public gggToken; // The $GGG token
    uint256 public rewardRate; // Rate of reward distribution per staked token per block
    uint256 public totalStaked; // Total amount of tokens staked in the contract

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 reward; // Accumulated rewards
        uint256 lastUpdated; // Last updated block number for rewards
    }

    mapping(address => Stake) private stakes; // Mapping of user stakes

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @param _gggToken Address of the $GGG token contract
     * @param _rewardRate Rate at which rewards are distributed
     */
    constructor(IERC20 _gggToken, uint256 _rewardRate) {
        require(address(_gggToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");

        gggToken = _gggToken;
        rewardRate = _rewardRate;
    }

    /**
     * @notice Stakes a specified amount of $GGG tokens
     * @param _amount Amount of $GGG tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Cannot stake 0");
        require(gggToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update user's stakes
        Stake storage userStake = stakes[msg.sender];
        userStake.reward += _calculateRewards(msg.sender);
        userStake.amount += _amount;
        userStake.lastUpdated = block.number;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstakes a specified amount of $GGG tokens
     * @param _amount Amount of $GGG tokens to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Cannot unstake 0");
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Update user's stakes
        userStake.reward += _calculateRewards(msg.sender);
        userStake.amount -= _amount;
        totalStaked -= _amount;

        require(gggToken.transfer(msg.sender, _amount), "Transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Claims the accumulated rewards for the caller
     */
    function claimRewards() external nonReentrant {
        uint256 reward = _calculateRewards(msg.sender) + stakes[msg.sender].reward;
        require(reward > 0, "No rewards available");

        stakes[msg.sender].reward = 0; // Reset rewards
        require(gggToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @notice Calculates rewards for a given user
     * @param user Address of the user
     * @return uint256 Total calculated rewards
     */
    function _calculateRewards(address user) internal view returns (uint256) {
        Stake storage userStake = stakes[user];
        return (userStake.amount * rewardRate * (block.number - userStake.lastUpdated)) / 1e18;
    }

    /**
     * @notice Allows the owner to set a new reward rate
     * @param _newRate New reward rate
     */
    function setRewardRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Reward rate must be greater than 0");
        rewardRate = _newRate;
    }

    /**
     * @notice Returns the staked amount and rewards for a user
     * @param user Address of the user
     * @return amount Staked amount
     * @return reward Accumulated rewards
     */
    function getUserStake(address user) external view returns (uint256 amount, uint256 reward) {
        Stake storage userStake = stakes[user];
        amount = userStake.amount;
        reward = userStake.reward + _calculateRewards(user);
    }
}
```
