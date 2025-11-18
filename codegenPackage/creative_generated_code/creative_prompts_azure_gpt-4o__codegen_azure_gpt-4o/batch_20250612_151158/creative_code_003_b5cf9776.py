"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appwienerclaim.pages.dev
Prompt: Write a Solidity smart contract for a token presale similar to WienerAI, including features like staged price increases and token allocation percentages.
Generated: DETERMINISTIC_b5cf97768bee8de6
Batch ID: 20250612_151158
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
 * @title TokenPresale
 * @dev A smart contract to conduct a token presale with staged price increases and allocation percentages.
 */
contract TokenPresale {
    // State variables
    address public owner; // Owner of the contract
    uint256 public constant TOTAL_SUPPLY = 1000000 * 10**18; // Total supply of tokens
    uint256 public tokensSold; // Total tokens sold during presale
    uint256 public presaleStage; // Current presale stage
    uint256 public constant MAX_STAGE = 3; // Maximum number of presale stages

    // Token price per stage (in wei)
    uint256[] public stagePrices = [0.001 ether, 0.002 ether, 0.005 ether];

    // Token allocation percentages per stage
    uint256[] public stageAllocations = [
        300000 * 10**18, // Stage 1 allocation (30%)
        400000 * 10**18, // Stage 2 allocation (40%)
        300000 * 10**18  // Stage 3 allocation (30%)
    ];

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 cost);

    // Constructor
    constructor() {
        owner = msg.sender;
    }

    // Modifier to enforce owner-only actions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Function to purchase tokens during presale
    function purchaseTokens(uint256 tokenAmount) external payable {
        require(presaleStage < MAX_STAGE, "Presale has ended");
        require(tokenAmount > 0, "Token amount must be greater than zero");
        require(tokensSold + tokenAmount <= stageAllocations[presaleStage], "Requested tokens exceed stage allocation");
        
        // Calculate the cost of tokens
        uint256 cost = tokenAmount * stagePrices[presaleStage];
        require(msg.value >= cost, "Insufficient funds sent");

        // Update tokensSold
        tokensSold += tokenAmount;

        // Check if the current stage allocation has been exhausted
        if (tokensSold == stageAllocations[presaleStage]) {
            presaleStage++; // Move to the next stage
        }

        // Emit purchase event
        emit TokensPurchased(msg.sender, tokenAmount, cost);
    }

    // Function to withdraw funds collected during presale (Owner-only)
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner).transfer(balance);
    }

    // Function to end the presale manually (Owner-only)
    function endPresale() external onlyOwner {
        presaleStage = MAX_STAGE; // Mark presale as ended
    }

    // Fallback function to prevent accidental ETH transfers
    fallback() external payable {
        revert("Direct transfers not allowed");
    }

    // Receive function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct transfers not allowed");
    }
}
```
