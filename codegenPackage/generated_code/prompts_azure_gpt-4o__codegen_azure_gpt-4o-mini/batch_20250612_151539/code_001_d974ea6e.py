"""
Generated Code Metadata:
========================
Original URL: https://whelps.io
Prompt: Develop a smart contract in Solidity to manage entry fees and prize distribution for the competitive mode of WhelpS: Slipstream, including a mechanism to burn a portion of the Dragon tokens.
Generated: DETERMINISTIC_d974ea6e8b2b70ad
Batch ID: 20250612_151539
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for managing entry fees and prize distribution
contract WhelpSlipstream is Ownable {
    // State variables
    IERC20 public dragonToken; // The Dragon token contract
    uint256 public entryFee; // Entry fee for the competitive mode
    uint256 public burnPercentage; // Percentage of tokens to burn from entry fees
    address[] public participants; // List of participants in the competition
    mapping(address => bool) public hasEntered; // Track if an address has entered

    // Event declarations
    event EntryFeePaid(address indexed participant, uint256 amount);
    event PrizeDistributed(address indexed winner, uint256 prizeAmount);
    event TokensBurned(uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _dragonToken, uint256 _entryFee, uint256 _burnPercentage) {
        require(_burnPercentage <= 100, "Burn percentage must be between 0 and 100");
        dragonToken = _dragonToken;
        entryFee = _entryFee;
        burnPercentage = _burnPercentage;
    }

    // Function to enter the competition
    function enterCompetition() external {
        require(!hasEntered[msg.sender], "You have already entered the competition");
        require(dragonToken.balanceOf(msg.sender) >= entryFee, "Insufficient balance to pay entry fee");

        // Transfer entry fee from participant to the contract
        dragonToken.transferFrom(msg.sender, address(this), entryFee);
        
        // Calculate burn amount
        uint256 burnAmount = (entryFee * burnPercentage) / 100;
        uint256 prizeAmount = entryFee - burnAmount;

        // Burn the specified amount of tokens
        _burnTokens(burnAmount);

        // Add participant to the list
        participants.push(msg.sender);
        hasEntered[msg.sender] = true;

        emit EntryFeePaid(msg.sender, entryFee);
    }

    // Internal function to burn tokens
    function _burnTokens(uint256 amount) internal {
        require(amount > 0, "Burn amount must be greater than zero");
        require(dragonToken.balanceOf(address(this)) >= amount, "Insufficient tokens to burn");

        // Transfer tokens to the zero address to burn them
        dragonToken.transfer(address(0), amount);
        emit TokensBurned(amount);
    }

    // Function to distribute prizes to the winner
    function distributePrize(address winner) external onlyOwner {
        require(hasEntered[winner], "Winner has not entered the competition");
        
        // Calculate total prize amount
        uint256 totalPrize = (entryFee * participants.length) - (entryFee * burnPercentage / 100);
        
        // Transfer prize to the winner
        require(dragonToken.balanceOf(address(this)) >= totalPrize, "Insufficient funds in contract to distribute prize");
        dragonToken.transfer(winner, totalPrize);

        emit PrizeDistributed(winner, totalPrize);
    }

    // Function to get the list of participants
    function getParticipants() external view returns (address[] memory) {
        return participants;
    }

    // Function to reset the competition (only owner)
    function resetCompetition() external onlyOwner {
        delete participants;
        for (uint256 i = 0; i < participants.length; i++) {
            hasEntered[participants[i]] = false;
        }
    }
}
```
