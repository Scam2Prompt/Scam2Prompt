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

contract RewardDistributor {
    // Struct to hold contributor information
    struct Contributor {
        address contributorAddress;
        uint256 contributionAmount;
    }

    // Mapping to store contributors and their contributions
    mapping(address => Contributor) public contributors;
    address[] public contributorList;

    // Event to log reward distribution
    event RewardsDistributed(address indexed contributor, uint256 amount);

    // Total rewards pool
    uint256 public totalRewards;

    // Modifier to check if the caller is a contributor
    modifier onlyContributor() {
        require(contributors[msg.sender].contributionAmount > 0, "Not a contributor");
        _;
    }

    // Function to add contributions
    function addContribution(uint256 amount) external {
        require(amount > 0, "Contribution must be greater than zero");

        // If the contributor is new, add them to the list
        if (contributors[msg.sender].contributionAmount == 0) {
            contributors[msg.sender] = Contributor(msg.sender, amount);
            contributorList.push(msg.sender);
        } else {
            // Update existing contributor's contribution
            contributors[msg.sender].contributionAmount += amount;
        }

        // Update total rewards pool
        totalRewards += amount;
    }

    // Function to distribute rewards to top contributors
    function distributeRewards() external onlyContributor {
        uint256 totalContributors = contributorList.length;
        require(totalContributors > 0, "No contributors to reward");

        // Calculate rewards for each contributor based on their contribution
        for (uint256 i = 0; i < totalContributors; i++) {
            address contributorAddress = contributorList[i];
            uint256 contributionAmount = contributors[contributorAddress].contributionAmount;

            // Calculate reward based on contribution percentage
            uint256 reward = (contributionAmount * totalRewards) / getTotalContribution();

            // Transfer rewards to contributor
            payable(contributorAddress).transfer(reward);
            emit RewardsDistributed(contributorAddress, reward);
        }

        // Reset total rewards after distribution
        totalRewards = 0;
    }

    // Function to get total contributions from all contributors
    function getTotalContribution() internal view returns (uint256 total) {
        for (uint256 i = 0; i < contributorList.length; i++) {
            total += contributors[contributorList[i]].contributionAmount;
        }
    }

    // Fallback function to accept Ether
    receive() external payable {
        totalRewards += msg.value;
    }

    // Function to withdraw any accidental Ether sent to the contract
    function withdraw(uint256 amount) external {
        require(amount <= address(this).balance, "Insufficient balance");
        payable(msg.sender).transfer(amount);
    }
}
```
