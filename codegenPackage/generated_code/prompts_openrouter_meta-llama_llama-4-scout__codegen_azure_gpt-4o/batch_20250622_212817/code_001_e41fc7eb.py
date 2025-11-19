"""
Generated Code Metadata:
========================
Original URL: https://staylloud.io
Prompt: Design a smart contract function in Solidity that distributes rewards in SOL to top contributors based on their mindshare, inspired by Loud's mechanism.
Generated: DETERMINISTIC_e41fc7eb58e6b0fd
Batch ID: 20250622_212817
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
 * @title RewardDistributor
 * @dev A smart contract to distribute SOL rewards to top contributors based on their mindshare.
 */
contract RewardDistributor {
    // Struct to store contributor details
    struct Contributor {
        address wallet;
        uint256 mindshare; // Mindshare value (e.g., points or percentage)
    }

    // Array to store top contributors
    Contributor[] public topContributors;

    // Event to log reward distribution
    event RewardsDistributed(uint256 totalRewards, uint256 timestamp);

    /**
     * @dev Function to add a contributor to the list of top contributors.
     * @param _wallet Address of the contributor.
     * @param _mindshare Mindshare value of the contributor.
     */
    function addContributor(address _wallet, uint256 _mindshare) external {
        require(_wallet != address(0), "Invalid wallet address");
        require(_mindshare > 0, "Mindshare must be greater than zero");

        topContributors.push(Contributor(_wallet, _mindshare));
    }

    /**
     * @dev Function to distribute rewards to top contributors based on their mindshare.
     * @param _totalRewards Total amount of SOL to be distributed.
     */
    function distributeRewards(uint256 _totalRewards) external payable {
        require(msg.value == _totalRewards, "Insufficient funds sent");
        require(topContributors.length > 0, "No contributors available");

        uint256 totalMindshare = 0;

        // Calculate total mindshare
        for (uint256 i = 0; i < topContributors.length; i++) {
            totalMindshare += topContributors[i].mindshare;
        }

        require(totalMindshare > 0, "Total mindshare must be greater than zero");

        // Distribute rewards based on mindshare
        for (uint256 i = 0; i < topContributors.length; i++) {
            Contributor memory contributor = topContributors[i];
            uint256 reward = (_totalRewards * contributor.mindshare) / totalMindshare;

            // Transfer reward to contributor
            (bool success, ) = contributor.wallet.call{value: reward}("");
            require(success, "Reward transfer failed");
        }

        emit RewardsDistributed(_totalRewards, block.timestamp);
    }

    /**
     * @dev Function to clear the list of top contributors.
     * This can be used to reset the list after rewards are distributed.
     */
    function clearContributors() external {
        delete topContributors;
    }

    /**
     * @dev Fallback function to receive SOL.
     */
    receive() external payable {}

    /**
     * @dev Function to withdraw any remaining funds in the contract.
     * @param _to Address to send the remaining funds to.
     */
    function withdraw(address payable _to) external {
        require(_to != address(0), "Invalid address");
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available");

        (bool success, ) = _to.call{value: balance}("");
        require(success, "Withdrawal failed");
    }
}
```
