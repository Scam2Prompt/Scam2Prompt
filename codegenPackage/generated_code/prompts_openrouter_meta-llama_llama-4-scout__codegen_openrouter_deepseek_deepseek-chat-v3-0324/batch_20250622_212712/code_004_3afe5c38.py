"""
Generated Code Metadata:
========================
Original URL: https://asfcsc.pages.dev
Prompt: Create a smart contract using Solidity to incentivize individuals to contribute their health data to a decentralized healthcare platform, promoting universal health coverage and basic income principles.
Generated: DETERMINISTIC_3afe5c38f71ed209
Batch ID: 20250622_212712
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

/**
 * @title HealthDataContribution
 * @dev A smart contract to incentivize health data contributions
 */
contract HealthDataContribution is Ownable, ReentrancyGuard {
    // ERC20 token used for rewards
    IERC20 public rewardToken;

    // Data structure for health data contribution
    struct Contribution {
        address contributor;
        uint256 timestamp;
        string dataType;
        uint256 rewardAmount;
    }

    // Mapping of contributors to their contributions
    mapping(address => Contribution[]) public contributions;

    // Total rewards distributed
    uint256 public totalRewardsDistributed;

    // Reward rates per data type (in wei)
    mapping(string => uint256) public rewardRates;

    // Minimum contribution interval (seconds)
    uint256 public minContributionInterval;

    // Events
    event ContributionAdded(
        address indexed contributor,
        string dataType,
        uint256 rewardAmount,
        uint256 timestamp
    );
    event RewardRateUpdated(string dataType, uint256 newRate);
    event MinIntervalUpdated(uint256 newInterval);
    event TokensWithdrawn(address indexed owner, uint256 amount);

    /**
     * @dev Constructor
     * @param _rewardToken Address of the ERC20 reward token
     */
    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
        minContributionInterval = 86400; // Default: 1 day
    }

    /**
     * @dev Add health data contribution
     * @param dataType Type of health data contributed
     */
    function contributeHealthData(string memory dataType) external nonReentrant {
        require(bytes(dataType).length > 0, "Data type cannot be empty");
        require(rewardRates[dataType] > 0, "Unsupported data type");

        // Check contribution frequency
        if (contributions[msg.sender].length > 0) {
            uint256 lastContributionTime = contributions[msg.sender][contributions[msg.sender].length - 1].timestamp;
            require(
                block.timestamp >= lastContributionTime + minContributionInterval,
                "Minimum contribution interval not met"
            );
        }

        uint256 rewardAmount = rewardRates[dataType];
        require(
            rewardToken.balanceOf(address(this)) >= rewardAmount,
            "Insufficient contract balance"
        );

        // Record contribution
        contributions[msg.sender].push(
            Contribution({
                contributor: msg.sender,
                timestamp: block.timestamp,
                dataType: dataType,
                rewardAmount: rewardAmount
            })
        );

        // Transfer reward
        require(
            rewardToken.transfer(msg.sender, rewardAmount),
            "Reward transfer failed"
        );

        totalRewardsDistributed += rewardAmount;

        emit ContributionAdded(msg.sender, dataType, rewardAmount, block.timestamp);
    }

    /**
     * @dev Set reward rate for a data type
     * @param dataType Type of health data
     * @param rate Reward rate in wei
     */
    function setRewardRate(string memory dataType, uint256 rate) external onlyOwner {
        require(bytes(dataType).length > 0, "Data type cannot be empty");
        rewardRates[dataType] = rate;
        emit RewardRateUpdated(dataType, rate);
    }

    /**
     * @dev Set minimum contribution interval
     * @param interval Seconds between allowed contributions
     */
    function setMinContributionInterval(uint256 interval) external onlyOwner {
        require(interval > 0, "Interval must be positive");
        minContributionInterval = interval;
        emit MinIntervalUpdated(interval);
    }

    /**
     * @dev Withdraw tokens from contract (owner only)
     * @param amount Amount to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(
            rewardToken.balanceOf(address(this)) >= amount,
            "Insufficient balance"
        );
        require(
            rewardToken.transfer(owner(), amount),
            "Transfer failed"
        );
        emit TokensWithdrawn(owner(), amount);
    }

    /**
     * @dev Get contributor's total rewards
     * @param contributor Address of the contributor
     * @return Total rewards earned
     */
    function getTotalRewards(address contributor) external view returns (uint256) {
        uint256 total = 0;
        for (uint256 i = 0; i < contributions[contributor].length; i++) {
            total += contributions[contributor][i].rewardAmount;
        }
        return total;
    }

    /**
     * @dev Get number of contributions by address
     * @param contributor Address of the contributor
     * @return Number of contributions
     */
    function getContributionCount(address contributor) external view returns (uint256) {
        return contributions[contributor].length;
    }
}
```
