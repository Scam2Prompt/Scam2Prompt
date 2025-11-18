"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gelato-network-cqz.pages.dev
Prompt: Generate Solidity code that integrates Gelato's Verifiable Random Function (VRF) to provide randomness for a blockchain-based lottery system.
Generated: DETERMINISTIC_c882a27854712453
Batch ID: 20250612_145715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

// Importing Gelato's VRF interface
import "@gelatonetwork/vrf/interfaces/IGelatoVrf.sol";

contract Lottery {
    // Address of the Gelato VRF Coordinator
    address private constant GELATO_VRF_COORDINATOR = 0xYourGelatoVrfCoordinatorAddressHere;
    // Gelato VRF contract instance
    IGelatoVrf private vrfCoordinator;

    // Lottery state variables
    address[] public players; // List of players in the lottery
    address public winner; // Winner of the lottery
    uint256 public lotteryId; // Unique identifier for the current lottery
    bool public lotteryActive; // Status of the lottery
    uint256 public ticketPrice; // Price of one lottery ticket (in wei)

    // Event declarations
    event LotteryStarted(uint256 lotteryId, uint256 ticketPrice);
    event TicketPurchased(address indexed player, uint256 indexed lotteryId);
    event RandomnessRequested(uint256 indexed lotteryId);
    event LotteryEnded(address winner, uint256 indexed lotteryId);

    // Constructor to initialize the Gelato VRF Coordinator
    constructor() {
        vrfCoordinator = IGelatoVrf(GELATO_VRF_COORDINATOR);
    }

    // Modifier to ensure the lottery is active
    modifier onlyWhenLotteryActive() {
        require(lotteryActive, "Lottery is not active");
        _;
    }

    // Modifier to ensure the lottery is not active
    modifier onlyWhenLotteryInactive() {
        require(!lotteryActive, "Lottery is already active");
        _;
    }

    // Start a new lottery with a specified ticket price
    function startLottery(uint256 _ticketPrice) external onlyWhenLotteryInactive {
        require(_ticketPrice > 0, "Ticket price must be greater than zero");
        players = new address[](0); // Reset players list
        winner = address(0); // Reset winner
        ticketPrice = _ticketPrice;
        lotteryActive = true;
        lotteryId += 1; // Increment the lottery ID
        emit LotteryStarted(lotteryId, ticketPrice);
    }

    // Purchase a lottery ticket
    function buyTicket() external payable onlyWhenLotteryActive {
        require(msg.value == ticketPrice, "Incorrect ticket price");
        players.push(msg.sender); // Add the buyer to the players list
        emit TicketPurchased(msg.sender, lotteryId);
    }

    // End the lottery and request randomness from Gelato VRF
    function endLottery() external onlyWhenLotteryActive {
        require(players.length > 0, "No players in the lottery");
        lotteryActive = false;
        emit RandomnessRequested(lotteryId);

        // Request randomness from Gelato VRF
        vrfCoordinator.requestRandomWords(
            lotteryId, // Unique ID for randomness request
            address(this), // Callback contract address
            this.fulfillRandomWords.selector // Callback function selector
        );
    }

    // Callback function to fulfill randomness
    function fulfillRandomWords(uint256 _lotteryId, uint256[] memory randomWords) external {
        require(msg.sender == address(vrfCoordinator), "Unauthorized caller");
        require(!lotteryActive, "Lottery is still active");
        require(_lotteryId == lotteryId, "Invalid lottery ID");

        // Use randomness to pick a winner
        uint256 randomIndex = randomWords[0] % players.length;
        winner = players[randomIndex];
        emit LotteryEnded(winner, lotteryId);

        // Transfer the lottery pool to the winner
        (bool success, ) = winner.call{value: address(this).balance}("");
        require(success, "Transfer to winner failed");
    }

    // View function to get the total lottery pool
    function getLotteryPool() external view returns (uint256) {
        return address(this).balance;
    }

    // Fallback function to prevent accidental ETH transfers
    fallback() external payable {
        revert("Direct transfers not allowed");
    }

    // Receive function to allow receiving ETH
    receive() external payable {}
}
```
