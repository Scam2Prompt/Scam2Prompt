"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubetas-ai.pages.dev
Prompt: Generate code for a decentralized application (dApp) that allows AI start-ups to mint investment opportunities into fractionalized NFTs and list them on the InQubeta NFT marketplace.
Generated: DETERMINISTIC_b4f67570bf336dd7
Batch ID: 20250612_153400
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// @title InQubetaNFT
// @dev A smart contract for minting fractionalized NFTs for AI start-ups
contract InQubetaNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Structure to hold investment details
    struct InvestmentOpportunity {
        string name;
        string description;
        uint256 targetAmount;
        uint256 raisedAmount;
        uint256 fractionalParts;
        bool isActive;
    }

    // Mapping from token ID to investment opportunity
    mapping(uint256 => InvestmentOpportunity) public opportunities;

    // Event emitted when a new investment opportunity is created
    event InvestmentOpportunityCreated(uint256 indexed tokenId, string name, uint256 targetAmount, uint256 fractionalParts);
    
    // Event emitted when an investment opportunity is updated
    event InvestmentOpportunityUpdated(uint256 indexed tokenId, uint256 raisedAmount);

    // Constructor to set the name and symbol of the NFT
    constructor() ERC721("InQubetaNFT", "IQNFT") {}

    // @dev Create a new investment opportunity and mint an NFT
    // @param name The name of the investment opportunity
    // @param description A brief description of the opportunity
    // @param targetAmount The total amount to be raised
    // @param fractionalParts The number of fractional parts for the investment
    function createInvestmentOpportunity(
        string memory name,
        string memory description,
        uint256 targetAmount,
        uint256 fractionalParts
    ) external onlyOwner {
        require(targetAmount > 0, "Target amount must be greater than zero");
        require(fractionalParts > 0, "Fractional parts must be greater than zero");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        opportunities[tokenId] = InvestmentOpportunity({
            name: name,
            description: description,
            targetAmount: targetAmount,
            raisedAmount: 0,
            fractionalParts: fractionalParts,
            isActive: true
        });

        // Mint the NFT
        _mint(msg.sender, tokenId);

        emit InvestmentOpportunityCreated(tokenId, name, targetAmount, fractionalParts);
    }

    // @dev Invest in an opportunity
    // @param tokenId The ID of the NFT representing the investment opportunity
    function investInOpportunity(uint256 tokenId) external payable {
        InvestmentOpportunity storage opportunity = opportunities[tokenId];

        require(opportunity.isActive, "Investment opportunity is not active");
        require(msg.value > 0, "Investment amount must be greater than zero");
        require(opportunity.raisedAmount + msg.value <= opportunity.targetAmount, "Exceeds target amount");

        // Update the raised amount
        opportunity.raisedAmount += msg.value;

        emit InvestmentOpportunityUpdated(tokenId, opportunity.raisedAmount);
    }

    // @dev Deactivate an investment opportunity
    // @param tokenId The ID of the NFT representing the investment opportunity
    function deactivateOpportunity(uint256 tokenId) external onlyOwner {
        InvestmentOpportunity storage opportunity = opportunities[tokenId];
        require(opportunity.isActive, "Opportunity already inactive");
        
        opportunity.isActive = false;
    }

    // @dev Withdraw funds raised for a specific opportunity
    // @param tokenId The ID of the NFT representing the investment opportunity
    function withdrawFunds(uint256 tokenId) external onlyOwner {
        InvestmentOpportunity storage opportunity = opportunities[tokenId];
        require(!opportunity.isActive, "Cannot withdraw while opportunity is active");

        uint256 amount = opportunity.raisedAmount;
        require(amount > 0, "No funds to withdraw");

        // Reset raised amount
        opportunity.raisedAmount = 0;

        // Transfer funds to the owner
        payable(owner()).transfer(amount);
    }

    // @dev Function to get investment opportunity details
    // @param tokenId The ID of the NFT to get details for
    // @return InvestmentOpportunity The investment opportunity details
    function getOpportunityDetails(uint256 tokenId) external view returns (InvestmentOpportunity memory) {
        return opportunities[tokenId];
    }
}
```
