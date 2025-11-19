"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decubate-platform.pages.dev
Prompt: How can I implement a smart contract to manage DCB staking rewards with a fixed APY of 22% for a 180-day lock term?
Generated: DETERMINISTIC_1e04fc4d29ce4f66
Batch ID: 20250612_162325
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
 * @title DCBStakingRewards
 * @dev A smart contract to manage staking rewards for DCB token holders.
 * Users can stake their tokens for a fixed 180-day lock term with an annualized percentage yield (APY) of 22%.
 */
contract DCBStakingRewards {
    // Address of the DCB token contract
    IERC20 public immutable dcbToken;

    // Annual Percentage Yield (APY) in percentage (e.g., 22 for 22%)
    uint256 public constant APY = 22;

    // Lock term duration in seconds (180 days)
    uint256 public constant LOCK_DURATION = 180 days;

    // Struct to store staking details for each user
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when staking started
        bool claimed; // Whether rewards have been claimed
    }

    // Mapping of user address to staking details
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 startTime);
    event RewardsClaimed(address indexed user, uint256 rewardAmount);
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the DCB token address.
     * @param _dcbToken Address of the DCB token contract.
     */
    constructor(IERC20 _dcbToken) {
        require(address(_dcbToken) != address(0), "Invalid token address");
        dcbToken = _dcbToken;
    }

    /**
     * @dev Allows a user to stake DCB tokens for the fixed lock term.
     * @param _amount The amount of DCB tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender].amount == 0, "Already staking");

        // Transfer tokens from user to contract
        require(dcbToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Record staking details
        stakes[msg.sender] = Stake({
            amount: _amount,
            startTime: block.timestamp,
            claimed: false
        });

        emit Staked(msg.sender, _amount, block.timestamp);
    }

    /**
     * @dev Allows a user to claim their staking rewards after the lock term has passed.
     */
    function claimRewards() external {
        Stake storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.amount > 0, "No active stake");
        require(!stakeInfo.claimed, "Rewards already claimed");
        require(block.timestamp >= stakeInfo.startTime + LOCK_DURATION, "Lock term not yet completed");

        // Calculate rewards
        uint256 rewardAmount = _calculateRewards(stakeInfo.amount);
        stakeInfo.claimed = true;

        // Transfer rewards to user
        require(dcbToken.transfer(msg.sender, rewardAmount), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Allows a user to unstake their tokens if the lock term has passed.
     */
    function unstake() external {
        Stake storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.amount > 0, "No active stake");
        require(block.timestamp >= stakeInfo.startTime + LOCK_DURATION, "Lock term not yet completed");

        uint256 amountToUnstake = stakeInfo.amount;
        stakeInfo.amount = 0; // Reset stake amount

        // Transfer staked tokens back to user
        require(dcbToken.transfer(msg.sender, amountToUnstake), "Unstake transfer failed");

        emit Unstaked(msg.sender, amountToUnstake);
    }

    /**
     * @dev Helper function to calculate staking rewards based on APY.
     * @param _amount The staked amount.
     * @return The reward amount.
     */
    function _calculateRewards(uint256 _amount) internal pure returns (uint256) {
        // Calculate rewards based on APY and lock duration
        return (_amount * APY * LOCK_DURATION) / (365 days * 100);
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
