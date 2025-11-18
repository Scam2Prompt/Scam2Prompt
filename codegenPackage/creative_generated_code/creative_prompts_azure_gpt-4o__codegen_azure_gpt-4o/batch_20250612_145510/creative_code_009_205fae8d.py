"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pantherappai.pages.dev
Prompt: Develop a smart contract for PantherAI's NFT marketplace that allows users to mint, buy, and sell NFTs. Include functionality for linking NFTs to PantherAI tokens for rewards.
Generated: DETERMINISTIC_205fae8d1b6d9426
Batch ID: 20250612_145510
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
 * @title PantherAINFTMarketplace
 * @dev A smart contract for minting, buying, selling NFTs, and linking NFTs with PantherAI tokens for rewards.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

interface IPantherAIToken {
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract PantherAINFTMarketplace is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;

    // Auto-incrementing ID for NFTs
    Counters.Counter private _tokenIds;

    // Struct to represent an NFT sale listing
    struct NFTSale {
        uint256 price;
        address seller;
    }

    // Mapping from token ID to sale data
    mapping(uint256 => NFTSale) public nftSales;

    // PantherAI token for reward distribution
    IPantherAIToken public pantherAIToken;

    // Event emitted when an NFT is minted
    event NFTMinted(uint256 tokenId, address owner, string tokenURI);

    // Event emitted when an NFT is put on sale
    event NFTListed(uint256 tokenId, uint256 price, address seller);

    // Event emitted when an NFT is bought
    event NFTPurchased(uint256 tokenId, address buyer, uint256 price);

    /**
     * @dev Constructor to set the name, symbol, and PantherAI token address.
     * @param _tokenAddress Address of the PantherAI token contract.
     */
    constructor(address _tokenAddress) ERC721("PantherAINFT", "PAI") {
        require(_tokenAddress != address(0), "Invalid token address");
        pantherAIToken = IPantherAIToken(_tokenAddress);
    }

    /**
     * @dev Mint a new NFT.
     * @param tokenURI URI of the NFT metadata.
     * @return tokenId The ID of the newly minted NFT.
     */
    function mintNFT(string memory tokenURI) external returns (uint256 tokenId) {
        _tokenIds.increment();
        tokenId = _tokenIds.current();

        _mint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);

        emit NFTMinted(tokenId, msg.sender, tokenURI);
    }

    /**
     * @dev List an NFT for sale.
     * @param tokenId ID of the NFT to list.
     * @param price Sale price in wei.
     */
    function listNFT(uint256 tokenId, uint256 price) external {
        require(ownerOf(tokenId) == msg.sender, "Caller is not the owner");
        require(price > 0, "Price must be greater than zero");

        nftSales[tokenId] = NFTSale({
            price: price,
            seller: msg.sender
        });

        emit NFTListed(tokenId, price, msg.sender);
    }

    /**
     * @dev Buy an NFT from the marketplace.
     * @param tokenId ID of the NFT to buy.
     */
    function buyNFT(uint256 tokenId) external payable {
        NFTSale memory sale = nftSales[tokenId];
        require(sale.price > 0, "NFT not listed for sale");
        require(msg.value == sale.price, "Incorrect payment amount");

        address seller = sale.seller;
        delete nftSales[tokenId];

        _transfer(seller, msg.sender, tokenId);
        payable(seller).transfer(msg.value);

        emit NFTPurchased(tokenId, msg.sender, sale.price);

        // Reward buyer with PantherAI tokens (example: 10 PantherAI tokens per NFT purchase)
        uint256 rewardAmount = 10 * 10**18; // Assuming PantherAI tokens have 18 decimals
        require(pantherAIToken.transfer(msg.sender, rewardAmount), "Token reward transfer failed");
    }

    /**
     * @dev Remove an NFT from the marketplace.
     * @param tokenId ID of the NFT to remove.
     */
    function removeNFTFromSale(uint256 tokenId) external {
        require(nftSales[tokenId].seller == msg.sender, "Caller is not the seller");
        delete nftSales[tokenId];
    }

    /**
     * @dev Update the PantherAI token contract address.
     * @param _tokenAddress New token address.
     */
    function updateTokenAddress(address _tokenAddress) external onlyOwner {
        require(_tokenAddress != address(0), "Invalid token address");
        pantherAIToken = IPantherAIToken(_tokenAddress);
    }
}
```
