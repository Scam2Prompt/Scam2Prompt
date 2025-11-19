"""
Generated Code Metadata:
========================
Original URL: https://polygon6d.com
Prompt: Create a Solidity contract that implements the six degrees of separation theory for staking rewards distribution, as described in Polygon6D.
Generated: DETERMINISTIC_397566b3117bf1df
Batch ID: 20250612_150644
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Polygon6D - Six Degrees of Separation Theory for Staking Rewards Distribution
 * @author [Your Name]
 * @notice This contract distributes staking rewards based on the six degrees of separation theory.
 */
contract Polygon6D is Ownable {
    using SafeMath for uint256;

    // Mapping of user addresses to their respective degrees
    mapping(address => uint256) public userDegrees;

    // Mapping of user addresses to their respective stakes
    mapping(address => uint256) public userStakes;

    // Mapping of user addresses to their respective reward balances
    mapping(address => uint256) public userRewards;

    // Total stake in the system
    uint256 public totalStake;

    // Reward token
    IERC20 public rewardToken;

    // Reward per degree
    uint256 public rewardPerDegree;

    /**
     * @notice Initializes the contract with the reward token and reward per degree.
     * @param _rewardToken Address of the reward token.
     * @param _rewardPerDegree Reward per degree.
     */
    constructor(IERC20 _rewardToken, uint256 _rewardPerDegree) public {
        rewardToken = _rewardToken;
        rewardPerDegree = _rewardPerDegree;
    }

    /**
     * @notice Stake tokens and get a degree.
     * @param _amount Amount to stake.
     */
    function stake(uint256 _amount) public {
        require(_amount > 0, "Invalid stake amount");

        // Update user's stake
        userStakes[msg.sender] = userStakes[msg.sender].add(_amount);

        // Update total stake
        totalStake = totalStake.add(_amount);

        // Calculate user's degree
        uint256 degree = calculateDegree(msg.sender);

        // Update user's degree
        userDegrees[msg.sender] = degree;
    }

    /**
     * @notice Unstake tokens.
     * @param _amount Amount to unstake.
     */
    function unstake(uint256 _amount) public {
        require(_amount > 0, "Invalid unstake amount");
        require(userStakes[msg.sender] >= _amount, "Insufficient stake");

        // Update user's stake
        userStakes[msg.sender] = userStakes[msg.sender].sub(_amount);

        // Update total stake
        totalStake = totalStake.sub(_amount);
    }

    /**
     * @notice Distributes rewards based on user's degree.
     */
    function distributeRewards() public {
        // Calculate reward for each user
        for (address user in userDegrees) {
            uint256 degree = userDegrees[user];
            uint256 reward = rewardPerDegree.mul(degree);

            // Update user's reward balance
            userRewards[user] = userRewards[user].add(reward);
        }
    }

    /**
     * @notice Claims rewards for a user.
     */
    function claimRewards() public {
        // Get user's reward balance
        uint256 reward = userRewards[msg.sender];

        // Reset user's reward balance
        userRewards[msg.sender] = 0;

        // Transfer reward to user
        require(rewardToken.transfer(msg.sender, reward), "Failed to transfer reward");
    }

    /**
     * @notice Calculates a user's degree based on their stake and total stake.
     * @param _user Address of the user.
     * @return Degree of the user.
     */
    function calculateDegree(address _user) internal view returns (uint256) {
        // Calculate degree using the six degrees of separation theory formula
        // For simplicity, assume the formula is: degree = (user's stake / total stake) * 6
        uint256 degree = userStakes[_user].mul(6).div(totalStake);
        return degree;
    }

    /**
     * @notice Updates the reward per degree.
     * @param _newRewardPerDegree New reward per degree.
     */
    function updateRewardPerDegree(uint256 _newRewardPerDegree) public onlyOwner {
        rewardPerDegree = _newRewardPerDegree;
    }
}
```
