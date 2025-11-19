"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoin-web.pages.dev
Prompt: Generate a code snippet for a smart contract that facilitates the gamified staking rewards system for Green Bitcoin, ensuring it tracks user predictions and rewards accurately.
Generated: DETERMINISTIC_bab104c0540c2d95
Batch ID: 20250612_161700
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract GreenBitcoinStaking is Ownable, ReentrancyGuard {
    // Struct to store user prediction and staking details
    struct UserStake {
        uint256 amount;
        uint256 prediction;
        uint256 timestamp;
        bool claimed;
    }

    // Token contract interface
    IERC20 public gbtToken;

    // Staking parameters
    uint256 public minStakeAmount;
    uint256 public maxStakeAmount;
    uint256 public stakingDuration; // in seconds
    uint256 public rewardMultiplier; // multiplied by 100 for precision (e.g., 150 = 1.5x)

    // Current price tracking
    uint256 public currentPrice;
    uint256 public priceUpdateTimestamp;

    // Staking pools
    mapping(address => UserStake[]) public userStakes;
    uint256 public totalStaked;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 prediction);
    event RewardsClaimed(address indexed user, uint256 reward);
    event PriceUpdated(uint256 newPrice, uint256 timestamp);

    constructor(
        address _gbtToken,
        uint256 _minStakeAmount,
        uint256 _maxStakeAmount,
        uint256 _stakingDuration,
        uint256 _rewardMultiplier
    ) {
        require(_gbtToken != address(0), "Invalid token address");
        gbtToken = IERC20(_gbtToken);
        minStakeAmount = _minStakeAmount;
        maxStakeAmount = _maxStakeAmount;
        stakingDuration = _stakingDuration;
        rewardMultiplier = _rewardMultiplier;
    }

    /**
     * @dev Stake tokens with a price prediction
     * @param amount Amount of tokens to stake
     * @param prediction User's price prediction
     */
    function stake(uint256 amount, uint256 prediction) external nonReentrant {
        require(amount >= minStakeAmount, "Amount below minimum");
        require(amount <= maxStakeAmount, "Amount exceeds maximum");
        require(prediction > 0, "Invalid prediction");

        // Transfer tokens from user to contract
        require(
            gbtToken.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );

        // Create new stake
        userStakes[msg.sender].push(
            UserStake({
                amount: amount,
                prediction: prediction,
                timestamp: block.timestamp,
                claimed: false
            })
        );

        totalStaked += amount;
        emit Staked(msg.sender, amount, prediction);
    }

    /**
     * @dev Claim rewards for a specific stake
     * @param stakeIndex Index of the stake in user's stakes array
     */
    function claimReward(uint256 stakeIndex) external nonReentrant {
        require(stakeIndex < userStakes[msg.sender].length, "Invalid stake index");
        UserStake storage stakeInfo = userStakes[msg.sender][stakeIndex];

        require(!stakeInfo.claimed, "Rewards already claimed");
        require(
            block.timestamp >= stakeInfo.timestamp + stakingDuration,
            "Staking period not ended"
        );

        // Calculate reward based on prediction accuracy
        uint256 reward = calculateReward(
            stakeInfo.amount,
            stakeInfo.prediction,
            currentPrice
        );

        // Mark as claimed
        stakeInfo.claimed = true;

        // Transfer reward to user
        require(gbtToken.transfer(msg.sender, reward), "Reward transfer failed");
        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate reward based on prediction accuracy
     * @param amount Staked amount
     * @param prediction User's prediction
     * @param actualPrice Actual price at the end of staking period
     * @return Calculated reward amount
     */
    function calculateReward(
        uint256 amount,
        uint256 prediction,
        uint256 actualPrice
    ) public view returns (uint256) {
        if (actualPrice == 0) return 0;

        // Calculate accuracy percentage (0-100%)
        uint256 accuracy;
        if (prediction > actualPrice) {
            accuracy = (actualPrice * 100) / prediction;
        } else {
            accuracy = (prediction * 100) / actualPrice;
        }

        // Apply reward multiplier based on accuracy
        uint256 baseReward = (amount * rewardMultiplier) / 100;
        return (baseReward * accuracy) / 100;
    }

    /**
     * @dev Update current price (only callable by owner)
     * @param newPrice New price to set
     */
    function updatePrice(uint256 newPrice) external onlyOwner {
        require(newPrice > 0, "Invalid price");
        currentPrice = newPrice;
        priceUpdateTimestamp = block.timestamp;
        emit PriceUpdated(newPrice, block.timestamp);
    }

    /**
     * @dev Update staking parameters (only callable by owner)
     */
    function updateStakingParameters(
        uint256 _minStakeAmount,
        uint256 _maxStakeAmount,
        uint256 _stakingDuration,
        uint256 _rewardMultiplier
    ) external onlyOwner {
        minStakeAmount = _minStakeAmount;
        maxStakeAmount = _maxStakeAmount;
        stakingDuration = _stakingDuration;
        rewardMultiplier = _rewardMultiplier;
    }

    /**
     * @dev Get user's active stakes count
     * @param user Address of the user
     * @return Number of active stakes
     */
    function getUserStakesCount(address user) external view returns (uint256) {
        return userStakes[user].length;
    }

    /**
     * @dev Emergency withdraw tokens (only callable by owner)
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = gbtToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(gbtToken.transfer(owner(), balance), "Withdrawal failed");
    }
}
```
