"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-edd.pages.dev
Prompt: Write a smart contract in Solidity for staking $DOGE20 tokens that distributes rewards over two years to participants in the staking pool.
Generated: DETERMINISTIC_8cbbf4dcb877617c
Batch ID: 20250612_163732
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
 * @dev A staking contract for $DOGE20 tokens that distributes rewards over two years.
 */
contract StakingContract {
    // ERC20 interface for interacting with the $DOGE20 token
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    struct Stake {
        uint256 amount;        // Amount of tokens staked by the user
        uint256 rewardDebt;    // Rewards already claimed
        uint256 stakeTime;     // Timestamp of when the stake was created
    }

    // State variables
    IERC20 public doge20Token;                   // ERC20 token address
    uint256 public rewardRate;                   // Reward rate in tokens per second
    uint256 public stakingPeriod = 2 * 365 days; // Total staking period (2 years)
    uint256 public totalStaked;                  // Total tokens staked in the pool
    mapping(address => Stake) public stakes;     // Mapping of user stakes

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor initializes the contract with $DOGE20 token address and reward rate.
     * @param _doge20Token Address of the $DOGE20 token contract.
     * @param _rewardRate Rewards distributed per second per token staked.
     */
    constructor(address _doge20Token, uint256 _rewardRate) {
        require(_doge20Token != address(0), "Token address cannot be zero");
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        doge20Token = IERC20(_doge20Token);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows users to stake tokens.
     * @param amount Number of $DOGE20 tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(doge20Token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Calculate pending rewards for previously staked tokens
        if (stakes[msg.sender].amount > 0) {
            uint256 pendingRewards = _calculateRewards(msg.sender);
            stakes[msg.sender].rewardDebt += pendingRewards;
        }

        // Update user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].stakeTime = block.timestamp;

        // Update total staked tokens
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to unstake tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate pending rewards
        uint256 pendingRewards = _calculateRewards(msg.sender);
        uint256 totalRewards = userStake.rewardDebt + pendingRewards;

        // Transfer staked tokens back to the user
        uint256 amount = userStake.amount;
        require(doge20Token.transfer(msg.sender, amount), "Token transfer failed");

        // Transfer rewards to the user
        if (totalRewards > 0) {
            require(doge20Token.transfer(msg.sender, totalRewards), "Reward transfer failed");
        }

        // Reset user's stake
        totalStaked -= userStake.amount;
        delete stakes[msg.sender];

        emit Unstaked(msg.sender, amount);
        emit RewardClaimed(msg.sender, totalRewards);
    }

    /**
     * @dev Calculates pending rewards for a user based on their stake.
     * @param user Address of the user.
     * @return Rewards pending for the user.
     */
    function _calculateRewards(address user) internal view returns (uint256) {
        Stake storage userStake = stakes[user];
        uint256 stakingDuration = block.timestamp - userStake.stakeTime;
        uint256 effectiveDuration = stakingDuration > stakingPeriod ? stakingPeriod : stakingDuration;
        return (userStake.amount * rewardRate * effectiveDuration) / 1e18;
    }

    /**
     * @dev Allows the owner to withdraw excess $DOGE20 tokens (non-staked tokens).
     * @param amount Number of tokens to withdraw.
     */
    function withdrawExcessTokens(uint256 amount) external {
        // For simplicity, assume the owner is the deployer (msg.sender here)
        // In production, implement access control (e.g., with Ownable)
        require(amount > 0, "Amount must be greater than zero");
        require(doge20Token.balanceOf(address(this)) >= amount + totalStaked, "Insufficient excess tokens");
        require(doge20Token.transfer(msg.sender, amount), "Token transfer failed");
    }
}
```
