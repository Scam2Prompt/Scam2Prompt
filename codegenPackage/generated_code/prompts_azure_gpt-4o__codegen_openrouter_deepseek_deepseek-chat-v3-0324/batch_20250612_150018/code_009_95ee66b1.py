"""
Generated Code Metadata:
========================
Original URL: https://orange-pepe.pages.dev
Prompt: Create a smart contract for $ORPE token rewards distribution in the upcoming podcast or gaming competitions, ensuring transparency and fairness.
Generated: DETERMINISTIC_95ee66b1fb825ff0
Batch ID: 20250612_150018
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

contract ORPERewards is Ownable, ReentrancyGuard {
    IERC20 public orpeToken;
    
    struct Competition {
        string name;
        uint256 totalRewards;
        uint256 startTime;
        uint256 endTime;
        bool isActive;
        bool rewardsDistributed;
        mapping(address => uint256) participantScores;
        address[] participants;
    }
    
    mapping(uint256 => Competition) public competitions;
    uint256 public competitionCount;
    
    event CompetitionCreated(uint256 indexed competitionId, string name, uint256 totalRewards, uint256 startTime, uint256 endTime);
    event ParticipantAdded(uint256 indexed competitionId, address participant);
    event ScoreUpdated(uint256 indexed competitionId, address participant, uint256 score);
    event RewardsDistributed(uint256 indexed competitionId);
    
    constructor(address _orpeTokenAddress) {
        require(_orpeTokenAddress != address(0), "Invalid token address");
        orpeToken = IERC20(_orpeTokenAddress);
    }
    
    function createCompetition(
        string memory _name,
        uint256 _totalRewards,
        uint256 _startTime,
        uint256 _endTime
    ) external onlyOwner {
        require(_startTime < _endTime, "Invalid time range");
        require(_totalRewards > 0, "Rewards must be positive");
        
        uint256 competitionId = competitionCount++;
        Competition storage c = competitions[competitionId];
        
        c.name = _name;
        c.totalRewards = _totalRewards;
        c.startTime = _startTime;
        c.endTime = _endTime;
        c.isActive = true;
        
        emit CompetitionCreated(competitionId, _name, _totalRewards, _startTime, _endTime);
    }
    
    function addParticipant(uint256 _competitionId, address _participant) external onlyOwner {
        Competition storage c = competitions[_competitionId];
        require(c.isActive, "Competition not active");
        require(block.timestamp >= c.startTime && block.timestamp <= c.endTime, "Outside competition period");
        
        for (uint256 i = 0; i < c.participants.length; i++) {
            if (c.participants[i] == _participant) {
                revert("Participant already added");
            }
        }
        
        c.participants.push(_participant);
        c.participantScores[_participant] = 0;
        
        emit ParticipantAdded(_competitionId, _participant);
    }
    
    function updateScore(
        uint256 _competitionId,
        address _participant,
        uint256 _score
    ) external onlyOwner {
        Competition storage c = competitions[_competitionId];
        require(c.isActive, "Competition not active");
        require(block.timestamp >= c.startTime && block.timestamp <= c.endTime, "Outside competition period");
        
        bool participantExists = false;
        for (uint256 i = 0; i < c.participants.length; i++) {
            if (c.participants[i] == _participant) {
                participantExists = true;
                break;
            }
        }
        require(participantExists, "Participant not found");
        
        c.participantScores[_participant] = _score;
        
        emit ScoreUpdated(_competitionId, _participant, _score);
    }
    
    function distributeRewards(uint256 _competitionId) external onlyOwner nonReentrant {
        Competition storage c = competitions[_competitionId];
        require(c.isActive, "Competition not active");
        require(block.timestamp > c.endTime, "Competition not ended");
        require(!c.rewardsDistributed, "Rewards already distributed");
        require(c.participants.length > 0, "No participants");
        
        uint256 totalScores = 0;
        for (uint256 i = 0; i < c.participants.length; i++) {
            totalScores += c.participantScores[c.participants[i]];
        }
        require(totalScores > 0, "No scores recorded");
        
        uint256 contractBalance = orpeToken.balanceOf(address(this));
        require(contractBalance >= c.totalRewards, "Insufficient contract balance");
        
        for (uint256 i = 0; i < c.participants.length; i++) {
            address participant = c.participants[i];
            uint256 participantScore = c.participantScores[participant];
            uint256 reward = (c.totalRewards * participantScore) / totalScores;
            
            if (reward > 0) {
                require(orpeToken.transfer(participant, reward), "Transfer failed");
            }
        }
        
        c.rewardsDistributed = true;
        c.isActive = false;
        
        emit RewardsDistributed(_competitionId);
    }
    
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = orpeToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(orpeToken.transfer(owner(), balance), "Transfer failed");
    }
    
    function getParticipants(uint256 _competitionId) external view returns (address[] memory) {
        return competitions[_competitionId].participants;
    }
    
    function getParticipantScore(uint256 _competitionId, address _participant) external view returns (uint256) {
        return competitions[_competitionId].participantScores[_participant];
    }
}
```
