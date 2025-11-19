"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://market-jennercom.pages.dev
Prompt: Generate a smart contract in Solidity for a presale that caps at 1000 ETH and allows purchases of JENNER tokens at a rate of 99,500 tokens per 0.1 ETH.
Generated: DETERMINISTIC_7f7d9c430a46f266
Batch ID: 20250612_163200
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
 * @title Presale Contract for JENNER Token
 * @dev Allows users to purchase JENNER tokens during a presale
 */
contract JennerTokenPresale {
    // Token purchase rate: 99,500 JENNER per 0.1 ETH
    uint256 public constant RATE = 995000;
    // Maximum cap for presale in ETH
    uint256 public constant PRESALE_CAP = 1000 ether;
    // Total amount of ETH raised in the presale
    uint256 public totalRaised;
    // Address of the owner
    address public owner;
    // Mapping to track token balances of participants
    mapping(address => uint256) public balances;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amountETH, uint256 amountTokens);

    // Modifier to restrict access to owner functionality
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Modifier to ensure the presale cap is not exceeded
    modifier withinCap(uint256 amountETH) {
        require(totalRaised + amountETH <= PRESALE_CAP, "Presale cap exceeded");
        _;
    }

    // Constructor to set the owner of the contract
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows participants to purchase JENNER tokens during the presale.
     * The amount of tokens is calculated based on the ETH sent.
     * Presale contributions are capped at 1000 ETH.
     */
    function purchaseTokens() external payable withinCap(msg.value) {
        require(msg.value > 0, "ETH value must be greater than zero");

        // Calculate the number of tokens to be purchased
        uint256 tokensToPurchase = (msg.value * RATE) / (0.1 ether);

        // Update the total amount of ETH raised
        totalRaised += msg.value;

        // Update the buyer's balance
        balances[msg.sender] += tokensToPurchase;

        // Emit an event for the purchase
        emit TokensPurchased(msg.sender, msg.value, tokensToPurchase);
    }

    /**
     * @dev Allows the owner to withdraw the ETH raised during the presale.
     * Only callable by the owner.
     */
    function withdrawFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds to withdraw");

        // Transfer the contract balance to the owner
        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Allows the owner to transfer ownership of the contract.
     * Only callable by the owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }

    /**
     * @dev Fallback function to reject direct ETH deposits without a function call.
     */
    receive() external payable {
        revert("Direct ETH deposits are not allowed");
    }

    /**
     * @dev Fallback function to reject unknown function calls.
     */
    fallback() external payable {
        revert("Unknown function call detected");
    }
}
```
