"""
Generated Code Metadata:
========================
Original URL: https://stalyoud.io
Prompt: "Generate a smart contract code snippet in Solidity that handles the distribution of rewards in SOL to top contributors on a platform like Loud, based on their mindshare and trading volume."
Generated: DETERMINISTIC_a5d73502b7d171ee
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title RewardDistributor
 * @author [Your Name]
 * @notice A smart contract for distributing SOL rewards to top contributors based on their mindshare and trading volume.
 */
contract RewardDistributor is Ownable {
    using SafeMath for uint256;

    // Mapping of contributor addresses to their mindshare and trading volume
    mapping (address => Contributor) public contributors;

    // Mapping of contributor addresses to their reward claims
    mapping (address => bool) public claimedRewards;

    // SOL token contract
    IERC20 public solToken;

    // Total rewards available for distribution
    uint256 public totalRewards;

    // Distribution parameters
    uint256 public mindshareWeight;
    uint256 public tradingVolumeWeight;

    /**
     * @dev Contributor struct
     * @param mindshare Mindshare score
     * @param tradingVolume Trading volume
     */
    struct Contributor {
        uint256 mindshare;
        uint256 tradingVolume;
    }

    /**
     * @dev Event emitted when rewards are distributed
     * @param contributor Contributor address
     * @param reward Reward amount
     */
    event RewardsDistributed(address indexed contributor, uint256 reward);

    /**
     * @dev Event emitted when contributor data is updated
     * @param contributor Contributor address
     * @param mindshare New mindshare score
     * @param tradingVolume New trading volume
     */
    event ContributorUpdated(address indexed contributor, uint256 mindshare, uint256 tradingVolume);

    /**
     * @dev Constructor
     * @param _solToken SOL token contract address
     * @param _mindshareWeight Mindshare weight
     * @param _tradingVolumeWeight Trading volume weight
     */
    constructor(address _solToken, uint256 _mindshareWeight, uint256 _tradingVolumeWeight) public {
        solToken = IERC20(_solToken);
        mindshareWeight = _mindshareWeight;
        tradingVolumeWeight = _tradingVolumeWeight;
    }

    /**
     * @dev Updates contributor data
     * @param _contributor Contributor address
     * @param _mindshare New mindshare score
     * @param _tradingVolume New trading volume
     */
    function updateContributor(address _contributor, uint256 _mindshare, uint256 _tradingVolume) public onlyOwner {
        contributors[_contributor] = Contributor(_mindshare, _tradingVolume);
        emit ContributorUpdated(_contributor, _mindshare, _tradingVolume);
    }

    /**
     * @dev Calculates contributor scores
     * @param _contributor Contributor address
     * @return score Contributor score
     */
    function calculateScore(address _contributor) internal view returns (uint256 score) {
        Contributor memory contributor = contributors[_contributor];
        score = contributor.mindshare.mul(mindshareWeight).add(contributor.tradingVolume.mul(tradingVolumeWeight));
    }

    /**
     * @dev Distributes rewards to top contributors
     * @param _numContributors Number of top contributors to reward
     */
    function distributeRewards(uint256 _numContributors) public onlyOwner {
        // Get all contributors
        address[] memory contributorsList = getContributors();

        // Sort contributors by score
        contributorsList = sortContributorsByScore(contributorsList);

        // Distribute rewards to top contributors
        for (uint256 i = 0; i < _numContributors; i++) {
            address contributor = contributorsList[i];
            uint256 score = calculateScore(contributor);
            uint256 reward = totalRewards.mul(score).div(getTotalScore());
            solToken.transfer(contributor, reward);
            claimedRewards[contributor] = true;
            emit RewardsDistributed(contributor, reward);
        }
    }

    /**
     * @dev Gets all contributors
     * @return contributorsList List of contributor addresses
     */
    function getContributors() internal view returns (address[] memory) {
        address[] memory contributorsList = new address[](contributors.length);
        uint256 index = 0;
        for (address contributor in contributors) {
            contributorsList[index] = contributor;
            index++;
        }
        return contributorsList;
    }

    /**
     * @dev Sorts contributors by score
     * @param _contributors List of contributor addresses
     * @return sortedContributorsList Sorted list of contributor addresses
     */
    function sortContributorsByScore(address[] memory _contributors) internal view returns (address[] memory) {
        // Bubble sort
        for (uint256 i = 0; i < _contributors.length; i++) {
            for (uint256 j = i + 1; j < _contributors.length; j++) {
                address contributor1 = _contributors[i];
                address contributor2 = _contributors[j];
                uint256 score1 = calculateScore(contributor1);
                uint256 score2 = calculateScore(contributor2);
                if (score1 < score2) {
                    // Swap
                    _contributors[i] = contributor2;
                    _contributors[j] = contributor1;
                }
            }
        }
        return _contributors;
    }

    /**
     * @dev Gets total score of all contributors
     * @return totalScore Total score
     */
    function getTotalScore() internal view returns (uint256 totalScore) {
        for (address contributor in contributors) {
            totalScore = totalScore.add(calculateScore(contributor));
        }
    }

    /**
     * @dev Sets total rewards available for distribution
     * @param _totalRewards Total rewards
     */
    function setTotalRewards(uint256 _totalRewards) public onlyOwner {
        totalRewards = _totalRewards;
    }

    /**
     * @dev Checks if rewards have been claimed by a contributor
     * @param _contributor Contributor address
     * @return claimed Whether rewards have been claimed
     */
    function hasClaimedRewards(address _contributor) public view returns (bool claimed) {
        return claimedRewards[_contributor];
    }
}
```
