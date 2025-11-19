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

contract RewardDistributor {
    // State variables
    address public owner;
    mapping(address => Contributor) public contributors;
    address[] public contributorList;

    struct Contributor {
        uint256 mindshare; // Mindshare score of the contributor
        uint256 tradingVolume; // Trading volume of the contributor
        uint256 reward; // Total rewards earned
    }

    // Events
    event RewardDistributed(address indexed contributor, uint256 amount);
    event ContributorAdded(address indexed contributor);
    event ContributorUpdated(address indexed contributor, uint256 mindshare, uint256 tradingVolume);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Function to add or update a contributor
    function updateContributor(address _contributor, uint256 _mindshare, uint256 _tradingVolume) external onlyOwner {
        if (contributors[_contributor].mindshare == 0 && contributors[_contributor].tradingVolume == 0) {
            contributorList.push(_contributor); // Add new contributor to the list
        }
        contributors[_contributor].mindshare = _mindshare;
        contributors[_contributor].tradingVolume = _tradingVolume;

        emit ContributorUpdated(_contributor, _mindshare, _tradingVolume);
    }

    // Function to distribute rewards based on mindshare and trading volume
    function distributeRewards() external onlyOwner {
        uint256 totalReward = address(this).balance; // Total available rewards in the contract
        require(totalReward > 0, "No rewards available for distribution");

        uint256 totalWeight = 0;
        // Calculate total weight based on mindshare and trading volume
        for (uint256 i = 0; i < contributorList.length; i++) {
            totalWeight += contributors[contributorList[i]].mindshare + contributors[contributorList[i]].tradingVolume;
        }

        // Distribute rewards proportionally
        for (uint256 i = 0; i < contributorList.length; i++) {
            address contributor = contributorList[i];
            uint256 contributorWeight = contributors[contributor].mindshare + contributors[contributor].tradingVolume;
            if (contributorWeight > 0) {
                uint256 rewardAmount = (totalReward * contributorWeight) / totalWeight;
                contributors[contributor].reward += rewardAmount; // Update contributor's total reward
                emit RewardDistributed(contributor, rewardAmount);
            }
        }
    }

    // Function to withdraw rewards by the contributor
    function withdrawRewards() external {
        uint256 reward = contributors[msg.sender].reward;
        require(reward > 0, "No rewards to withdraw");

        contributors[msg.sender].reward = 0; // Reset reward before transfer to prevent re-entrancy
        payable(msg.sender).transfer(reward); // Transfer the reward to the contributor
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
