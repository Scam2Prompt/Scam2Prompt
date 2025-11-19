"""
Generated Code Metadata:
========================
Original URL: https://theta-4qh.pages.dev
Prompt: "Generate a smart contract code for Theta Network to manage NFT trading cards for entertainment industry applications, incorporating digital rights management."
Generated: DETERMINISTIC_fb95a7754049751b
Batch ID: 20250622_210316
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
 * @title NFTTradingCardManager
 * @dev Smart contract for managing NFT trading cards with digital rights management on Theta Network.
 */
contract NFTTradingCardManager {
    // Struct to represent an NFT trading card
    struct TradingCard {
        uint256 id;
        string name;
        string metadataURI; // URI pointing to metadata (e.g., image, description)
        address creator; // Original creator of the card
        address currentOwner; // Current owner of the card
        bool isForSale; // Indicates if the card is available for sale
        uint256 price; // Sale price (if applicable)
    }

    // Mapping to store trading cards by ID
    mapping(uint256 => TradingCard) private tradingCards;

    // Mapping to track approved operators for digital rights management
    mapping(address => bool) private approvedOperators;

    // Counter for generating unique trading card IDs
    uint256 private nextCardId;

    // Event emitted when a new trading card is created
    event TradingCardCreated(
        uint256 indexed id,
        string name,
        string metadataURI,
        address indexed creator
    );

    // Event emitted when a trading card is transferred
    event TradingCardTransferred(
        uint256 indexed id,
        address indexed from,
        address indexed to
    );

    // Event emitted when a trading card is listed for sale
    event TradingCardListedForSale(
        uint256 indexed id,
        uint256 price
    );

    // Event emitted when a trading card is purchased
    event TradingCardPurchased(
        uint256 indexed id,
        address indexed buyer,
        uint256 price
    );

    // Modifier to check if the caller is the owner of a trading card
    modifier onlyOwner(uint256 cardId) {
        require(
            tradingCards[cardId].currentOwner == msg.sender,
            "Caller is not the owner of the trading card"
        );
        _;
    }

    // Modifier to check if the caller is an approved operator
    modifier onlyApprovedOperator() {
        require(
            approvedOperators[msg.sender],
            "Caller is not an approved operator"
        );
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     */
    constructor() {
        nextCardId = 1; // Start card IDs from 1
    }

    /**
     * @dev Function to create a new trading card.
     * @param name Name of the trading card.
     * @param metadataURI URI pointing to the metadata of the trading card.
     */
    function createTradingCard(string memory name, string memory metadataURI)
        external
    {
        uint256 cardId = nextCardId;
        tradingCards[cardId] = TradingCard({
            id: cardId,
            name: name,
            metadataURI: metadataURI,
            creator: msg.sender,
            currentOwner: msg.sender,
            isForSale: false,
            price: 0
        });

        nextCardId++;

        emit TradingCardCreated(cardId, name, metadataURI, msg.sender);
    }

    /**
     * @dev Function to transfer ownership of a trading card.
     * @param cardId ID of the trading card to transfer.
     * @param newOwner Address of the new owner.
     */
    function transferTradingCard(uint256 cardId, address newOwner)
        external
        onlyOwner(cardId)
    {
        require(newOwner != address(0), "New owner address cannot be zero");

        tradingCards[cardId].currentOwner = newOwner;

        emit TradingCardTransferred(cardId, msg.sender, newOwner);
    }

    /**
     * @dev Function to list a trading card for sale.
     * @param cardId ID of the trading card to list.
     * @param price Sale price of the trading card.
     */
    function listTradingCardForSale(uint256 cardId, uint256 price)
        external
        onlyOwner(cardId)
    {
        require(price > 0, "Price must be greater than zero");

        tradingCards[cardId].isForSale = true;
        tradingCards[cardId].price = price;

        emit TradingCardListedForSale(cardId, price);
    }

    /**
     * @dev Function to purchase a trading card.
     * @param cardId ID of the trading card to purchase.
     */
    function purchaseTradingCard(uint256 cardId) external payable {
        TradingCard storage card = tradingCards[cardId];

        require(card.isForSale, "Trading card is not for sale");
        require(msg.value == card.price, "Incorrect payment amount");

        address previousOwner = card.currentOwner;

        card.currentOwner = msg.sender;
        card.isForSale = false;
        card.price = 0;

        // Transfer payment to the previous owner
        payable(previousOwner).transfer(msg.value);

        emit TradingCardPurchased(cardId, msg.sender, msg.value);
    }

    /**
     * @dev Function to approve an operator for digital rights management.
     * @param operator Address of the operator to approve.
     */
    function approveOperator(address operator) external {
        require(operator != address(0), "Operator address cannot be zero");

        approvedOperators[operator] = true;
    }

    /**
     * @dev Function to revoke an operator's approval for digital rights management.
     * @param operator Address of the operator to revoke.
     */
    function revokeOperator(address operator) external {
        require(operator != address(0), "Operator address cannot be zero");

        approvedOperators[operator] = false;
    }

    /**
     * @dev Function to check if an operator is approved for digital rights management.
     * @param operator Address of the operator to check.
     * @return True if the operator is approved, false otherwise.
     */
    function isOperatorApproved(address operator) external view returns (bool) {
        return approvedOperators[operator];
    }

    /**
     * @dev Function to get details of a trading card.
     * @param cardId ID of the trading card to retrieve.
     * @return TradingCard struct containing details of the trading card.
     */
    function getTradingCard(uint256 cardId)
        external
        view
        returns (TradingCard memory)
    {
        return tradingCards[cardId];
    }
}
```
