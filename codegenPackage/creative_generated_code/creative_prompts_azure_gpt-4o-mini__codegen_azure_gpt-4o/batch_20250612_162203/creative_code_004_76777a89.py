"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gigachadgpt.pages.dev
Prompt: Describe the steps to implement a staking mechanism for $GIGA tokens and provide a code example for a smart contract that manages staking rewards.
Generated: DETERMINISTIC_76777a89f9cc690b
Batch ID: 20250612_162203
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
 * @title GIGA Token Staking Contract
 * @dev This contract allows users to stake GIGA tokens and earn staking rewards.
 */
contract GIGAStaking {
    // ERC20 token interface
    interface IERC20 {
        function transferFrom(address from, address to, uint256 amount) external returns (bool);
        function transfer(address to, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // Address of the GIGA token contract
    IERC20 public immutable gigaToken;

    // Annual percentage rate (APR) for rewards (e.g., 10 means 10%)
    uint256 public immutable rewardRate;
    uint256 public constant REWARD_DIVISOR = 100;

    // Struct to store staking information
    struct Stake {
        uint256 amount;       // The amount staked by the user
        uint256 rewardDebt;   // Rewards already paid out
        uint256 lastStakedAt; // Timestamp of the last staking action
    }

    // Mapping to track stakes for each address
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the GIGA token address and reward rate.
     * @param _gigaToken Address of the GIGA token contract
     * @param _rewardRate Annual percentage rate (APR) for staking rewards
     */
    constructor(IERC20 _gigaToken, uint256 _rewardRate) {
        require(address(_gigaToken) != address(0), "Invalid GIGA token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        gigaToken = _gigaToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows a user to stake GIGA tokens.
     * @param _amount The amount of tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the user's wallet to the contract
        require(gigaToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        Stake storage userStake = stakes[msg.sender];
        uint256 pendingRewards = _calculateRewards(msg.sender);

        // Update the user's stake
        userStake.rewardDebt += pendingRewards;
        userStake.amount += _amount;
        userStake.lastStakedAt = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows a user to unstake their GIGA tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        uint256 pendingRewards = _calculateRewards(msg.sender);
        uint256 totalRewards = userStake.rewardDebt + pendingRewards;
        uint256 stakedAmount = userStake.amount;

        // Reset user's stake
        userStake.amount = 0;
        userStake.rewardDebt = 0;
        userStake.lastStakedAt = 0;

        // Transfer staked tokens and rewards back to the user
        require(gigaToken.transfer(msg.sender, stakedAmount), "Token transfer failed");
        require(gigaToken.transfer(msg.sender, totalRewards), "Reward transfer failed");

        emit Unstaked(msg.sender, stakedAmount);
        emit RewardClaimed(msg.sender, totalRewards);
    }

    /**
     * @dev Allows a user to claim their staking rewards without unstaking.
     */
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        uint256 pendingRewards = _calculateRewards(msg.sender);
        uint256 totalRewards = userStake.rewardDebt + pendingRewards;

        // Update reward debt
        userStake.rewardDebt = 0;
        userStake.lastStakedAt = block.timestamp;

        // Transfer rewards to the user
        require(gigaToken.transfer(msg.sender, totalRewards), "Reward transfer failed");

        emit RewardClaimed(msg.sender, totalRewards);
    }

    /**
     * @dev Internal function to calculate pending rewards for a user.
     * @param _user Address of the user
     * @return The amount of pending rewards
     */
    function _calculateRewards(address _user) internal view returns (uint256) {
        Stake storage userStake = stakes[_user];
        if (userStake.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp - userStake.lastStakedAt;
        uint256 annualRewards = (userStake.amount * rewardRate) / REWARD_DIVISOR;
        uint256 pendingRewards = (annualRewards * stakingDuration) / 365 days;

        return pendingRewards;
    }
}
```
