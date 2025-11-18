"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimalvara.pages.dev
Prompt: Write a smart contract in Solidity to create an ERC-7621 Basket Token (BTS) that allows users to mint, burn, and rebalance tokenized baskets of ERC-20 assets, as described in the Alvara Protocol documentation.
Generated: DETERMINISTIC_ca8c544c131bde94
Batch ID: 20250612_154820
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
 * @title ERC-7621 Basket Token (BTS) Implementation
 * @author [Your Name]
 * 
 * @notice This smart contract allows users to create tokenized baskets of ERC-20 assets.
 * Users can mint, burn, and rebalance baskets according to the ERC-7621 standard.
 * 
 * @dev Complies with the Alvara Protocol documentation and implements error handling.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract BasketToken is Ownable {
    // Struct representing a basket item
    struct BasketItem {
        address tokenAddress; // Address of the ERC-20 token
        uint256 weight;       // Weight of the token in the basket (percentage scaled by decimals)
    }

    // Mapping of basket IDs to their respective basket items
    mapping(uint256 => BasketItem[]) private baskets;

    // Mapping of basket IDs to their owners
    mapping(uint256 => address) private basketOwners;

    // Counter for unique basket IDs
    uint256 private basketIdCounter;

    // Event emitted when a basket is minted
    event BasketMinted(uint256 basketId, address indexed owner, BasketItem[] items);

    // Event emitted when a basket is burned
    event BasketBurned(uint256 basketId, address indexed owner);

    // Event emitted when a basket is rebalanced
    event BasketRebalanced(uint256 basketId, BasketItem[] newItems);

    /**
     * @notice Mint a new basket token containing specified ERC-20 assets.
     * @param items Array of BasketItem structs defining the assets and their weights.
     */
    function mintBasket(BasketItem[] memory items) external {
        require(items.length > 0, "Basket must contain at least one token.");

        // Validate each basket item
        for (uint256 i = 0; i < items.length; i++) {
            require(items[i].tokenAddress != address(0), "Invalid token address.");
            require(items[i].weight > 0, "Weight must be greater than zero.");
        }

        // Increment basket ID counter
        uint256 newBasketId = ++basketIdCounter;

        // Assign ownership of the basket
        basketOwners[newBasketId] = msg.sender;

        // Save basket items
        for (uint256 i = 0; i < items.length; i++) {
            baskets[newBasketId].push(items[i]);
        }

        // Emit basket minting event
        emit BasketMinted(newBasketId, msg.sender, items);
    }

    /**
     * @notice Burn an existing basket token owned by the caller.
     * @param basketId ID of the basket to burn.
     */
    function burnBasket(uint256 basketId) external {
        require(basketOwners[basketId] == msg.sender, "Caller is not the owner of the basket.");

        // Delete basket items
        delete baskets[basketId];

        // Remove ownership
        delete basketOwners[basketId];

        // Emit basket burning event
        emit BasketBurned(basketId, msg.sender);
    }

    /**
     * @notice Rebalance an existing basket by updating its assets and weights.
     * @param basketId ID of the basket to rebalance.
     * @param newItems Array of BasketItem structs defining the new assets and weights.
     */
    function rebalanceBasket(uint256 basketId, BasketItem[] memory newItems) external {
        require(basketOwners[basketId] == msg.sender, "Caller is not the owner of the basket.");
        require(newItems.length > 0, "Basket must contain at least one token.");

        // Validate each basket item
        for (uint256 i = 0; i < newItems.length; i++) {
            require(newItems[i].tokenAddress != address(0), "Invalid token address.");
            require(newItems[i].weight > 0, "Weight must be greater than zero.");
        }

        // Update basket items
        delete baskets[basketId];
        for (uint256 i = 0; i < newItems.length; i++) {
            baskets[basketId].push(newItems[i]);
        }

        // Emit basket rebalancing event
        emit BasketRebalanced(basketId, newItems);
    }

    /**
     * @notice Get details of a specific basket.
     * @param basketId ID of the basket to query.
     * @return owner Address of the basket owner.
     * @return items Array of BasketItem structs representing the basket's assets and weights.
     */
    function getBasket(uint256 basketId) external view returns (address owner, BasketItem[] memory items) {
        owner = basketOwners[basketId];
        items = baskets[basketId];
    }
}
```
