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

/**
 * @title RewardDistribution
 * @dev A smart contract to distribute SOL rewards to top contributors based on mindshare and trading volume.
 */
contract RewardDistribution {
    // Struct to store contributor details
    struct Contributor {
        uint256 mindshare; // Contributor's mindshare score
        uint256 tradingVolume; // Contributor's trading volume
        uint256 rewards; // Rewards allocated to the contributor
    }

    // Mapping to store contributors' data
    mapping(address => Contributor) public contributors;

    // Address of the owner (platform admin)
    address public owner;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed contributor, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Constructor to set the owner of the contract
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to add or update a contributor's data.
     * @param _contributor Address of the contributor.
     * @param _mindshare Mindshare score of the contributor.
     * @param _tradingVolume Trading volume of the contributor.
     */
    function updateContributor(
        address _contributor,
        uint256 _mindshare,
        uint256 _tradingVolume
    ) external onlyOwner {
        contributors[_contributor].mindshare = _mindshare;
        contributors[_contributor].tradingVolume = _tradingVolume;
    }

    /**
     * @dev Function to distribute rewards to contributors based on their mindshare and trading volume.
     * @param _totalRewards Total amount of rewards to be distributed.
     */
    function distributeRewards(uint256 _totalRewards) external onlyOwner {
        uint256 totalMindshare = 0;
        uint256 totalTradingVolume = 0;

        // Calculate total mindshare and trading volume
        for (uint256 i = 0; i < contributors.length; i++) {
            totalMindshare += contributors[i].mindshare;
            totalTradingVolume += contributors[i].tradingVolume;
        }

        // Distribute rewards to each contributor
        for (uint256 i = 0; i < contributors.length; i++) {
            uint256 mindshareWeight = contributors[i].mindshare / totalMindshare;
            uint256 tradingVolumeWeight = contributors[i].tradingVolume / totalTradingVolume;

            uint256 reward = _totalRewards * (mindshareWeight + tradingVolumeWeight) / 2;
            contributors[i].rewards += reward;

            // Emit event for reward distribution
            emit RewardsDistributed(contributors[i].address, reward);
        }
    }

    /**
     * @dev Function to withdraw rewards by a contributor.
     */
    function withdrawRewards() external {
        uint256 reward = contributors[msg.sender].rewards;
        require(reward > 0, "No rewards available to withdraw");

        // Reset rewards to zero before transferring
        contributors[msg.sender].rewards = 0;

        // Transfer rewards to the contributor
        (bool success, ) = msg.sender.call{value: reward}("");
        require(success, "Reward transfer failed");
    }

    // Fallback function to receive SOL
    receive() external payable {}

    // Function to get the balance of the contract
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
