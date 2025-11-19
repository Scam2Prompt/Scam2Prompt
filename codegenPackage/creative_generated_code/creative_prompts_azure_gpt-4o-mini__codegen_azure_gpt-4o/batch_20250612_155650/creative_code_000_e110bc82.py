"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://good-games-guild.gitbook.io
Prompt: Generate a smart contract for staking the $GGG token as described in the Good Games Guild documentation.
Generated: DETERMINISTIC_e110bc82f7fd5c4f
Batch ID: 20250612_155650
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
 * @title StakingContract
 * @dev A smart contract for staking $GGG tokens as described in the Good Games Guild documentation.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingContract is Ownable {
    IERC20 public gggToken; // Interface for $GGG token contract
    uint256 public rewardRate; // Reward rate per second per staked token
    uint256 public totalStaked; // Total tokens staked
    
    struct Stake {
        uint256 amount; // Amount of tokens staked by the user
        uint256 lastStakedTime; // Timestamp of last staking
        uint256 rewardsEarned; // Accumulated rewards
    }

    mapping(address => Stake) public stakes; // Mapping of user stakes

    event TokensStaked(address indexed user, uint256 amount);
    event TokensUnstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the staking contract with $GGG token and reward rate.
     * @param _gggToken Address of the $GGG token contract.
     * @param _rewardRate Reward rate per second per staked token.
     */
    constructor(IERC20 _gggToken, uint256 _rewardRate) {
        require(address(_gggToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        gggToken = _gggToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows a user to stake $GGG tokens.
     * @param amount The number of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(gggToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        _updateRewards(msg.sender);

        stakes[msg.sender].amount += amount;
        stakes[msg.sender].lastStakedTime = block.timestamp;
        totalStaked += amount;

        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to unstake their staked $GGG tokens.
     * @param amount The number of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked tokens");

        _updateRewards(msg.sender);

        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;
        require(gggToken.transfer(msg.sender, amount), "Token transfer failed");

        emit TokensUnstaked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to claim their staking rewards.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);

        uint256 rewards = stakes[msg.sender].rewardsEarned;
        require(rewards > 0, "No rewards available to claim");

        stakes[msg.sender].rewardsEarned = 0;
        require(gggToken.transfer(msg.sender, rewards), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param user The address of the user.
     */
    function _updateRewards(address user) internal {
        Stake storage stakeData = stakes[user];
        if (stakeData.amount > 0) {
            uint256 elapsedTime = block.timestamp - stakeData.lastStakedTime;
            uint256 newRewards = stakeData.amount * rewardRate * elapsedTime;
            stakeData.rewardsEarned += newRewards;
            stakeData.lastStakedTime = block.timestamp;
        }
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param newRewardRate The new reward rate per second per staked token.
     */
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        require(newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = newRewardRate;
    }
}
```
