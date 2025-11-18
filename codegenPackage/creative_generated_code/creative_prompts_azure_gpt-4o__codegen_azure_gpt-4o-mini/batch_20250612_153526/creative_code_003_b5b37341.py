"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://javierlinked-consensys.vercel.app
Prompt: Provide an example of a Solidity function to allow users to purchase tokens for an event, ensuring the maximum ticket limit per person is enforced.
Generated: DETERMINISTIC_b5b3734119200811
Batch ID: 20250612_153526
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
    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed purchaser, uint256 amount);

    // Mapping to track the number of tickets purchased by each user
    mapping(address => uint256) private _purchases;

    // Maximum number of tickets a user can buy
    uint256 public constant MAX_TICKETS_PER_USER = 5;

    // Total supply of tokens available for purchase
    uint256 public constant TOTAL_TOKENS = 1000;
    uint256 public totalTokensSold;

    // Purchase function to buy tokens for the event
    function buyTokens(uint256 amount) external {
        // Validate the amount of tokens requested
        require(amount > 0, "Amount must be greater than 0");
        require(totalTokensSold + amount <= TOTAL_TOKENS, "Not enough tokens available");

        // Check if the user has already purchased tokens
        require(_purchases[msg.sender] + amount <= MAX_TICKETS_PER_USER, "Exceeds maximum ticket limit");

        // Update the total tokens sold and the purchaser's record
        totalTokensSold += amount;
        _purchases[msg.sender] += amount;

        // Emit event for successful purchase
        emit TokensPurchased(msg.sender, amount);
    }

    // Function to get the number of tickets purchased by a user
    function getPurchasedTickets() external view returns (uint256) {
        return _purchases[msg.sender];
    }
}
```
