"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-flockerz-com.pages.dev
Prompt: Generate a Solidity smart contract that implements a staking mechanism for $FLOCK tokens with a 220% APY for a 2-year staking period.
Generated: DETERMINISTIC_9891ce2dae284239
Batch ID: 20250612_154239
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title FlockStaking
 * @dev A smart contract for staking $FLOCK tokens with a 220% APY for a 2-year period.
 */
contract FlockStaking is ReentrancyGuard {
    using SafeMath for uint256;

    // Constants
    uint256 public constant APY = 220; // 220% APY
    uint256 public constant STAKING_PERIOD = 730 days; // 2 years
    uint256 public constant BASE = 100; // Base for percentage calculations

    // Token to be staked
    IERC20 public flockToken;

    // Struct for staking information
    struct Stake {
        uint256 amount;
        uint256 startTime;
        bool isActive;
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) private stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Constructor to initialize the token contract
    constructor(IERC20 _flockToken) {
        flockToken = _flockToken;
    }

    /**
     * @dev Stake $FLOCK tokens for a specified duration.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(flockToken.balanceOf(msg.sender) >= amount, "Insufficient balance");
        require(flockToken.allowance(msg.sender, address(this)) >= amount, "Token allowance required");

        // Transfer tokens from the user to the contract
        flockToken.transferFrom(msg.sender, address(this), amount);

        // Create or update the user's stake
        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount.add(amount),
            startTime: block.timestamp,
            isActive: true
        });

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and receive rewards after the staking period.
     */
    function unstake() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.isActive, "No active stake found");
        require(block.timestamp >= userStake.startTime + STAKING_PERIOD, "Staking period not yet over");

        // Calculate the reward
        uint256 reward = calculateReward(userStake.amount);
        
        // Update the stake status
        userStake.isActive = false;
        
        // Transfer staked tokens and rewards back to the user
        flockToken.transfer(msg.sender, userStake.amount.add(reward));

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    /**
     * @dev Calculate the reward based on the staked amount.
     * @param amount Amount of tokens staked.
     * @return uint256 Total reward amount.
     */
    function calculateReward(uint256 amount) private view returns (uint256) {
        return amount.mul(APY).div(BASE).mul(STAKING_PERIOD).div(365 days);
    }

    /**
     * @dev Get the staking information for a user.
     * @param user The address of the user.
     * @return amount The amount staked by the user.
     * @return startTime The time when the user started staking.
     * @return isActive The status of the stake.
     */
    function getStakeInfo(address user) external view returns (uint256 amount, uint256 startTime, bool isActive) {
        Stake storage userStake = stakes[user];
        return (userStake.amount, userStake.startTime, userStake.isActive);
    }
}
```
