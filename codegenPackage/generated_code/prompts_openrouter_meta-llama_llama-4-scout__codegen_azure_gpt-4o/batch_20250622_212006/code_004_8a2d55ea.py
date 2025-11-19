"""
Generated Code Metadata:
========================
Original URL: https://artorvias.com
Prompt: Develop a smart contract code for managing the sale and ownership of digital collectibles on Artorvia, using Solidity or a similar programming language.
Generated: DETERMINISTIC_8a2d55ea6b13451e
Batch ID: 20250622_212006
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
 * @title ArtorviaCollectibles
 * @dev A smart contract for managing the sale and ownership of digital collectibles on Artorvia.
 */
contract ArtorviaCollectibles {
    // Struct to represent a collectible
    struct Collectible {
        uint256 id;
        string name;
        string metadataURI; // URI pointing to the metadata of the collectible
        address owner;
        uint256 price; // Price in wei
        bool forSale;
    }

    // Mapping from collectible ID to Collectible struct
    mapping(uint256 => Collectible) private collectibles;

    // Counter for generating unique collectible IDs
    uint256 private nextCollectibleId;

    // Event emitted when a new collectible is created
    event CollectibleCreated(uint256 indexed id, string name, string metadataURI, address indexed owner);

    // Event emitted when a collectible is listed for sale
    event CollectibleListed(uint256 indexed id, uint256 price);

    // Event emitted when a collectible is sold
    event CollectibleSold(uint256 indexed id, address indexed oldOwner, address indexed newOwner, uint256 price);

    // Modifier to check if the caller is the owner of a collectible
    modifier onlyOwner(uint256 collectibleId) {
        require(collectibles[collectibleId].owner == msg.sender, "Caller is not the owner");
        _;
    }

    /**
     * @dev Create a new collectible.
     * @param name Name of the collectible.
     * @param metadataURI URI pointing to the metadata of the collectible.
     */
    function createCollectible(string memory name, string memory metadataURI) external {
        uint256 collectibleId = nextCollectibleId;
        collectibles[collectibleId] = Collectible({
            id: collectibleId,
            name: name,
            metadataURI: metadataURI,
            owner: msg.sender,
            price: 0,
            forSale: false
        });

        nextCollectibleId++;

        emit CollectibleCreated(collectibleId, name, metadataURI, msg.sender);
    }

    /**
     * @dev List a collectible for sale.
     * @param collectibleId ID of the collectible to list.
     * @param price Price in wei for the collectible.
     */
    function listCollectibleForSale(uint256 collectibleId, uint256 price) external onlyOwner(collectibleId) {
        require(price > 0, "Price must be greater than zero");
        collectibles[collectibleId].price = price;
        collectibles[collectibleId].forSale = true;

        emit CollectibleListed(collectibleId, price);
    }

    /**
     * @dev Buy a collectible.
     * @param collectibleId ID of the collectible to buy.
     */
    function buyCollectible(uint256 collectibleId) external payable {
        Collectible storage collectible = collectibles[collectibleId];

        require(collectible.forSale, "Collectible is not for sale");
        require(msg.value == collectible.price, "Incorrect payment amount");

        address oldOwner = collectible.owner;

        // Transfer ownership
        collectible.owner = msg.sender;
        collectible.forSale = false;
        collectible.price = 0;

        // Transfer payment to the old owner
        payable(oldOwner).transfer(msg.value);

        emit CollectibleSold(collectibleId, oldOwner, msg.sender, msg.value);
    }

    /**
     * @dev Get details of a collectible.
     * @param collectibleId ID of the collectible to fetch details for.
     * @return Collectible details.
     */
    function getCollectible(uint256 collectibleId) external view returns (Collectible memory) {
        return collectibles[collectibleId];
    }
}
```
