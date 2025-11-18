"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethxy-layer2.pages.dev
Prompt: Create a smart contract in Solidity for managing NFT minting slots, optimized for deployment on an Ethereum Layer 2 network.
Generated: DETERMINISTIC_98d8b4e1c04fd66a
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title NFT Minting Slot Manager
 * @dev This contract manages minting slots for NFTs on an Ethereum Layer 2 network.
 */
contract NFTMintingSlotManager {
    // State variables
    address public owner; // Contract owner
    uint256 public maxSlots; // Maximum number of minting slots
    uint256 public slotPrice; // Price per minting slot in wei
    mapping(address => uint256) public purchasedSlots; // Tracks slots purchased by each address
    uint256 public totalSlotsSold; // Tracks total slots sold

    // Events
    event SlotsPurchased(address indexed buyer, uint256 quantity);
    event SlotPriceUpdated(uint256 newPrice);
    event MaxSlotsUpdated(uint256 newMaxSlots);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier validPurchase(uint256 quantity) {
        require(quantity > 0, "Quantity must be greater than 0");
        require(totalSlotsSold + quantity <= maxSlots, "Not enough slots available");
        require(msg.value == quantity * slotPrice, "Incorrect payment amount");
        _;
    }

    // Constructor
    constructor(uint256 _maxSlots, uint256 _slotPrice) {
        require(_maxSlots > 0, "Max slots must be greater than 0");
        require(_slotPrice > 0, "Slot price must be greater than 0");
        owner = msg.sender;
        maxSlots = _maxSlots;
        slotPrice = _slotPrice;
    }

    /**
     * @dev Purchase minting slots by sending the required payment.
     * @param quantity Number of slots to purchase.
     */
    function purchaseSlots(uint256 quantity) external payable validPurchase(quantity) {
        purchasedSlots[msg.sender] += quantity;
        totalSlotsSold += quantity;

        emit SlotsPurchased(msg.sender, quantity);
    }

    /**
     * @dev Update the price per minting slot. Only the owner can call this function.
     * @param newPrice The new price per slot in wei.
     */
    function updateSlotPrice(uint256 newPrice) external onlyOwner {
        require(newPrice > 0, "Slot price must be greater than 0");
        slotPrice = newPrice;

        emit SlotPriceUpdated(newPrice);
    }

    /**
     * @dev Update the maximum number of minting slots. Only the owner can call this function.
     * @param newMaxSlots The new maximum number of slots.
     */
    function updateMaxSlots(uint256 newMaxSlots) external onlyOwner {
        require(newMaxSlots >= totalSlotsSold, "New max slots cannot be less than slots sold");
        maxSlots = newMaxSlots;

        emit MaxSlotsUpdated(newMaxSlots);
    }

    /**
     * @dev Withdraw accumulated funds from the contract. Only the owner can call this function.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct transfers not allowed");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct transfers not allowed");
    }
}
```
