"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dev--ethereumorg.netlify.app
Prompt: Generate code for a dApp that allows users to mint and trade NFTs, following the standards described on Ethereum.org.
Generated: DETERMINISTIC_3b659a1e2b630c6a
Batch ID: 20250612_151948
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title NFTMintAndTrade
 * @dev A decentralized application (dApp) for minting and trading NFTs following ERC721 standards.
 */

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract NFTMintAndTrade is ERC721URIStorage, Ownable, ReentrancyGuard {
    // Counter to track NFT IDs
    uint256 private _tokenIdCounter;

    // Mapping to store listed NFTs and their prices
    mapping(uint256 => uint256) public listedNFTs;

    // Event emitted when an NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId, string tokenURI);

    // Event emitted when an NFT is listed for sale
    event NFTListed(uint256 indexed tokenId, uint256 price);

    // Event emitted when an NFT is purchased
    event NFTSold(address indexed buyer, uint256 indexed tokenId, uint256 price);

    constructor() ERC721("NFTMintAndTrade", "NMT") {}

    /**
     * @dev Allows the owner to mint a new NFT.
     * @param to The address to receive the minted NFT.
     * @param tokenURI The URI pointing to the metadata of the NFT.
     */
    function mintNFT(address to, string memory tokenURI) external onlyOwner {
        _tokenIdCounter++;
        uint256 newTokenId = _tokenIdCounter;

        _mint(to, newTokenId);
        _setTokenURI(newTokenId, tokenURI);

        emit NFTMinted(to, newTokenId, tokenURI);
    }

    /**
     * @dev Lists an NFT for sale at a specified price.
     * @param tokenId The ID of the NFT to be listed.
     * @param price The price to list the NFT for.
     */
    function listNFT(uint256 tokenId, uint256 price) external {
        require(ownerOf(tokenId) == msg.sender, "Caller is not the owner of the NFT");
        require(price > 0, "Price must be greater than zero");

        listedNFTs[tokenId] = price;

        emit NFTListed(tokenId, price);
    }

    /**
     * @dev Allows anyone to purchase a listed NFT.
     * @param tokenId The ID of the NFT to purchase.
     */
    function purchaseNFT(uint256 tokenId) external payable nonReentrant {
        uint256 price = listedNFTs[tokenId];
        require(price > 0, "NFT is not listed for sale");
        require(msg.value >= price, "Insufficient payment");

        address seller = ownerOf(tokenId);

        // Transfer the NFT to the buyer
        _transfer(seller, msg.sender, tokenId);

        // Transfer funds to the seller
        payable(seller).transfer(price);

        // Refund excess payment (if any)
        if (msg.value > price) {
            payable(msg.sender).transfer(msg.value - price);
        }

        // Remove the NFT from listings
        listedNFTs[tokenId] = 0;

        emit NFTSold(msg.sender, tokenId, price);
    }

    /**
     * @dev Withdraw contract balance to owner's address.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to reject direct payments.
     */
    receive() external payable {
        revert("Direct payments are not accepted");
    }
}
```
