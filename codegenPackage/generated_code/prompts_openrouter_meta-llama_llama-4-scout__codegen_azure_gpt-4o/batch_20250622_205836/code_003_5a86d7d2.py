"""
Generated Code Metadata:
========================
Original URL: https://bafybeifzsc2fqkmtu3f77p3b3xr5mea4rugk5sb3zsww46ufwpltulpw3u.ipfs.dweb.link
Prompt: Generate a smart contract code snippet for participating in the Sophon node sale on zkSync, considering the tiered pricing system and non-transferable nodes for one year.
Generated: DETERMINISTIC_5a86d7d2eb8acdf3
Batch ID: 20250622_205836
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
 * @title SophonNodeSale
 * @dev Smart contract for participating in the Sophon node sale on zkSync.
 *      Implements tiered pricing and non-transferable nodes for one year.
 */
contract SophonNodeSale {
    // Owner of the contract
    address public owner;

    // Node pricing tiers
    uint256 public constant TIER_1_PRICE = 1 ether; // Tier 1 price
    uint256 public constant TIER_2_PRICE = 2 ether; // Tier 2 price
    uint256 public constant TIER_3_PRICE = 3 ether; // Tier 3 price

    // Mapping to track purchased nodes and their lock expiration
    mapping(address => uint256) public nodeLockExpiration;

    // Event emitted when a node is purchased
    event NodePurchased(address indexed buyer, uint256 tier, uint256 lockExpiration);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to purchase a node based on the tier.
     * @param tier The tier of the node to purchase (1, 2, or 3).
     */
    function purchaseNode(uint256 tier) external payable {
        // Validate the tier and payment amount
        require(tier >= 1 && tier <= 3, "Invalid tier");
        uint256 price = getTierPrice(tier);
        require(msg.value == price, "Incorrect payment amount");

        // Ensure the buyer has not already purchased a node
        require(nodeLockExpiration[msg.sender] == 0, "Node already purchased");

        // Set the lock expiration to one year from now
        uint256 lockExpiration = block.timestamp + 365 days;
        nodeLockExpiration[msg.sender] = lockExpiration;

        // Emit the NodePurchased event
        emit NodePurchased(msg.sender, tier, lockExpiration);
    }

    /**
     * @dev Function to get the price of a node based on the tier.
     * @param tier The tier of the node (1, 2, or 3).
     * @return The price of the node in wei.
     */
    function getTierPrice(uint256 tier) public pure returns (uint256) {
        if (tier == 1) {
            return TIER_1_PRICE;
        } else if (tier == 2) {
            return TIER_2_PRICE;
        } else if (tier == 3) {
            return TIER_3_PRICE;
        } else {
            revert("Invalid tier");
        }
    }

    /**
     * @dev Function to withdraw contract balance. Restricted to the owner.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Function to check if a node is transferable.
     * @param buyer The address of the node owner.
     * @return True if the node is transferable, false otherwise.
     */
    function isNodeTransferable(address buyer) external view returns (bool) {
        return block.timestamp > nodeLockExpiration[buyer];
    }
}
```
