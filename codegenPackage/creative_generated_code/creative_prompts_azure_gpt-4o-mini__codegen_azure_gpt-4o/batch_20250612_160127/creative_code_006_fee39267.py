"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orange-pepe.pages.dev
Prompt: Create a smart contract that allows users to purchase exclusive merchandise using $ORPE tokens on the upcoming e-commerce platform.
Generated: DETERMINISTIC_fee39267a460a6ed
Batch ID: 20250612_160127
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
 * @title ExclusiveMerchandiseStore
 * @dev A smart contract for purchasing exclusive merchandise using $ORPE tokens.
 *      This contract allows users to buy items if they have sufficient $ORPE tokens.
 *      The contract is designed to be used within an e-commerce platform.
 */
contract ExclusiveMerchandiseStore {
    // Address of the $ORPE token contract
    IERC20 public immutable orpeToken;

    // Owner of the store (platform owner)
    address public owner;

    // Mapping to track merchandise stock and prices
    struct Merchandise {
        uint256 price; // Price in $ORPE tokens
        uint256 stock; // Available stock
    }
    mapping(uint256 => Merchandise) public merchandise; // merchandiseId => Merchandise details

    // Event emitted when a merchandise item is purchased
    event MerchandisePurchased(address indexed buyer, uint256 indexed merchandiseId, uint256 quantity);

    // Event emitted when merchandise stock or price is updated
    event MerchandiseUpdated(uint256 indexed merchandiseId, uint256 price, uint256 stock);

    // Modifier to restrict access to only the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized - Only owner can execute");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _orpeToken Address of the $ORPE token contract.
     */
    constructor(IERC20 _orpeToken) {
        require(address(_orpeToken) != address(0), "Invalid token address");
        orpeToken = _orpeToken;
        owner = msg.sender;
    }

    /**
     * @dev Update merchandise details (price and stock).
     * @param merchandiseId ID of the merchandise item.
     * @param price Price in $ORPE tokens.
     * @param stock Available stock.
     */
    function updateMerchandise(uint256 merchandiseId, uint256 price, uint256 stock) external onlyOwner {
        require(price > 0, "Price must be greater than zero");
        merchandise[merchandiseId] = Merchandise({price: price, stock: stock});
        emit MerchandiseUpdated(merchandiseId, price, stock);
    }

    /**
     * @dev Purchase merchandise item.
     * @param merchandiseId ID of the merchandise item.
     * @param quantity Quantity of merchandise to purchase.
     */
    function purchaseMerchandise(uint256 merchandiseId, uint256 quantity) external {
        require(quantity > 0, "Quantity must be greater than zero");
        Merchandise storage item = merchandise[merchandiseId];
        require(item.stock >= quantity, "Insufficient stock");
        uint256 totalPrice = item.price * quantity;
        require(orpeToken.balanceOf(msg.sender) >= totalPrice, "Insufficient $ORPE balance");

        // Transfer $ORPE tokens from buyer to owner
        require(orpeToken.transferFrom(msg.sender, owner, totalPrice), "Token transfer failed");

        // Update stock after purchase
        item.stock -= quantity;

        // Emit purchase event
        emit MerchandisePurchased(msg.sender, merchandiseId, quantity);
    }
}

// Minimal IERC20 interface for interacting with the $ORPE token contract
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
