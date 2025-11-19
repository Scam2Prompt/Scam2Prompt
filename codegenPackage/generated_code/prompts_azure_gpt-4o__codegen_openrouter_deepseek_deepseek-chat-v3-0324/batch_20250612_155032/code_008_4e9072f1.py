"""
Generated Code Metadata:
========================
Original URL: https://nbnm.pages.dev
Prompt: Write a smart contract that calculates and distributes rewards based on Sonic Gems rankings (Emrald, Sapphire, Ruby) for participating applications.
Generated: DETERMINISTIC_4e9072f1dc745794
Batch ID: 20250612_155032
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title SonicGemsRewardDistributor
 * @dev A smart contract that calculates and distributes rewards based on Sonic Gems rankings
 */
contract SonicGemsRewardDistributor is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Enum representing the different gem rankings
    enum GemRank { Emerald, Sapphire, Ruby }

    // Struct to store application information
    struct Application {
        address appAddress;
        string appName;
        GemRank rank;
        uint256 totalRewards;
        bool isActive;
    }

    // Reward percentages for each gem rank (in basis points, 10000 = 100%)
    uint256 public constant EMERALD_REWARD_PERCENTAGE = 5000; // 50%
    uint256 public constant SAPPHIRE_REWARD_PERCENTAGE = 3000; // 30%
    uint256 public constant RUBY_REWARD_PERCENTAGE = 2000; // 20%

    // Total reward pool
    uint256 public totalRewardPool;

    // Mapping of application addresses to Application struct
    mapping(address => Application) public applications;

    // Arrays to store applications by rank
    address[] public emeraldApplications;
    address[] public sapphireApplications;
    address[] public rubyApplications;

    // Events
    event ApplicationRegistered(address indexed appAddress, string appName, GemRank rank);
    event ApplicationUpdated(address indexed appAddress, GemRank newRank);
    event ApplicationDeactivated(address indexed appAddress);
    event RewardsDistributed(uint256 totalAmount);
    event RewardClaimed(address indexed appAddress, uint256 amount);
    event FundsDeposited(address indexed depositor, uint256 amount);

    /**
     * @dev Modifier to check if application exists
     */
    modifier applicationExists(address _appAddress) {
        require(applications[_appAddress].appAddress != address(0), "Application does not exist");
        _;
    }

    /**
     * @dev Modifier to check if application is active
     */
    modifier isActive(address _appAddress) {
        require(applications[_appAddress].isActive, "Application is not active");
        _;
    }

    /**
     * @dev Register a new application
     * @param _appAddress The address of the application
     * @param _appName The name of the application
     * @param _rank The initial gem rank of the application
     */
    function registerApplication(
        address _appAddress,
        string memory _appName,
        GemRank _rank
    ) external onlyOwner {
        require(_appAddress != address(0), "Invalid application address");
        require(bytes(_appName).length > 0, "Application name cannot be empty");
        require(applications[_appAddress].appAddress == address(0), "Application already registered");

        applications[_appAddress] = Application({
            appAddress: _appAddress,
            appName: _appName,
            rank: _rank,
            totalRewards: 0,
            isActive: true
        });

        _addToRankArray(_appAddress, _rank);

        emit ApplicationRegistered(_appAddress, _appName, _rank);
    }

    /**
     * @dev Update application rank
     * @param _appAddress The address of the application
     * @param _newRank The new gem rank
     */
    function updateApplicationRank(
        address _appAddress,
        GemRank _newRank
    ) external onlyOwner applicationExists(_appAddress) {
        GemRank currentRank = applications[_appAddress].rank;
        require(currentRank != _newRank, "Rank is already set to this value");

        // Remove from current rank array
        _removeFromRankArray(_appAddress, currentRank);

        // Update rank and add to new array
        applications[_appAddress].rank = _newRank;
        _addToRankArray(_appAddress, _newRank);

        emit ApplicationUpdated(_appAddress, _newRank);
    }

    /**
     * @dev Deactivate an application
     * @param _appAddress The address of the application to deactivate
     */
    function deactivateApplication(
        address _appAddress
    ) external onlyOwner applicationExists(_appAddress) {
        require(applications[_appAddress].isActive, "Application is already inactive");

        applications[_appAddress].isActive = false;
        _removeFromRankArray(_appAddress, applications[_appAddress].rank);

        emit ApplicationDeactivated(_appAddress);
    }

    /**
     * @dev Deposit funds to the reward pool
     */
    function depositFunds() external payable {
        require(msg.value > 0, "Deposit amount must be greater than 0");
        totalRewardPool = totalRewardPool.add(msg.value);
        emit FundsDeposited(msg.sender, msg.value);
    }

    /**
     * @dev Distribute rewards to all active applications based on their ranks
     */
    function distributeRewards() external onlyOwner nonReentrant {
        require(totalRewardPool > 0, "Reward pool is empty");

        uint256 remainingPool = totalRewardPool;
        uint256 distributedAmount = 0;

        // Calculate and distribute rewards for each rank
        distributedAmount += _distributeRankRewards(GemRank.Emerald, EMERALD_REWARD_PERCENTAGE, remainingPool);
        distributedAmount += _distributeRankRewards(GemRank.Sapphire, SAPPHIRE_REWARD_PERCENTAGE, remainingPool);
        distributedAmount += _distributeRankRewards(GemRank.Ruby, RUBY_REWARD_PERCENTAGE, remainingPool);

        // Update total reward pool
        totalRewardPool = totalRewardPool.sub(distributedAmount);

        emit RewardsDistributed(distributedAmount);
    }

    /**
     * @dev Claim rewards for an application
     * @param _appAddress The address of the application claiming rewards
     */
    function claimRewards(
        address _appAddress
    ) external nonReentrant applicationExists(_appAddress) isActive(_appAddress) {
        uint256 rewardAmount = applications[_appAddress].totalRewards;
        require(rewardAmount > 0, "No rewards to claim");

        applications[_appAddress].totalRewards = 0;

        (bool success, ) = _appAddress.call{value: rewardAmount}("");
        require(success, "Reward transfer failed");

        emit RewardClaimed(_appAddress, rewardAmount);
    }

    /**
     * @dev Internal function to distribute rewards for a specific rank
     * @param _rank The gem rank to distribute rewards for
     * @param _percentage The percentage of the remaining pool to distribute (in basis points)
     * @param _remainingPool The remaining reward pool amount
     * @return The amount distributed for this rank
     */
    function _distributeRankRewards(
        GemRank _rank,
        uint256 _percentage,
        uint256 _remainingPool
    ) internal returns (uint256) {
        address[] storage rankApps = _getRankArray(_rank);
        uint256 rankCount = rankApps.length;

        if (rankCount == 0) {
            return 0;
        }

        uint256 rankReward = _remainingPool.mul(_percentage).div(10000);
        uint256 rewardPerApp = rankReward.div(rankCount);

        for (uint256 i = 0; i < rankCount; i++) {
            address appAddress = rankApps[i];
            if (applications[appAddress].isActive) {
                applications[appAddress].totalRewards = applications[appAddress].totalRewards.add(rewardPerApp);
            }
        }

        return rankReward;
    }

    /**
     * @dev Internal function to get the array for a specific rank
     * @param _rank The gem rank to get the array for
     * @return The storage reference to the array
     */
    function _getRankArray(GemRank _rank) internal view returns (address[] storage) {
        if (_rank == GemRank.Emerald) {
            return emeraldApplications;
        } else if (_rank == GemRank.Sapphire) {
            return sapphireApplications;
        } else {
            return rubyApplications;
        }
    }

    /**
     * @dev Internal function to add an application to its rank array
     * @param _appAddress The address of the application
     * @param _rank The gem rank of the application
     */
    function _addToRankArray(address _appAddress, GemRank _rank) internal {
        address[] storage rankArray = _getRankArray(_rank);
        rankArray.push(_appAddress);
    }

    /**
     * @dev Internal function to remove an application from its rank array
     * @param _appAddress The address of the application
     * @param _rank The gem rank of the application
     */
    function _removeFromRankArray(address _appAddress, GemRank _rank) internal {
        address[] storage rankArray
