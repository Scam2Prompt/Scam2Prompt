"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://genesisgamersguild.pages.dev
Prompt: Generate an example of a custom smart contract for a game that utilizes the Genesis Gamers Guild's zero gas fee feature.
Generated: DETERMINISTIC_c543c2e6215e8fb2
Batch ID: 20250612_160804
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

// Importing OpenZeppelin's ERC721 implementation for creating an NFT
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Custom smart contract for a game utilizing the Genesis Gamers Guild zero gas fee feature
contract GenesisGamersGame is ERC721, Ownable {
    // Structure to hold game item information
    struct GameItem {
        uint256 id;
        string name;
        string rarity;
    }

    // Mapping to store GameItem by ID
    mapping(uint256 => GameItem) public gameItems;

    // Counter for generating unique item IDs
    uint256 private nextItemId;

    // Event emitted when a new game item is created
    event GameItemCreated(uint256 indexed itemId, string name, string rarity);

    // Constructor to initialize the ERC721 token
    constructor() ERC721("GenesisGamersItem", "GGI") {
        nextItemId = 1; // Start item IDs from 1
    }

    // Function to create a new game item
    function createGameItem(string memory name, string memory rarity) external onlyOwner {
        require(bytes(name).length > 0, "Item name is required");
        require(bytes(rarity).length > 0, "Item rarity is required");

        // Create new game item
        GameItem memory newItem = GameItem({
            id: nextItemId,
            name: name,
            rarity: rarity
        });

        // Store the new item in the mapping
        gameItems[nextItemId] = newItem;

        // Mint a new NFT for the game item
        _mint(msg.sender, nextItemId);

        // Emit event for item creation
        emit GameItemCreated(nextItemId, name, rarity);

        // Increment the item ID counter for the next item
        nextItemId++;
    }

    // Function to get game item details by ID
    function getGameItem(uint256 itemId) external view returns (GameItem memory) {
        require(itemId < nextItemId, "Item does not exist");
        return gameItems[itemId];
    }

    // Function to withdraw any accidental Ether sent to the contract
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to prevent Ether from being sent to the contract
    receive() external payable {
        revert("Direct Ether transfer not allowed");
    }
}
```
