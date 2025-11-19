"""
Generated Code Metadata:
========================
Original URL: https://looksrare.tech
Prompt: Write a Solidity contract that implements a reward distribution system for early adopters, similar to the token distribution model described for LOOKS tokens on LooksRare.
Generated: DETERMINISTIC_73be225ef7fd8c75
Batch ID: 20250612_145121
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract RewardDistributor is Ownable {
    using SafeMath for uint256;

    // The token being distributed
    IERC20 public rewardToken;

    // Total amount of tokens to be distributed
    uint256 public totalRewards;

    // Amount of tokens already claimed
    uint256 public totalClaimed;

    // Distribution start time (timestamp)
    uint256 public distributionStart;

    // Distribution duration in seconds
    uint256 public distributionDuration;

    // Mapping of user addresses to their reward amount
    mapping(address => uint256) public rewards;

    // Mapping of user addresses to claimed status
    mapping(address => bool) public hasClaimed;

    // Events
    event RewardAdded(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event DistributionStarted(uint256 startTime, uint256 duration);

    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @dev Set up the distribution parameters
     * @param _totalRewards Total amount of tokens to distribute
     * @param _distributionDuration Duration of distribution in seconds
     */
    function setupDistribution(uint256 _totalRewards, uint256 _distributionDuration) external onlyOwner {
        require(distributionStart == 0, "Distribution already started");
        require(_totalRewards > 0, "Invalid reward amount");
        require(_distributionDuration > 0, "Invalid duration");

        totalRewards = _totalRewards;
        distributionDuration = _distributionDuration;
    }

    /**
     * @dev Start the distribution period
     */
    function startDistribution() external onlyOwner {
        require(distributionStart == 0, "Distribution already started");
        require(totalRewards > 0, "Distribution not set up");
        
        distributionStart = block.timestamp;
        emit DistributionStarted(distributionStart, distributionDuration);
    }

    /**
     * @dev Add rewards for multiple users
     * @param users Array of user addresses
     * @param amounts Array of reward amounts
     */
    function addRewards(address[] calldata users, uint256[] calldata amounts) external onlyOwner {
        require(users.length == amounts.length, "Arrays length mismatch");
        
        for (uint256 i = 0; i < users.length; i++) {
            require(users[i] != address(0), "Invalid user address");
            require(amounts[i] > 0, "Invalid reward amount");
            
            rewards[users[i]] = rewards[users[i]].add(amounts[i]);
            emit RewardAdded(users[i], amounts[i]);
        }
    }

    /**
     * @dev Claim available rewards
     */
    function claimReward() external {
        require(distributionStart > 0, "Distribution not started");
        require(!hasClaimed[msg.sender], "Already claimed");
        require(rewards[msg.sender] > 0, "No rewards available");

        uint256 claimableAmount = calculateClaimableAmount(msg.sender);
        require(claimableAmount > 0, "No tokens claimable yet");

        hasClaimed[msg.sender] = true;
        totalClaimed = totalClaimed.add(claimableAmount);

        require(rewardToken.transfer(msg.sender, claimableAmount), "Transfer failed");
        emit RewardClaimed(msg.sender, claimableAmount);
    }

    /**
     * @dev Calculate currently claimable amount for a user
     * @param user Address of the user
     * @return Amount of tokens currently claimable
     */
    function calculateClaimableAmount(address user) public view returns (uint256) {
        if (distributionStart == 0 || rewards[user] == 0 || hasClaimed[user]) {
            return 0;
        }

        uint256 elapsedTime = block.timestamp.sub(distributionStart);
        if (elapsedTime >= distributionDuration) {
            return rewards[user];
        }

        return rewards[user].mul(elapsedTime).div(distributionDuration);
    }

    /**
     * @dev Withdraw any remaining tokens after distribution ends
     */
    function withdrawRemaining() external onlyOwner {
        require(distributionStart > 0, "Distribution not started");
        require(block.timestamp >= distributionStart.add(distributionDuration), "Distribution not ended");

        uint256 remaining = rewardToken.balanceOf(address(this)).sub(totalRewards.sub(totalClaimed));
        if (remaining > 0) {
            require(rewardToken.transfer(owner(), remaining), "Transfer failed");
        }
    }
}
```
