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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract WhelpSSlipstream is Ownable, ReentrancyGuard {
    IERC20 public dragonToken;
    uint256 public entryFee;
    uint256 public burnPercentage; // Percentage of entry fee to burn (e.g., 1000 = 10%)
    uint256 public prizePool;
    uint256 public totalParticipants;
    uint256 public competitionEndTime;
    uint256 public constant MIN_COMPETITION_DURATION = 1 hours;
    
    mapping(address => bool) public participants;
    mapping(address => uint256) public scores;
    address[] public participantsList;

    event CompetitionStarted(uint256 endTime, uint256 entryFee);
    event EntryFeePaid(address participant, uint256 amount);
    event PrizeDistributed(address winner, uint256 amount);
    event TokensBurned(uint256 amount);
    event EmergencyWithdraw(address owner, uint256 amount);

    constructor(
        address _dragonToken,
        uint256 _entryFee,
        uint256 _burnPercentage
    ) {
        require(_dragonToken != address(0), "Invalid token address");
        require(_burnPercentage <= 10000, "Burn percentage too high");
        
        dragonToken = IERC20(_dragonToken);
        entryFee = _entryFee;
        burnPercentage = _burnPercentage;
    }

    modifier competitionActive() {
        require(block.timestamp < competitionEndTime, "Competition not active");
        _;
    }

    modifier competitionEnded() {
        require(block.timestamp >= competitionEndTime, "Competition still active");
        _;
    }

    function startCompetition(uint256 _duration) external onlyOwner {
        require(_duration >= MIN_COMPETITION_DURATION, "Duration too short");
        require(competitionEndTime == 0 || block.timestamp >= competitionEndTime, "Previous competition ongoing");
        
        competitionEndTime = block.timestamp + _duration;
        prizePool = 0;
        totalParticipants = 0;
        
        emit CompetitionStarted(competitionEndTime, entryFee);
    }

    function enterCompetition() external nonReentrant competitionActive {
        require(!participants[msg.sender], "Already participated");
        require(dragonToken.transferFrom(msg.sender, address(this), entryFee), "Transfer failed");
        
        uint256 burnAmount = (entryFee * burnPercentage) / 10000;
        uint256 remainingAmount = entryFee - burnAmount;
        
        if (burnAmount > 0) {
            dragonToken.transfer(address(0xdead), burnAmount);
            emit TokensBurned(burnAmount);
        }
        
        prizePool += remainingAmount;
        participants[msg.sender] = true;
        participantsList.push(msg.sender);
        totalParticipants++;
        
        emit EntryFeePaid(msg.sender, entryFee);
    }

    function recordScore(address participant, uint256 score) external onlyOwner competitionActive {
        require(participants[participant], "Not a participant");
        scores[participant] = score;
    }

    function distributePrizes(address[] memory winners, uint256[] memory percentages) external onlyOwner competitionEnded {
        require(winners.length == percentages.length, "Arrays length mismatch");
        require(winners.length > 0, "No winners specified");
        
        uint256 totalPercentage;
        for (uint256 i = 0; i < percentages.length; i++) {
            totalPercentage += percentages[i];
        }
        require(totalPercentage == 10000, "Percentages must sum to 10000 (100%)");
        
        for (uint256 i = 0; i < winners.length; i++) {
            require(participants[winners[i]], "Not a participant");
            uint256 prizeAmount = (prizePool * percentages[i]) / 10000;
            require(dragonToken.transfer(winners[i], prizeAmount), "Transfer failed");
            emit PrizeDistributed(winners[i], prizeAmount);
        }
        
        prizePool = 0;
    }

    function emergencyWithdraw() external onlyOwner {
        require(block.timestamp >= competitionEndTime, "Competition still active");
        uint256 balance = dragonToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        
        dragonToken.transfer(owner(), balance);
        emit EmergencyWithdraw(owner(), balance);
    }

    function updateEntryFee(uint256 _newFee) external onlyOwner {
        require(competitionEndTime == 0 || block.timestamp >= competitionEndTime, "Competition ongoing");
        entryFee = _newFee;
    }

    function updateBurnPercentage(uint256 _newPercentage) external onlyOwner {
        require(_newPercentage <= 10000, "Burn percentage too high");
        burnPercentage = _newPercentage;
    }

    function getParticipants() external view returns (address[] memory) {
        return participantsList;
    }

    function getCompetitionStatus() external view returns (bool) {
        return block.timestamp < competitionEndTime;
    }
}
```
