"""
Generated Code Metadata:
========================
Original URL: https://rebelsatoshi-io.web.app
Prompt: Generate a Solidity code snippet for a staking mechanism similar to the one described in the Rebel Satoshi project, which rewards users with a percentage return for locking up $RBLZ tokens.
Generated: DETERMINISTIC_6dd331832c8315aa
Batch ID: 20250622_210216
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
 * @dev A staking mechanism for $RBLZ tokens that rewards users with a percentage return for locking up tokens.
 */
contract StakingContract {
    // ERC20 token interface
    IERC20 public rblzToken;

    // Reward percentage (e.g., 5% = 500 basis points)
    uint256 public rewardRateBasisPoints;

    // Duration of staking in seconds
    uint256 public stakingDuration;

    // Struct to store staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when staking started
        bool claimed; // Whether rewards have been claimed
    }

    // Mapping of user address to their stake
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 startTime);
    event RewardsClaimed(address indexed user, uint256 rewardAmount);
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _rblzToken Address of the $RBLZ token contract.
     * @param _rewardRateBasisPoints Reward rate in basis points (e.g., 500 for 5%).
     * @param _stakingDuration Duration of staking in seconds.
     */
    constructor(
        IERC20 _rblzToken,
        uint256 _rewardRateBasisPoints,
        uint256 _stakingDuration
    ) {
        require(address(_rblzToken) != address(0), "Invalid token address");
        require(_rewardRateBasisPoints > 0, "Reward rate must be positive");
        require(_stakingDuration > 0, "Staking duration must be positive");

        rblzToken = _rblzToken;
        rewardRateBasisPoints = _rewardRateBasisPoints;
        stakingDuration = _stakingDuration;
    }

    /**
     * @dev Stake $RBLZ tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(
            stakes[msg.sender].amount == 0,
            "Already staking, please unstake first"
        );

        // Transfer tokens from user to contract
        require(
            rblzToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Record staking information
        stakes[msg.sender] = Stake({
            amount: _amount,
            startTime: block.timestamp,
            claimed: false
        });

        emit Staked(msg.sender, _amount, block.timestamp);
    }

    /**
     * @dev Claim rewards after staking duration has passed.
     */
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No active stake found");
        require(!userStake.claimed, "Rewards already claimed");
        require(
            block.timestamp >= userStake.startTime + stakingDuration,
            "Staking duration not yet completed"
        );

        // Calculate reward amount
        uint256 rewardAmount = (userStake.amount * rewardRateBasisPoints) /
            10000;

        // Mark rewards as claimed
        userStake.claimed = true;

        // Transfer rewards to user
        require(
            rblzToken.transfer(msg.sender, rewardAmount),
            "Reward transfer failed"
        );

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Unstake tokens after claiming rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No active stake found");
        require(userStake.claimed, "Claim rewards before unstaking");

        uint256 amountToUnstake = userStake.amount;

        // Reset stake information
        delete stakes[msg.sender];

        // Transfer staked tokens back to user
        require(
            rblzToken.transfer(msg.sender, amountToUnstake),
            "Unstake transfer failed"
        );

        emit Unstaked(msg.sender, amountToUnstake);
    }
}

// Minimal ERC20 interface
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
