"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld.pages.dev
Prompt: Develop a smart contract in Solidity for a provably fair, on-chain drawing system similar to Everyworld’s weekly token drawing mechanism.
Generated: DETERMINISTIC_c3f08c9bd56ef8ac
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

contract FairDrawing {
    address public owner;
    uint256 public drawingCount;
    uint256 public ticketPrice;
    
    // Struct to hold entries
    struct Entry {
        address participant;
        uint256 amount;
    }

    // Mapping to hold entries for each drawing
    mapping(uint256 => Entry[]) public entries;

    // Event to notify when a drawing occurs
    event DrawingConducted(uint256 indexed drawingId, address winner, uint256 prizeAmount);

    // Constructor to initialize parameters
    constructor(uint256 _ticketPrice) {
        require(_ticketPrice > 0, "Ticket price must be greater than zero");
        owner = msg.sender;
        ticketPrice = _ticketPrice;
        drawingCount = 0;
    }

    // Function to enter the drawing
    function enterDrawing() external payable {
        require(msg.value == ticketPrice, "Incorrect amount sent");

        // Add entry
        entries[drawingCount].push(Entry({
            participant: msg.sender,
            amount: msg.value
        }));
    }

    // Function to conduct the drawing
    function conductDrawing() external onlyOwner {
        require(entries[drawingCount].length > 0, "No entries in this drawing");

        // Randomly select a winner
        uint256 winnerIndex = random() % entries[drawingCount].length;
        address winner = entries[drawingCount][winnerIndex].participant;
        uint256 totalPrize = address(this).balance;

        // Transfer the prize to the winner
        (bool success, ) = winner.call{value: totalPrize}("");
        require(success, "Transfer failed");

        // Emit event for the drawing
        emit DrawingConducted(drawingCount, winner, totalPrize);

        // Prepare for the next drawing
        drawingCount++;
    }

    // Function to get the current balance of the contract
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    // Function to generate a random number (not secure for production use)
    function random() private view returns (uint256) {
        return uint256(keccak256(abi.encodePacked(block.difficulty, block.timestamp, entries[drawingCount].length)));
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Fallback function to accept Ether
    receive() external payable {}

    // Function to withdraw funds in case of emergency (only owner)
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }
}
```
