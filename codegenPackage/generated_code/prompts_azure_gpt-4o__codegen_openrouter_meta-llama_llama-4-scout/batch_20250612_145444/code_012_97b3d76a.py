"""
Generated Code Metadata:
========================
Original URL: https://flockerz-claim.web.app
Prompt: Create a Solidity contract for a presale mechanism that rewards early adopters with staking bonuses and voting rights, as described in Flockerz.
Generated: DETERMINISTIC_97b3d76a4d6bed12
Batch ID: 20250612_145444
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Flockerz Presale Contract
 * @author [Your Name]
 * @notice This contract manages the presale mechanism for Flockerz, 
 *          rewarding early adopters with staking bonuses and voting rights.
 */
contract FlockerzPresale is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping (address => UserStaking) public userStakings;

    // Mapping of user voting rights
    mapping (address => uint256) public userVotingRights;

    // Token contract instance
    ERC20Burnable public token;

    // Presale start and end timestamps
    uint256 public presaleStart;
    uint256 public presaleEnd;

    // Staking bonus rates
    uint256 public constant STAKING_BONUS_RATE_1 = 10; // 10% bonus for first 100 users
    uint256 public constant STAKING_BONUS_RATE_2 = 5;  // 5% bonus for next 200 users

    // Maximum staking amount
    uint256 public constant MAX_STAKING_AMOUNT = 1000 ether;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user claims staking bonus
    event StakingBonusClaimed(address indexed user, uint256 bonus);

    // Event emitted when user claims voting rights
    event VotingRightsClaimed(address indexed user, uint256 votingRights);

    /**
     * @param _token Token contract address
     * @param _presaleStart Presale start timestamp
     * @param _presaleEnd Presale end timestamp
     */
    constructor(ERC20Burnable _token, uint256 _presaleStart, uint256 _presaleEnd) public {
        require(_presaleStart < _presaleEnd, "Presale start timestamp must be less than presale end timestamp");

        token = _token;
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
    }

    /**
     * @notice Stake tokens and earn bonus
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(msg.sender != address(0), "User address cannot be zero");
        require(_amount > 0, "Staking amount must be greater than zero");
        require(_amount <= MAX_STAKING_AMOUNT, "Staking amount exceeds maximum allowed");
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale period has not started or has ended");

        // Update user staking information
        userStakings[msg.sender].stakedAmount = userStakings[msg.sender].stakedAmount.add(_amount);
        userStakings[msg.sender].stakedAt = block.timestamp;

        // Transfer tokens from user to contract
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Claim staking bonus
     */
    function claimStakingBonus() external nonReentrant {
        require(userStakings[msg.sender].stakedAmount > 0, "User has not staked tokens");
        require(userStakings[msg.sender].bonusClaimed == false, "Staking bonus has already been claimed");

        // Calculate staking bonus
        uint256 stakingBonus = calculateStakingBonus(userStakings[msg.sender].stakedAmount, userStakings[msg.sender].stakedAt);

        // Update user staking information
        userStakings[msg.sender].bonusClaimed = true;

        // Transfer staking bonus to user
        require(token.transfer(msg.sender, stakingBonus), "Token transfer failed");

        emit StakingBonusClaimed(msg.sender, stakingBonus);
    }

    /**
     * @notice Claim voting rights
     */
    function claimVotingRights() external nonReentrant {
        require(userStakings[msg.sender].stakedAmount > 0, "User has not staked tokens");
        require(userVotingRights[msg.sender] == 0, "Voting rights have already been claimed");

        // Calculate voting rights
        uint256 votingRights = calculateVotingRights(userStakings[msg.sender].stakedAmount);

        // Update user voting rights
        userVotingRights[msg.sender] = votingRights;

        emit VotingRightsClaimed(msg.sender, votingRights);
    }

    /**
     * @notice Calculate staking bonus
     * @param _stakedAmount Staked amount
     * @param _stakedAt Timestamp when tokens were staked
     * @return Staking bonus
     */
    function calculateStakingBonus(uint256 _stakedAmount, uint256 _stakedAt) internal view returns (uint256) {
        // Implement staking bonus calculation logic here
        // For demonstration purposes, a simple calculation is used
        uint256 stakingBonusRate = (userStakings[msg.sender].stakedAt < presaleStart.add(1 days)) ? STAKING_BONUS_RATE_1 : STAKING_BONUS_RATE_2;
        return _stakedAmount.mul(stakingBonusRate).div(100);
    }

    /**
     * @notice Calculate voting rights
     * @param _stakedAmount Staked amount
     * @return Voting rights
     */
    function calculateVotingRights(uint256 _stakedAmount) internal view returns (uint256) {
        // Implement voting rights calculation logic here
        // For demonstration purposes, a simple calculation is used
        return _stakedAmount.div(10 ether);
    }

    // User staking information struct
    struct UserStaking {
        uint256 stakedAmount;
        uint256 stakedAt;
        bool bonusClaimed;
    }
}
```
