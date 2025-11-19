"""
Generated Code Metadata:
========================
Original URL: https://sol-boxs.web.app
Prompt: Write code to enforce trading restrictions and royalties on NFTs minted using the Open Creator Protocol, as highlighted in the Magic Box section.
Generated: DETERMINISTIC_340b92b7eb8cfdf7
Batch ID: 20250612_150557
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Interface for the Open Creator Protocol
interface IOpenCreatorProtocol {
    function enforceTradingRestrictions(uint256 tokenId) external view returns (bool);
    function calculateRoyalty(uint256 tokenId, uint256 salePrice) external view returns (uint256);
}

// NFT contract that implements trading restrictions and royalties
contract NFTWithTradingRestrictions is ERC721Enumerable, Ownable, IOpenCreatorProtocol {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping to store trading restrictions for each token
    mapping(uint256 => bool) private _tradingRestricted;

    // Mapping to store royalty percentages for each token
    mapping(uint256 => uint256) private _royaltyPercentages;

    // Event emitted when a token's trading restriction is set
    event TradingRestrictionSet(uint256 indexed tokenId, bool restricted);

    // Event emitted when a royalty percentage is set
    event RoyaltyPercentageSet(uint256 indexed tokenId, uint256 percentage);

    // Constructor to initialize the NFT contract
    constructor() ERC721("NFTWithTradingRestrictions", "NTR") {}

    // Function to mint a new NFT
    function mintNFT(address to, uint256 royaltyPercentage) external onlyOwner {
        require(royaltyPercentage <= 100, "Royalty percentage must be between 0 and 100");
        
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _mint(to, tokenId);
        _royaltyPercentages[tokenId] = royaltyPercentage;

        emit RoyaltyPercentageSet(tokenId, royaltyPercentage);
    }

    // Function to set trading restrictions on a specific token
    function setTradingRestriction(uint256 tokenId, bool restricted) external onlyOwner {
        require(_exists(tokenId), "Token does not exist");
        
        _tradingRestricted[tokenId] = restricted;
        emit TradingRestrictionSet(tokenId, restricted);
    }

    // Function to check if trading is restricted for a specific token
    function enforceTradingRestrictions(uint256 tokenId) external view override returns (bool) {
        require(_exists(tokenId), "Token does not exist");
        return _tradingRestricted[tokenId];
    }

    // Function to calculate the royalty for a specific token based on sale price
    function calculateRoyalty(uint256 tokenId, uint256 salePrice) external view override returns (uint256) {
        require(_exists(tokenId), "Token does not exist");
        uint256 royaltyPercentage = _royaltyPercentages[tokenId];
        return (salePrice * royaltyPercentage) / 100;
    }

    // Function to retrieve the royalty percentage for a specific token
    function getRoyaltyPercentage(uint256 tokenId) external view returns (uint256) {
        require(_exists(tokenId), "Token does not exist");
        return _royaltyPercentages[tokenId];
    }
}
```
