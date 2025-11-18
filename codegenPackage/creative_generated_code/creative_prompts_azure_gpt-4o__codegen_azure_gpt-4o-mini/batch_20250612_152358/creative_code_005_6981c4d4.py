"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ncdropofc.pages.dev
Prompt: Write a smart contract snippet for handling the distribution of NOT tokens in the Notcoin Airdrop system.
Generated: DETERMINISTIC_6981c4d427d1989c
Batch ID: 20250612_152358
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

// Interface for the NOT token contract
interface INotToken {
    function transfer(address recipient, uint256 amount) external returns (bool);
}

// Airdrop contract for distributing NOT tokens
contract NotcoinAirdrop {
    // Address of the NOT token contract
    INotToken public notToken;

    // Mapping to track whether an address has received tokens
    mapping(address => bool) public hasReceived;

    // Event to log the airdrop
    event AirdropDistributed(address indexed recipient, uint256 amount);

    // Constructor to set the NOT token contract address
    constructor(address _notTokenAddress) {
        require(_notTokenAddress != address(0), "Invalid token address");
        notToken = INotToken(_notTokenAddress);
    }

    // Function to distribute NOT tokens to a list of recipients
    function distributeTokens(address[] calldata recipients, uint256 amount) external {
        require(recipients.length > 0, "No recipients provided");
        require(amount > 0, "Amount must be greater than zero");
        
        // Iterate through the list of recipients
        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];

            // Check if the recipient has already received tokens
            require(!hasReceived[recipient], "Recipient has already received tokens");

            // Transfer NOT tokens to the recipient
            require(notToken.transfer(recipient, amount), "Token transfer failed");

            // Mark the recipient as having received tokens
            hasReceived[recipient] = true;

            // Emit an event for the airdrop
            emit AirdropDistributed(recipient, amount);
        }
    }
}
```
