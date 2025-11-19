"""
Generated Code Metadata:
========================
Original URL: https://sayloud.io
Prompt: Design a smart contract in Solidity to automate the distribution of rewards to top contributors on Loud.
Generated: DETERMINISTIC_3822f418d9cae0aa
Batch ID: 20250622_212813
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract LoudRewardDistributor is Ownable, ReentrancyGuard {
    // Struct to store contributor information
    struct Contributor {
        address wallet;
        uint256 points;
        bool exists;
    }

    // Reward token interface
    IERC20 public rewardToken;

    // Mapping of contributors
    mapping(address => Contributor) public contributors;
    address[] public contributorAddresses;

    // Reward distribution parameters
    uint256 public totalRewardPool;
    uint256 public distributionInterval;
    uint256 public lastDistributionTime;
    uint256 public topContributorsCount;

    // Events
    event ContributorAdded(address indexed wallet, uint256 points);
    event ContributorUpdated(address indexed wallet, uint256 newPoints);
    event RewardsDistributed(address[] recipients, uint256[] amounts);
    event RewardPoolFunded(uint256 amount);
    event DistributionIntervalUpdated(uint256 newInterval);
    event TopContributorsCountUpdated(uint256 newCount);

    constructor(
        address _rewardToken,
        uint256 _distributionInterval,
        uint256 _topContributorsCount
    ) {
        require(_rewardToken != address(0), "Invalid token address");
        require(_distributionInterval > 0, "Interval must be > 0");
        require(_topContributorsCount > 0, "Count must be > 0");

        rewardToken = IERC20(_rewardToken);
        distributionInterval = _distributionInterval;
        topContributorsCount = _topContributorsCount;
        lastDistributionTime = block.timestamp;
    }

    // Add or update contributor points
    function updateContributor(address _wallet, uint256 _points) external onlyOwner {
        require(_wallet != address(0), "Invalid wallet address");

        if (!contributors[_wallet].exists) {
            contributors[_wallet] = Contributor(_wallet, _points, true);
            contributorAddresses.push(_wallet);
            emit ContributorAdded(_wallet, _points);
        } else {
            contributors[_wallet].points = _points;
            emit ContributorUpdated(_wallet, _points);
        }
    }

    // Fund the reward pool
    function fundRewardPool(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be > 0");
        require(
            rewardToken.transferFrom(msg.sender, address(this), _amount),
            "Transfer failed"
        );
        totalRewardPool += _amount;
        emit RewardPoolFunded(_amount);
    }

    // Distribute rewards to top contributors
    function distributeRewards() external nonReentrant {
        require(
            block.timestamp >= lastDistributionTime + distributionInterval,
            "Distribution interval not reached"
        );
        require(totalRewardPool > 0, "Reward pool is empty");
        require(contributorAddresses.length >= topContributorsCount, "Not enough contributors");

        // Sort contributors by points (descending)
        _sortContributors();

        // Calculate total points for top contributors
        uint256 totalPoints;
        for (uint256 i = 0; i < topContributorsCount; i++) {
            totalPoints += contributors[contributorAddresses[i]].points;
        }

        require(totalPoints > 0, "No points to distribute");

        // Prepare distribution data
        address[] memory recipients = new address[](topContributorsCount);
        uint256[] memory amounts = new uint256[](topContributorsCount);
        uint256 distributedAmount;

        // Calculate and transfer rewards
        for (uint256 i = 0; i < topContributorsCount; i++) {
            address contributor = contributorAddresses[i];
            uint256 share = (contributors[contributor].points * totalRewardPool) / totalPoints;
            
            recipients[i] = contributor;
            amounts[i] = share;
            distributedAmount += share;

            require(
                rewardToken.transfer(contributor, share),
                "Reward transfer failed"
            );
        }

        // Update state
        totalRewardPool -= distributedAmount;
        lastDistributionTime = block.timestamp;

        emit RewardsDistributed(recipients, amounts);
    }

    // Set distribution interval
    function setDistributionInterval(uint256 _interval) external onlyOwner {
        require(_interval > 0, "Interval must be > 0");
        distributionInterval = _interval;
        emit DistributionIntervalUpdated(_interval);
    }

    // Set number of top contributors to reward
    function setTopContributorsCount(uint256 _count) external onlyOwner {
        require(_count > 0, "Count must be > 0");
        topContributorsCount = _count;
        emit TopContributorsCountUpdated(_count);
    }

    // Internal function to sort contributors by points (descending)
    function _sortContributors() private {
        uint256 n = contributorAddresses.length;
        for (uint256 i = 0; i < n; i++) {
            for (uint256 j = i + 1; j < n; j++) {
                if (contributors[contributorAddresses[i]].points < contributors[contributorAddresses[j]].points) {
                    address temp = contributorAddresses[i];
                    contributorAddresses[i] = contributorAddresses[j];
                    contributorAddresses[j] = temp;
                }
            }
        }
    }

    // Emergency withdraw remaining tokens
    function emergencyWithdraw(address _token) external onlyOwner {
        require(_token != address(0), "Invalid token address");
        IERC20 token = IERC20(_token);
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No balance to withdraw");
        require(token.transfer(owner(), balance), "Transfer failed");
    }
}
```
