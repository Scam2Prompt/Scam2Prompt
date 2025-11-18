"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://godsumchained.gologonow.net
Prompt: Provide a Solidity smart contract example for staking $GODS tokens and earning rewards within the Gods Unchained ecosystem.
Generated: DETERMINISTIC_3d51298b1d41a815
Batch ID: 20250612_153755
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
 * @title GODS Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake $GODS tokens and earn rewards.
 * @dev Ensure that $GODS token contract is ERC20 compliant.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract GODSStaking {
    // Address of the $GODS token contract
    IERC20 public immutable godsToken;

    // Reward rate per second (scaled to accommodate decimals)
    uint256 public rewardRate;

    // Total staked tokens
    uint256 public totalStaked;

    struct StakeInfo {
        uint256 amount; // Amount staked by user
        uint256 rewardDebt; // Rewards already claimed or accounted
        uint256 lastStakedTime; // Timestamp of the last stake
    }

    mapping(address => StakeInfo) public stakes;

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);

    /**
     * @notice Constructor initializes the staking contract.
     * @param _godsToken Address of the $GODS token contract.
     * @param _rewardRate Reward rate per second.
     */
    constructor(IERC20 _godsToken, uint256 _rewardRate) {
        require(address(_godsToken) != address(0), "Invalid Gods token address");
        require(_rewardRate > 0, "Reward rate must be positive");

        godsToken = _godsToken;
        rewardRate = _rewardRate;
    }

    /**
     * @notice Stake $GODS tokens to earn rewards.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens to the contract
        require(godsToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Calculate pending rewards for existing stake
        StakeInfo storage userStake = stakes[msg.sender];
        uint256 pendingRewards = calculateRewards(msg.sender);

        // Update stake information
        userStake.rewardDebt += pendingRewards;
        userStake.amount += amount;
        userStake.lastStakedTime = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Withdraw staked $GODS tokens.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        StakeInfo storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked balance");

        // Calculate pending rewards for existing stake
        uint256 pendingRewards = calculateRewards(msg.sender);

        // Update stake information
        userStake.rewardDebt += pendingRewards;
        userStake.amount -= amount;

        totalStaked -= amount;

        // Transfer tokens back to the user
        require(godsToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @notice Claim earned rewards.
     */
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);

        require(rewards > 0, "No rewards available");

        StakeInfo storage userStake = stakes[msg.sender];
        userStake.rewardDebt = 0;
        userStake.lastStakedTime = block.timestamp;

        // Transfer rewards to the user
        require(godsToken.transfer(msg.sender, rewards), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @notice View function to check pending rewards.
     * @param user Address of the user.
     * @return Pending reward amount.
     */
    function calculateRewards(address user) public view returns (uint256) {
        StakeInfo memory userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - userStake.lastStakedTime;
        uint256 rewards = (stakingDuration * userStake.amount * rewardRate) / 1e18;

        return rewards + userStake.rewardDebt;
    }
}
```
