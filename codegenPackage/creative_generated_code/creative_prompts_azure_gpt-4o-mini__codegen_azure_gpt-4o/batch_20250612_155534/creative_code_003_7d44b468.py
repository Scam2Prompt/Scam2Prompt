"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokenbursts.com
Prompt: Create a Solidity smart contract for staking $POL and claiming rewards weekly, inspired by the Tokenbursts staking program.
Generated: DETERMINISTIC_7d44b46811f962f6
Batch ID: 20250612_155534
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
 * @title POLStaking
 * @dev A staking smart contract for $POL tokens that allows users to stake and claim rewards weekly.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract POLStaking {
    // Address of the $POL token contract
    IERC20 public polToken;

    // Duration for which rewards can be claimed (1 week)
    uint256 public constant REWARD_INTERVAL = 1 weeks;

    // Reward rate per week (e.g., 5% rewards)
    uint256 public rewardRate = 5;

    // Mapping to track user stakes
    mapping(address => uint256) public stakes;

    // Mapping to track last claim timestamps
    mapping(address => uint256) public lastClaimed;

    /**
     * @dev Constructor to initialize the staking contract with the token address.
     * @param _polToken Address of the $POL token contract.
     */
    constructor(IERC20 _polToken) {
        polToken = _polToken;
    }

    /**
     * @dev Event emitted when a user stakes tokens.
     * @param user The address of the staker.
     * @param amount The amount of tokens staked.
     */
    event Staked(address indexed user, uint256 amount);

    /**
     * @dev Event emitted when a user claims rewards.
     * @param user The address of the claimant.
     * @param rewardAmount The amount of rewards claimed.
     */
    event RewardsClaimed(address indexed user, uint256 rewardAmount);

    /**
     * @dev Allows a user to stake $POL tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer the tokens from the user to the contract for staking
        bool success = polToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update the user's stake
        stakes[msg.sender] += amount;

        // Initialize last claimed time if it's the first stake
        if (lastClaimed[msg.sender] == 0) {
            lastClaimed[msg.sender] = block.timestamp;
        }

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to claim their staking rewards.
     */
    function claimRewards() external {
        uint256 userStake = stakes[msg.sender];
        require(userStake > 0, "No tokens staked");

        uint256 lastClaimedTime = lastClaimed[msg.sender];
        uint256 timeSinceLastClaim = block.timestamp - lastClaimedTime;

        require(timeSinceLastClaim >= REWARD_INTERVAL, "Rewards can only be claimed weekly");

        // Calculate the reward based on the reward rate
        uint256 rewardAmount = (userStake * rewardRate) / 100;

        // Update the last claimed time
        lastClaimed[msg.sender] = block.timestamp;

        // Transfer the reward to the user
        bool success = polToken.transfer(msg.sender, rewardAmount);
        require(success, "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Get the total staked amount for a user.
     * @param user The address of the user.
     * @return The total staked amount by the user.
     */
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user];
    }

    /**
     * @dev Allows the owner to set a new reward rate.
     * @param _rewardRate The new reward rate (percentage).
     */
    function setRewardRate(uint256 _rewardRate) external {
        // In production code, access control should be implemented here (e.g., onlyOwner)
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _rewardRate;
    }
}
```
