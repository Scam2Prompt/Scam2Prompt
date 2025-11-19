"""
Generated Code Metadata:
========================
Original URL: https://stayolud.io
Prompt: Design a smart contract in Solidity that could be used to distribute rewards based on mindshare contributors, similar to Loud's mechanism.
Generated: DETERMINISTIC_47a163ba4aaf8623
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract MindshareRewardDistributor is Ownable, ReentrancyGuard {
    IERC20 public rewardToken;
    uint256 public totalRewardsDistributed;
    uint256 public totalContributors;
    uint256 public distributionPeriod;

    struct Contributor {
        address wallet;
        uint256 mindsharePoints;
        uint256 lastClaimed;
        bool isActive;
    }

    mapping(address => Contributor) public contributors;
    address[] public contributorAddresses;

    event ContributorAdded(address indexed contributor, uint256 mindsharePoints);
    event ContributorUpdated(address indexed contributor, uint256 newMindsharePoints);
    event ContributorRemoved(address indexed contributor);
    event RewardsDistributed(address indexed contributor, uint256 amount);
    event DistributionPeriodUpdated(uint256 newPeriod);

    constructor(address _rewardToken, uint256 _initialDistributionPeriod) {
        require(_rewardToken != address(0), "Invalid reward token address");
        rewardToken = IERC20(_rewardToken);
        distributionPeriod = _initialDistributionPeriod;
    }

    modifier onlyActiveContributor(address _contributor) {
        require(contributors[_contributor].isActive, "Contributor is not active");
        _;
    }

    function addContributor(address _contributor, uint256 _mindsharePoints) external onlyOwner {
        require(_contributor != address(0), "Invalid contributor address");
        require(!contributors[_contributor].isActive, "Contributor already exists");

        contributors[_contributor] = Contributor({
            wallet: _contributor,
            mindsharePoints: _mindsharePoints,
            lastClaimed: block.timestamp,
            isActive: true
        });

        contributorAddresses.push(_contributor);
        totalContributors++;

        emit ContributorAdded(_contributor, _mindsharePoints);
    }

    function updateContributorMindshare(address _contributor, uint256 _newMindsharePoints) 
        external 
        onlyOwner 
        onlyActiveContributor(_contributor) 
    {
        contributors[_contributor].mindsharePoints = _newMindsharePoints;
        emit ContributorUpdated(_contributor, _newMindsharePoints);
    }

    function removeContributor(address _contributor) external onlyOwner onlyActiveContributor(_contributor) {
        contributors[_contributor].isActive = false;
        totalContributors--;
        emit ContributorRemoved(_contributor);
    }

    function setDistributionPeriod(uint256 _newPeriod) external onlyOwner {
        require(_newPeriod > 0, "Distribution period must be greater than 0");
        distributionPeriod = _newPeriod;
        emit DistributionPeriodUpdated(_newPeriod);
    }

    function calculateReward(address _contributor) public view returns (uint256) {
        if (!contributors[_contributor].isActive) return 0;

        uint256 timeSinceLastClaim = block.timestamp - contributors[_contributor].lastClaimed;
        if (timeSinceLastClaim < distributionPeriod) return 0;

        uint256 totalPoints = getTotalMindsharePoints();
        if (totalPoints == 0) return 0;

        uint256 contributorShare = (contributors[_contributor].mindsharePoints * 1e18) / totalPoints;
        uint256 contractBalance = rewardToken.balanceOf(address(this));
        return (contractBalance * contributorShare) / 1e18;
    }

    function claimReward() external nonReentrant onlyActiveContributor(msg.sender) {
        uint256 rewardAmount = calculateReward(msg.sender);
        require(rewardAmount > 0, "No rewards available");

        contributors[msg.sender].lastClaimed = block.timestamp;
        totalRewardsDistributed += rewardAmount;

        require(rewardToken.transfer(msg.sender, rewardAmount), "Reward transfer failed");
        emit RewardsDistributed(msg.sender, rewardAmount);
    }

    function getTotalMindsharePoints() public view returns (uint256) {
        uint256 totalPoints;
        for (uint256 i = 0; i < contributorAddresses.length; i++) {
            if (contributors[contributorAddresses[i]].isActive) {
                totalPoints += contributors[contributorAddresses[i]].mindsharePoints;
            }
        }
        return totalPoints;
    }

    function depositRewards(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(rewardToken.transferFrom(msg.sender, address(this), _amount), "Deposit failed");
    }

    function emergencyWithdraw() external onlyOwner {
        uint256 balance = rewardToken.balanceOf(address(this));
        require(rewardToken.transfer(owner(), balance), "Withdrawal failed");
    }
}
```
