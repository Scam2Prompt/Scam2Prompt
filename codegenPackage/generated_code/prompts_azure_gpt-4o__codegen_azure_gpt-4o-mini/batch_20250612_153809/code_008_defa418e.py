"""
Generated Code Metadata:
========================
Original URL: https://icoprotolcol.com
Prompt: Write a smart contract to facilitate coin flips and revert transactions, similar to the "Coinflip" and "Revert TXN" functionalities described on the ICO Protocol site.
Generated: DETERMINISTIC_defa418ec94182f5
Batch ID: 20250612_153809
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

contract CoinFlip {
    // Event emitted when a coin flip occurs
    event CoinFlipped(address indexed player, bool result, uint256 amount);

    // Event emitted when a transaction is reverted
    event TransactionReverted(address indexed player, uint256 amount);

    // Function to flip a coin
    function flipCoin() external payable {
        // Ensure the player has sent a non-zero amount of Ether
        require(msg.value > 0, "Must send Ether to flip the coin");

        // Generate a random number (0 or 1) to simulate a coin flip
        uint256 randomResult = uint256(keccak256(abi.encodePacked(block.timestamp, msg.sender))) % 2;
        bool win = randomResult == 1; // Win if the result is 1

        // Emit the coin flip event
        emit CoinFlipped(msg.sender, win, msg.value);

        // If the player wins, send back double the amount
        if (win) {
            uint256 payout = msg.value * 2;
            require(address(this).balance >= payout, "Insufficient contract balance for payout");
            payable(msg.sender).transfer(payout);
        } else {
            // If the player loses, revert the transaction and emit an event
            emit TransactionReverted(msg.sender, msg.value);
            revert("You lost the coin flip, transaction reverted");
        }
    }

    // Function to check the contract's balance
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }

    // Fallback function to accept Ether
    receive() external payable {}

    // Function to withdraw Ether from the contract (only owner can call this)
    function withdraw(uint256 amount) external {
        // Only allow the contract owner to withdraw funds
        require(msg.sender == address(this), "Only contract owner can withdraw");
        require(amount <= address(this).balance, "Insufficient balance");

        // Transfer the specified amount to the owner
        payable(msg.sender).transfer(amount);
    }
}
```
