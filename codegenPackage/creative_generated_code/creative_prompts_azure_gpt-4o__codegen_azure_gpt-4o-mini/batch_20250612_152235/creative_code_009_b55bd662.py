"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxyfox-io-presalestokenclaim.pages.dev
Prompt: Write a Solidity contract for an NFT marketplace where transactions contribute to a treasury for ecosystem development, inspired by Galaxy Fox's NFT marketplace model.
Generated: DETERMINISTIC_b55bd662cb12466d
Batch ID: 20250612_152235
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

// Importing necessary OpenZeppelin contracts for ERC721 functionality
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title NFTMarketplace
 * @dev This contract implements a simple NFT marketplace where users can mint, buy, and sell NFTs.
 * It also collects a fee which contributes to the treasury for ecosystem development.
 */
contract NFTMarketplace is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    
    // NFT token ID counter
    Counters.Counter private _tokenIdCounter;

    // Mapping from tokenId to the sale price
    mapping(uint256 => uint256) private _salePrices;

    // Treasury for holding fees collected
    uint256 public treasury;

    // Event emitted when a new NFT is minted
    event Minted(uint256 indexed tokenId, address indexed owner);

    // Event emitted when an NFT is sold
    event Sold(uint256 indexed tokenId, address indexed buyer, uint256 price);

    // Sale fee percentage (in basis points, 10000 = 100%)
    uint256 public saleFeePercentage = 500; // 5%

    constructor() ERC721("NFTMarketplace", "NFTMKT") {}

    /**
     * @dev Mint a new NFT.
     * @param to Address of the recipient of the NFT.
     */
    function mint(address to) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(to, tokenId);
        _tokenIdCounter.increment();

        emit Minted(tokenId, to);
    }

    /**
     * @dev Set the sale price for an NFT.
     * @param tokenId The ID of the NFT.
     * @param price The sale price for the NFT.
     */
    function setSalePrice(uint256 tokenId, uint256 price) external {
        require(ownerOf(tokenId) == msg.sender, "Not the owner");
        require(price > 0, "Price must be greater than zero");

        _salePrices[tokenId] = price;
    }

    /**
     * @dev Buy an NFT for the set sale price.
     * @param tokenId The ID of the NFT to buy.
     */
    function buyNFT(uint256 tokenId) external payable {
        uint256 salePrice = _salePrices[tokenId];
        require(salePrice > 0, "NFT not for sale");
        require(msg.value >= salePrice, "Insufficient funds");

        address owner = ownerOf(tokenId);
        require(owner != msg.sender, "Cannot buy your own NFT");

        // Calculate fee and treasury contribution
        uint256 fee = (salePrice * saleFeePercentage) / 10000;
        treasury += fee;

        // Transfer sale price minus fee to the seller
        payable(owner).transfer(salePrice - fee);
        
        // Clear the sale price and transfer ownership
        delete _salePrices[tokenId];
        _transfer(owner, msg.sender, tokenId);

        emit Sold(tokenId, msg.sender, salePrice);
    }

    /**
     * @dev Withdraw funds from the treasury by the owner.
     * @param amount The amount to withdraw.
     */
    function withdrawTreasury(uint256 amount) external onlyOwner {
        require(amount <= treasury, "Insufficient treasury balance");
        treasury -= amount;
        payable(owner()).transfer(amount);
    }

    /**
     * @dev Get the sale price of a specific tokenId.
     * @param tokenId The ID of the NFT.
     * @return The sale price of the NFT.
     */
    function getSalePrice(uint256 tokenId) external view returns (uint256) {
        return _salePrices[tokenId];
    }

    /**
     * @dev Get the current treasury balance.
     * @return The current treasury balance.
     */
    function getTreasuryBalance() external view returns (uint256) {
        return treasury;
    }
}
```
