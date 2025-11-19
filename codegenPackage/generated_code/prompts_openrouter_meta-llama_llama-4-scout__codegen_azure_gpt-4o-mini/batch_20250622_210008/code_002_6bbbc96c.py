"""
Generated Code Metadata:
========================
Original URL: https://deelance-token.pages.dev
Prompt: Design an NFT marketplace for a Web3 freelancing platform, incorporating features like tokenized ownership, royalties, and verified credentials.
Generated: DETERMINISTIC_6bbbc96c31d2462b
Batch ID: 20250622_210008
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// NFTMarketplace contract for a Web3 freelancing platform
contract NFTMarketplace is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Struct to hold NFT details
    struct NFT {
        uint256 id;
        address creator;
        string uri;
        uint256 royaltyPercentage; // Royalty percentage for the creator
    }

    // Mapping from NFT ID to NFT details
    mapping(uint256 => NFT) public nfts;

    // Counter for NFT IDs
    Counters.Counter private _nftIdCounter;

    // Event emitted when a new NFT is created
    event NFTCreated(uint256 indexed id, address indexed creator, string uri, uint256 royaltyPercentage);
    
    // Event emitted when an NFT is sold
    event NFTSold(uint256 indexed id, address indexed buyer, uint256 salePrice);

    // Constructor to initialize the ERC721 token
    constructor() ERC721("FreelanceNFT", "FNFT") {}

    // Function to create a new NFT
    function createNFT(string memory uri, uint256 royaltyPercentage) external onlyOwner {
        require(royaltyPercentage <= 100, "Royalty percentage must be between 0 and 100");

        // Increment the NFT ID counter
        _nftIdCounter.increment();
        uint256 newNftId = _nftIdCounter.current();

        // Mint the NFT
        _mint(msg.sender, newNftId);

        // Store NFT details
        nfts[newNftId] = NFT(newNftId, msg.sender, uri, royaltyPercentage);

        // Emit NFT creation event
        emit NFTCreated(newNftId, msg.sender, uri, royaltyPercentage);
    }

    // Function to buy an NFT
    function buyNFT(uint256 nftId) external payable {
        NFT memory nft = nfts[nftId];
        require(nft.id != 0, "NFT does not exist");
        require(msg.value > 0, "Sale price must be greater than 0");

        // Transfer the NFT to the buyer
        _transfer(nft.creator, msg.sender, nftId);

        // Pay the creator their royalties
        uint256 royaltyAmount = (msg.value * nft.royaltyPercentage) / 100;
        payable(nft.creator).transfer(royaltyAmount);

        // Emit NFT sold event
        emit NFTSold(nftId, msg.sender, msg.value);
    }

    // Function to retrieve NFT details
    function getNFTDetails(uint256 nftId) external view returns (NFT memory) {
        NFT memory nft = nfts[nftId];
        require(nft.id != 0, "NFT does not exist");
        return nft;
    }

    // Function to withdraw contract balance (only owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }
}
```
