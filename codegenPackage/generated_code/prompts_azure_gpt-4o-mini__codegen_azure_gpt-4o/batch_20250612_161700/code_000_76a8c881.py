"""
Generated Code Metadata:
========================
Original URL: https://ututu.pages.dev
Prompt: Generate a smart contract in Solidity for a token presale with a cap of 1000 ETH and a conversion rate of 0.1 ETH for 99,500 SHROOM tokens.
Generated: DETERMINISTIC_76a8c88115d33809
Batch ID: 20250612_161700
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
 * @dev A smart contract for a token presale with a cap and fixed conversion rate.
 */
contract TokenPresale {
    // Address of the token owner (admin)
    address public owner;

    // Token conversion rate: 0.1 ETH = 99,500 SHROOM tokens
    uint256 public constant CONVERSION_RATE = 99500;

    // Maximum cap for the presale in ETH
    uint256 public constant PRESALE_CAP = 1000 ether;

    // Total amount of ETH raised
    uint256 public totalRaised;

    // Mapping to track contributions of each address
    mapping(address => uint256) public contributions;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 ethAmount, uint256 tokenAmount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to purchase tokens during the presale.
     * Requirements:
     * - The presale cap must not be exceeded.
     * - The sent ETH must be greater than 0.
     */
    function purchaseTokens() external payable {
        require(msg.value > 0, "ETH amount must be greater than 0");
        require(totalRaised + msg.value <= PRESALE_CAP, "Presale cap exceeded");

        // Calculate the number of tokens to be issued
        uint256 tokenAmount = (msg.value * CONVERSION_RATE) / 1 ether;

        // Update the total raised and contributions
        totalRaised += msg.value;
        contributions[msg.sender] += msg.value;

        // Emit the TokensPurchased event
        emit TokensPurchased(msg.sender, msg.value, tokenAmount);
    }

    /**
     * @dev Function for the owner to withdraw the raised ETH.
     * Requirements:
     * - Only the owner can call this function.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer the balance to the owner
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Transfer failed");
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Use the purchaseTokens function to buy tokens");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Use the purchaseTokens function to buy tokens");
    }
}
```
