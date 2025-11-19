"""
Generated Code Metadata:
========================
Original URL: https://ututu.pages.dev
Prompt: Write a Solidity function that prevents purchases exceeding the presale cap of 1000 ETH and ensures accurate token allocation based on the specified exchange rate.
Generated: DETERMINISTIC_1ea1034207bca137
Batch ID: 20250612_152924
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

contract Presale {
    // State variables
    uint256 public constant PRESALE_CAP = 1000 ether; // Maximum ETH for presale
    uint256 public constant EXCHANGE_RATE = 1000; // Tokens per ETH
    uint256 public totalRaised; // Total ETH raised in presale
    mapping(address => uint256) public contributions; // Track contributions by address

    // Event to log purchases
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 ethSpent);

    // Modifier to check if the purchase exceeds the presale cap
    modifier withinCap(uint256 _amount) {
        require(totalRaised + _amount <= PRESALE_CAP, "Purchase exceeds presale cap");
        _;
    }

    // Function to purchase tokens during the presale
    function purchaseTokens() external payable withinCap(msg.value) {
        require(msg.value > 0, "Must send ETH to purchase tokens");

        // Update total raised and individual contribution
        totalRaised += msg.value;
        contributions[msg.sender] += msg.value;

        // Calculate the number of tokens to allocate
        uint256 tokensToAllocate = msg.value * EXCHANGE_RATE;

        // Emit event for the purchase
        emit TokensPurchased(msg.sender, tokensToAllocate, msg.value);
    }

    // Function to withdraw funds (only owner can call this)
    function withdrawFunds() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to get the contract's balance
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    // Owner management
    address private _owner;

    constructor() {
        _owner = msg.sender; // Set the contract deployer as the owner
    }

    modifier onlyOwner() {
        require(msg.sender == _owner, "Caller is not the owner");
        _;
    }
}
```
