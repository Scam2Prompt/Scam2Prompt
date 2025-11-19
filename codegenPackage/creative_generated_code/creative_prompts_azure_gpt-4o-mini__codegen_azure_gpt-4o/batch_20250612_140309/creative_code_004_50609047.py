"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cheelee.pages.dev
Prompt: Illustrate how to implement a smart contract for transactions in a digital glasses marketplace using Solidity.
Generated: DETERMINISTIC_506090470696d12a
Batch ID: 20250612_140309
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
 * @title DigitalGlassesMarketplace
 * @dev A smart contract for buying and selling digital glasses in a decentralized marketplace.
 */
contract DigitalGlassesMarketplace {
    // Owner of the contract
    address public owner;

    // Structure to represent a digital glasses item
    struct Glasses {
        uint256 id;
        string name;
        string description;
        uint256 price; // Price in wei
        address payable seller;
        bool isSold;
    }

    // Mapping to store glasses by ID
    mapping(uint256 => Glasses) public glassesItems;

    // Counter for glasses IDs
    uint256 public glassesCount;

    // Event emitted when a new glasses item is listed
    event GlassesListed(uint256 id, string name, uint256 price, address seller);

    // Event emitted when a glasses item is sold
    event GlassesSold(uint256 id, string name, uint256 price, address buyer);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    // Modifier to ensure an item exists
    modifier glassesExists(uint256 id) {
        require(glassesItems[id].id == id, "Glasses item does not exist");
        _;
    }

    // Modifier to ensure item is not sold
    modifier notSold(uint256 id) {
        require(!glassesItems[id].isSold, "Glasses item is already sold");
        _;
    }

    constructor() {
        // Set contract deployer as owner
        owner = msg.sender;
    }

    /**
     * @dev Allows a seller to list a new glasses item.
     * @param name Name of the glasses
     * @param description Description of the glasses
     * @param price Price of the glasses in wei
     */
    function listGlasses(string memory name, string memory description, uint256 price) external {
        require(price > 0, "Price must be greater than zero");

        glassesCount++;
        glassesItems[glassesCount] = Glasses(
            glassesCount,
            name,
            description,
            price,
            payable(msg.sender),
            false
        );

        emit GlassesListed(glassesCount, name, price, msg.sender);
    }

    /**
     * @dev Allows a buyer to purchase a glasses item.
     * @param id ID of the glasses item to purchase
     */
    function buyGlasses(uint256 id) external payable glassesExists(id) notSold(id) {
        Glasses storage glasses = glassesItems[id];
        require(msg.value == glasses.price, "Incorrect payment amount");

        // Mark as sold
        glasses.isSold = true;

        // Transfer payment to seller
        glasses.seller.transfer(msg.value);

        emit GlassesSold(id, glasses.name, glasses.price, msg.sender);
    }

    /**
     * @dev Allows the owner to withdraw contract balance (if any).
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");

        payable(owner).transfer(balance);
    }

    /**
     * @dev Fallback function to handle accidental ETH transfers.
     */
    fallback() external payable {}

    /**
     * @dev Receive function to accept ETH transfers directly to the contract.
     */
    receive() external payable {}
}
```
