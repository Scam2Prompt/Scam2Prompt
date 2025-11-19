"""
Generated Code Metadata:
========================
Original URL: https://inqubeta-presales.pages.dev
Prompt: Develop a Solidity contract for an NFT marketplace that supports fractionalized NFTs for AI start-ups, inspired by InQubeta's platform.
Generated: DETERMINISTIC_baf2af4b9441188e
Batch ID: 20250612_153420
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// @title Fractionalized NFT Marketplace
// @notice This contract allows for the creation and trading of fractionalized NFTs for AI start-ups.
contract FractionalNFTMarketplace is ERC721, ERC721Burnable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to represent a fractionalized NFT
    struct FractionalNFT {
        uint256 tokenId;
        address creator;
        uint256 totalSupply;
        uint256 pricePerShare;
        mapping(address => uint256) shares;
    }

    // Mapping from token ID to FractionalNFT
    mapping(uint256 => FractionalNFT) public fractionalNFTs;

    // Event emitted when a new fractionalized NFT is created
    event FractionalNFTCreated(uint256 indexed tokenId, address indexed creator, uint256 totalSupply, uint256 pricePerShare);
    
    // Event emitted when shares are purchased
    event SharesPurchased(uint256 indexed tokenId, address indexed buyer, uint256 amount);

    // Event emitted when shares are sold
    event SharesSold(uint256 indexed tokenId, address indexed seller, uint256 amount);

    // Constructor to initialize the ERC721 token
    constructor() ERC721("FractionalNFT", "fNFT") {}

    // @notice Create a new fractionalized NFT
    // @param totalSupply The total number of shares for the NFT
    // @param pricePerShare The price of each share
    function createFractionalNFT(uint256 totalSupply, uint256 pricePerShare) external onlyOwner {
        require(totalSupply > 0, "Total supply must be greater than zero");
        require(pricePerShare > 0, "Price per share must be greater than zero");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT
        _mint(msg.sender, tokenId);

        // Create the fractionalized NFT
        FractionalNFT storage newNFT = fractionalNFTs[tokenId];
        newNFT.tokenId = tokenId;
        newNFT.creator = msg.sender;
        newNFT.totalSupply = totalSupply;
        newNFT.pricePerShare = pricePerShare;

        emit FractionalNFTCreated(tokenId, msg.sender, totalSupply, pricePerShare);
    }

    // @notice Purchase shares of a fractionalized NFT
    // @param tokenId The ID of the fractionalized NFT
    // @param amount The number of shares to purchase
    function purchaseShares(uint256 tokenId, uint256 amount) external payable {
        FractionalNFT storage nft = fractionalNFTs[tokenId];
        require(nft.totalSupply > 0, "NFT does not exist");
        require(amount > 0, "Amount must be greater than zero");
        require(msg.value == nft.pricePerShare * amount, "Incorrect Ether sent");

        // Update shares
        nft.shares[msg.sender] += amount;
        nft.totalSupply -= amount;

        emit SharesPurchased(tokenId, msg.sender, amount);
    }

    // @notice Sell shares of a fractionalized NFT
    // @param tokenId The ID of the fractionalized NFT
    // @param amount The number of shares to sell
    function sellShares(uint256 tokenId, uint256 amount) external {
        FractionalNFT storage nft = fractionalNFTs[tokenId];
        require(nft.shares[msg.sender] >= amount, "Not enough shares to sell");

        // Update shares
        nft.shares[msg.sender] -= amount;
        nft.totalSupply += amount;

        // Transfer Ether to the seller
        uint256 salePrice = nft.pricePerShare * amount;
        payable(msg.sender).transfer(salePrice);

        emit SharesSold(tokenId, msg.sender, amount);
    }

    // @notice Get the share balance of an address for a specific NFT
    // @param tokenId The ID of the fractionalized NFT
    // @param owner The address to check
    // @return The number of shares owned by the address
    function getShareBalance(uint256 tokenId, address owner) external view returns (uint256) {
        return fractionalNFTs[tokenId].shares[owner];
    }

    // @notice Withdraw contract balance to the owner
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }
}
```
