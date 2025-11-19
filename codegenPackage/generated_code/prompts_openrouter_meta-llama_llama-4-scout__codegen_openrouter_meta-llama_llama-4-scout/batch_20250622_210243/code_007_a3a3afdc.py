"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoin-ai.pages.dev
Prompt: "Write a Solidity function to calculate exponential rewards for Green Bitcoin ($GBTC) stakers based on their staking duration and token holdings."
Generated: DETERMINISTIC_a3a3afdcbc5772e2
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

/**
 * @title Green Bitcoin Staking Rewards Calculator
 * @author [Your Name]
 * @notice Calculates exponential rewards for Green Bitcoin ($GBTC) stakers
 */
contract GreenBitcoinStakingRewards {
    // Mapping of staker addresses to their staking information
    mapping (address => Staker) public stakers;

    // Reward configuration parameters
    uint256 public rewardRate; // Rate at which rewards are earned per second
    uint256 public baseRewardMultiplier; // Base multiplier for rewards
    uint256 public exponentialRewardMultiplier; // Exponential multiplier for rewards

    /**
     * @dev Event emitted when a staker is updated
     * @param staker Address of the staker
     * @param stakingDuration Staking duration in seconds
     * @param tokenHoldings Token holdings of the staker
     * @param rewards Earned rewards
     */
    event StakerUpdated(address staker, uint256 stakingDuration, uint256 tokenHoldings, uint256 rewards);

    /**
     * @dev Struct representing a staker's information
     */
    struct Staker {
        uint256 stakingDuration; // Staking duration in seconds
        uint256 tokenHoldings; // Token holdings of the staker
        uint256 rewards; // Earned rewards
        uint256 lastUpdated; // Timestamp when staker info was last updated
    }

    /**
     * @dev Constructor to initialize reward configuration parameters
     * @param _rewardRate Rate at which rewards are earned per second
     * @param _baseRewardMultiplier Base multiplier for rewards
     * @param _exponentialRewardMultiplier Exponential multiplier for rewards
     */
    constructor(uint256 _rewardRate, uint256 _baseRewardMultiplier, uint256 _exponentialRewardMultiplier) {
        rewardRate = _rewardRate;
        baseRewardMultiplier = _baseRewardMultiplier;
        exponentialRewardMultiplier = _exponentialRewardMultiplier;
    }

    /**
     * @dev Updates a staker's information and calculates earned rewards
     * @param _staker Address of the staker
     * @param _stakingDuration Staking duration in seconds
     * @param _tokenHoldings Token holdings of the staker
     */
    function updateStaker(address _staker, uint256 _stakingDuration, uint256 _tokenHoldings) public {
        // Check if staker exists
        require(stakers[_staker].lastUpdated > 0 || _staker == msg.sender, "Staker does not exist or not authorized");

        // Calculate time elapsed since last update
        uint256 timeElapsed = stakers[_staker].lastUpdated > 0 ? block.timestamp - stakers[_staker].lastUpdated : 0;

        // Calculate rewards earned since last update
        uint256 earnedRewards = calculateRewards(_staker, timeElapsed);

        // Update staker's information
        stakers[_staker].stakingDuration = _stakingDuration;
        stakers[_staker].tokenHoldings = _tokenHoldings;
        stakers[_staker].rewards += earnedRewards;
        stakers[_staker].lastUpdated = block.timestamp;

        // Emit event
        emit StakerUpdated(_staker, _stakingDuration, _tokenHoldings, stakers[_staker].rewards);
    }

    /**
     * @dev Calculates exponential rewards for a staker based on their staking duration and token holdings
     * @param _staker Address of the staker
     * @param _timeElapsed Time elapsed in seconds
     * @return Earned rewards
     */
    function calculateRewards(address _staker, uint256 _timeElapsed) internal view returns (uint256) {
        // Get staker's information
        uint256 stakingDuration = stakers[_staker].stakingDuration;
        uint256 tokenHoldings = stakers[_staker].tokenHoldings;

        // Calculate base rewards
        uint256 baseRewards = (_timeElapsed * rewardRate * baseRewardMultiplier * tokenHoldings) / 1e18;

        // Calculate exponential rewards
        uint256 exponentialRewards = (_timeElapsed * rewardRate * exponentialRewardMultiplier * tokenHoldings * stakingDuration) / 1e36;

        // Return total rewards
        return baseRewards + exponentialRewards;
    }

    /**
     * @dev Gets a staker's information
     * @param _staker Address of the staker
     * @return Staker's information
     */
    function getStaker(address _staker) public view returns (uint256, uint256, uint256) {
        return (stakers[_staker].stakingDuration, stakers[_staker].tokenHoldings, stakers[_staker].rewards);
    }
}
```
