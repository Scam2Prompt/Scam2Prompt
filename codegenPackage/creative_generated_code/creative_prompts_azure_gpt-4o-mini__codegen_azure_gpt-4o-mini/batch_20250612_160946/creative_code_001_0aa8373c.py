"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://threeprotocol-claimreward.pages.dev
Prompt: How can I create a decentralized marketplace using Tri-Signature DAO governance and No-KYC ZKP for user privacy, as outlined in the Three Protocol's features?
Generated: DETERMINISTIC_0aa8373c5fbf7d2f
Batch ID: 20250612_160946
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

// Import necessary libraries and interfaces
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Interface for Zero Knowledge Proof (ZKP) verification
interface IZKProof {
    function verifyProof(bytes memory proof, bytes32[] memory inputs) external returns (bool);
}

// Main contract for Decentralized Marketplace
contract DecentralizedMarketplace is Ownable {
    using Counters for Counters.Counter;

    // Struct for item listings
    struct Item {
        uint256 id;
        address seller;
        string description;
        uint256 price;
        bool isSold;
    }

    // State variables
    Counters.Counter private _itemIdCounter;
    mapping(uint256 => Item) private _items;
    IZKProof public zkProofContract;

    // Event emitted when an item is listed
    event ItemListed(uint256 indexed itemId, address indexed seller, string description, uint256 price);
    
    // Event emitted when an item is purchased
    event ItemPurchased(uint256 indexed itemId, address indexed buyer);

    // Constructor to set ZKP contract address
    constructor(address _zkProofAddress) {
        zkProofContract = IZKProof(_zkProofAddress);
    }

    // Function to list an item in the marketplace
    function listItem(string memory description, uint256 price) external {
        require(price > 0, "Price must be greater than zero");
        
        _itemIdCounter.increment();
        uint256 newItemId = _itemIdCounter.current();
        
        _items[newItemId] = Item(newItemId, msg.sender, description, price, false);
        
        emit ItemListed(newItemId, msg.sender, description, price);
    }

    // Function to purchase an item
    function purchaseItem(uint256 itemId, bytes memory proof, bytes32[] memory inputs) external payable {
        Item storage item = _items[itemId];
        
        require(item.id != 0, "Item does not exist");
        require(!item.isSold, "Item is already sold");
        require(msg.value == item.price, "Incorrect value sent");

        // Verify ZKP before completing the purchase
        require(zkProofContract.verifyProof(proof, inputs), "ZKP verification failed");

        item.isSold = true;
        
        // Transfer Ether to the seller
        payable(item.seller).transfer(msg.value);
        
        emit ItemPurchased(itemId, msg.sender);
    }

    // Function to fetch details of an item
    function getItem(uint256 itemId) external view returns (Item memory) {
        Item memory item = _items[itemId];
        require(item.id != 0, "Item does not exist");
        return item;
    }

    // Function to withdraw contract's balance (only owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
