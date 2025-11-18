"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jamcards.io
Prompt: Using the Ethereum blockchain, write a Solidity smart contract to enable users to buy and sell NFTs from the "Heart Full of Love JamCards" collection.
Generated: DETERMINISTIC_8aa3f123ac56b9dd
Batch ID: 20250612_150034
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

// Importing OpenZeppelin ERC721 library for NFT functionality
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title HeartFullOfLoveJamCards
 * @dev This contract allows users to buy and sell NFTs from the Heart Full of Love JamCards collection.
 */
contract HeartFullOfLoveJamCards is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Struct for NFT metadata
    struct JamCard {
        string name;
        string artist;
        uint256 price;
        bool isForSale;
    }

    // Mapping from token ID to JamCard metadata
    mapping(uint256 => JamCard) private jamCards;
    // Counter for current token ID
    Counters.Counter private _tokenIdCounter;

    // Event emitted when a new NFT is created
    event JamCardCreated(uint256 indexed tokenId, string name, string artist, uint256 price);
    // Event emitted when an NFT is listed for sale
    event JamCardListed(uint256 indexed tokenId, uint256 price);
    // Event emitted when an NFT is sold
    event JamCardSold(uint256 indexed tokenId, address buyer);

    /**
     * @dev Constructor to set the name and symbol of the NFT collection.
     */
    constructor() ERC721("Heart Full of Love JamCards", "HFOLJC") {}

    /**
     * @dev Function to create a new Jam Card NFT.
     * @param name The name of the Jam Card.
     * @param artist The artist of the Jam Card.
     * @param price The sale price of the Jam Card.
     */
    function createJamCard(string memory name, string memory artist, uint256 price) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        jamCards[tokenId] = JamCard(name, artist, price, false);
        _safeMint(msg.sender, tokenId);
        _tokenIdCounter.increment();

        emit JamCardCreated(tokenId, name, artist, price);
    }

    /**
     * @dev Function to list a Jam Card NFT for sale.
     * @param tokenId The ID of the Jam Card to list.
     * @param price The sale price of the Jam Card.
     */
    function listJamCardForSale(uint256 tokenId, uint256 price) external {
        require(ownerOf(tokenId) == msg.sender, "You are not the owner of this NFT");
        require(price > 0, "Price must be greater than zero");

        jamCards[tokenId].price = price;
        jamCards[tokenId].isForSale = true;

        emit JamCardListed(tokenId, price);
    }

    /**
     * @dev Function to buy a Jam Card NFT listed for sale.
     * @param tokenId The ID of the Jam Card to purchase.
     */
    function buyJamCard(uint256 tokenId) external payable {
        JamCard memory jamCard = jamCards[tokenId];
        
        require(jamCard.isForSale, "This NFT is not for sale");
        require(msg.value >= jamCard.price, "Insufficient funds sent");

        address seller = ownerOf(tokenId);

        // Transfer the NFT to the buyer
        _transfer(seller, msg.sender, tokenId);
        // Transfer the payment to the seller
        payable(seller).transfer(msg.value);

        // Mark the NFT as not for sale
        jamCards[tokenId].isForSale = false;

        emit JamCardSold(tokenId, msg.sender);
    }

    /**
     * @dev Function to get details of a specific Jam Card NFT.
     * @param tokenId The ID of the Jam Card to retrieve.
     * @return name The name of the Jam Card.
     * @return artist The artist of the Jam Card.
     * @return price The price of the Jam Card.
     * @return isForSale Whether the Jam Card is for sale.
     */
    function getJamCard(uint256 tokenId) external view returns (string memory name, string memory artist, uint256 price, bool isForSale) {
        JamCard memory jamCard = jamCards[tokenId];
        return (jamCard.name, jamCard.artist, jamCard.price, jamCard.isForSale);
    }
}
```
