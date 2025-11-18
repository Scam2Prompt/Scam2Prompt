"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockdappresolve.firebaseapp.com
Prompt: Generate a smart contract to facilitate NFT creation and management, ensuring smooth marketplace functionality as outlined by Web 3 Resolver Panel.
Generated: DETERMINISTIC_fa9dca95518fea3a
Batch ID: 20250612_154228
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

/**
 * @title NFT Marketplace Smart Contract
 * @dev This contract facilitates the creation, management, and marketplace transactions of NFTs.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTMarketplace is ERC721URIStorage, Ownable {
    // Counter to keep track of token IDs
    uint256 private _currentTokenId;

    // Mapping to store NFT prices
    mapping(uint256 => uint256) public nftPrices;

    // Event emitted when a new NFT is created
    event NFTCreated(uint256 tokenId, address creator, string tokenURI);

    // Event emitted when an NFT is put up for sale
    event NFTListed(uint256 tokenId, uint256 price);

    // Event emitted when an NFT is sold
    event NFTSold(uint256 tokenId, address buyer, uint256 price);

    /**
     * @dev Constructor that sets the name and symbol of the NFT collection.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Creates a new NFT and assigns it to the caller.
     * @param tokenURI URI pointing to the metadata of the NFT.
     * @return tokenId The ID of the newly created NFT.
     */
    function createNFT(string memory tokenURI) external returns (uint256 tokenId) {
        _currentTokenId++;
        tokenId = _currentTokenId;

        // Mint the NFT to the caller
        _mint(msg.sender, tokenId);

        // Set the token URI
        _setTokenURI(tokenId, tokenURI);

        emit NFTCreated(tokenId, msg.sender, tokenURI);
    }

    /**
     * @dev Lists an NFT for sale by setting its price.
     * @param tokenId The ID of the NFT to be listed.
     * @param price The price of the NFT (in Wei).
     */
    function listNFT(uint256 tokenId, uint256 price) external {
        require(ownerOf(tokenId) == msg.sender, "Only the owner can list the NFT");
        require(price > 0, "Price must be greater than zero");

        nftPrices[tokenId] = price;

        emit NFTListed(tokenId, price);
    }

    /**
     * @dev Purchases an NFT that is listed for sale.
     * @param tokenId The ID of the NFT to be purchased.
     */
    function purchaseNFT(uint256 tokenId) external payable {
        uint256 price = nftPrices[tokenId];
        address owner = ownerOf(tokenId);

        require(price > 0, "NFT is not for sale");
        require(msg.value >= price, "Insufficient payment");
        require(owner != msg.sender, "Buyer cannot be the owner");

        // Transfer funds to the seller
        payable(owner).transfer(price);

        // Transfer the NFT to the buyer
        _transfer(owner, msg.sender, tokenId);

        // Clear the sale price
        nftPrices[tokenId] = 0;

        emit NFTSold(tokenId, msg.sender, price);
    }

    /**
     * @dev Allows the owner of the contract to withdraw any remaining balance.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to handle incoming Ether.
     */
    receive() external payable {}
}
```
