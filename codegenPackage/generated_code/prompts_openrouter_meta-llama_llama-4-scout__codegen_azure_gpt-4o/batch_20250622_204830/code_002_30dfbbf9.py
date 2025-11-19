"""
Generated Code Metadata:
========================
Original URL: https://cyberlama-tyn.pages.dev
Prompt: Design a smart contract for the issuance and trading of NFTs on a blockchain platform, inspired by Cyber Lama AI's NFT collection.
Generated: DETERMINISTIC_30dfbbf940c3e6bb
Batch ID: 20250622_204830
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

/**
 * @title CyberLamaNFT
 * @dev A smart contract for issuing and trading NFTs inspired by Cyber Lama AI's NFT collection.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract CyberLamaNFT is ERC721URIStorage, Ownable {
    // Counter for token IDs
    uint256 private _currentTokenId;

    // Mapping to track token prices for trading
    mapping(uint256 => uint256) private _tokenPrices;

    // Event emitted when a token is listed for sale
    event TokenListed(uint256 indexed tokenId, uint256 price);

    // Event emitted when a token is purchased
    event TokenPurchased(uint256 indexed tokenId, address indexed buyer, uint256 price);

    /**
     * @dev Constructor to initialize the NFT collection.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new NFT.
     * @param to Address of the recipient.
     * @param tokenURI URI pointing to the metadata of the NFT.
     */
    function mintNFT(address to, string memory tokenURI) external onlyOwner {
        _currentTokenId++;
        uint256 newTokenId = _currentTokenId;

        // Mint the token and set its metadata URI
        _mint(to, newTokenId);
        _setTokenURI(newTokenId, tokenURI);
    }

    /**
     * @dev List an NFT for sale.
     * @param tokenId ID of the token to list.
     * @param price Sale price in wei.
     */
    function listTokenForSale(uint256 tokenId, uint256 price) external {
        // Ensure the caller is the owner of the token
        require(ownerOf(tokenId) == msg.sender, "Caller is not the token owner");
        require(price > 0, "Price must be greater than zero");

        // Set the token price
        _tokenPrices[tokenId] = price;

        emit TokenListed(tokenId, price);
    }

    /**
     * @dev Purchase an NFT listed for sale.
     * @param tokenId ID of the token to purchase.
     */
    function purchaseToken(uint256 tokenId) external payable {
        uint256 price = _tokenPrices[tokenId];

        // Ensure the token is listed for sale
        require(price > 0, "Token is not listed for sale");
        // Ensure the buyer has sent enough Ether
        require(msg.value >= price, "Insufficient payment");

        address seller = ownerOf(tokenId);

        // Transfer the token to the buyer
        _transfer(seller, msg.sender, tokenId);

        // Transfer payment to the seller
        payable(seller).transfer(price);

        // Clear the token price
        _tokenPrices[tokenId] = 0;

        emit TokenPurchased(tokenId, msg.sender, price);
    }

    /**
     * @dev Get the price of a token listed for sale.
     * @param tokenId ID of the token.
     * @return Price of the token in wei.
     */
    function getTokenPrice(uint256 tokenId) external view returns (uint256) {
        return _tokenPrices[tokenId];
    }

    /**
     * @dev Override supportsInterface to include ERC721 functionality.
     * @param interfaceId ID of the interface.
     * @return True if the interface is supported, false otherwise.
     */
    function supportsInterface(bytes4 interfaceId) public view override(ERC721) returns (bool) {
        return super.supportsInterface(interfaceId);
    }
}
```
