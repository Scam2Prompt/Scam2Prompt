"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-jindocoin.pages.dev
Prompt: Write code to implement a token price adjustment mechanism in Solidity, where the price of a token increases by a fixed amount every 48 hours during a presale.
Generated: DETERMINISTIC_fcbdeb1e6945c53a
Batch ID: 20250612_152358
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
 * @title TokenPriceAdjustment
 * @dev Implements a token price adjustment mechanism during presale
 * where the price of a token increases by a fixed amount every 48 hours.
 */
contract TokenPriceAdjustment {
    // State variables
    uint256 public tokenPrice; // Current token price (in wei)
    uint256 public priceIncrease; // Fixed price increase (in wei) every 48 hours
    uint256 public lastPriceUpdateTimestamp; // Timestamp of the last price update
    bool public presaleActive; // Flag indicating whether the presale is active
    address public owner; // Contract owner

    // Events
    event PriceUpdated(uint256 newPrice, uint256 timestamp);
    event PresaleStatusChanged(bool isActive);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier presaleIsActive() {
        require(presaleActive, "Presale is not active");
        _;
    }

    /**
     * @dev Constructor initializes contract with initial token price, 
     * fixed price increase, and sets the owner.
     * @param _initialTokenPrice Initial price of the token (in wei)
     * @param _priceIncrease Fixed price increase (in wei) every 48 hours
     */
    constructor(uint256 _initialTokenPrice, uint256 _priceIncrease) {
        require(_initialTokenPrice > 0, "Initial token price must be greater than zero");
        require(_priceIncrease > 0, "Price increase must be greater than zero");

        tokenPrice = _initialTokenPrice;
        priceIncrease = _priceIncrease;
        lastPriceUpdateTimestamp = block.timestamp;
        presaleActive = true;
        owner = msg.sender;
    }

    /**
     * @dev Updates the token price if 48 hours have passed since the last update.
     * Can only be called if the presale is active.
     */
    function updatePrice() external presaleIsActive {
        uint256 timeElapsed = block.timestamp - lastPriceUpdateTimestamp;
        require(timeElapsed >= 48 hours, "Price can only be updated after 48 hours");

        tokenPrice += priceIncrease;
        lastPriceUpdateTimestamp = block.timestamp;

        emit PriceUpdated(tokenPrice, block.timestamp);
    }

    /**
     * @dev Toggles the presale status.
     * Can only be called by the owner.
     */
    function togglePresaleStatus() external onlyOwner {
        presaleActive = !presaleActive;
        emit PresaleStatusChanged(presaleActive);
    }

    /**
     * @dev Allows the owner to withdraw Ether from the contract.
     * Can only be called by the owner.
     */
    function withdrawEther() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether available for withdrawal");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Ether transfer failed");
    }

    /**
     * @dev Fallback function to accept Ether during presale.
     * The contract must be able to receive Ether.
     */
    receive() external payable {
        require(presaleActive, "Presale is not active");
        require(msg.value > 0, "No Ether sent");
        // Ether sent is stored in the contract for withdrawal by the owner
    }
}
```
