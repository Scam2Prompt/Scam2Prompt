"""
Generated Code Metadata:
========================
Original URL: https://walletconnect-v3-presale-boilerplate-website.pages.dev
Prompt: Design a simple smart contract for a token presale using Solidity that includes functionality similar to the BOI token sale.
Generated: DETERMINISTIC_0bca525deca85d7c
Batch ID: 20250622_205158
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
 * @dev A simple smart contract for a token presale.
 */
contract TokenPresale {
    // Token details
    string public constant name = "BOI Token";
    string public constant symbol = "BOI";
    uint8 public constant decimals = 18;

    // Total supply of tokens
    uint256 public constant totalSupply = 1000000 * (10 ** uint256(decimals));

    // Presale parameters
    uint256 public constant tokenPrice = 0.001 ether; // Price per token in Ether
    uint256 public constant maxTokensPerAddress = 1000 * (10 ** uint256(decimals)); // Max tokens per address

    // Owner of the contract
    address public owner;

    // Mapping to track token balances
    mapping(address => uint256) public balances;

    // Event to log token purchases
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to purchase tokens during the presale.
     * @notice Buyers must send Ether equal to the price of the tokens they want to purchase.
     */
    function buyTokens() external payable {
        // Calculate the number of tokens to purchase
        uint256 tokensToPurchase = (msg.value * (10 ** uint256(decimals))) / tokenPrice;

        // Ensure the buyer does not exceed the max tokens per address
        require(
            balances[msg.sender] + tokensToPurchase <= maxTokensPerAddress,
            "Purchase exceeds max tokens per address"
        );

        // Ensure there are enough tokens available for purchase
        require(
            balances[msg.sender] + tokensToPurchase <= totalSupply,
            "Not enough tokens available for purchase"
        );

        // Update the buyer's balance
        balances[msg.sender] += tokensToPurchase;

        // Emit the purchase event
        emit TokensPurchased(msg.sender, tokensToPurchase);
    }

    /**
     * @dev Function to withdraw Ether collected during the presale.
     * @notice Only the owner can call this function.
     */
    function withdrawFunds() external onlyOwner {
        // Transfer the contract's Ether balance to the owner
        payable(owner).transfer(address(this).balance);
    }

    /**
     * @dev Function to check the contract's Ether balance.
     * @return The Ether balance of the contract.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @dev Function to check the token balance of an address.
     * @param account The address to check the balance of.
     * @return The token balance of the address.
     */
    function getTokenBalance(address account) external view returns (uint256) {
        return balances[account];
    }
}
```
