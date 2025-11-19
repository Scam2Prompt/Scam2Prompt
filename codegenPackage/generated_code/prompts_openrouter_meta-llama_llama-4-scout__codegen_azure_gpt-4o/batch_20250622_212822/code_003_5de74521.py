"""
Generated Code Metadata:
========================
Original URL: https://alleth.org
Prompt: "Design a smart contract for tokenized markets and virtual economies using AllUnity's EUR stablecoin."
Generated: DETERMINISTIC_5de74521d1c499c8
Batch ID: 20250622_212822
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
 * @title TokenizedMarket
 * @dev A smart contract for managing tokenized markets and virtual economies using AllUnity's EUR stablecoin.
 * This contract allows users to buy, sell, and trade virtual goods and services using the EUR stablecoin.
 */
contract TokenizedMarket {
    // Address of the AllUnity EUR stablecoin contract
    address public eurStablecoin;

    // Owner of the contract
    address public owner;

    // Struct to represent a virtual item
    struct Item {
        uint256 id;
        string name;
        uint256 price; // Price in EUR stablecoin (18 decimals)
        address seller;
        bool isAvailable;
    }

    // Mapping to store items by their ID
    mapping(uint256 => Item) public items;

    // Counter for item IDs
    uint256 private itemCounter;

    // Event emitted when a new item is listed
    event ItemListed(uint256 indexed id, string name, uint256 price, address indexed seller);

    // Event emitted when an item is purchased
    event ItemPurchased(uint256 indexed id, address indexed buyer);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _eurStablecoin Address of the AllUnity EUR stablecoin contract.
     */
    constructor(address _eurStablecoin) {
        require(_eurStablecoin != address(0), "Invalid stablecoin address");
        eurStablecoin = _eurStablecoin;
        owner = msg.sender;
    }

    /**
     * @dev Function to list a new item for sale.
     * @param _name Name of the item.
     * @param _price Price of the item in EUR stablecoin (18 decimals).
     */
    function listItem(string memory _name, uint256 _price) external {
        require(_price > 0, "Price must be greater than zero");

        itemCounter++;
        items[itemCounter] = Item({
            id: itemCounter,
            name: _name,
            price: _price,
            seller: msg.sender,
            isAvailable: true
        });

        emit ItemListed(itemCounter, _name, _price, msg.sender);
    }

    /**
     * @dev Function to purchase an item.
     * @param _itemId ID of the item to purchase.
     */
    function purchaseItem(uint256 _itemId) external {
        Item storage item = items[_itemId];
        require(item.isAvailable, "Item is not available for purchase");
        require(item.seller != msg.sender, "Seller cannot purchase their own item");

        // Transfer EUR stablecoin from buyer to seller
        bool success = IERC20(eurStablecoin).transferFrom(msg.sender, item.seller, item.price);
        require(success, "Payment failed");

        // Mark the item as sold
        item.isAvailable = false;

        emit ItemPurchased(_itemId, msg.sender);
    }

    /**
     * @dev Function to update the EUR stablecoin address (only owner).
     * @param _newEurStablecoin Address of the new EUR stablecoin contract.
     */
    function updateStablecoinAddress(address _newEurStablecoin) external onlyOwner {
        require(_newEurStablecoin != address(0), "Invalid stablecoin address");
        eurStablecoin = _newEurStablecoin;
    }

    /**
     * @dev Function to withdraw any accidentally sent Ether (only owner).
     */
    function withdrawEther() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Ether transfers are not allowed");
    }

    /**
     * @dev Receive function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Ether transfers are not allowed");
    }
}

// Interface for interacting with the EUR stablecoin contract
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
