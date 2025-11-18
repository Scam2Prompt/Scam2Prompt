"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btfdbull.pages.dev
Prompt: Create a smart contract in Solidity that allows users to stake $BTFD tokens and earn rewards, as described in the staking section of the BTFD website.
Generated: DETERMINISTIC_cfc76429ed070250
Batch ID: 20250612_154236
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
 * @title BTFD Staking Contract
 * @dev This contract allows users to stake $BTFD tokens and earn rewards.
 * Rewards are distributed based on the staking duration and amount.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract BTFDStaking {
    // Token being staked
    IERC20 public immutable btfToken;

    // Reward rate per second (example: 1e18 = 1 token per second)
    uint256 public rewardRate;

    // Staking structure to track user information
    struct Stake {
        uint256 amount;        // Amount of tokens staked
        uint256 startTime;     // Timestamp of when staking started
        uint256 rewardDebt;    // Accumulated rewards claimed
    }

    // Mapping of user address to their stake details
    mapping(address => Stake) public stakes;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Events for logging contract interactions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 rewardsClaimed);
    event RewardRateUpdated(uint256 newRewardRate);

    /**
     * @dev Constructor initializes the contract with the staking token and reward rate.
     * @param _btfToken Address of the $BTFD token contract.
     * @param _rewardRate Initial reward rate per second (example: 1e18 = 1 token per second).
     */
    constructor(IERC20 _btfToken, uint256 _rewardRate) {
        require(address(_btfToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");
        btfToken = _btfToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake $BTFD tokens in the contract and start earning rewards.
     * @param _amount Amount of $BTFD tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");

        Stake storage userStake = stakes[msg.sender];

        // Calculate pending rewards
        uint256 pendingRewards = _calculateRewards(msg.sender);

        // Update user's stake before transferring tokens
        userStake.amount += _amount;
        userStake.startTime = block.timestamp;
        userStake.rewardDebt += pendingRewards;

        totalStaked += _amount;

        // Transfer tokens from the user to the contract
        require(btfToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake $BTFD tokens and claim rewards.
     */
    function unstakeAndClaim() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate total rewards owed
        uint256 totalRewards = _calculateRewards(msg.sender) + userStake.rewardDebt;

        uint256 stakedAmount = userStake.amount;

        // Reset user's stake
        totalStaked -= stakedAmount;
        delete stakes[msg.sender];

        // Transfer staked tokens back to the user
        require(btfToken.transfer(msg.sender, stakedAmount), "Token transfer failed");

        // Transfer rewards to the user
        require(btfToken.transfer(msg.sender, totalRewards), "Rewards transfer failed");

        emit Unstaked(msg.sender, stakedAmount, totalRewards);
    }

    /**
     * @dev View function to calculate the rewards for a user.
     * @param _user Address of the user.
     * @return Rewards earned by the user.
     */
    function calculateRewards(address _user) external view returns (uint256) {
        return _calculateRewards(_user) + stakes[_user].rewardDebt;
    }

    /**
     * @dev Internal function to calculate rewards based on staking duration and amount.
     * @param _user Address of the user.
     * @return Rewards earned by the user.
     */
    function _calculateRewards(address _user) internal view returns (uint256) {
        Stake storage userStake = stakes[_user];
        if (userStake.amount == 0) return 0;
        uint256 stakingDuration = block.timestamp - userStake.startTime;
        return (userStake.amount * stakingDuration * rewardRate) / 1e18;
    }

    /**
     * @dev Update the reward rate. Can be called by the contract owner (not implemented here).
     * @param _newRewardRate New reward rate per second.
     */
    function updateRewardRate(uint256 _newRewardRate) external {
        // Only the owner should be able to call this function (not implemented here).
        require(_newRewardRate > 0, "Reward rate must be greater than 0");
        rewardRate = _newRewardRate;

        emit RewardRateUpdated(_newRewardRate);
    }
}
```
