"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-inqubeta-ai.pages.dev
Prompt: Create a Solidity smart contract that allows AI start-ups to mint fractionalized NFTs representing investment opportunities, as described in the InQubeta NFT marketplace.
Generated: DETERMINISTIC_ff349d6d481d8639
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title FractionalNFT
 * @dev A smart contract for minting fractionalized NFTs representing investment opportunities for AI start-ups.
 */
contract FractionalNFT is ERC721, ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for assigning unique token IDs
    Counters.Counter private _tokenIdCounter;

    // Struct to represent an NFT investment opportunity
    struct InvestmentOpportunity {
        uint256 id;
        string name;
        string description;
        address creator;
        uint256 totalShares;
        uint256 availableShares;
        mapping(address => uint256) sharesOwned; // Tracks shares owned by each investor
    }

    // Mapping from token ID to investment opportunity
    mapping(uint256 => InvestmentOpportunity) private _investmentOpportunities;

    // Event emitted when a new investment opportunity is created
    event InvestmentOpportunityCreated(uint256 indexed tokenId, string name, address indexed creator);

    // Event emitted when shares are purchased
    event SharesPurchased(uint256 indexed tokenId, address indexed buyer, uint256 shares);

    // Constructor to set the NFT collection name and symbol
    constructor() ERC721("InQubeta NFT", "IQB") {}

    /**
     * @dev Create a new investment opportunity NFT.
     * @param name The name of the investment opportunity.
     * @param description A brief description of the investment opportunity.
     * @param totalShares The total number of shares available for this opportunity.
     */
    function createInvestmentOpportunity(string memory name, string memory description, uint256 totalShares) external onlyOwner {
        require(totalShares > 0, "Total shares must be greater than zero");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        InvestmentOpportunity storage newOpportunity = _investmentOpportunities[tokenId];
        newOpportunity.id = tokenId;
        newOpportunity.name = name;
        newOpportunity.description = description;
        newOpportunity.creator = msg.sender;
        newOpportunity.totalShares = totalShares;
        newOpportunity.availableShares = totalShares;

        _mint(msg.sender, tokenId);
        emit InvestmentOpportunityCreated(tokenId, name, msg.sender);
    }

    /**
     * @dev Purchase shares of an existing investment opportunity.
     * @param tokenId The ID of the investment opportunity NFT.
     * @param shares The number of shares to purchase.
     */
    function purchaseShares(uint256 tokenId, uint256 shares) external payable {
        InvestmentOpportunity storage opportunity = _investmentOpportunities[tokenId];

        require(_exists(tokenId), "Investment opportunity does not exist");
        require(opportunity.availableShares >= shares, "Not enough shares available");
        require(shares > 0, "Must purchase at least one share");

        // Simulate a price calculation based on shares (for demo purposes)
        uint256 pricePerShare = 0.01 ether; // Example price (in ether)
        require(msg.value >= shares * pricePerShare, "Insufficient payment");

        // Update the shares owned by the buyer
        opportunity.sharesOwned[msg.sender] += shares;
        opportunity.availableShares -= shares;

        // Emit event for purchased shares
        emit SharesPurchased(tokenId, msg.sender, shares);
    }

    /**
     * @dev Get investment opportunity details by token ID.
     * @param tokenId The ID of the investment opportunity NFT.
     * @return The details of the investment opportunity.
     */
    function getInvestmentOpportunity(uint256 tokenId) external view returns (string memory name, string memory description, address creator, uint256 totalShares, uint256 availableShares) {
        InvestmentOpportunity storage opportunity = _investmentOpportunities[tokenId];
        require(_exists(tokenId), "Investment opportunity does not exist");

        return (opportunity.name, opportunity.description, opportunity.creator, opportunity.totalShares, opportunity.availableShares);
    }

    /**
     * @dev Override required for ERC721Enumerable
     */
    function supportsInterface(bytes4 interfaceId) public view virtual override(ERC721, ERC721Enumerable) returns (bool) {
        return super.supportsInterface(interfaceId);
    }

    /**
     * @dev Override required for ERC721Enumerable
     */
    function _beforeTokenTransfer(address from, address to, uint256 tokenId) internal virtual override(ERC721, ERC721Enumerable) {
        super._beforeTokenTransfer(from, to, tokenId);
    }
}
```
