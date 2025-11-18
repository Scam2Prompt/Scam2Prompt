"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monarch-game.pages.dev
Prompt: Write a Solidity contract to implement staking functionality for dragon holders, allowing them to earn `$LEGACY` tokens and claim add-ons.
Generated: DETERMINISTIC_e4ecc4b5b66a8db2
Batch ID: 20250612_153517
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
 * @title DragonStaking
 * @dev Implements staking functionality for dragon holders to earn $LEGACY tokens and claim add-ons.
 */
contract DragonStaking {
    // Token used for rewards
    IERC20 public legacyToken;

    // Struct to hold staking details for a user
    struct StakeInfo {
        uint256 amountStaked;
        uint256 lastRewardTimestamp;
        uint256 pendingRewards;
    }

    // Mapping of user address to their staking info
    mapping(address => StakeInfo) public stakes;

    // Reward rate: Tokens earned per second per dragon staked (example: 1e18 = 1 $LEGACY per second)
    uint256 public rewardRatePerSecond;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewards);
    event AddonClaimed(address indexed user, string addon);

    // Constructor
    constructor(IERC20 _legacyToken, uint256 _rewardRatePerSecond) {
        legacyToken = _legacyToken;
        rewardRatePerSecond = _rewardRatePerSecond;
    }

    /**
     * @dev Stake dragons to start earning rewards.
     * @param amount The number of dragons to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Calculate pending rewards for the user before updating stake
        _updateRewards(msg.sender);

        // Update user stake info
        StakeInfo storage userStake = stakes[msg.sender];
        userStake.amountStaked += amount;

        // Set the last reward timestamp
        userStake.lastRewardTimestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake dragons and stop earning rewards.
     * @param amount The number of dragons to unstake.
     */
    function unstake(uint256 amount) external {
        StakeInfo storage userStake = stakes[msg.sender];
        require(userStake.amountStaked >= amount, "Insufficient staked amount");

        // Calculate pending rewards before unstaking
        _updateRewards(msg.sender);

        // Update user stake info
        userStake.amountStaked -= amount;

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards in $LEGACY tokens.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);

        StakeInfo storage userStake = stakes[msg.sender];
        uint256 rewardsToClaim = userStake.pendingRewards;

        require(rewardsToClaim > 0, "No rewards to claim");

        userStake.pendingRewards = 0;

        // Transfer rewards to the user
        require(legacyToken.transfer(msg.sender, rewardsToClaim), "Failed to transfer rewards");

        emit RewardsClaimed(msg.sender, rewardsToClaim);
    }

    /**
     * @dev Claim an add-on for staked dragons (example: special skin, accessory, etc.).
     * @param addonName Name of the add-on being claimed.
     */
    function claimAddon(string memory addonName) external {
        require(stakes[msg.sender].amountStaked > 0, "Must have dragons staked to claim add-ons");

        emit AddonClaimed(msg.sender, addonName);
    }

    /**
     * @dev Internal function to update the rewards for a user.
     * @param user The address of the user to update rewards for.
     */
    function _updateRewards(address user) internal {
        StakeInfo storage userStake = stakes[user];
        if (userStake.amountStaked > 0) {
            uint256 timeElapsed = block.timestamp - userStake.lastRewardTimestamp;
            uint256 newRewards = timeElapsed * userStake.amountStaked * rewardRatePerSecond;

            userStake.pendingRewards += newRewards;
            userStake.lastRewardTimestamp = block.timestamp;
        }
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param newRewardRate The new reward rate per second.
     */
    function updateRewardRate(uint256 newRewardRate) external {
        // Add access control logic here if necessary
        rewardRatePerSecond = newRewardRate;
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
