"""
Generated Code Metadata:
========================
Original URL: https://vetterplatform.pages.dev
Prompt: Develop a smart contract in Solidity that facilitates the staking of VSL tokens, calculates preons, and applies tier multipliers for bonus preons based on the Vetter platform's rules.
Generated: DETERMINISTIC_4f1c98d54b2309e3
Batch ID: 20250612_152710
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title VSL Staking Contract
 * @author [Your Name]
 * @notice This contract facilitates the staking of VSL tokens, calculates preons, and applies tier multipliers for bonus preons.
 */
contract VSLStaking is ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfos;

    // VSL token contract
    IERC20 public vslToken;

    // Preon calculation parameters
    uint256 public preonCalculationRate; // Rate of preon calculation per VSL token
    uint256 public tier1Threshold; // Threshold for tier 1
    uint256 public tier2Threshold; // Threshold for tier 2
    uint256 public tier3Threshold; // Threshold for tier 3

    // Tier multipliers
    uint256 public tier1Multiplier; // Multiplier for tier 1
    uint256 public tier2Multiplier; // Multiplier for tier 2
    uint256 public tier3Multiplier; // Multiplier for tier 3

    // Event emitted when user stakes VSL tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes VSL tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when preons are calculated
    event PreonsCalculated(address indexed user, uint256 preons);

    // Struct to store user staking information
    struct UserStakingInfo {
        uint256 stakedAmount; // Amount of VSL tokens staked
        uint256 preons; // Preons calculated
    }

    /**
     * @notice Constructor
     * @param _vslToken VSL token contract
     * @param _preonCalculationRate Rate of preon calculation per VSL token
     * @param _tier1Threshold Threshold for tier 1
     * @param _tier2Threshold Threshold for tier 2
     * @param _tier3Threshold Threshold for tier 3
     * @param _tier1Multiplier Multiplier for tier 1
     * @param _tier2Multiplier Multiplier for tier 2
     * @param _tier3Multiplier Multiplier for tier 3
     */
    constructor(
        IERC20 _vslToken,
        uint256 _preonCalculationRate,
        uint256 _tier1Threshold,
        uint256 _tier2Threshold,
        uint256 _tier3Threshold,
        uint256 _tier1Multiplier,
        uint256 _tier2Multiplier,
        uint256 _tier3Multiplier
    ) {
        vslToken = _vslToken;
        preonCalculationRate = _preonCalculationRate;
        tier1Threshold = _tier1Threshold;
        tier2Threshold = _tier2Threshold;
        tier3Threshold = _tier3Threshold;
        tier1Multiplier = _tier1Multiplier;
        tier2Multiplier = _tier2Multiplier;
        tier3Multiplier = _tier3Multiplier;
    }

    /**
     * @notice Stake VSL tokens
     * @param amount Amount of VSL tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Invalid stake amount");

        // Transfer VSL tokens from user to contract
        vslToken.safeTransferFrom(msg.sender, address(this), amount);

        // Update user staking information
        userStakingInfos[msg.sender].stakedAmount += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake VSL tokens
     * @param amount Amount of VSL tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Invalid unstake amount");
        require(userStakingInfos[msg.sender].stakedAmount >= amount, "Insufficient staked amount");

        // Update user staking information
        userStakingInfos[msg.sender].stakedAmount -= amount;

        // Transfer VSL tokens from contract to user
        vslToken.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Calculate preons
     */
    function calculatePreons() external nonReentrant {
        uint256 stakedAmount = userStakingInfos[msg.sender].stakedAmount;
        require(stakedAmount > 0, "No staked amount");

        uint256 preons = stakedAmount * preonCalculationRate;

        // Apply tier multipliers
        if (stakedAmount >= tier3Threshold) {
            preons *= tier3Multiplier;
        } else if (stakedAmount >= tier2Threshold) {
            preons *= tier2Multiplier;
        } else if (stakedAmount >= tier1Threshold) {
            preons *= tier1Multiplier;
        }

        userStakingInfos[msg.sender].preons += preons;

        emit PreonsCalculated(msg.sender, preons);
    }

    /**
     * @notice Get user staking information
     * @param user User address
     * @return User staking information
     */
    function getUserStakingInfo(address user) external view returns (UserStakingInfo memory) {
        return userStakingInfos[user];
    }
}
```
