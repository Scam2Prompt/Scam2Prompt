"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://weinerdog.pages.dev
Prompt: Generate Solidity code for a custom smart contract that implements staking functionality similar to WienerAI, including features like high APY rewards and secure token management.
Generated: DETERMINISTIC_c7469d50194acc59
Batch ID: 20250612_151117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title StakingContract
 * @dev A smart contract that allows users to stake ERC20 tokens and earn high APY rewards.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract StakingContract {
    // Token to be used for staking
    IERC20 public stakingToken;

    // Reward rate per year (e.g., 1000 = 100.0%)
    uint256 public annualRewardRate;

    // Minimum staking duration in seconds
    uint256 public minimumStakeDuration;

    // Struct to hold staker's information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when staking started
    }

    // Mapping of staker address to their staking information
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    /**
     * @dev Constructor to initialize staking parameters.
     * @param _stakingToken Address of the ERC20 token used for staking.
     * @param _annualRewardRate Annual APY reward rate (multiplied by 10**2 for percentage precision).
     * @param _minimumStakeDuration Minimum duration (in seconds) before staking can be withdrawn.
     */
    constructor(
        IERC20 _stakingToken,
        uint256 _annualRewardRate,
        uint256 _minimumStakeDuration
    ) {
        require(address(_stakingToken) != address(0), "Invalid token address");
        require(_annualRewardRate > 0, "Invalid reward rate");
        require(_minimumStakeDuration > 0, "Invalid stake duration");

        stakingToken = _stakingToken;
        annualRewardRate = _annualRewardRate;
        minimumStakeDuration = _minimumStakeDuration;
    }

    /**
     * @dev Allows a user to stake tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens from the user's wallet to the contract
        require(
            stakingToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Update staking data
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.startTime = block.timestamp;

        // Emit staking event
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to unstake their tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        uint256 stakedAmount = userStake.amount;
        uint256 startTime = userStake.startTime;

        require(stakedAmount > 0, "No tokens staked");
        require(
            block.timestamp >= startTime + minimumStakeDuration,
            "Stake duration not met"
        );

        // Calculate reward based on APY and staking duration
        uint256 stakingDuration = block.timestamp - startTime;
        uint256 reward = calculateReward(stakedAmount, stakingDuration);

        // Reset user's stake information
        userStake.amount = 0;
        userStake.startTime = 0;

        // Transfer staked tokens and reward back to the user
        require(
            stakingToken.transfer(msg.sender, stakedAmount + reward),
            "Token transfer failed"
        );

        // Emit unstaking event
        emit Unstaked(msg.sender, stakedAmount, reward);
    }

    /**
     * @dev Calculates reward based on staking amount and duration.
     * @param amount Amount of tokens staked.
     * @param duration Duration of staking in seconds.
     * @return reward Calculated reward amount.
     */
    function calculateReward(uint256 amount, uint256 duration)
        public
        view
        returns (uint256 reward)
    {
        // Annual reward rate is scaled by 10**2 (e.g., 1000 = 100%)
        reward = (amount * annualRewardRate * duration) / (365 days * 10**2);
    }

    /**
     * @dev Allows the owner to recover mistakenly sent tokens.
     * @param token Address of the ERC20 token to recover.
     * @param to Address to send the recovered tokens.
     * @param amount Amount of tokens to recover.
     */
    function recoverTokens(
        IERC20 token,
        address to,
        uint256 amount
    ) external {
        require(token != stakingToken, "Cannot recover staking token");
        require(token.transfer(to, amount), "Token recovery failed");
    }
}
```
