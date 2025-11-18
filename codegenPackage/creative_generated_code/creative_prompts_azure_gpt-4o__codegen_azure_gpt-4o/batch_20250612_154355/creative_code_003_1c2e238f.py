"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jellyesports.web.app
Prompt: Create a smart contract function for implementing a lottery system similar to Jellotto, ensuring compatibility with the $Jelly ecosystem.
Generated: DETERMINISTIC_1c2e238fc5bd4c50
Batch ID: 20250612_154355
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
 * @title Lottery System Smart Contract
 * @dev Implements a lottery system compatible with the $Jelly ecosystem.
 */

interface IJellyToken {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract JellyLottery {
    IJellyToken public jellyToken; // $Jelly token interface
    address public owner; // Owner of the contract
    uint256 public ticketPrice; // Price of one lottery ticket in $Jelly tokens
    address[] public participants; // List of participants

    // Events
    event TicketPurchased(address indexed participant);
    event WinnerSelected(address indexed winner, uint256 reward);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the lottery system.
     * @param _jellyTokenAddress Address of the $Jelly token smart contract.
     * @param _ticketPrice Price of one lottery ticket in $Jelly tokens.
     */
    constructor(address _jellyTokenAddress, uint256 _ticketPrice) {
        require(_jellyTokenAddress != address(0), "Invalid token address");
        require(_ticketPrice > 0, "Ticket price must be greater than zero");

        jellyToken = IJellyToken(_jellyTokenAddress);
        ticketPrice = _ticketPrice;
        owner = msg.sender;
    }

    /**
     * @dev Allows a participant to purchase a lottery ticket using $Jelly tokens.
     */
    function purchaseTicket() external {
        require(jellyToken.balanceOf(msg.sender) >= ticketPrice, "Insufficient $Jelly balance");
        require(jellyToken.transfer(address(this), ticketPrice), "Token transfer failed");

        participants.push(msg.sender);
        emit TicketPurchased(msg.sender);
    }

    /**
     * @dev Allows the owner to select a random winner and transfer the reward.
     * The reward is the total $Jelly tokens collected from ticket sales.
     */
    function selectWinner() external onlyOwner {
        require(participants.length > 0, "No participants in the lottery");

        // Pseudo-random number generation (not suitable for production!)
        uint256 randomIndex = uint256(
            keccak256(abi.encodePacked(block.timestamp, block.difficulty, participants))
        ) % participants.length;

        address winner = participants[randomIndex];
        uint256 reward = jellyToken.balanceOf(address(this));

        require(jellyToken.transfer(winner, reward), "Reward transfer failed");
        emit WinnerSelected(winner, reward);

        // Reset participants for the next round
        delete participants;
    }

    /**
     * @dev Allows the owner to change the ticket price.
     * @param _newTicketPrice The new ticket price in $Jelly tokens.
     */
    function setTicketPrice(uint256 _newTicketPrice) external onlyOwner {
        require(_newTicketPrice > 0, "Ticket price must be greater than zero");
        ticketPrice = _newTicketPrice;
    }

    /**
     * @dev Allows the owner to withdraw any remaining tokens in case of an emergency.
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = jellyToken.balanceOf(address(this));
        require(balance > 0, "No balance to withdraw");
        require(jellyToken.transfer(owner, balance), "Withdraw failed");
    }
}
```
