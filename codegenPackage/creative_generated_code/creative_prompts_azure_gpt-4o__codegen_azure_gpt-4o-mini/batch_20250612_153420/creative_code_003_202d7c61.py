"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-dogcoin.pages.dev
Prompt: Generate a Solidity function to enforce a presale cap of 1000 ETH for a token sale, ensuring that any transactions exceeding the cap are rejected.
Generated: DETERMINISTIC_202d7c616965d412
Batch ID: 20250612_153420
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

contract TokenSale {
    // State variable to store the total raised funds
    uint256 public totalRaised;

    // Constant for the presale cap
    uint256 public constant PRESALE_CAP = 1000 ether;

    // Event to log successful purchases
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Fallback function to allow receiving ETH
    receive() external payable {
        buyTokens();
    }

    // Function to buy tokens
    function buyTokens() public payable {
        // Ensure the transaction does not exceed the presale cap
        require(totalRaised + msg.value <= PRESALE_CAP, "Purchase exceeds presale cap");

        // Update the total raised amount
        totalRaised += msg.value;

        // Emit an event for the purchase
        emit TokensPurchased(msg.sender, msg.value);
    }

    // Function to withdraw funds (only owner should be able to withdraw)
    function withdrawFunds() external {
        // Logic for withdrawing funds (e.g., onlyOwner modifier can be added)
        // This function should be implemented for secure fund management
    }
}
```
