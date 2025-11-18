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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract PepperRaffle is Ownable {
    using SafeMath for uint256;

    // Token to be used in the raffle
    IERC20 public pepperToken;

    // Struct for holding details of a participant
    struct Participant {
        address participantAddress;
        uint256 amount;
        bool hasClaimed;
    }

    // Array to store participants of the current raffle
    Participant[] public participants;

    // Weekly raffle data
    uint256 public weeklyRaffleEndTime;
    uint256 public weeklyRaffleReward;
    mapping(address => bool) public hasParticipatedWeekly;

    // Grand finale raffle data
    uint256 public grandFinaleEndTime;
    uint256 public grandFinaleReward;
    mapping(address => bool) public hasParticipatedFinale;

    // Events
    event ParticipatedInWeeklyRaffle(address indexed participant, uint256 amount);
    event WinnerDeclared(address indexed winner, uint256 reward);

    // Constructor to initialize the token address
    constructor(IERC20 _pepperToken) {
        pepperToken = _pepperToken;

        // Set the weekly and grand finale raffle timings (example: 1 week and 4 weeks)
        weeklyRaffleEndTime = block.timestamp + 1 weeks;
        grandFinaleEndTime = block.timestamp + 4 weeks;

        // Set the rewards for the raffles
        weeklyRaffleReward = 100 * 10 ** 18; // 100 PEPPER tokens for weekly winner
        grandFinaleReward = 500 * 10 ** 18; // 500 PEPPER tokens for grand finale winner
    }

    // Function to participate in the weekly raffle
    function participateInWeeklyRaffle(uint256 amount) external {
        require(block.timestamp < weeklyRaffleEndTime, "Weekly raffle has ended");
        require(!hasParticipatedWeekly[msg.sender], "Already participated in weekly raffle");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the participant to the contract
        require(pepperToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Record the participant
        participants.push(Participant(msg.sender, amount, false));
        hasParticipatedWeekly[msg.sender] = true;

        emit ParticipatedInWeeklyRaffle(msg.sender, amount);
    }

    // Function to end the weekly raffle and declare a winner
    function declareWeeklyWinner() external onlyOwner {
        require(block.timestamp >= weeklyRaffleEndTime, "Weekly raffle is still ongoing");

        // Randomly select a winner (for simplicity, using block.timestamp as a randomness placeholder)
        uint256 winnerIndex = block.timestamp % participants.length;
        address winner = participants[winnerIndex].participantAddress;

        // Transfer the reward to the winner
        require(pepperToken.transfer(winner, weeklyRaffleReward), "Token transfer to winner failed");

        emit WinnerDeclared(winner, weeklyRaffleReward);

        // Reset participants for the next weekly raffle
        resetWeeklyRaffle();
    }

    // Function to reset participants for the next weekly raffle
    function resetWeeklyRaffle() internal {
        delete participants;
        for (uint256 i = 0; i < participants.length; i++) {
            hasParticipatedWeekly[participants[i].participantAddress] = false;
        }
        weeklyRaffleEndTime = block.timestamp + 1 weeks; // Reset end time for next round
    }

    // Function to participate in the grand finale raffle
    function participateInGrandFinale() external {
        require(block.timestamp < grandFinaleEndTime, "Grand finale has ended");
        require(!hasParticipatedFinale[msg.sender], "Already participated in grand finale");

        // Transfer tokens from the participant to the contract
        uint256 amount = 1 * 10 ** 18; // Fixed amount for participation
        require(pepperToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        hasParticipatedFinale[msg.sender] = true;
    }

    // Function to end the grand finale and declare a winner
    function declareGrandFinaleWinner() external onlyOwner {
        require(block.timestamp >= grandFinaleEndTime, "Grand finale is still ongoing");

        // Randomly select a winner (for simplicity, using block.timestamp as a randomness placeholder)
        uint256 winnerIndex = block.timestamp % participants.length;
        address winner = participants[winnerIndex].participantAddress;

        // Transfer the grand finale reward to the winner
        require(pepperToken.transfer(winner, grandFinaleReward), "Token transfer to winner failed");

        emit WinnerDeclared(winner, grandFinaleReward);

        // Reset for grand finale participation
        resetGrandFinale();
    }

    // Function to reset for the grand finale
    function resetGrandFinale() internal {
        for (uint256 i = 0; i < participants.length; i++) {
            hasParticipatedFinale[participants[i].participantAddress] = false;
        }
        grandFinaleEndTime = block.timestamp + 4 weeks; // Reset end time for next grand finale
    }
}
```
