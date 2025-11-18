"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beckeerererer.pages.dev
Prompt: Write a Solidity function to distribute BCKR tokens based on the presale rate (99,500 BCKR per 0.1 ETH) and ensure the total supply does not exceed 100,000,000 tokens.
Generated: DETERMINISTIC_e24464846b16b12c
Batch ID: 20250612_152620
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
 * @title BCKRTokenPresale
 * @dev This contract allows for distributing BCKR tokens based on a presale rate, ensuring the total supply does not exceed 100,000,000 tokens.
 */
contract BCKRTokenPresale {
    // Token details
    uint256 public constant MAX_SUPPLY = 100_000_000 * 10 ** 18; // Maximum token supply (18 decimals)
    uint256 public totalSupply; // Current total supply of tokens
    uint256 public constant RATE = 99_500 * 10 ** 18; // Presale rate: 99,500 BCKR per 0.1 ETH

    // Mapping to store balances of token holders
    mapping(address => uint256) public balances;

    // Address of the owner
    address public owner;

    // Events
    event TokensPurchased(address indexed buyer, uint256 ethAmount, uint256 tokenAmount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Constructor to initialize the owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to purchase tokens during the presale
     * @notice The amount of ETH sent determines the number of tokens distributed based on the presale rate.
     * @notice Reverts if the purchase would exceed the maximum supply.
     */
    function purchaseTokens() public payable {
        require(msg.value > 0, "ETH amount must be greater than zero");

        // Calculate the number of tokens to distribute
        uint256 tokensToDistribute = (msg.value * RATE) / (0.1 ether);

        // Ensure the total supply does not exceed the maximum limit
        require(totalSupply + tokensToDistribute <= MAX_SUPPLY, "Purchase exceeds maximum token supply");

        // Update user balance and total supply
        balances[msg.sender] += tokensToDistribute;
        totalSupply += tokensToDistribute;

        // Emit the purchase event
        emit TokensPurchased(msg.sender, msg.value, tokensToDistribute);
    }

    /**
     * @dev Function to withdraw ETH collected from presale
     * @notice Only the owner can call this function.
     */
    function withdrawETH() public onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH available for withdrawal");

        // Transfer the ETH to the owner
        (bool success, ) = owner.call{value: balance}("");
        require(success, "ETH withdrawal failed");
    }

    /**
     * @dev Function to transfer ownership of the contract
     * @notice Only the current owner can call this function.
     * @param newOwner The address of the new owner
     */
    function transferOwnership(address newOwner) public onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");

        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    // Fallback function to accept ETH directly
    receive() external payable {
        purchaseTokens();
    }

    // Fallback function to handle other calls
    fallback() external payable {
        purchaseTokens();
    }
}
```
