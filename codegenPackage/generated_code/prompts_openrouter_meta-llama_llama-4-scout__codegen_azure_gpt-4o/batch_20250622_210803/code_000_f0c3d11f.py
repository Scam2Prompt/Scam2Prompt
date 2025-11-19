"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20ai.pages.dev
Prompt: Write a smart contract in Solidity for a staking system that distributes rewards to stakers over a period of two years, similar to Dogecoin20's staking mechanism.
Generated: DETERMINISTIC_f0c3d11f271cc2dc
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title StakingContract
 * @dev A staking contract that allows users to stake tokens and earn rewards over a period of two years.
 */
contract StakingContract {
    // Token interface
    IERC20 public immutable stakingToken;

    // Duration of the staking rewards distribution (2 years)
    uint256 public constant REWARD_DURATION = 2 * 365 days;

    // Total rewards to be distributed
    uint256 public immutable totalReward;

    // Timestamp when staking starts
    uint256 public immutable startTime;

    // Timestamp when staking ends
    uint256 public immutable endTime;

    // Total staked tokens
    uint256 public totalStaked;

    // Mapping of user address to staked amount
    mapping(address => uint256) public stakedBalances;

    // Mapping of user address to rewards claimed
    mapping(address => uint256) public rewardsClaimed;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _stakingToken Address of the ERC20 token to be staked.
     * @param _totalReward Total reward to be distributed over the staking period.
     */
    constructor(IERC20 _stakingToken, uint256 _totalReward) {
        require(address(_stakingToken) != address(0), "Invalid token address");
        require(_totalReward > 0, "Reward must be greater than zero");

        stakingToken = _stakingToken;
        totalReward = _totalReward;
        startTime = block.timestamp;
        endTime = startTime + REWARD_DURATION;
    }

    /**
     * @dev Modifier to ensure staking is active.
     */
    modifier stakingActive() {
        require(block.timestamp >= startTime, "Staking has not started yet");
        require(block.timestamp <= endTime, "Staking period has ended");
        _;
    }

    /**
     * @dev Modifier to ensure staking has ended.
     */
    modifier stakingEnded() {
        require(block.timestamp > endTime, "Staking period is still active");
        _;
    }

    /**
     * @dev Stake tokens to participate in the rewards program.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external stakingActive {
        require(amount > 0, "Cannot stake zero tokens");

        // Transfer tokens from the user to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staked balance and total staked
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens after the staking period has ended.
     */
    function unstake() external stakingEnded {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No tokens to unstake");

        // Reset staked balance
        stakedBalances[msg.sender] = 0;

        // Transfer staked tokens back to the user
        require(stakingToken.transfer(msg.sender, stakedAmount), "Token transfer failed");

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev Claim rewards based on the user's staked amount and elapsed time.
     */
    function claimReward() external {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No staked tokens");

        // Calculate reward based on elapsed time and staked amount
        uint256 elapsedTime = block.timestamp > endTime ? endTime - startTime : block.timestamp - startTime;
        uint256 reward = (stakedAmount * totalReward * elapsedTime) / (totalStaked * REWARD_DURATION);

        // Ensure rewards are not claimed multiple times
        uint256 claimableReward = reward - rewardsClaimed[msg.sender];
        require(claimableReward > 0, "No rewards to claim");

        // Update claimed rewards
        rewardsClaimed[msg.sender] += claimableReward;

        // Transfer reward to the user
        require(stakingToken.transfer(msg.sender, claimableReward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, claimableReward);
    }

    /**
     * @dev Get the claimable reward for a user.
     * @param user Address of the user.
     * @return Claimable reward amount.
     */
    function getClaimableReward(address user) external view returns (uint256) {
        uint256 stakedAmount = stakedBalances[user];
        if (stakedAmount == 0) {
            return 0;
        }

        uint256 elapsedTime = block.timestamp > endTime ? endTime - startTime : block.timestamp - startTime;
        uint256 reward = (stakedAmount * totalReward * elapsedTime) / (totalStaked * REWARD_DURATION);
        return reward - rewardsClaimed[user];
    }
}

/**
 * @dev Interface for ERC20 token.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
