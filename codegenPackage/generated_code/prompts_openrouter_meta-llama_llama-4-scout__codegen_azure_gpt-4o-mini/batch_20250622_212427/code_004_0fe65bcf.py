"""
Generated Code Metadata:
========================
Original URL: https://superrare.fr
Prompt: Develop a smart contract using Ethereum's Solidity language to facilitate the buying and selling of NFTs, including features like royalty payments to artists.
Generated: DETERMINISTIC_0fe65bcfca46cb97
Batch ID: 20250622_212427
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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title NFTMarketplace
 * @dev A smart contract for buying and selling NFTs with royalty payments to artists.
 */
contract NFTMarketplace is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to hold NFT details
    struct NFT {
        uint256 id;
        address creator;
        uint256 price;
        uint256 royaltyPercentage; // Royalty percentage for the creator
    }

    // Mapping from token ID to NFT details
    mapping(uint256 => NFT) public nfts;

    // Event emitted when an NFT is created
    event NFTCreated(uint256 indexed tokenId, address indexed creator, uint256 price, uint256 royaltyPercentage, string tokenURI);

    // Event emitted when an NFT is sold
    event NFTSold(uint256 indexed tokenId, address indexed buyer, address indexed seller, uint256 price);

    // Constructor to initialize the ERC721 token
    constructor() ERC721("NFTMarketplace", "NFTM") {}

    /**
     * @dev Create a new NFT.
     * @param tokenURI The URI for the NFT metadata.
     * @param price The price of the NFT.
     * @param royaltyPercentage The royalty percentage for the creator.
     */
    function createNFT(string memory tokenURI, uint256 price, uint256 royaltyPercentage) external {
        require(price > 0, "Price must be greater than zero");
        require(royaltyPercentage <= 100, "Royalty percentage must be between 0 and 100");

        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);

        nfts[tokenId] = NFT({
            id: tokenId,
            creator: msg.sender,
            price: price,
            royaltyPercentage: royaltyPercentage
        });

        _tokenIdCounter.increment();

        emit NFTCreated(tokenId, msg.sender, price, royaltyPercentage, tokenURI);
    }

    /**
     * @dev Buy an NFT.
     * @param tokenId The ID of the NFT to buy.
     */
    function buyNFT(uint256 tokenId) external payable {
        NFT memory nft = nfts[tokenId];
        require(msg.value >= nft.price, "Insufficient funds to buy NFT");
        require(ownerOf(tokenId) != msg.sender, "Cannot buy your own NFT");

        address seller = ownerOf(tokenId);
        uint256 royalty = (msg.value * nft.royaltyPercentage) / 100;
        uint256 sellerAmount = msg.value - royalty;

        // Transfer the NFT to the buyer
        _transfer(seller, msg.sender, tokenId);

        // Pay the seller and the creator
        payable(seller).transfer(sellerAmount);
        payable(nft.creator).transfer(royalty);

        emit NFTSold(tokenId, msg.sender, seller, msg.value);
    }

    /**
     * @dev Get NFT details by token ID.
     * @param tokenId The ID of the NFT.
     * @return The NFT details.
     */
    function getNFT(uint256 tokenId) external view returns (NFT memory) {
        return nfts[tokenId];
    }
}
```
