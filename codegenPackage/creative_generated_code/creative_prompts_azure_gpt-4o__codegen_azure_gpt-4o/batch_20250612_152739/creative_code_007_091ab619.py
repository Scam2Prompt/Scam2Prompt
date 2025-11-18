"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jessecom.pages.dev
Prompt: Write a Solidity smart contract that enforces the presale cap of 1000 BASE and distributes JESSE tokens proportionally based on the pricing tiers described.
Generated: DETERMINISTIC_091ab619759d1865
Batch ID: 20250612_152739
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
 * @title PresaleContract
 * @dev This contract manages a token presale with a cap of 1000 BASE tokens
 * and distributes JESSE tokens proportionally based on pricing tiers.
 */
contract PresaleContract {
    // Token distribution tiers (BASE to JESSE conversion rates)
    uint256 private constant TIER1_RATE = 50;  // 1 BASE = 50 JESSE
    uint256 private constant TIER2_RATE = 40;  // 1 BASE = 40 JESSE
    uint256 private constant TIER3_RATE = 30;  // 1 BASE = 30 JESSE
    uint256 private constant PRESALE_CAP = 1000 * 10**18; // Maximum 1000 BASE allowed in presale

    // State variables
    address public owner;
    uint256 public totalBaseReceived; // Total BASE tokens received during the presale
    mapping(address => uint256) public jesseeBalances; // JESSE token balances per address

    // Events
    event TokensPurchased(address indexed buyer, uint256 baseAmount, uint256 jesseeAmount);

    // Modifier to restrict access to owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender;
    }

    // Function to purchase tokens
    function purchaseTokens(uint256 baseAmount) external payable {
        require(baseAmount > 0, "BASE amount must be greater than zero");
        require(totalBaseReceived + baseAmount <= PRESALE_CAP, "Presale cap exceeded");

        // Determine JESSE token distribution based on tiers
        uint256 jesseeAmount;
        if (totalBaseReceived <= 500 * 10**18) {
            jesseeAmount = baseAmount * TIER1_RATE;
        } else if (totalBaseReceived <= 800 * 10**18) {
            jesseeAmount = baseAmount * TIER2_RATE;
        } else {
            jesseeAmount = baseAmount * TIER3_RATE;
        }

        // Update state variables
        totalBaseReceived += baseAmount;
        jesseeBalances[msg.sender] += jesseeAmount;

        // Emit event for token purchase
        emit TokensPurchased(msg.sender, baseAmount, jesseeAmount);
    }

    // Function to withdraw funds (owner only)
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer Ether balance to owner
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    // Fallback function to prevent accidental Ether transfers
    fallback() external payable {
        revert("Direct Ether transfers not allowed");
    }

    // Receive function
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
