"""
Generated Code Metadata:
========================
Original URL: https://wwwstayloud.io
Prompt: "Write a Solidity function to handle the 4% fee split on Loud, ensuring that rewards are distributed correctly to top contributors each week."
Generated: DETERMINISTIC_29543b9571cc4b13
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

contract Loud {
    // State variables
    address public owner;
    uint256 public totalContributions;
    mapping(address => uint256) public contributions;
    address[] public topContributors;
    
    // Event to log fee distribution
    event FeeDistributed(address indexed contributor, uint256 amount);

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Function to contribute to the Loud project
    function contribute() external payable {
        require(msg.value > 0, "Contribution must be greater than 0");
        
        // Update total contributions and individual contributor's amount
        contributions[msg.sender] += msg.value;
        totalContributions += msg.value;
        
        // Update top contributors if necessary
        updateTopContributors(msg.sender);
    }

    // Function to update the list of top contributors
    function updateTopContributors(address contributor) internal {
        // Logic to determine if the contributor is in the top contributors list
        // This is a placeholder for actual logic to maintain top contributors
        // For simplicity, we will just add the contributor if they are not already in the list
        if (contributions[contributor] > 0 && !isTopContributor(contributor)) {
            topContributors.push(contributor);
        }
    }

    // Function to check if an address is a top contributor
    function isTopContributor(address contributor) internal view returns (bool) {
        for (uint256 i = 0; i < topContributors.length; i++) {
            if (topContributors[i] == contributor) {
                return true;
            }
        }
        return false;
    }

    // Function to distribute the 4% fee to top contributors
    function distributeFees() external onlyOwner {
        require(totalContributions > 0, "No contributions to distribute fees from");
        
        uint256 feeAmount = (totalContributions * 4) / 100; // Calculate 4% fee
        uint256 sharePerContributor = feeAmount / topContributors.length; // Equal share for each top contributor

        // Distribute fees to each top contributor
        for (uint256 i = 0; i < topContributors.length; i++) {
            address contributor = topContributors[i];
            payable(contributor).transfer(sharePerContributor);
            emit FeeDistributed(contributor, sharePerContributor);
        }
    }

    // Function to withdraw funds (only for the owner)
    function withdraw() external onlyOwner {
        require(address(this).balance > 0, "No funds to withdraw");
        payable(owner).transfer(address(this).balance);
    }

    // Fallback function to accept Ether
    receive() external payable {
        contribute();
    }
}
```
