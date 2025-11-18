"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icoprotolcol.com
Prompt: Write a smart contract to facilitate coin flips and revert transactions, similar to the "Coinflip" and "Revert TXN" functionalities described on the ICO Protocol site.
Generated: DETERMINISTIC_defa418ec94182f5
Batch ID: 20250612_153809
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

contract CoinFlip {
    // Define the events to log coin flip results
    event CoinFlipped(address indexed player, bool result, uint256 amount);
    event TransactionReverted(address indexed player, uint256 amount);

    // Address of the contract owner
    address public owner;

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    // Function to perform a coin flip
    function flipCoin() external payable {
        // Ensure the player sent some Ether
        require(msg.value > 0, "Must send Ether to flip the coin");

        // Generate a random coin flip result (0 or 1)
        bool result = (block.timestamp % 2) == 0;

        // Emit the coin flip result
        emit CoinFlipped(msg.sender, result, msg.value);

        // If the result is heads (true), send the player back double their wager
        if (result) {
            uint256 payout = msg.value * 2;
            require(address(this).balance >= payout, "Insufficient contract balance for payout");
            (bool sent, ) = msg.sender.call{value: payout}("");
            require(sent, "Failed to send Ether");
        } else {
            // Log the transaction revert if the coin flip fails
            emit TransactionReverted(msg.sender, msg.value);
            // Revert the transaction to simulate loss
            revert("Coin flip lost, transaction reverted");
        }
    }

    // Function to withdraw funds from the contract (only owner can call this)
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance to withdraw");
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Failed to withdraw Ether");
    }

    // Fallback function to receive Ether
    receive() external payable {}

    // Function to check the contract's balance
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
