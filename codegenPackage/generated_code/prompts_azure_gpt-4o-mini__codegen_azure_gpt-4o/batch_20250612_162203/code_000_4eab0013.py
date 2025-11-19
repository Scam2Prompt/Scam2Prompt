"""
Generated Code Metadata:
========================
Original URL: https://jessecoin-1sa.pages.dev
Prompt: Generate a code snippet for a smart contract that manages a token presale with a cap of 1000 BASE and a total supply of 100,000,000 JESSE.
Generated: DETERMINISTIC_4eab0013497f2a31
Batch ID: 20250612_162203
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
 * @title TokenPresale
 * @dev A smart contract to manage a token presale with a cap and total supply.
 */
contract TokenPresale {
    // Token details
    string public constant name = "JESSE Token";
    string public constant symbol = "JESSE";
    uint8 public constant decimals = 18;
    uint256 public constant totalSupply = 100_000_000 * (10 ** uint256(decimals));

    // Presale details
    uint256 public constant presaleCap = 1000 * (10 ** uint256(decimals)); // 1000 BASE
    uint256 public presaleRaised; // Tracks the amount raised during presale
    uint256 public tokenPrice = 0.001 ether; // Price per JESSE token in ETH

    // Address of the owner
    address public owner;

    // Mapping to track token balances
    mapping(address => uint256) public balances;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 cost);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier withinCap(uint256 amount) {
        require(presaleRaised + amount <= presaleCap, "Purchase exceeds presale cap");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     */
    constructor() {
        owner = msg.sender;
        balances[owner] = totalSupply; // Assign total supply to the owner
    }

    /**
     * @dev Function to purchase tokens during the presale.
     */
    function buyTokens() external payable withinCap(msg.value) {
        require(msg.value > 0, "Ether value must be greater than 0");

        // Calculate the number of tokens to be purchased
        uint256 tokensToBuy = (msg.value * (10 ** uint256(decimals))) / tokenPrice;

        // Ensure the owner has enough tokens to sell
        require(balances[owner] >= tokensToBuy, "Not enough tokens available for sale");

        // Update balances and presale raised amount
        balances[owner] -= tokensToBuy;
        balances[msg.sender] += tokensToBuy;
        presaleRaised += msg.value;

        emit TokensPurchased(msg.sender, tokensToBuy, msg.value);
    }

    /**
     * @dev Function to withdraw funds raised during the presale.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct ETH transfers not allowed");
    }

    /**
     * @dev Receive function to handle ETH sent directly to the contract.
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
