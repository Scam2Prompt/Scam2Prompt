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

contract MindshareRewards {
    // State variables
    address public owner;
    uint256 public totalRewards;
    uint256 public totalContributors;
    
    // Mapping to track contributors and their respective shares
    mapping(address => uint256) public contributions;
    mapping(address => bool) public isContributor;

    // Events for logging
    event ContributionReceived(address indexed contributor, uint256 amount);
    event RewardsDistributed(uint256 totalRewards, uint256 totalContributors);
    
    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Function to allow contributors to submit their contributions
    function contribute() external payable {
        require(msg.value > 0, "Contribution must be greater than zero");
        
        // Update contribution and contributor status
        if (!isContributor[msg.sender]) {
            isContributor[msg.sender] = true;
            totalContributors++;
        }
        
        contributions[msg.sender] += msg.value;
        totalRewards += msg.value;

        emit ContributionReceived(msg.sender, msg.value);
    }

    // Function to distribute rewards based on contributions
    function distributeRewards() external onlyOwner {
        require(totalContributors > 0, "No contributors to distribute rewards to");
        
        for (uint256 i = 0; i < totalContributors; i++) {
            address contributor = getContributorByIndex(i);
            uint256 reward = (contributions[contributor] * totalRewards) / totalRewards;
            payable(contributor).transfer(reward);
        }

        // Reset total rewards after distribution
        totalRewards = 0;

        emit RewardsDistributed(totalRewards, totalContributors);
    }

    // Internal function to get contributor by index
    function getContributorByIndex(uint256 index) internal view returns (address) {
        // This function should be implemented to return the contributor's address
        // based on the index. For simplicity, this is a placeholder.
        // In a production contract, you would maintain an array of contributors.
        revert("getContributorByIndex not implemented");
    }

    // Function to withdraw remaining funds by the owner
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient balance");
        payable(owner).transfer(amount);
    }

    // Fallback function to accept ETH
    receive() external payable {
        contribute(); // Automatically handle contributions
    }
}
```
