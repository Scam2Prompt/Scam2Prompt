"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memekombatio.pages.dev
Prompt: Create a step-by-step guide for integrating $MK token staking functionality into a decentralized application using the Meme Kombat platform.
Generated: DETERMINISTIC_b2166605ef0586f4
Batch ID: 20250612_152620
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

/**
 * @title Meme Kombat Token Staking Contract
 * @dev This contract allows users to stake $MK tokens, calculate rewards, and withdraw them.
 * It integrates functionality required for a decentralized application using the Meme Kombat platform.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MKTokenStaking is Ownable {
    // Address of the $MK token contract
    IERC20 public mkToken;

    // Struct to store staking details for each user
    struct Stake {
        uint256 amount;        // Amount of tokens staked
        uint256 lastUpdated;   // Timestamp of last reward calculation
        uint256 rewardDebt;    // Rewards due to the user
    }

    // Mapping to store staking details for each user
    mapping(address => Stake) public stakes;

    // Reward rate per second (e.g., 0.01 tokens per second)
    uint256 public rewardRate;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract.
     * @param _mkToken Address of the $MK token contract.
     * @param _rewardRate Reward rate per second.
     */
    constructor(IERC20 _mkToken, uint256 _rewardRate) {
        require(address(_mkToken) != address(0), "Invalid MK token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        mkToken = _mkToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Function to allow users to stake $MK tokens.
     * @param _amount Amount of $MK tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Update rewards before staking
        _updateReward(msg.sender);

        // Transfer $MK tokens from the user to the contract
        mkToken.transferFrom(msg.sender, address(this), _amount);

        // Update staking details
        stakes[msg.sender].amount += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to allow users to withdraw their staked tokens.
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender].amount >= _amount, "Insufficient staked amount");

        // Update rewards before withdrawing
        _updateReward(msg.sender);

        // Update staking details
        stakes[msg.sender].amount -= _amount;

        // Transfer $MK tokens back to the user
        mkToken.transfer(msg.sender, _amount);

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Function for users to claim their accumulated rewards.
     */
    function claimReward() external {
        // Update rewards before claiming
        _updateReward(msg.sender);

        uint256 reward = stakes[msg.sender].rewardDebt;
        require(reward > 0, "No rewards available");

        // Reset reward debt
        stakes[msg.sender].rewardDebt = 0;

        // Transfer rewards to the user
        mkToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param _user Address of the user.
     */
    function _updateReward(address _user) internal {
        Stake storage userStake = stakes[_user];
        uint256 timeElapsed = block.timestamp - userStake.lastUpdated;
        uint256 pendingReward = timeElapsed * userStake.amount * rewardRate;

        userStake.rewardDebt += pendingReward;
        userStake.lastUpdated = block.timestamp;
    }

    /**
     * @dev Owner-only function to update the reward rate.
     * @param _newRate New reward rate per second.
     */
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Reward rate must be greater than zero");
        rewardRate = _newRate;
    }

    /**
     * @dev Emergency function to allow the owner to withdraw all tokens from the contract.
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 contractBalance = mkToken.balanceOf(address(this));
        mkToken.transfer(owner(), contractBalance);
    }
}
```
