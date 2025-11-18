"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheai-def.web.app
Prompt: Create a function in Solidity to implement the $SCOTTY token staking mechanism, including reward calculation and lock period extension.
Generated: DETERMINISTIC_b0b4a2054233193d
Batch ID: 20250612_152620
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
 * @title SCOTTY Token Staking Contract
 * @dev Implements staking mechanism with reward calculation and lock period extension
 */
contract ScottyTokenStaking {
    IERC20 public scottyToken;

    // Struct to store staking information
    struct Stake {
        uint256 amount;         // Amount of tokens staked
        uint256 rewardDebt;     // Rewards earned but not withdrawn
        uint256 lockEndTime;    // Timestamp when the lock period ends
    }

    // Mapping to track stakes for each user
    mapping(address => Stake) private stakes;

    // Reward rate per second (example: 0.01 tokens per second)
    uint256 public rewardRate = 10; // 10 tokens per 1,000 seconds as an example

    // Minimum lock period in seconds (example: 30 days)
    uint256 public constant MIN_LOCK_PERIOD = 30 days;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 lockEndTime);
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);
    event RewardsClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the contract with the token address
     * @param _token Address of the SCOTTY token contract
     */
    constructor(IERC20 _token) {
        scottyToken = _token;
    }

    /**
     * @dev Stake SCOTTY tokens with a lock period
     * @param _amount Amount of tokens to stake
     * @param _lockDuration Lock duration in seconds (must be >= MIN_LOCK_PERIOD)
     */
    function stake(uint256 _amount, uint256 _lockDuration) external {
        require(_amount > 0, "Staking amount must be greater than zero");
        require(_lockDuration >= MIN_LOCK_PERIOD, "Lock duration must be at least MIN_LOCK_PERIOD");

        Stake storage userStake = stakes[msg.sender];

        // Update rewards before modifying stake
        _updateRewards(msg.sender);

        // Transfer tokens from user to the contract
        require(scottyToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update stake details
        userStake.amount += _amount;
        userStake.lockEndTime = block.timestamp + _lockDuration;

        emit Staked(msg.sender, _amount, userStake.lockEndTime);
    }

    /**
     * @dev Withdraw staked tokens and claim rewards
     */
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked tokens found");
        require(block.timestamp >= userStake.lockEndTime, "Tokens are still locked");

        // Update rewards before withdrawal
        _updateRewards(msg.sender);

        uint256 amount = userStake.amount;
        uint256 reward = userStake.rewardDebt;

        // Reset stake
        userStake.amount = 0;
        userStake.rewardDebt = 0;
        userStake.lockEndTime = 0;

        // Transfer staked tokens and rewards to the user
        require(scottyToken.transfer(msg.sender, amount), "Token transfer failed");
        require(scottyToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit Withdrawn(msg.sender, amount, reward);
    }

    /**
     * @dev Claim rewards without withdrawing staked tokens
     */
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked tokens found");

        // Update rewards before claiming
        _updateRewards(msg.sender);

        uint256 reward = userStake.rewardDebt;
        require(reward > 0, "No rewards available");

        // Reset reward debt
        userStake.rewardDebt = 0;

        // Transfer rewards to the user
        require(scottyToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Extend the lock period for staked tokens
     * @param _additionalDuration Additional lock duration in seconds
     */
    function extendLockPeriod(uint256 _additionalDuration) external {
        require(_additionalDuration >= MIN_LOCK_PERIOD, "Extension must be at least MIN_LOCK_PERIOD");

        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked tokens found");

        // Update rewards before modifying lock period
        _updateRewards(msg.sender);

        // Extend lock period
        userStake.lockEndTime += _additionalDuration;

        emit Staked(msg.sender, userStake.amount, userStake.lockEndTime);
    }

    /**
     * @dev Internal function to update rewards for a user
     * @param _user Address of the user
     */
    function _updateRewards(address _user) internal {
        Stake storage userStake = stakes[_user];

        if (userStake.amount > 0) {
            uint256 timeStaked = block.timestamp > userStake.lockEndTime
                ? userStake.lockEndTime - (block.timestamp - userStake.lockEndTime)
                : block.timestamp;

            uint256 pendingReward = (timeStaked * userStake.amount * rewardRate) / 1e18;

            userStake.rewardDebt += pendingReward;
        }
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
