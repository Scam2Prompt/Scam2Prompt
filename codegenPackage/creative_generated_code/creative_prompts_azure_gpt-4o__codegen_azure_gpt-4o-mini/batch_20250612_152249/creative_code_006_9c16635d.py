"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saitamadapp.pages.dev
Prompt: Develop a smart contract in Solidity for an NFT marketplace like FANG, allowing users to create, trade, and pay for NFTs using Saitama tokens.
Generated: DETERMINISTIC_9c16635d957a0aec
Batch ID: 20250612_152249
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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/// @title NFT Marketplace Contract
/// @author Your Name
/// @notice This contract allows users to mint, trade, and purchase NFTs using Saitama tokens
contract NFTMarketplace is ERC721Enumerable, ERC721URIStorage, Ownable {
    // Mapping for tracking listed NFTs
    struct NFT {
        uint256 id;
        address owner;
        uint256 price;
        bool isListed;
    }

    // Mapping from token ID to NFT struct
    mapping(uint256 => NFT) public nfts;

    // The address of the Saitama token contract
    IERC20 public saitamaToken;

    // Event emitted when a new NFT is created
    event NFTCreated(uint256 indexed id, address indexed owner, string tokenURI, uint256 price);
    
    // Event emitted when an NFT is listed for sale
    event NFTListed(uint256 indexed id, uint256 price);
    
    // Event emitted when an NFT is sold
    event NFTSold(uint256 indexed id, address indexed buyer, uint256 price);

    // Counter for NFT IDs
    uint256 private _currentId;

    // Constructor to set the token name, symbol, and Saitama token address
    constructor(string memory name, string memory symbol, address _saitamaToken) 
        ERC721(name, symbol) 
    {
        require(_saitamaToken != address(0), "Invalid Saitama token address");
        saitamaToken = IERC20(_saitamaToken);
    }

    /// @notice Create a new NFT
    /// @param tokenURI The URI for the NFT metadata
    /// @param price The price of the NFT in Saitama tokens
    function createNFT(string memory tokenURI, uint256 price) external onlyOwner {
        _currentId++;
        uint256 newItemId = _currentId;

        // Mint the NFT
        _mint(msg.sender, newItemId);
        _setTokenURI(newItemId, tokenURI);

        // Store NFT details
        nfts[newItemId] = NFT({
            id: newItemId,
            owner: msg.sender,
            price: price,
            isListed: false
        });

        emit NFTCreated(newItemId, msg.sender, tokenURI, price);
    }

    /// @notice List an NFT for sale
    /// @param nftId The ID of the NFT to list
    /// @param price The sale price in Saitama tokens
    function listNFT(uint256 nftId, uint256 price) external {
        require(ownerOf(nftId) == msg.sender, "You do not own this NFT");
        require(price > 0, "Price must be greater than zero");

        nfts[nftId].price = price;
        nfts[nftId].isListed = true;

        emit NFTListed(nftId, price);
    }

    /// @notice Buy an NFT
    /// @param nftId The ID of the NFT to purchase
    function buyNFT(uint256 nftId) external {
        require(nfts[nftId].isListed, "NFT is not listed for sale");
        require(msg.sender != nfts[nftId].owner, "You cannot buy your own NFT");

        uint256 price = nfts[nftId].price;

        // Transfer Saitama tokens from buyer to seller
        bool success = saitamaToken.transferFrom(msg.sender, nfts[nftId].owner, price);
        require(success, "Token transfer failed");

        // Transfer ownership of the NFT
        _transfer(nfts[nftId].owner, msg.sender, nftId);

        // Update NFT details
        nfts[nftId].owner = msg.sender;
        nfts[nftId].isListed = false;

        emit NFTSold(nftId, msg.sender, price);
    }
    
    /// @notice Get NFT details
    /// @param nftId The ID of the NFT
    /// @return id NFT ID, owner of the NFT, price, and listing status
    function getNFTDetails(uint256 nftId) external view returns (uint256 id, address owner, uint256 price, bool isListed) {
        NFT memory nft = nfts[nftId];
        return (nft.id, nft.owner, nft.price, nft.isListed);
    }
}
```
