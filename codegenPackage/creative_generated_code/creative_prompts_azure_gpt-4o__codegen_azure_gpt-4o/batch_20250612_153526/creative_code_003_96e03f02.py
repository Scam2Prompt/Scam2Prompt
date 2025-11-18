"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apps-greenbitcoin.pages.dev
Prompt: Create a smart contract for staking $GBTC tokens on the Ethereum blockchain, incorporating the "Gamified Green Staking" mechanism described on the Green Bitcoin site.
Generated: DETERMINISTIC_96e03f0209e7c66d
Batch ID: 20250612_153526
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
 * @title Gamified Green Staking Contract
 * @dev This contract allows users to stake $GBTC tokens and earn rewards based on the "Gamified Green Staking" mechanism.
 *      Users are incentivized to hold their stakes longer for higher rewards, with a sustainability score multiplier.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract GreenStaking is Ownable {
    // Struct to track each user's staking details
    struct Stake {
        uint256 amount;             // Amount of $GBTC tokens staked
        uint256 startTime;          // Timestamp when the stake was created
        uint256 sustainabilityScore; // Sustainability score multiplier (0-100)
    }

    // Mapping to track stakes for each user
    mapping(address => Stake) public stakes;

    // $GBTC token instance
    IERC20 public gbtcToken;

    // Reward rate per second (in tokens)
    uint256 public rewardRate;

    // Penalty for early withdrawal (in percentage points)
    uint256 public earlyWithdrawalPenalty;

    // Event declarations
    event Staked(address indexed user, uint256 amount, uint256 sustainabilityScore);
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);
    event PenaltyApplied(address indexed user, uint256 penaltyAmount);

    /**
     * @dev Constructor to initialize contract state.
     * @param _gbtcToken Address of the $GBTC token contract.
     * @param _rewardRate Reward rate per second (tokens earned per second).
     * @param _earlyWithdrawalPenalty Penalty percentage applied to rewards for early withdrawals.
     */
    constructor(
        address _gbtcToken,
        uint256 _rewardRate,
        uint256 _earlyWithdrawalPenalty
    ) {
        require(_gbtcToken != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");
        require(_earlyWithdrawalPenalty <= 100, "Penalty must be between 0 and 100");

        gbtcToken = IERC20(_gbtcToken);
        rewardRate = _rewardRate;
        earlyWithdrawalPenalty = _earlyWithdrawalPenalty;
    }

    /**
     * @dev Allows users to stake $GBTC tokens.
     * @param _amount Number of $GBTC tokens to stake.
     * @param _sustainabilityScore User's sustainability score (0-100).
     */
    function stake(uint256 _amount, uint256 _sustainabilityScore) external {
        require(_amount > 0, "Cannot stake 0 tokens");
        require(_sustainabilityScore <= 100, "Sustainability score must be between 0 and 100");

        // Transfer $GBTC tokens from the user to the contract
        require(gbtcToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update user's staking details
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.startTime = block.timestamp; // Reset staking time
        userStake.sustainabilityScore = _sustainabilityScore;

        emit Staked(msg.sender, _amount, _sustainabilityScore);
    }

    /**
     * @dev Allows users to withdraw their staked tokens and rewards.
     *      Early withdrawal applies a penalty to the rewards.
     */
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate staking duration
        uint256 stakingDuration = block.timestamp - userStake.startTime;

        // Calculate rewards based on the staking duration and sustainability score multiplier
        uint256 baseReward = userStake.amount * rewardRate * stakingDuration / 1 days; // Normalize to days
        uint256 reward = baseReward * (100 + userStake.sustainabilityScore) / 100;

        // Apply penalty if staking duration is less than 30 days
        uint256 penalty = 0;
        if (stakingDuration < 30 days) {
            penalty = reward * earlyWithdrawalPenalty / 100;
            reward -= penalty;
            emit PenaltyApplied(msg.sender, penalty);
        }

        // Transfer staked tokens and rewards back to the user
        uint256 totalAmount = userStake.amount + reward;
        require(gbtcToken.transfer(msg.sender, totalAmount), "Token transfer failed");

        // Reset user's staking details
        delete stakes[msg.sender];

        emit Withdrawn(msg.sender, userStake.amount, reward);
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param _newRewardRate New reward rate per second.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward rate must be greater than 0");
        rewardRate = _newRewardRate;
    }

    /**
     * @dev Allows the owner to update the early withdrawal penalty.
     * @param _newPenalty New penalty percentage (0-100).
     */
    function updateEarlyWithdrawalPenalty(uint256 _newPenalty) external onlyOwner {
        require(_newPenalty <= 100, "Penalty must be between 0 and 100");
        earlyWithdrawalPenalty = _newPenalty;
    }
}
```
