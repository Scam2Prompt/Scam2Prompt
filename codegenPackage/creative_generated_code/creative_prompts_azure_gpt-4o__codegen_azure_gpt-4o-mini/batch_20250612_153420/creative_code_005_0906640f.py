"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://richpepe.vercel.app
Prompt: Create a Solidity contract for a lottery system tied to a meme-based cryptocurrency token, referencing the "Rich Pepe" special meme lottery concept.
Generated: DETERMINISTIC_0906640f2cb9e6eb
Batch ID: 20250612_153420
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

// Importing necessary OpenZeppelin contracts for security and standards
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Lottery contract
contract MemeLottery is Ownable {
    using SafeMath for uint256;

    // State variables
    IERC20 public memeToken; // The meme-based cryptocurrency token
    address[] public participants; // List of participants
    uint256 public lotteryEndTime; // End time of the lottery
    bool public lotteryActive; // Indicates if the lottery is active

    // Events
    event LotteryEntered(address indexed participant);
    event LotteryEnded(address indexed winner, uint256 prize);

    // Constructor to initialize the contract with the meme token address
    constructor(address _memeTokenAddress) {
        memeToken = IERC20(_memeTokenAddress);
    }

    // Function to start the lottery
    function startLottery(uint256 duration) external onlyOwner {
        require(!lotteryActive, "Lottery is already active");
        lotteryActive = true;
        lotteryEndTime = block.timestamp.add(duration);
        delete participants; // Clear participants for the new lottery
    }

    // Function to enter the lottery
    function enterLottery() external {
        require(lotteryActive, "Lottery is not active");
        require(block.timestamp < lotteryEndTime, "Lottery has ended");

        // Transfer a certain amount of meme tokens as ticket
        uint256 ticketPrice = 1 * 10**18; // Assuming ticket price is 1 token
        memeToken.transferFrom(msg.sender, address(this), ticketPrice);

        participants.push(msg.sender); // Add participant to the list
        emit LotteryEntered(msg.sender);
    }

    // Function to end the lottery and pick a winner
    function endLottery() external onlyOwner {
        require(lotteryActive, "Lottery is not active");
        require(block.timestamp >= lotteryEndTime, "Lottery is still ongoing");
        require(participants.length > 0, "No participants in the lottery");

        lotteryActive = false; // Mark lottery as inactive

        // Pseudorandom winner selection
        uint256 winnerIndex = random() % participants.length;
        address winner = participants[winnerIndex];

        // Calculate the prize amount (total tokens collected)
        uint256 prizeAmount = memeToken.balanceOf(address(this));
        require(prizeAmount > 0, "No prize available");

        // Transfer prize to winner
        memeToken.transfer(winner, prizeAmount);
        emit LotteryEnded(winner, prizeAmount);
    }

    // Internal function for random number generation (basic approach)
    function random() internal view returns (uint256) {
        return uint256(keccak256(abi.encodePacked(block.difficulty, block.timestamp, participants)));
    }

    // Function to withdraw funds in case of emergency (only owner)
    function withdrawTokens() external onlyOwner {
        uint256 balance = memeToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        memeToken.transfer(owner(), balance);
    }
}
```
