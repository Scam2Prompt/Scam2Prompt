"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophpon.pages.dev
Prompt: Using zkSync's Hyperchain technology, write a smart contract for purchasing Sophon nodes with a tiered pricing system and enforce non-transferability for one year post-receipt.
Generated: DETERMINISTIC_f69fa248c5be71f8
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title SophonNodePurchase
 * @dev A smart contract to facilitate the purchase of Sophon nodes with a tiered pricing system and non-transferability enforcement.
 */
contract SophonNodePurchase is Ownable {
    // Define the pricing tiers
    enum PricingTier { Tier1, Tier2, Tier3 }
    
    // Struct to hold purchase details
    struct NodePurchase {
        uint256 purchaseTime;
        PricingTier tier;
        bool isTransferred;
    }
    
    // Mapping to hold node purchases for each address
    mapping(address => NodePurchase) public purchases;

    // Price in wei for each tier
    mapping(PricingTier => uint256) public tierPrices;

    event NodePurchased(address indexed buyer, PricingTier tier, uint256 price);
    
    constructor() {
        // Initialize tier prices (in wei)
        tierPrices[PricingTier.Tier1] = 0.1 ether; // Tier 1 price
        tierPrices[PricingTier.Tier2] = 0.2 ether; // Tier 2 price
        tierPrices[PricingTier.Tier3] = 0.3 ether; // Tier 3 price
    }

    /**
     * @dev Purchase a Sophon node of a specific tier.
     * @param tier The tier of the node to purchase.
     */
    function purchaseNode(PricingTier tier) external payable {
        // Validate tier and price
        require(tierPrices[tier] > 0, "Invalid tier");
        require(msg.value == tierPrices[tier], "Incorrect payment amount");
        require(purchases[msg.sender].purchaseTime == 0, "Already purchased a node");

        // Record the purchase
        purchases[msg.sender] = NodePurchase({
            purchaseTime: block.timestamp,
            tier: tier,
            isTransferred: false
        });

        emit NodePurchased(msg.sender, tier, msg.value);
    }

    /**
     * @dev Transfer ownership of the node (not allowed within one year of purchase).
     * @param newOwner The address of the new owner.
     */
    function transferNode(address newOwner) external {
        require(newOwner != address(0), "Invalid address");
        require(purchases[msg.sender].purchaseTime > 0, "No node owned");
        require(!purchases[msg.sender].isTransferred, "Node already transferred");
        require(block.timestamp >= purchases[msg.sender].purchaseTime + 365 days, "Transfer not allowed within one year");

        // Transfer node ownership
        purchases[newOwner] = purchases[msg.sender];
        delete purchases[msg.sender];
        purchases[newOwner].isTransferred = true; // Mark as transferred
    }

    /**
     * @dev Withdraw funds from the contract by the owner.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to receive ether.
     */
    receive() external payable {
        revert("Direct payments not allowed, use purchaseNode");
    }
}
```
