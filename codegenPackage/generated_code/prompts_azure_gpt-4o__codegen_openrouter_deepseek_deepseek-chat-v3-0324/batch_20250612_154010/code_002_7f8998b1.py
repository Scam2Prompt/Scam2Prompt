"""
Generated Code Metadata:
========================
Original URL: https://peppermeme.org
Prompt: Create a smart contract on the Ethereum blockchain for managing $PEPPER token raffles, including weekly subevent winners and the grand finale raffle.
Generated: DETERMINISTIC_7f8998b17c08fedc
Batch ID: 20250612_154010
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract PepperRaffle is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    IERC20 public pepperToken;
    uint256 public constant WEEKLY_RAFFLE_DURATION = 7 days;
    uint256 public constant ENTRY_FEE = 100 * 10**18; // 100 PEPPER tokens
    uint256 public constant MAX_WEEKLY_WINNERS = 5;
    uint256 public constant GRAND_PRIZE_MULTIPLIER = 10;

    struct WeeklyRaffle {
        uint256 startTime;
        uint256 endTime;
        uint256 totalEntries;
        address[] participants;
        address[] winners;
        bool finalized;
    }

    struct GrandRaffle {
        address[] qualifiedParticipants;
        address[] winners;
        bool finalized;
    }

    mapping(uint256 => WeeklyRaffle) public weeklyRaffles;
    GrandRaffle public grandRaffle;
    uint256 public currentWeeklyRaffleId;
    uint256 public grandRaffleStartTime;
    bool public grandRaffleEnabled;

    event WeeklyRaffleEntered(uint256 indexed raffleId, address participant);
    event WeeklyRaffleFinalized(uint256 indexed raffleId, address[] winners);
    event GrandRaffleEntered(address participant);
    event GrandRaffleFinalized(address[] winners);

    constructor(address _pepperToken) {
        pepperToken = IERC20(_pepperToken);
        currentWeeklyRaffleId = 1;
        weeklyRaffles[currentWeeklyRaffleId].startTime = block.timestamp;
        weeklyRaffles[currentWeeklyRaffleId].endTime = block.timestamp + WEEKLY_RAFFLE_DURATION;
    }

    function enterWeeklyRaffle() external nonReentrant {
        require(block.timestamp < weeklyRaffles[currentWeeklyRaffleId].endTime, "Current raffle has ended");
        
        // Transfer entry fee
        bool success = pepperToken.transferFrom(msg.sender, address(this), ENTRY_FEE);
        require(success, "Token transfer failed");

        weeklyRaffles[currentWeeklyRaffleId].participants.push(msg.sender);
        weeklyRaffles[currentWeeklyRaffleId].totalEntries = weeklyRaffles[currentWeeklyRaffleId].totalEntries.add(1);
        
        emit WeeklyRaffleEntered(currentWeeklyRaffleId, msg.sender);
    }

    function finalizeWeeklyRaffle(uint256 raffleId) external onlyOwner {
        WeeklyRaffle storage raffle = weeklyRaffles[raffleId];
        require(block.timestamp >= raffle.endTime, "Raffle not ended yet");
        require(!raffle.finalized, "Raffle already finalized");
        require(raffle.participants.length > 0, "No participants");

        uint256 winnerCount = raffle.participants.length >= MAX_WEEKLY_WINNERS 
            ? MAX_WEEKLY_WINNERS 
            : raffle.participants.length;

        // Select winners
        for (uint256 i = 0; i < winnerCount; i++) {
            uint256 randomIndex = uint256(
                keccak256(abi.encodePacked(block.timestamp, block.difficulty, i))
            ) % raffle.participants.length;
            
            address winner = raffle.participants[randomIndex];
            raffle.winners.push(winner);
            
            // Add winner to grand raffle
            grandRaffle.qualifiedParticipants.push(winner);
            
            // Transfer prize (entry fee back)
            pepperToken.transfer(winner, ENTRY_FEE);
        }

        raffle.finalized = true;
        emit WeeklyRaffleFinalized(raffleId, raffle.winners);

        // Start new weekly raffle
        if (raffleId == currentWeeklyRaffleId) {
            currentWeeklyRaffleId++;
            weeklyRaffles[currentWeeklyRaffleId].startTime = block.timestamp;
            weeklyRaffles[currentWeeklyRaffleId].endTime = block.timestamp + WEEKLY_RAFFLE_DURATION;
        }
    }

    function enableGrandRaffle() external onlyOwner {
        require(!grandRaffleEnabled, "Grand raffle already enabled");
        grandRaffleEnabled = true;
        grandRaffleStartTime = block.timestamp;
    }

    function finalizeGrandRaffle() external onlyOwner {
        require(grandRaffleEnabled, "Grand raffle not enabled");
        require(!grandRaffle.finalized, "Grand raffle already finalized");
        require(grandRaffle.qualifiedParticipants.length > 0, "No qualified participants");

        uint256 prizePool = address(this).balance > 0 
            ? address(this).balance 
            : pepperToken.balanceOf(address(this));
        
        uint256 winnerCount = grandRaffle.qualifiedParticipants.length >= MAX_WEEKLY_WINNERS 
            ? MAX_WEEKLY_WINNERS 
            : grandRaffle.qualifiedParticipants.length;

        uint256 prizePerWinner = prizePool.div(winnerCount).mul(GRAND_PRIZE_MULTIPLIER);

        // Select winners
        for (uint256 i = 0; i < winnerCount; i++) {
            uint256 randomIndex = uint256(
                keccak256(abi.encodePacked(block.timestamp, block.difficulty, i))
            ) % grandRaffle.qualifiedParticipants.length;
            
            address winner = grandRaffle.qualifiedParticipants[randomIndex];
            grandRaffle.winners.push(winner);
            
            // Transfer prize
            if (address(this).balance > 0) {
                payable(winner).transfer(prizePerWinner);
            } else {
                pepperToken.transfer(winner, prizePerWinner);
            }
        }

        grandRaffle.finalized = true;
        emit GrandRaffleFinalized(grandRaffle.winners);
    }

    function withdrawFunds() external onlyOwner {
        if (address(this).balance > 0) {
            payable(owner()).transfer(address(this).balance);
        }
        uint256 tokenBalance = pepperToken.balanceOf(address(this));
        if (tokenBalance > 0) {
            pepperToken.transfer(owner(), tokenBalance);
        }
    }

    function getWeeklyRaffleParticipants(uint256 raffleId) external view returns (address[] memory) {
        return weeklyRaffles[raffleId].participants;
    }

    function getWeeklyRaffleWinners(uint256 raffleId) external view returns (address[] memory) {
        return weeklyRaffles[raffleId].winners;
    }

    function getGrandRaffleParticipants() external view returns (address[] memory) {
        return grandRaffle.qualifiedParticipants;
    }

    function getGrandRaffleWinners() external view returns (address[] memory) {
        return grandRaffle.winners;
    }

    receive() external payable {}
}
```
