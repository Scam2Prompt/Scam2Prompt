"""
Generated Code Metadata:
========================
Original URL: https://webs-bigtime.pages.dev
Prompt: Create a simple smart contract in Solidity to manage the $BIGTIME Token, including functions for collecting, crafting, and upgrading digital items.
Generated: DETERMINISTIC_6aa1c140f5b52eb9
Batch ID: 20250622_211131
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
 * @title BIGTIME Token Smart Contract
 * @dev This contract manages the $BIGTIME Token, allowing users to collect, craft, and upgrade digital items.
 */
contract BigTimeToken {
    // Token name and symbol
    string public constant name = "$BIGTIME Token";
    string public constant symbol = "BIGTIME";

    // Owner of the contract
    address public owner;

    // Mapping to store balances of $BIGTIME tokens for each user
    mapping(address => uint256) public balances;

    // Struct to represent a digital item
    struct Item {
        string name;
        uint256 level;
        uint256 craftingCost;
    }

    // Mapping to store items owned by each user
    mapping(address => Item[]) public userItems;

    // Event declarations
    event TokensCollected(address indexed user, uint256 amount);
    event ItemCrafted(address indexed user, string itemName);
    event ItemUpgraded(address indexed user, string itemName, uint256 newLevel);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to collect $BIGTIME tokens.
     * @param amount The amount of tokens to collect.
     */
    function collectTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Increase the user's balance
        balances[msg.sender] += amount;

        emit TokensCollected(msg.sender, amount);
    }

    /**
     * @dev Function to craft a new digital item.
     * @param itemName The name of the item to craft.
     * @param craftingCost The cost in $BIGTIME tokens to craft the item.
     */
    function craftItem(string memory itemName, uint256 craftingCost) external {
        require(bytes(itemName).length > 0, "Item name cannot be empty");
        require(craftingCost > 0, "Crafting cost must be greater than zero");
        require(balances[msg.sender] >= craftingCost, "Insufficient $BIGTIME tokens");

        // Deduct the crafting cost from the user's balance
        balances[msg.sender] -= craftingCost;

        // Create the new item and add it to the user's inventory
        userItems[msg.sender].push(Item(itemName, 1, craftingCost));

        emit ItemCrafted(msg.sender, itemName);
    }

    /**
     * @dev Function to upgrade an existing digital item.
     * @param itemIndex The index of the item in the user's inventory.
     * @param upgradeCost The cost in $BIGTIME tokens to upgrade the item.
     */
    function upgradeItem(uint256 itemIndex, uint256 upgradeCost) external {
        require(itemIndex < userItems[msg.sender].length, "Invalid item index");
        require(upgradeCost > 0, "Upgrade cost must be greater than zero");
        require(balances[msg.sender] >= upgradeCost, "Insufficient $BIGTIME tokens");

        // Deduct the upgrade cost from the user's balance
        balances[msg.sender] -= upgradeCost;

        // Upgrade the item's level
        userItems[msg.sender][itemIndex].level += 1;

        emit ItemUpgraded(msg.sender, userItems[msg.sender][itemIndex].name, userItems[msg.sender][itemIndex].level);
    }

    /**
     * @dev Function to retrieve the user's inventory of items.
     * @return An array of items owned by the user.
     */
    function getUserItems() external view returns (Item[] memory) {
        return userItems[msg.sender];
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        owner = newOwner;
    }
}
```
