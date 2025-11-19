"""
Generated Code Metadata:
========================
Original URL: https://aria.fyi
Prompt: Develop a staking system for the Aria token, incorporating the information from the Arianee Protocol's FAQ and tokenomics.
Generated: DETERMINISTIC_bee5b929df2ce0ce
Batch ID: 20250622_212323
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
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title AriaToken Staking Contract
 * @dev Allows users to stake Aria tokens and earn rewards based on staking duration
 */
contract AriaStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to store user staking details
    struct Stake {
        uint256 amount;
        uint256 stakedAt;
        uint256 unlockTime;
        uint256 rewardRate;
        bool active;
    }

    // Aria token contract
    IERC20 public immutable ariaToken;

    // Staking parameters
    uint256 public constant MIN_STAKE_DURATION = 30 days;
    uint256 public constant MAX_STAKE_DURATION = 365 days;
    uint256 public constant MIN_STAKE_AMOUNT = 1000 * 10**18; // 1000 ARIA
    uint256 public totalStaked;

    // Reward rates (percentage per year)
    uint256 public shortTermRate = 5;   // 30-90 days
    uint256 public mediumTermRate = 10; // 91-180 days
    uint256 public longTermRate = 15;   // 181-365 days

    // Mapping of user addresses to their stakes
    mapping(address => Stake[]) public userStakes;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 duration, uint256 rewardRate);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event RewardClaimed(address indexed user, uint256 amount);
    event RatesUpdated(uint256 shortTerm, uint256 mediumTerm, uint256 longTerm);

    /**
     * @dev Constructor
     * @param _ariaToken Address of the Aria token contract
     */
    constructor(address _ariaToken) {
        require(_ariaToken != address(0), "Invalid token address");
        ariaToken = IERC20(_ariaToken);
    }

    /**
     * @dev Stake Aria tokens
     * @param amount Amount of tokens to stake
     * @param duration Duration of stake in seconds
     */
    function stake(uint256 amount, uint256 duration) external nonReentrant {
        require(amount >= MIN_STAKE_AMOUNT, "Amount below minimum");
        require(duration >= MIN_STAKE_DURATION, "Duration too short");
        require(duration <= MAX_STAKE_DURATION, "Duration too long");

        uint256 rewardRate = getRewardRate(duration);
        uint256 unlockTime = block.timestamp + duration;

        userStakes[msg.sender].push(Stake({
            amount: amount,
            stakedAt: block.timestamp,
            unlockTime: unlockTime,
            rewardRate: rewardRate,
            active: true
        }));

        totalStaked += amount;
        ariaToken.safeTransferFrom(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount, duration, rewardRate);
    }

    /**
     * @dev Unstake tokens and claim rewards
     * @param stakeIndex Index of the stake to unstake
     */
    function unstake(uint256 stakeIndex) external nonReentrant {
        require(stakeIndex < userStakes[msg.sender].length, "Invalid stake index");
        Stake storage userStake = userStakes[msg.sender][stakeIndex];
        require(userStake.active, "Stake already unstaked");
        require(block.timestamp >= userStake.unlockTime, "Stake not yet unlocked");

        uint256 stakedAmount = userStake.amount;
        uint256 reward = calculateReward(msg.sender, stakeIndex);

        userStake.active = false;
        totalStaked -= stakedAmount;

        ariaToken.safeTransfer(msg.sender, stakedAmount + reward);

        emit Unstaked(msg.sender, stakedAmount, reward);
    }

    /**
     * @dev Claim rewards for an active stake
     * @param stakeIndex Index of the stake to claim rewards from
     */
    function claimReward(uint256 stakeIndex) external nonReentrant {
        require(stakeIndex < userStakes[msg.sender].length, "Invalid stake index");
        Stake storage userStake = userStakes[msg.sender][stakeIndex];
        require(userStake.active, "Stake not active");

        uint256 reward = calculateReward(msg.sender, stakeIndex);
        require(reward > 0, "No rewards available");

        userStake.stakedAt = block.timestamp; // Reset staking time for next reward period
        ariaToken.safeTransfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate reward for a stake
     * @param user Address of the staker
     * @param stakeIndex Index of the stake
     * @return reward Calculated reward amount
     */
    function calculateReward(address user, uint256 stakeIndex) public view returns (uint256 reward) {
        require(stakeIndex < userStakes[user].length, "Invalid stake index");
        Stake memory userStake = userStakes[user][stakeIndex];
        if (!userStake.active) return 0;

        uint256 stakingDuration = block.timestamp - userStake.stakedAt;
        uint256 annualReward = (userStake.amount * userStake.rewardRate) / 100;
        reward = (annualReward * stakingDuration) / 365 days;
    }

    /**
     * @dev Get reward rate based on duration
     * @param duration Duration in seconds
     * @return rewardRate Appropriate reward rate
     */
    function getRewardRate(uint256 duration) public view returns (uint256 rewardRate) {
        if (duration <= 90 days) {
            return shortTermRate;
        } else if (duration <= 180 days) {
            return mediumTermRate;
        } else {
            return longTermRate;
        }
    }

    /**
     * @dev Update reward rates (owner only)
     * @param _shortTerm New short term rate
     * @param _mediumTerm New medium term rate
     * @param _longTerm New long term rate
     */
    function updateRates(uint256 _shortTerm, uint256 _mediumTerm, uint256 _longTerm) external onlyOwner {
        require(_shortTerm > 0 && _mediumTerm > 0 && _longTerm > 0, "Rates must be positive");
        require(_shortTerm < _mediumTerm && _mediumTerm < _longTerm, "Rates must be increasing");

        shortTermRate = _shortTerm;
        mediumTermRate = _mediumTerm;
        longTermRate = _longTerm;

        emit RatesUpdated(_shortTerm, _mediumTerm, _longTerm);
    }

    /**
     * @dev Get all stakes for a user
     * @param user Address of the user
     * @return Array of user's stakes
     */
    function getUserStakes(address user) external view returns (Stake[] memory) {
        return userStakes[user];
    }

    /**
     * @dev Get total staked amount for a user
     * @param user Address of the user
     * @return total Total staked amount
     */
    function getUserTotalStaked(address user) external view returns (uint256 total) {
        Stake[] memory stakes = userStakes[user];
        for (uint256 i = 0; i < stakes.length; i++) {
            if (stakes[i].active) {
                total += stakes[i].amount;
            }
        }
    }

    /**
     * @dev Emergency withdraw stuck tokens (owner only)
     * @param token Address of the token to withdraw
     */
    function emergencyWithdraw(address token) external onlyOwner {
        require(token != address(ariaToken), "Cannot withdraw staking token");
        IERC20(token).safeTransfer(owner(), IERC20(token).balanceOf(address(this)));
    }
}
```
