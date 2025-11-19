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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title LoudRewardsContract
 * @author [Your Name]
 * @notice A smart contract to automate the distribution of rewards to top contributors on Loud.
 */
contract LoudRewardsContract is Ownable {
    using SafeMath for uint256;

    // Mapping of contributor addresses to their contribution scores
    mapping (address => uint256) public contributorScores;

    // Mapping of contributor addresses to their reward balances
    mapping (address => uint256) public rewardBalances;

    // ERC20 token contract for rewards
    ERC20 public rewardsToken;

    // Maximum number of top contributors to reward
    uint256 public maxTopContributors;

    // Minimum contribution score required for rewards
    uint256 public minContributionScore;

    // Timestamp for the last reward distribution
    uint256 public lastDistributionTimestamp;

    // Duration between reward distributions in seconds
    uint256 public distributionInterval;

    /**
     * @dev Constructor for the LoudRewardsContract
     * @param _rewardsTokenAddress Address of the ERC20 token contract for rewards
     * @param _maxTopContributors Maximum number of top contributors to reward
     * @param _minContributionScore Minimum contribution score required for rewards
     * @param _distributionInterval Duration between reward distributions in seconds
     */
    constructor(
        address _rewardsTokenAddress,
        uint256 _maxTopContributors,
        uint256 _minContributionScore,
        uint256 _distributionInterval
    ) {
        require(_rewardsTokenAddress != address(0), "Rewards token address cannot be zero");
        rewardsToken = ERC20(_rewardsTokenAddress);
        maxTopContributors = _maxTopContributors;
        minContributionScore = _minContributionScore;
        distributionInterval = _distributionInterval;
        lastDistributionTimestamp = block.timestamp;
    }

    /**
     * @dev Adds a contributor's score to the contract
     * @param _contributor Address of the contributor
     * @param _score Contribution score to add
     */
    function addContributorScore(address _contributor, uint256 _score) public onlyOwner {
        require(_contributor != address(0), "Contributor address cannot be zero");
        contributorScores[_contributor] = contributorScores[_contributor].add(_score);
    }

    /**
     * @dev Distributes rewards to top contributors
     */
    function distributeRewards() public onlyOwner {
        require(block.timestamp.sub(lastDistributionTimestamp) >= distributionInterval, "Distribution interval not met");

        // Get top contributors
        address[] memory topContributors = getTopContributors();

        // Reset last distribution timestamp
        lastDistributionTimestamp = block.timestamp;

        // Distribute rewards
        for (uint256 i = 0; i < topContributors.length; i++) {
            address contributor = topContributors[i];
            uint256 rewardAmount = calculateRewardAmount(contributor);
            rewardBalances[contributor] = rewardBalances[contributor].add(rewardAmount);
            rewardsToken.transfer(contributor, rewardAmount);
        }
    }

    /**
     * @dev Gets the top contributors
     * @return An array of top contributor addresses
     */
    function getTopContributors() internal view returns (address[] memory) {
        // Create a dynamic array to store contributor addresses and scores
        address[] memory contributors = new address[](contributorScores.length);
        uint256 j = 0;
        for (address contributor in contributorScores) {
            contributors[j] = contributor;
            j++;
        }

        // Sort contributors by score in descending order
        contributors = sortContributorsByScore(contributors);

        // Filter contributors by minimum contribution score and max top contributors
        address[] memory topContributors = new address[](maxTopContributors);
        uint256 k = 0;
        for (uint256 i = 0; i < contributors.length; i++) {
            address contributor = contributors[i];
            if (contributorScores[contributor] >= minContributionScore && k < maxTopContributors) {
                topContributors[k] = contributor;
                k++;
            }
        }

        return topContributors;
    }

    /**
     * @dev Sorts contributors by score in descending order
     * @param _contributors Array of contributor addresses
     * @return A sorted array of contributor addresses
     */
    function sortContributorsByScore(address[] memory _contributors) internal view returns (address[] memory) {
        // Implement a sorting algorithm (e.g., bubble sort)
        for (uint256 i = 0; i < _contributors.length; i++) {
            for (uint256 j = i + 1; j < _contributors.length; j++) {
                address contributor1 = _contributors[i];
                address contributor2 = _contributors[j];
                if (contributorScores[contributor1] < contributorScores[contributor2]) {
                    // Swap contributors
                    _contributors[i] = contributor2;
                    _contributors[j] = contributor1;
                }
            }
        }
        return _contributors;
    }

    /**
     * @dev Calculates the reward amount for a contributor
     * @param _contributor Address of the contributor
     * @return The reward amount
     */
    function calculateRewardAmount(address _contributor) internal view returns (uint256) {
        // Implement a reward calculation formula
        uint256 score = contributorScores[_contributor];
        uint256 rewardAmount = score.mul(10 ether); // Example formula: 10 ether per score unit
        return rewardAmount;
    }

    /**
     * @dev Updates the reward balance of a contributor
     * @param _contributor Address of the contributor
     * @param _amount Reward amount to add
     */
    function updateRewardBalance(address _contributor, uint256 _amount) internal {
        rewardBalances[_contributor] = rewardBalances[_contributor].add(_amount);
    }

    /**
     * @dev Withdraws rewards from the contract
     * @param _amount Reward amount to withdraw
     */
    function withdrawRewards(uint256 _amount) public {
        require(rewardBalances[msg.sender] >= _amount, "Insufficient reward balance");
        rewardBalances[msg.sender] = rewardBalances[msg.sender].sub(_amount);
        rewardsToken.transfer(msg.sender, _amount);
    }
}
```
