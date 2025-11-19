"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nakamigos-c4d.pages.dev
Prompt: Explain how to implement a blockchain-based solution for trading Nakamigos cards, referencing the commercial rights and unique features highlighted on the Nakamigos site.
Generated: DETERMINISTIC_4e8c762e1e803c5e
Batch ID: 20250612_155956
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Blockchain-based Nakamigos Trading Platform

This script implements a blockchain-based solution for trading Nakamigos cards. Each card is represented
as a digital asset (ERC-721 NFT standard). The solution allows users to list, buy, and trade cards. It includes 
commercial rights management and ensures immutability of card features.

Key Features:
- Card metadata includes unique features as highlighted on the Nakamigos site.
- Users can transfer ownership of cards, respecting commercial rights.
- Solidity smart contract on Ethereum blockchain.

Note: This code is for educational purposes and should be tested and audited before production deployment.
"""

# SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/** 
 * @title NakamigosCardTrading
 * @dev ERC-721 NFT Smart Contract for Nakamigos card trading platform
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NakamigosCardTrading is ERC721, Ownable {
    // Mapping to store metadata for each card
    mapping(uint256 => string) public cardFeatures;

    // Event emitted when a card is listed for sale
    event CardListed(uint256 tokenId, address seller, uint256 price);

    // Event emitted when a card is successfully bought
    event CardSold(uint256 tokenId, address buyer, uint256 price);

    // Struct to store sale details
    struct SaleDetails {
        address seller;
        uint256 price;
        bool isListed;
    }

    // Mapping for token ID to sale details
    mapping(uint256 => SaleDetails) public sales;

    // Constructor to set the name and symbol of the NFT collection
    constructor() ERC721("Nakamigos Cards", "NAKA") {}

    /** 
     * @dev Mint a new card with unique features
     * @param _to Address to mint the card to
     * @param _tokenId The unique ID of the card
     * @param _features Metadata of the card's unique features
     */
    function mintCard(address _to, uint256 _tokenId, string memory _features) external onlyOwner {
        _mint(_to, _tokenId);
        cardFeatures[_tokenId] = _features; // Store unique features
    }

    /** 
     * @dev List a card for sale
     * @param _tokenId Token ID of the card to list
     * @param _price Price of the card in wei
     */
    function listCard(uint256 _tokenId, uint256 _price) external {
        require(ownerOf(_tokenId) == msg.sender, "Caller is not the card owner");
        require(_price > 0, "Price must be greater than zero");

        sales[_tokenId] = SaleDetails({
            seller: msg.sender,
            price: _price,
            isListed: true
        });

        emit CardListed(_tokenId, msg.sender, _price);
    }

    /**
     * @dev Buy a card that is listed for sale
     * @param _tokenId Token ID of the card to buy
     */
    function buyCard(uint256 _tokenId) external payable {
        SaleDetails memory sale = sales[_tokenId];
        require(sale.isListed, "Card is not listed for sale");
        require(msg.value == sale.price, "Incorrect payment amount");

        // Transfer funds to the seller
        (bool success, ) = sale.seller.call{value: msg.value}("");
        require(success, "Payment transfer failed");

        // Transfer ownership of the card
        _transfer(sale.seller, msg.sender, _tokenId);

        // Remove sale details
        delete sales[_tokenId];

        emit CardSold(_tokenId, msg.sender, sale.price);
    }

    /** 
     * @dev Retrieve metadata of a card by token ID
     * @param _tokenId Token ID of the card
     * @return Metadata of the card's unique features
     */
    function getCardFeatures(uint256 _tokenId) external view returns (string memory) {
        return cardFeatures[_tokenId];
    }

    /**
     * @dev Override to ensure a card cannot be transferred while listed for sale
     * @param from Address transferring the card
     * @param to Address receiving the card
     * @param tokenId Token ID being transferred
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override {
        require(!sales[tokenId].isListed, "Card cannot be transferred while listed for sale");
        super._beforeTokenTransfer(from, to, tokenId);
    }

    /**
     * @dev Fallback function to handle incorrect Ether transfers.
     */
    fallback() external payable {
        revert("Invalid transaction");
    }

    /**
     * @dev Receive function to accept Ether directly into the contract.
     */
    receive() external payable {
        revert("Direct Ether transfer not allowed");
    }
}
```
