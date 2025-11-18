"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ututu.pages.dev
Prompt: Write a Solidity function that prevents purchases exceeding the presale cap of 1000 ETH and ensures accurate token allocation based on the specified exchange rate.
Generated: DETERMINISTIC_1ea1034207bca137
Batch ID: 20250612_152924
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
    // State variables
    uint256 public constant PRESALE_CAP = 1000 ether; // Presale cap in ETH
    uint256 public constant EXCHANGE_RATE = 100; // Exchange rate: 1 ETH = 100 Tokens
    uint256 public totalRaised; // Total ETH raised in presale
    mapping(address => uint256) public contributions; // Contributions by each address
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalSpent);

    // Modifier to check if the purchase does not exceed the presale cap
    modifier withinPresaleCap(uint256 _amount) {
        require(totalRaised + _amount <= PRESALE_CAP, "Purchase exceeds presale cap");
        _;
    }

    // Function to purchase tokens
    // The function accepts ETH and calculates the token allocation based on the exchange rate
    function purchaseTokens() external payable withinPresaleCap(msg.value) {
        // Ensure the transaction has sent ETH
        require(msg.value > 0, "Must send ETH to purchase tokens");

        // Update total raised amount
        totalRaised += msg.value;

        // Update the contribution of the sender
        contributions[msg.sender] += msg.value;

        // Calculate the number of tokens to be allocated
        uint256 tokenAmount = msg.value * EXCHANGE_RATE;

        // Emit an event for the purchase
        emit TokensPurchased(msg.sender, tokenAmount, msg.value);
    }

    // Function to withdraw funds (only for the contract owner, add ownership control as needed)
    function withdrawFunds(address payable _to) external {
        // Ensure that the caller is the owner (implement ownership logic as needed)
        require(msg.sender == address(this), "Only owner can withdraw funds");
        
        // Transfer the raised ETH to the specified address
        _to.transfer(address(this).balance);
    }

    // Fallback function to prevent accidental ETH transfers to the contract
    receive() external payable {
        revert("Direct ETH transfers not allowed. Use purchaseTokens method.");
    }
}
```
