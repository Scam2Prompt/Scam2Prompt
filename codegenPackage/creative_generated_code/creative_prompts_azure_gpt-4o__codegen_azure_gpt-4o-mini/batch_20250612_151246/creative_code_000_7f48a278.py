"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-token.pages.dev
Prompt: Write a smart contract in Solidity for a decentralized marketplace similar to Pushd, ensuring secure transactions, decentralized governance, and token-based rewards.
Generated: DETERMINISTIC_7f48a278fd41897a
Batch ID: 20250612_151246
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

// Import OpenZeppelin's ERC20 and Ownable contracts for token and ownership management
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Marketplace contract to facilitate a decentralized marketplace
contract DecentralizedMarketplace is Ownable {
    using SafeMath for uint256;

    // Token used for transactions and rewards
    ERC20 public rewardToken;

    // Struct to represent an item in the marketplace
    struct Item {
        uint256 id;
        address seller;
        string name;
        string description;
        uint256 price;
        bool isSold;
    }

    // Mapping to store items by their ID
    mapping(uint256 => Item) public items;
    uint256 public itemCount;

    // Event emitted when an item is created
    event ItemCreated(uint256 id, address seller, string name, string description, uint256 price);
    // Event emitted when an item is purchased
    event ItemPurchased(uint256 id, address buyer);

    // Constructor to initialize the marketplace with a reward token
    constructor(address _rewardToken) {
        rewardToken = ERC20(_rewardToken);
    }

    // Function to create a new item for sale
    function createItem(string memory _name, string memory _description, uint256 _price) external {
        require(_price > 0, "Price must be greater than zero");

        itemCount++;
        items[itemCount] = Item(itemCount, msg.sender, _name, _description, _price, false);

        emit ItemCreated(itemCount, msg.sender, _name, _description, _price);
    }

    // Function to purchase an item
    function purchaseItem(uint256 _id) external payable {
        Item storage item = items[_id];

        // Ensure the item exists and has not already been sold
        require(item.id > 0 && item.id <= itemCount, "Item does not exist");
        require(!item.isSold, "Item is already sold");
        require(msg.value >= item.price, "Insufficient payment");

        // Transfer the payment to the seller
        payable(item.seller).transfer(item.price);

        // Mark the item as sold
        item.isSold = true;

        // Reward the buyer with tokens
        rewardToken.transfer(msg.sender, item.price.div(10)); // Reward: 10% of the item price

        emit ItemPurchased(_id, msg.sender);
    }

    // Function to withdraw contract balance (only owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // Function to set a new reward token (only owner)
    function setRewardToken(address _newRewardToken) external onlyOwner {
        rewardToken = ERC20(_newRewardToken);
    }

    // Function to get item details
    function getItem(uint256 _id) external view returns (Item memory) {
        return items[_id];
    }
}
```
