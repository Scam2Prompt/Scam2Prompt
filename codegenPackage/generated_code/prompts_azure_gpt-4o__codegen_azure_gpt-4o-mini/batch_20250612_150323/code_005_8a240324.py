"""
Generated Code Metadata:
========================
Original URL: https://cryptotitties.fun
Prompt: Provide an example of a Solidity contract for a prize wallet system, similar to the MotorBoat Prize Wallet described on the CryptoTitties webpage.
Generated: DETERMINISTIC_8a240324b21bd7a6
Batch ID: 20250612_150323
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Contract for a Prize Wallet System
contract PrizeWallet is Ownable {
    using SafeMath for uint256;

    // Event emitted when a prize is added
    event PrizeAdded(uint256 indexed prizeId, string prizeName, uint256 amount);
    
    // Event emitted when a prize is claimed
    event PrizeClaimed(uint256 indexed prizeId, address indexed winner);

    // Struct to represent a prize
    struct Prize {
        string name;        // Name of the prize
        uint256 amount;     // Amount of the prize in wei
        bool claimed;       // Status of the prize
    }

    // Mapping to store prizes by their ID
    mapping(uint256 => Prize) public prizes;
    uint256 public prizeCount; // Counter for the number of prizes

    // Modifier to check if the prize exists and is unclaimed
    modifier prizeExists(uint256 prizeId) {
        require(prizes[prizeId].amount > 0, "Prize does not exist");
        require(!prizes[prizeId].claimed, "Prize already claimed");
        _;
    }

    // Function to add a new prize to the wallet
    function addPrize(string memory prizeName, uint256 amount) external onlyOwner {
        require(amount > 0, "Prize amount must be greater than zero");

        // Increment the prize count
        prizeCount = prizeCount.add(1);

        // Create a new prize and store it in the mapping
        prizes[prizeCount] = Prize({
            name: prizeName,
            amount: amount,
            claimed: false
        });

        emit PrizeAdded(prizeCount, prizeName, amount);
    }

    // Function to claim a prize
    function claimPrize(uint256 prizeId) external prizeExists(prizeId) {
        // Mark the prize as claimed
        prizes[prizeId].claimed = true;

        // Transfer the prize amount to the winner
        (bool success, ) = msg.sender.call{value: prizes[prizeId].amount}("");
        require(success, "Transfer failed");

        emit PrizeClaimed(prizeId, msg.sender);
    }

    // Function to withdraw funds from the contract (only owner)
    function withdraw(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient balance");

        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
    }

    // Function to receive Ether. msg.data must be empty
    receive() external payable {}

    // Function to receive Ether. msg.data must not be empty
    fallback() external payable {}
}
```
