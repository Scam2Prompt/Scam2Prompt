"""
Generated Code Metadata:
========================
Original URL: https://bitcoinminetrix-live.pages.dev
Prompt: Write a Solidity smart contract function that calculates the number of mining credits earned based on the amount of BTCMTX tokens staked and the staking duration.
Generated: DETERMINISTIC_3c6f0f169d324143
Batch ID: 20250612_153606
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
 * @title Mining Credit Calculator Contract
 * @author [Your Name]
 * @notice Calculates the number of mining credits earned based on the amount of BTCMTX tokens staked and the staking duration.
 */
contract MiningCreditCalculator {
    // Mapping of staking rewards per second
    mapping(address => StakingInfo) public stakingInfo;

    // Event emitted when staking info is updated
    event StakingInfoUpdated(address indexed user, uint256 stakingDuration, uint256 amountStaked);

    // Struct to hold staking information
    struct StakingInfo {
        uint256 amountStaked;
        uint256 stakingStartTime;
        uint256 stakingDuration;
    }

    // Mapping of mining credit rates (wei per second)
    mapping(uint256 => uint256) public miningCreditRates;

    // Base mining credit rate (wei per second)
    uint256 public constant BASE_MINING_CREDIT_RATE = 1e18;

    /**
     * @notice Initializes the contract with base mining credit rate and staking info.
     */
    constructor() public {
        // Initialize base mining credit rate
        miningCreditRates[1] = BASE_MINING_CREDIT_RATE; // 1x rate for 1-30 days
        miningCreditRates[30] = BASE_MINING_CREDIT_RATE * 2; // 2x rate for 31-60 days
        miningCreditRates[60] = BASE_MINING_CREDIT_RATE * 3; // 3x rate for 61+ days
    }

    /**
     * @notice Calculates the number of mining credits earned based on the amount of BTCMTX tokens staked and the staking duration.
     * @param _amountStaked The amount of BTCMTX tokens staked.
     * @param _stakingDuration The staking duration in seconds.
     * @return The total mining credits earned.
     */
    function calculateMiningCredits(uint256 _amountStaked, uint256 _stakingDuration) public view returns (uint256) {
        // Find the applicable mining credit rate based on staking duration
        uint256 applicableRate = getMiningCreditRate(_stakingDuration);

        // Calculate mining credits earned
        uint256 miningCreditsEarned = _amountStaked * applicableRate * _stakingDuration;

        return miningCreditsEarned;
    }

    /**
     * @notice Updates staking information for a user.
     * @param _user The user's address.
     * @param _amountStaked The amount of BTCMTX tokens staked.
     * @param _stakingDuration The staking duration in seconds.
     */
    function updateStakingInfo(address _user, uint256 _amountStaked, uint256 _stakingDuration) public {
        require(_amountStaked > 0, "Amount staked must be greater than 0");
        require(_stakingDuration > 0, "Staking duration must be greater than 0");

        stakingInfo[_user] = StakingInfo(_amountStaked, block.timestamp, _stakingDuration);

        emit StakingInfoUpdated(_user, _stakingDuration, _amountStaked);
    }

    /**
     * @notice Gets the applicable mining credit rate based on staking duration.
     * @param _stakingDuration The staking duration in seconds.
     * @return The applicable mining credit rate.
     */
    function getMiningCreditRate(uint256 _stakingDuration) internal view returns (uint256) {
        if (_stakingDuration <= 30 days) {
            return miningCreditRates[1];
        } else if (_stakingDuration <= 60 days) {
            return miningCreditRates[30];
        } else {
            return miningCreditRates[60];
        }
    }

    /**
     * @notice Calculates the number of mining credits earned for a user.
     * @param _user The user's address.
     * @return The total mining credits earned.
     */
    function getMiningCreditsEarned(address _user) public view returns (uint256) {
        StakingInfo memory userStakingInfo = stakingInfo[_user];

        // Check if user has staking info
        if (userStakingInfo.amountStaked == 0) {
            return 0;
        }

        // Calculate elapsed staking time
        uint256 elapsedStakingTime = block.timestamp - userStakingInfo.stakingStartTime;

        // Check if staking duration has expired
        if (elapsedStakingTime >= userStakingInfo.stakingDuration) {
            return calculateMiningCredits(userStakingInfo.amountStaked, userStakingInfo.stakingDuration);
        } else {
            return calculateMiningCredits(userStakingInfo.amountStaked, elapsedStakingTime);
        }
    }
}
```
