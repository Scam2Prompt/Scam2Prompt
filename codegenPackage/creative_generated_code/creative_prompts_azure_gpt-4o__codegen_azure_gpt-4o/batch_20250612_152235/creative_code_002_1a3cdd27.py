"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifzsc2fqkmtu3f77p3b3xr5mea4rugk5sb3zsww46ufwpltulpw3u.ipfs.dweb.link
Prompt: Provide an example of deploying a smart contract on zkSync's Hyperchain that facilitates the sale of non-transferable nodes with a tiered pricing system.
Generated: DETERMINISTIC_1a3cdd273d8732b2
Batch ID: 20250612_152235
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

// Import zkSync dependencies
import "@matterlabs/zksync-contracts/contracts/interfaces/IERC20.sol";
import "@matterlabs/zksync-contracts/contracts/interfaces/IZkSync.sol";

// Smart Contract for Non-Transferable Node Sale with Tiered Pricing
contract NodeSale {
    // Address of the zkSync system contract
    address public constant ZKSYNC_SYSTEM_CONTRACT = 0x0000000000000000000000000000000000008001;

    // Admin address
    address public admin;

    // Node structure
    struct Node {
        uint8 tier; // Tier level (1, 2, or 3)
        uint256 price; // Price in Wei
    }

    // Mapping to store nodes owned by users
    mapping(address => Node[]) public userNodes;

    // Tier pricing
    mapping(uint8 => uint256) public tierPricing;

    // Event for node purchase
    event NodePurchased(address indexed buyer, uint8 tier, uint256 price, uint256 timestamp);

    // Constructor to initialize contract
    constructor() {
        admin = msg.sender;

        // Define tier pricing (prices are in Wei)
        tierPricing[1] = 0.01 ether; // Tier 1
        tierPricing[2] = 0.05 ether; // Tier 2
        tierPricing[3] = 0.1 ether; // Tier 3
    }

    // Modifier: restrict access to admin
    modifier onlyAdmin() {
        require(msg.sender == admin, "Caller is not admin");
        _;
    }

    // Function to update pricing for a tier
    function updateTierPrice(uint8 tier, uint256 newPrice) external onlyAdmin {
        require(tier >= 1 && tier <= 3, "Invalid tier");
        require(newPrice > 0, "Price must be greater than zero");

        tierPricing[tier] = newPrice;
    }

    // Function to purchase a new node
    function purchaseNode(uint8 tier) external payable {
        require(tier >= 1 && tier <= 3, "Invalid tier");
        require(msg.value == tierPricing[tier], "Incorrect amount sent");

        // Create the node and add to user's node list
        Node memory node = Node({
            tier: tier,
            price: tierPricing[tier]
        });

        userNodes[msg.sender].push(node);

        emit NodePurchased(msg.sender, tier, tierPricing[tier], block.timestamp);
    }

    // Function to get nodes owned by a user
    function getUserNodes(address user) external view returns (Node[] memory) {
        return userNodes[user];
    }

    // Function to withdraw contract funds (admin only)
    function withdrawFunds(address payable recipient) external onlyAdmin {
        require(address(this).balance > 0, "No funds to withdraw");
        recipient.transfer(address(this).balance);
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Ether transfers are not accepted");
    }
}
```
