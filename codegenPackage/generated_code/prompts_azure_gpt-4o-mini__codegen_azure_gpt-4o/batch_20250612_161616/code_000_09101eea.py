"""
Generated Code Metadata:
========================
Original URL: https://presale-jesse-9kw.pages.dev
Prompt: Generate a smart contract in Solidity for a presale event with a cap of 1000 BASE and a total supply of 100,000,000 JESSE tokens.
Generated: DETERMINISTIC_09101eea22e89c36
Batch ID: 20250612_161616
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
 * @title PresaleContract
 * @dev A smart contract for a presale event with a cap of 1000 BASE and a total supply of 100,000,000 JESSE tokens.
 */
contract PresaleContract {
    // Token details
    string public constant name = "JESSE Token";
    string public constant symbol = "JESSE";
    uint8 public constant decimals = 18;
    uint256 public constant totalSupply = 100_000_000 * (10 ** uint256(decimals));

    // Presale details
    uint256 public constant presaleCap = 1000 * (10 ** uint256(decimals)); // Cap in BASE tokens
    uint256 public presaleRaised; // Amount of BASE raised during presale
    uint256 public tokenPrice = 1 * (10 ** uint256(decimals)); // Price of 1 JESSE token in BASE

    // Address of the contract owner
    address public owner;

    // Mapping to track balances of JESSE tokens
    mapping(address => uint256) public balances;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier withinPresaleCap(uint256 amount) {
        require(presaleRaised + amount <= presaleCap, "Presale cap exceeded");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to purchase tokens during the presale.
     * @param amount The amount of BASE tokens sent to purchase JESSE tokens.
     */
    function purchaseTokens(uint256 amount) external payable withinPresaleCap(amount) {
        require(amount > 0, "Amount must be greater than zero");
        require(msg.value == amount, "Incorrect BASE amount sent");

        // Calculate the number of JESSE tokens to be purchased
        uint256 tokensToPurchase = amount / tokenPrice;

        // Update presale raised amount
        presaleRaised += amount;

        // Update buyer's balance
        balances[msg.sender] += tokensToPurchase;

        emit TokensPurchased(msg.sender, tokensToPurchase);
    }

    /**
     * @dev Function to withdraw BASE tokens collected during the presale.
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
     * @dev Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
