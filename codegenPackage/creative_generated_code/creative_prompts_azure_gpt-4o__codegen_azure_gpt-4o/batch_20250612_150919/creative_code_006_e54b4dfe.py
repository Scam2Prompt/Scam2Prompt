"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lover-nobodyxyz.pages.dev
Prompt: Write a smart contract for managing NFT lotteries and verifying winners, referencing the features described on the Nobody Manifesto page.
Generated: DETERMINISTIC_e54b4dfedd23e894
Batch ID: 20250612_150919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, efficient, and well-documented smart contract written in Solidity for managing NFT lotteries and verifying winners:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title NFT Lottery Contract
 * @author Nobody Manifesto-inspired
 * @notice This contract allows users to participate in NFT lotteries and verifies winners.
 * @dev Follows modern Solidity practices and includes error handling.
 */
contract NFTLottery {
    // Structure to represent a lottery
    struct Lottery {
        uint256 id;
        string name;
        address nftContract;
        uint256 nftTokenId;
        uint256 ticketPrice;
        uint256 endTime;
        address winner;
        bool isClosed;
    }

    // State variables
    mapping(uint256 => Lottery) public lotteries; // Stores all lotteries by ID
    mapping(uint256 => address[]) public participants; // Stores participants for each lottery
    uint256 public lotteryCount; // Tracks the number of lotteries
    address public owner; // Contract owner

    // Events
    event LotteryCreated(uint256 lotteryId, string name, address nftContract, uint256 nftTokenId, uint256 ticketPrice, uint256 endTime);
    event TicketPurchased(uint256 lotteryId, address participant);
    event WinnerSelected(uint256 lotteryId, address winner);

    // Modifier to ensure only the owner can execute certain functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Modifier to ensure a lottery exists
    modifier lotteryExists(uint256 lotteryId) {
        require(lotteryId < lotteryCount, "Lottery does not exist");
        _;
    }

    // Modifier to ensure a lottery is still active
    modifier lotteryActive(uint256 lotteryId) {
        require(block.timestamp < lotteries[lotteryId].endTime, "Lottery has ended");
        require(!lotteries[lotteryId].isClosed, "Lottery is closed");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender;
    }

    /**
     * @notice Creates a new lottery
     * @param name Name of the lottery
     * @param nftContract Address of the NFT contract
     * @param nftTokenId ID of the NFT token
     * @param ticketPrice Price of each ticket (in wei)
     * @param duration Duration of the lottery (in seconds)
     */
    function createLottery(
        string memory name,
        address nftContract,
        uint256 nftTokenId,
        uint256 ticketPrice,
        uint256 duration
    ) external onlyOwner {
        require(duration > 0, "Duration must be greater than 0");

        uint256 lotteryId = lotteryCount++;
        lotteries[lotteryId] = Lottery({
            id: lotteryId,
            name: name,
            nftContract: nftContract,
            nftTokenId: nftTokenId,
            ticketPrice: ticketPrice,
            endTime: block.timestamp + duration,
            winner: address(0),
            isClosed: false
        });

        emit LotteryCreated(lotteryId, name, nftContract, nftTokenId, ticketPrice, block.timestamp + duration);
    }

    /**
     * @notice Allows users to purchase a ticket for a lottery
     * @param lotteryId ID of the lottery
     */
    function purchaseTicket(uint256 lotteryId) external payable lotteryExists(lotteryId) lotteryActive(lotteryId) {
        Lottery storage lottery = lotteries[lotteryId];

        require(msg.value == lottery.ticketPrice, "Incorrect ticket price");

        participants[lotteryId].push(msg.sender);

        emit TicketPurchased(lotteryId, msg.sender);
    }

    /**
     * @notice Selects a random winner for a lottery
     * @param lotteryId ID of the lottery
     */
    function selectWinner(uint256 lotteryId) external onlyOwner lotteryExists(lotteryId) {
        Lottery storage lottery = lotteries[lotteryId];

        require(block.timestamp >= lottery.endTime, "Lottery is still ongoing");
        require(!lottery.isClosed, "Winner already selected");
        require(participants[lotteryId].length > 0, "No participants in the lottery");

        // Generate a random index using keccak256 (not perfect randomness but sufficient for demonstration)
        uint256 randomIndex = uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty, participants[lotteryId]))) % participants[lotteryId].length;

        address winner = participants[lotteryId][randomIndex];
        lottery.winner = winner;
        lottery.isClosed = true;

        emit WinnerSelected(lotteryId, winner);
    }

    /**
     * @notice Withdraws funds collected from ticket sales
     * @dev Only callable by the owner
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        payable(owner).transfer(balance);
    }
}
```
