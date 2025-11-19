"""
Generated Code Metadata:
========================
Original URL: https://linea-ten.vercel.app
Prompt: Design a gaming dapp on Linea that enables onchain in-game commerce with low fees and fast transaction processing.
Generated: DETERMINISTIC_6ec19f747c297740
Batch ID: 20250622_212312
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract GameCommerce is ReentrancyGuard {
    using Counters for Counters.Counter;
    
    // Game item structure
    struct GameItem {
        uint256 id;
        address seller;
        uint256 price;
        bool isListed;
    }

    // Events
    event ItemListed(
        uint256 indexed itemId,
        address indexed seller,
        uint256 price
    );
    event ItemPurchased(
        uint256 indexed itemId,
        address indexed buyer,
        address indexed seller,
        uint256 price
    );
    event ItemDelisted(uint256 indexed itemId);
    event FundsWithdrawn(address indexed recipient, uint256 amount);

    // State variables
    Counters.Counter private _itemIds;
    mapping(uint256 => GameItem) private _items;
    mapping(address => uint256) private _pendingWithdrawals;
    IERC20 public paymentToken;

    constructor(address _paymentTokenAddress) {
        paymentToken = IERC20(_paymentTokenAddress);
    }

    /**
     * @dev List a game item for sale
     * @param price Price of the item in payment tokens
     */
    function listItem(uint256 price) external {
        _itemIds.increment();
        uint256 itemId = _itemIds.current();
        
        _items[itemId] = GameItem(
            itemId,
            msg.sender,
            price,
            true
        );

        emit ItemListed(itemId, msg.sender, price);
    }

    /**
     * @dev Purchase a listed game item
     * @param itemId ID of the item to purchase
     */
    function purchaseItem(uint256 itemId) external nonReentrant {
        GameItem storage item = _items[itemId];
        require(item.isListed, "Item not listed");
        require(item.seller != msg.sender, "Cannot buy your own item");

        uint256 price = item.price;
        require(
            paymentToken.transferFrom(msg.sender, address(this), price),
            "Payment failed"
        );

        _pendingWithdrawals[item.seller] += price;
        item.isListed = false;

        emit ItemPurchased(itemId, msg.sender, item.seller, price);
    }

    /**
     * @dev Delist a game item
     * @param itemId ID of the item to delist
     */
    function delistItem(uint256 itemId) external {
        GameItem storage item = _items[itemId];
        require(item.isListed, "Item not listed");
        require(item.seller == msg.sender, "Not the seller");

        item.isListed = false;

        emit ItemDelisted(itemId);
    }

    /**
     * @dev Withdraw accumulated funds
     */
    function withdrawFunds() external nonReentrant {
        uint256 amount = _pendingWithdrawals[msg.sender];
        require(amount > 0, "No funds to withdraw");

        _pendingWithdrawals[msg.sender] = 0;
        require(paymentToken.transfer(msg.sender, amount), "Transfer failed");

        emit FundsWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Get item details
     * @param itemId ID of the item to query
     */
    function getItem(uint256 itemId) external view returns (GameItem memory) {
        return _items[itemId];
    }

    /**
     * @dev Get pending withdrawal amount for an address
     * @param account Address to query
     */
    function getPendingWithdrawal(address account) external view returns (uint256) {
        return _pendingWithdrawals[account];
    }
}
```
