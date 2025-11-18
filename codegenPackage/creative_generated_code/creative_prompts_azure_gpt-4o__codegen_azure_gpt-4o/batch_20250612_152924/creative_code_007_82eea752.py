"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ututu.pages.dev
Prompt: Write a Solidity contract that includes an event to log each SHROOM token purchase, including the buyer's address, ETH amount, and token quantity.
Generated: DETERMINISTIC_82eea752cf2daaab
Batch ID: 20250612_152924
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
 * @title SHROOMTokenSale
 * @dev A contract to facilitate the purchase of SHROOM tokens.
 */
contract SHROOMTokenSale {
    // Token price in wei (e.g., 1 SHROOM = 0.001 ETH)
    uint256 public tokenPrice;

    // Owner of the contract
    address public owner;

    // Event to log token purchases
    event TokenPurchased(
        address indexed buyer,   // Address of the buyer
        uint256 ethAmount,       // Amount of ETH sent
        uint256 tokenQuantity    // Quantity of tokens purchased
    );

    // Modifier to restrict function access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this operation.");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the token price.
     * @param _tokenPrice Price of one SHROOM token in wei.
     */
    constructor(uint256 _tokenPrice) {
        require(_tokenPrice > 0, "Token price must be greater than zero.");
        tokenPrice = _tokenPrice;
        owner = msg.sender;
    }

    /**
     * @dev Purchase SHROOM tokens. Sends ETH to the contract and receives tokens.
     */
    function purchaseTokens() external payable {
        require(msg.value > 0, "You must send ETH to purchase tokens.");

        // Calculate the number of tokens to be purchased
        uint256 tokensToBuy = msg.value / tokenPrice;
        require(tokensToBuy > 0, "Insufficient ETH sent to purchase tokens.");

        // Emit the TokenPurchased event
        emit TokenPurchased(msg.sender, msg.value, tokensToBuy);

        // Note: Tokens are not actually transferred in this contract.
        // In a real implementation, you would interface with an ERC-20 token contract.
    }

    /**
     * @dev Allows the owner to withdraw the ETH collected from token sales.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal.");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Failed to withdraw funds.");
    }

    /**
     * @dev Update the price of SHROOM tokens. Only callable by the owner.
     * @param _newPrice The new price for one SHROOM token in wei.
     */
    function updateTokenPrice(uint256 _newPrice) external onlyOwner {
        require(_newPrice > 0, "Token price must be greater than zero.");
        tokenPrice = _newPrice;
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct ETH transfers are not allowed. Use the purchaseTokens function.");
    }
}
```
