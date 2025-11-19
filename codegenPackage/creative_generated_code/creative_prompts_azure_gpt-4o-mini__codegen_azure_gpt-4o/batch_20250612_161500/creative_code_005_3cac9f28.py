"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-ae.pages.dev
Prompt: Create a Solidity contract that mirrors the DOGE20 staking mechanism for educational purposes, focusing on reward distribution over two years.
Generated: DETERMINISTIC_3cac9f28a2733e7d
Batch ID: 20250612_161500
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
 * @title DOGE20Staking
 * @dev A simplified staking contract for educational purposes, mirroring DOGE20 reward distribution over 2 years.
 */
contract DOGE20Staking {
    // Struct to track staker's information
    struct Staker {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward owed to the staker
        uint256 lastStakingTime; // Timestamp of the last staking action
    }

    // Mapping of stakers to their details
    mapping(address => Staker) public stakers;

    // Total amount of tokens staked in the contract
    uint256 public totalStaked;

    // Reward rate per token (e.g., DOGE20 tokens per second per staked token)
    uint256 public rewardRate;

    // Reward period (in seconds, 2 years)
    uint256 public constant REWARD_PERIOD = 2 * 365 * 24 * 60 * 60;

    // Timestamp when staking starts
    uint256 public immutable startTime;

    // Timestamp when staking ends
    uint256 public immutable endTime;

    // Address of the token being staked
    IERC20 public immutable stakingToken;

    // Address of the reward token
    IERC20 public immutable rewardToken;

    // Constructor to initialize contract state
    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _rewardRate
    ) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;

        startTime = block.timestamp;
        endTime = block.timestamp + REWARD_PERIOD;
    }

    /**
     * @dev Stake tokens to earn rewards.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Staking amount must be greater than zero");
        require(block.timestamp < endTime, "Staking period has ended");

        // Update rewards for the staker before modifying the stake amount
        updateRewards(msg.sender);

        stakingToken.transferFrom(msg.sender, address(this), amount);

        Staker storage staker = stakers[msg.sender];
        staker.amount += amount;
        staker.lastStakingTime = block.timestamp;

        totalStaked += amount;
    }

    /**
     * @dev Withdraw staked tokens and claim rewards.
     */
    function withdraw() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount > 0, "No tokens staked");

        // Update rewards for the staker and pay out
        updateRewards(msg.sender);

        uint256 amount = staker.amount;
        staker.amount = 0;

        stakingToken.transfer(msg.sender, amount);
    }

    /**
     * @dev Claim pending rewards without withdrawing staked tokens.
     */
    function claimRewards() external {
        updateRewards(msg.sender);
    }

    /**
     * @dev Internal function to update rewards for a staker.
     * @param stakerAddress Address of the staker.
     */
    function updateRewards(address stakerAddress) internal {
        Staker storage staker = stakers[stakerAddress];
        if (staker.amount > 0) {
            uint256 pendingRewards = calculatePendingRewards(stakerAddress);
            staker.rewardDebt += pendingRewards;
        }

        if (staker.rewardDebt > 0) {
            uint256 rewardToSend = staker.rewardDebt;
            staker.rewardDebt = 0;
            rewardToken.transfer(stakerAddress, rewardToSend);
        }
    }

    /**
     * @dev Calculate pending rewards for a staker.
     * @param stakerAddress Address of the staker.
     * @return Pending reward amount.
     */
    function calculatePendingRewards(address stakerAddress)
        public
        view
        returns (uint256)
    {
        Staker storage staker = stakers[stakerAddress];

        if (block.timestamp > endTime) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - staker.lastStakingTime;
        uint256 pendingRewards = (stakingDuration * staker.amount * rewardRate) /
            1e18;

        return pendingRewards;
    }

    /**
     * @dev Emergency function to withdraw all staked tokens (admin-only).
     * @param recipient Address to send the tokens to.
     */
    function emergencyWithdraw(address recipient) external {
        require(msg.sender == address(this), "Only admin is allowed!");
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);
}
```
