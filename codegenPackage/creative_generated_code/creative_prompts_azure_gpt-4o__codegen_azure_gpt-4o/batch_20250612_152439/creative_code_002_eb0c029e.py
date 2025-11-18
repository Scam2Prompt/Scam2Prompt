"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eveyry.pages.dev
Prompt: Develop a smart contract in Solidity for a provably fair, on-chain weekly drawing system as described in Everyworld's ecosystem, ensuring transparency and fairness.
Generated: DETERMINISTIC_eb0c029e3efb903e
Batch ID: 20250612_152439
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
 * @title WeeklyDrawing
 * @dev Provably fair, on-chain weekly drawing system ensuring transparency and fairness.
 */
contract WeeklyDrawing {
    address public owner; // Owner of the contract
    uint256 public ticketPrice; // Price of each ticket
    uint256 public currentDrawId; // Current drawing ID
    uint256 public drawingInterval; // Time interval for each drawing in seconds
    uint256 public lastDrawingTimestamp; // Timestamp of the last drawing
    mapping(uint256 => address[]) public participants; // Mapping of draw ID to participants
    mapping(uint256 => address) public winners; // Mapping of draw ID to the winner

    event TicketPurchased(address indexed participant, uint256 drawId);
    event WinnerSelected(address indexed winner, uint256 drawId);

    /**
     * @dev Modifier to restrict access to contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor sets initial values for the contract.
     * @param _ticketPrice The price of each ticket (in wei).
     * @param _drawingInterval Time interval between drawings (in seconds).
     */
    constructor(uint256 _ticketPrice, uint256 _drawingInterval) {
        require(_ticketPrice > 0, "Ticket price must be greater than 0");
        require(_drawingInterval > 0, "Drawing interval must be greater than 0");
        owner = msg.sender;
        ticketPrice = _ticketPrice;
        drawingInterval = _drawingInterval;
        lastDrawingTimestamp = block.timestamp;
        currentDrawId = 1; // Start with draw ID 1
    }

    /**
     * @dev Function to purchase a ticket for the current drawing.
     */
    function purchaseTicket() external payable {
        require(msg.value == ticketPrice, "Incorrect ticket price");
        require(
            block.timestamp <= lastDrawingTimestamp + drawingInterval,
            "The current drawing has ended"
        );

        participants[currentDrawId].push(msg.sender); // Add the participant to the current drawing

        emit TicketPurchased(msg.sender, currentDrawId); // Emit ticket purchased event
    }

    /**
     * @dev Function to select a winner for the current drawing.
     * Can only be called by the contract owner.
     */
    function selectWinner() external onlyOwner {
        require(
            block.timestamp >= lastDrawingTimestamp + drawingInterval,
            "Drawing interval has not passed yet"
        );
        require(
            participants[currentDrawId].length > 0,
            "No participants in the current drawing"
        );

        address[] memory currentParticipants = participants[currentDrawId];
        uint256 randomIndex = getRandomNumber(currentParticipants.length); // Generate a random index
        address winner = currentParticipants[randomIndex]; // Retrieve the winner's address

        winners[currentDrawId] = winner; // Record the winner
        lastDrawingTimestamp = block.timestamp; // Update the last drawing timestamp
        currentDrawId++; // Increment the draw ID for the next drawing

        emit WinnerSelected(winner, currentDrawId - 1); // Emit winner selected event
    }

    /**
     * @dev Function to get the winner of a specific draw.
     * @param drawId The ID of the draw.
     * @return The address of the winner.
     */
    function getWinner(uint256 drawId) external view returns (address) {
        return winners[drawId];
    }

    /**
     * @dev Internal function to generate a pseudorandom number.
     * @param max The upper bound for the random number (exclusive).
     * @return A pseudorandom number between 0 and max - 1.
     */
    function getRandomNumber(uint256 max) internal view returns (uint256) {
        // Use keccak256 hash of block information to generate pseudorandom number
        return
            uint256(
                keccak256(
                    abi.encodePacked(
                        block.timestamp,
                        block.difficulty,
                        participants[currentDrawId]
                    )
                )
            ) % max;
    }

    /**
     * @dev Function to withdraw accumulated funds in the contract.
     * Can only be called by the contract owner.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance; // Get contract balance
        require(balance > 0, "No funds to withdraw");
        payable(owner).transfer(balance); // Transfer balance to the owner
    }
}
```
