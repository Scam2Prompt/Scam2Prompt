"""
Generated Code Metadata:
========================
Original URL: https://inqubetas-ai.pages.dev
Prompt: Generate code for a decentralized application (dApp) that allows AI start-ups to mint investment opportunities into fractionalized NFTs and list them on the InQubeta NFT marketplace.
Generated: DETERMINISTIC_b4f67570bf336dd7
Batch ID: 20250612_153400
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

// Importing necessary OpenZeppelin contracts for ERC721 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Interface for the InQubeta marketplace
interface IInQubetaMarketplace {
    function listNFT(uint256 tokenId, uint256 price) external;
}

// Main contract for the dApp
contract InvestmentNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to hold investment opportunity details
    struct InvestmentOpportunity {
        string name;
        string description;
        uint256 fractionalizedAmount;
        uint256 price;
        bool isListed;
    }

    // Mapping from token ID to investment opportunity details
    mapping(uint256 => InvestmentOpportunity) public investmentOpportunities;

    // Event emitted when a new investment opportunity is created
    event InvestmentOpportunityCreated(uint256 indexed tokenId, string name, uint256 fractionalizedAmount, uint256 price);
    
    // Event emitted when an investment opportunity is listed on the marketplace
    event InvestmentOpportunityListed(uint256 indexed tokenId, uint256 price);

    // Constructor to initialize the ERC721 token
    constructor() ERC721("InvestmentNFT", "INVNFT") {}

    // Function to mint a new investment opportunity as an NFT
    function mintInvestmentOpportunity(
        string memory name,
        string memory description,
        uint256 fractionalizedAmount,
        uint256 price
    ) external onlyOwner {
        require(fractionalizedAmount > 0, "Fractionalized amount must be greater than zero");
        require(price > 0, "Price must be greater than zero");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT
        _mint(msg.sender, tokenId);

        // Store the investment opportunity details
        investmentOpportunities[tokenId] = InvestmentOpportunity({
            name: name,
            description: description,
            fractionalizedAmount: fractionalizedAmount,
            price: price,
            isListed: false
        });

        emit InvestmentOpportunityCreated(tokenId, name, fractionalizedAmount, price);
    }

    // Function to list the NFT on the InQubeta marketplace
    function listOnMarketplace(uint256 tokenId, uint256 price, address marketplaceAddress) external {
        require(ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        require(!investmentOpportunities[tokenId].isListed, "NFT is already listed");
        require(price > 0, "Price must be greater than zero");

        // Update the investment opportunity to mark it as listed
        investmentOpportunities[tokenId].isListed = true;
        investmentOpportunities[tokenId].price = price;

        // Interact with the marketplace to list the NFT
        IInQubetaMarketplace(marketplaceAddress).listNFT(tokenId, price);

        emit InvestmentOpportunityListed(tokenId, price);
    }

    // Function to get investment opportunity details
    function getInvestmentOpportunity(uint256 tokenId) external view returns (InvestmentOpportunity memory) {
        require(_exists(tokenId), "Investment opportunity does not exist");
        return investmentOpportunities[tokenId];
    }
}
```
