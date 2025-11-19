"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presalenest-goodeggtoken.web.app
Prompt: Illustrate how to implement a feature that allows users to stake their $GEGG tokens and earn rewards within the GoodEgg ecosystem.
Generated: DETERMINISTIC_382af93a45dbe479
Batch ID: 20250612_155449
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title GoodEggStaking
 * @dev A staking contract that allows users to stake their $GEGG tokens and earn rewards.
 */
contract GoodEggStaking is ReentrancyGuard, Ownable {
    IERC20 public geggToken; // The $GEGG token contract
    uint256 public rewardRate; // Reward rate per block
    uint256 public totalStaked; // Total tokens staked
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public rewards; // Rewards for each user
    mapping(address => uint256) public lastUpdate; // Last time rewards were updated for each user

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the $GEGG token and reward rate.
     * @param _geggToken Address of the $GEGG token contract.
     * @param _rewardRate Reward rate per block (in tokens).
     */
    constructor(IERC20 _geggToken, uint256 _rewardRate) {
        geggToken = _geggToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Staking function that allows users to stake $GEGG tokens.
     * @param amount Amount of $GEGG tokens to stake.
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(geggToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        // Update rewards before staking
        _updateRewards(msg.sender);

        stakedAmount[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstaking function that allows users to unstake their $GEGG tokens.
     * @param amount Amount of $GEGG tokens to unstake.
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedAmount[msg.sender] >= amount, "Not enough staked tokens");

        // Update rewards before unstaking
        _updateRewards(msg.sender);

        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;

        require(geggToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim their accumulated rewards.
     */
    function claimRewards() external nonReentrant {
        _updateRewards(msg.sender);
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available");

        rewards[msg.sender] = 0;
        require(geggToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Internal function to update the rewards of a user.
     * @param user Address of the user to update rewards for.
     */
    function _updateRewards(address user) internal {
        uint256 staked = stakedAmount[user];
        uint256 blocksPassed = block.number - lastUpdate[user];

        if (blocksPassed > 0 && staked > 0) {
            rewards[user] += staked * blocksPassed * rewardRate;
        }

        lastUpdate[user] = block.number;
    }

    /**
     * @dev Allows the owner to set a new reward rate.
     * @param newRewardRate New reward rate per block.
     */
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        _updateAllRewards();
        rewardRate = newRewardRate;
    }

    /**
     * @dev Internal function to update rewards for all users.
     */
    function _updateAllRewards() internal {
        for (uint256 i = 0; i < totalStaked; i++) {
            address user = address(i); // Placeholder, implement logic to iterate users
            _updateRewards(user);
        }
    }
}
```

Ensure you have the OpenZeppelin library integrated in your project to use the imported contracts.
