"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peppermeme.org
Prompt: Create a smart contract on the Ethereum blockchain for managing $PEPPER token raffles, including weekly subevent winners and the grand finale raffle.
Generated: DETERMINISTIC_7f8998b17c08fedc
Batch ID: 20250612_154010
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
 * @title PEPPER Raffle Contract
 * @notice This smart contract manages weekly $PEPPER token raffles and a grand finale raffle.
 * @dev Ensure this contract is audited before deploying in a production environment.
 */

contract PepperRaffle {
    // State variables
    address public owner; // Contract owner
    uint256 public grandFinalePrize; // Grand finale prize in $PEPPER tokens
    uint256 public weeklyPrize; // Weekly prize in $PEPPER tokens
    uint256 public raffleEndTime; // End time for the grand finale raffle
    uint256 public weeklyRaffleInterval; // Interval between weekly raffles
    uint256 public lastWeeklyRaffleTime; // Timestamp of the last weekly raffle

    mapping(address => bool) public hasEntered; // Tracks participants
    address[] public participants; // List of participants for the raffle
    address[] public weeklyWinners; // List of weekly winners

    // ERC20-compatible $PEPPER token interface
    IERC20 public pepperToken;

    // Events
    event RaffleEntered(address indexed participant);
    event WeeklyWinnerSelected(address indexed winner, uint256 prizeAmount);
    event GrandFinaleWinnerSelected(address indexed winner, uint256 prizeAmount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier raffleOpen() {
        require(block.timestamp < raffleEndTime, "Raffle has ended");
        _;
    }

    // Constructor
    constructor(
        address _pepperTokenAddress,
        uint256 _weeklyPrize,
        uint256 _grandFinalePrize,
        uint256 _raffleDurationInDays,
        uint256 _weeklyIntervalInDays
    ) {
        owner = msg.sender; // Set contract owner
        pepperToken = IERC20(_pepperTokenAddress); // Set $PEPPER token contract address
        weeklyPrize = _weeklyPrize; // Set weekly prize
        grandFinalePrize = _grandFinalePrize; // Set grand finale prize
        raffleEndTime = block.timestamp + (_raffleDurationInDays * 1 days); // Set raffle end time
        weeklyRaffleInterval = _weeklyIntervalInDays * 1 days; // Set weekly raffle interval
        lastWeeklyRaffleTime = block.timestamp; // Initialize last weekly raffle timestamp
    }

    // Function to enter the raffle
    function enterRaffle() external raffleOpen {
        require(!hasEntered[msg.sender], "You have already entered the raffle");
        require(
            pepperToken.balanceOf(msg.sender) > 0,
            "You must hold $PEPPER tokens to enter"
        );

        participants.push(msg.sender); // Add participant to the list
        hasEntered[msg.sender] = true; // Mark participant as entered

        emit RaffleEntered(msg.sender); // Emit event
    }

    // Function to pick a weekly winner
    function pickWeeklyWinner() external onlyOwner {
        require(
            block.timestamp >= lastWeeklyRaffleTime + weeklyRaffleInterval,
            "Weekly raffle interval has not passed"
        );
        require(participants.length > 0, "No participants in the raffle");

        // Select random winner
        address winner = participants[getRandomIndex()];

        // Transfer weekly prize to the winner
        pepperToken.transfer(winner, weeklyPrize);

        weeklyWinners.push(winner); // Record winner
        lastWeeklyRaffleTime = block.timestamp; // Update last weekly raffle time

        emit WeeklyWinnerSelected(winner, weeklyPrize); // Emit event
    }

    // Function to pick the grand finale winner
    function pickGrandFinaleWinner() external onlyOwner {
        require(block.timestamp >= raffleEndTime, "Grand finale raffle not ready");
        require(participants.length > 0, "No participants in the raffle");

        // Select random winner
        address winner = participants[getRandomIndex()];

        // Transfer grand finale prize to the winner
        pepperToken.transfer(winner, grandFinalePrize);

        emit GrandFinaleWinnerSelected(winner, grandFinalePrize); // Emit event
    }

    // Internal function to generate random index
    function getRandomIndex() internal view returns (uint256) {
        return uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty, participants))) % participants.length;
    }

    // Function to withdraw tokens (owner only)
    function withdrawTokens(uint256 amount) external onlyOwner {
        pepperToken.transfer(owner, amount);
    }

    // Interface for ERC20 token compatibility
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }
}
```
