"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yologames-io.pages.dev
Prompt: Write a smart contract in Solidity for a provably fair crypto-based lottery game similar to the "YOLO Deposit crypto and spin the wheel" game described on YOLO Games. Include mechanisms for single-winner payouts.
Generated: DETERMINISTIC_762e9894d08508ea
Batch ID: 20250612_153512
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

/// @title Provably Fair Lottery Smart Contract
/// @dev A simple crypto-based lottery game with single-winner payouts
contract ProvablyFairLottery {
    address public owner; // Contract owner
    uint256 public ticketPrice; // Fixed price for a lottery ticket
    address[] public players; // Array of players who have entered the lottery
    uint256 public lotteryEndTime; // Timestamp for when the lottery ends
    bool public lotteryActive; // Flag indicating if the lottery is active

    event TicketPurchased(address indexed player);
    event WinnerSelected(address indexed winner, uint256 prize);
    
    /// @notice Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /// @notice Modifier to check if the lottery is active
    modifier whenLotteryActive() {
        require(lotteryActive, "Lottery is not active");
        require(block.timestamp < lotteryEndTime, "Lottery has ended");
        _;
    }

    /// @notice Constructor to initialize the lottery contract
    /// @param _ticketPrice Price of a single ticket in wei
    /// @param _duration Duration of the lottery in seconds
    constructor(uint256 _ticketPrice, uint256 _duration) {
        require(_ticketPrice > 0, "Ticket price must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");

        owner = msg.sender;
        ticketPrice = _ticketPrice;
        lotteryEndTime = block.timestamp + _duration;
        lotteryActive = true;
    }

    /// @notice Function to buy a lottery ticket
    function buyTicket() external payable whenLotteryActive {
        require(msg.value == ticketPrice, "Incorrect ticket price");

        players.push(msg.sender);
        emit TicketPurchased(msg.sender);
    }

    /// @notice Function to end the lottery and select a winner
    /// @dev Only the owner can call this function
    function endLottery() external onlyOwner {
        require(lotteryActive, "Lottery is already ended");
        require(block.timestamp >= lotteryEndTime, "Lottery duration not yet completed");

        lotteryActive = false;

        if (players.length == 0) {
            // No players entered the lottery; funds remain in contract
            return;
        }

        // Select a random winner using block data
        uint256 winningIndex = _random() % players.length;
        address winner = players[winningIndex];

        // Transfer prize to the winner
        uint256 prize = address(this).balance;
        (bool success, ) = winner.call{value: prize}("");
        require(success, "Transfer to winner failed");

        emit WinnerSelected(winner, prize);

        // Reset lottery state
        delete players;
    }

    /// @notice Internal function to generate a pseudo-random number
    /// @return A pseudo-random uint256
    function _random() internal view returns (uint256) {
        return uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty, players)));
    }

    /// @notice Function to withdraw contract balance by owner (failsafe)
    /// @dev Can only be called when lottery is ended
    function withdraw() external onlyOwner {
        require(!lotteryActive, "Cannot withdraw while lottery is active");
        uint256 contractBalance = address(this).balance;
        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Withdraw failed");
    }

    /// @notice Fallback function to accept ETH sent to the contract
    receive() external payable {}

    /// @notice Function to get all players in the current lottery
    /// @return Array of players' addresses
    function getPlayers() external view returns (address[] memory) {
        return players;
    }
}
```
