"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcointoken.pages.dev
Prompt: Provide an example of a smart contract for staking Green Bitcoin ($GBTC) that incorporates gamification elements for user engagement.
Generated: DETERMINISTIC_1e62090e86d66ab0
Batch ID: 20250612_140246
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
 * @title Green Bitcoin Staking Contract with Gamification
 * @notice A smart contract for staking $GBTC that incorporates gamification elements
 */
contract GreenBitcoinStaking {
    // Struct to hold user staking information
    struct Stake {
        uint256 amount;       // Amount of $GBTC staked
        uint256 stakeTime;    // Timestamp when staking started
        uint256 points;       // Gamification points earned
    }

    // Mapping to track stakes of each user
    mapping(address => Stake) public stakes;

    // Parameters for gamification
    uint256 public rewardRate;        // Points earned per second per $GBTC staked
    uint256 public bonusThreshold;   // Minimum stake amount to qualify for bonuses
    uint256 public bonusPoints;      // Bonus points awarded for meeting the threshold

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 points);
    event BonusAwarded(address indexed user, uint256 points);

    /**
     * @dev Constructor to initialize gamification parameters
     * @param _rewardRate Points earned per second per $GBTC staked
     * @param _bonusThreshold Minimum stake amount for bonus eligibility
     * @param _bonusPoints Bonus points awarded for meeting the threshold
     */
    constructor(uint256 _rewardRate, uint256 _bonusThreshold, uint256 _bonusPoints) {
        rewardRate = _rewardRate;
        bonusThreshold = _bonusThreshold;
        bonusPoints = _bonusPoints;
    }

    /**
     * @dev Function to stake $GBTC tokens
     * @param _amount The amount of $GBTC to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Staking amount must be greater than zero");

        // Update existing stake or start a new stake
        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount > 0) {
            // Calculate and update points for the existing stake
            userStake.points += calculatePoints(msg.sender);
        }
        userStake.amount += _amount;
        userStake.stakeTime = block.timestamp;

        // Award bonus points if eligible
        if (userStake.amount >= bonusThreshold) {
            userStake.points += bonusPoints;
            emit BonusAwarded(msg.sender, bonusPoints);
        }

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to unstake $GBTC tokens
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked amount to unstake");

        // Calculate final points earned
        uint256 finalPoints = userStake.points + calculatePoints(msg.sender);

        // Transfer staked amount back to the user (pseudo-code for token transfer)
        // token.transfer(msg.sender, userStake.amount);

        // Reset user stake
        userStake.amount = 0;
        userStake.stakeTime = 0;
        userStake.points = 0;

        emit Unstaked(msg.sender, userStake.amount, finalPoints);
    }

    /**
     * @dev Helper function to calculate points earned by a user
     * @param _user Address of the user
     * @return The points earned
     */
    function calculatePoints(address _user) internal view returns (uint256) {
        Stake storage userStake = stakes[_user];
        if (userStake.amount == 0 || userStake.stakeTime == 0) {
            return 0;
        }

        // Calculate points based on staked amount and time
        uint256 stakingDuration = block.timestamp - userStake.stakeTime;
        return stakingDuration * userStake.amount * rewardRate;
    }

    /**
     * @dev Function to view the total points earned by a user
     * @param _user Address of the user
     * @return Total points earned
     */
    function getTotalPoints(address _user) external view returns (uint256) {
        Stake storage userStake = stakes[_user];
        uint256 calculatedPoints = calculatePoints(_user);
        return userStake.points + calculatedPoints;
    }
}
```
