"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xai327k.com
Prompt: Write a smart contract in Solidity for managing xAI327K token presale contributions and distributing bonuses.
Generated: DETERMINISTIC_938af590b3f08c40
Batch ID: 20250612_150034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Presale {
    // State variables
    address public owner;
    uint256 public tokenPrice; // Price of each token in wei
    uint256 public totalContributions; // Total contributions made during the presale
    uint256 public bonusThreshold; // Minimum contribution amount to qualify for bonus
    uint256 public bonusPercentage; // Bonus percentage for qualifying contributions
    mapping(address => uint256) public contributions; // Maps addresses to their contributions

    // Events
    event ContributionReceived(address indexed contributor, uint256 amount);
    event BonusDistributed(address indexed contributor, uint256 bonusAmount);
    event TokensClaimed(address indexed contributor, uint256 tokenAmount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _tokenPrice, uint256 _bonusThreshold, uint256 _bonusPercentage) {
        owner = msg.sender; // Set the contract deployer as the owner
        tokenPrice = _tokenPrice;
        bonusThreshold = _bonusThreshold;
        bonusPercentage = _bonusPercentage;
    }

    // Function to contribute to the presale
    function contribute() external payable {
        require(msg.value > 0, "Contribution must be greater than 0");
        
        contributions[msg.sender] += msg.value;
        totalContributions += msg.value;

        emit ContributionReceived(msg.sender, msg.value);
    }

    // Function to calculate and distribute bonuses
    function distributeBonuses() external onlyOwner {
        for (uint256 i = 0; i < totalContributions; i++) {
            address contributor = address(uint160(i)); // Cast uint to address (placeholder logic)
            uint256 contribution = contributions[contributor];
            if (contribution >= bonusThreshold) {
                uint256 bonusAmount = (contribution * bonusPercentage) / 100;
                emit BonusDistributed(contributor, bonusAmount);
                // Logic to distribute bonus (would typically be handled via a token transfer)
            }
        }
    }

    // Function to claim tokens after presale ends
    function claimTokens() external {
        uint256 contributedAmount = contributions[msg.sender];
        require(contributedAmount > 0, "No contribution found for this address");

        // Calculate the number of tokens to be allocated
        uint256 tokensToClaim = contributedAmount / tokenPrice;

        // Reset contribution after claiming
        contributions[msg.sender] = 0;

        emit TokensClaimed(msg.sender, tokensToClaim);
        // Logic to transfer tokens to the contributor
    }

    // Function to withdraw contract balance (only owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner).transfer(balance);
    }

    // Fallback function to accept ETH contributions
    receive() external payable {
        contribute();
    }
}
```
