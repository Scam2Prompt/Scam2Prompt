"""
Generated Code Metadata:
========================
Original URL: https://whelps.io
Prompt: "Design a game mode for a blockchain-based racing game like Slipstream, including a tokenomics system for earning and using Dragon tokens."
Generated: DETERMINISTIC_3e024e3642230c39
Batch ID: 20250622_205211
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

contract DragonToken is ERC20, Ownable, Pausable {
    uint256 public constant MAX_SUPPLY = 100000000 * 10**18; // 100 million tokens
    uint256 public constant REWARD_RATE = 10 * 10**18; // 10 tokens per race completion
    
    mapping(address => bool) public approvedRacingContracts;
    
    constructor() ERC20("Dragon Token", "DRGN") {
        _mint(msg.sender, MAX_SUPPLY * 20 / 100); // Initial distribution (20%)
    }
    
    modifier onlyApprovedContracts() {
        require(approvedRacingContracts[msg.sender], "Caller is not approved");
        _;
    }
    
    function approveRacingContract(address contractAddress) external onlyOwner {
        approvedRacingContracts[contractAddress] = true;
    }
    
    function revokeRacingContract(address contractAddress) external onlyOwner {
        approvedRacingContracts[contractAddress] = false;
    }
    
    function awardTokens(address recipient) external onlyApprovedContracts whenNotPaused {
        _mint(recipient, REWARD_RATE);
    }
    
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }
    
    function pause() external onlyOwner {
        _pause();
    }
    
    function unpause() external onlyOwner {
        _unpause();
    }
}

contract RacingGame is Ownable, Pausable {
    DragonToken public dragonToken;
    
    struct Race {
        uint256 entryFee;
        uint256 prizePool;
        uint256 maxParticipants;
        uint256 startTime;
        bool isActive;
        address[] participants;
    }
    
    struct PlayerStats {
        uint256 racesCompleted;
        uint256 tokensEarned;
        uint256 tokensSpent;
    }
    
    mapping(uint256 => Race) public races;
    mapping(address => PlayerStats) public playerStats;
    uint256 public raceCount;
    
    event RaceCreated(uint256 raceId, uint256 entryFee, uint256 maxParticipants);
    event RaceJoined(uint256 raceId, address player);
    event RaceCompleted(uint256 raceId, address winner);
    
    constructor(address tokenAddress) {
        dragonToken = DragonToken(tokenAddress);
    }
    
    function createRace(uint256 entryFee, uint256 maxParticipants) external onlyOwner {
        require(entryFee > 0, "Entry fee must be positive");
        require(maxParticipants > 1, "Need at least 2 participants");
        
        uint256 raceId = raceCount++;
        races[raceId] = Race({
            entryFee: entryFee,
            prizePool: 0,
            maxParticipants: maxParticipants,
            startTime: block.timestamp + 1 hours,
            isActive: true,
            participants: new address[](0)
        });
        
        emit RaceCreated(raceId, entryFee, maxParticipants);
    }
    
    function joinRace(uint256 raceId) external whenNotPaused {
        Race storage race = races[raceId];
        require(race.isActive, "Race is not active");
        require(block.timestamp < race.startTime, "Race has already started");
        require(race.participants.length < race.maxParticipants, "Race is full");
        
        dragonToken.transferFrom(msg.sender, address(this), race.entryFee);
        race.prizePool += race.entryFee;
        race.participants.push(msg.sender);
        
        emit RaceJoined(raceId, msg.sender);
    }
    
    function completeRace(uint256 raceId, address winner) external onlyOwner {
        Race storage race = races[raceId];
        require(race.isActive, "Race is not active");
        require(block.timestamp >= race.startTime, "Race hasn't started yet");
        
        // Verify winner is a participant
        bool isParticipant = false;
        for (uint i = 0; i < race.participants.length; i++) {
            if (race.participants[i] == winner) {
                isParticipant = true;
                break;
            }
        }
        require(isParticipant, "Winner must be a participant");
        
        // Distribute rewards
        uint256 prize = race.prizePool * 80 / 100; // 80% to winner
        uint256 burnAmount = race.prizePool * 10 / 100; // 10% burned
        uint256 devCut = race.prizePool - prize - burnAmount; // 10% to dev
        
        dragonToken.transfer(winner, prize);
        dragonToken.burn(burnAmount);
        dragonToken.transfer(owner(), devCut);
        
        // Award participation tokens
        for (uint i = 0; i < race.participants.length; i++) {
            dragonToken.awardTokens(race.participants[i]);
            playerStats[race.participants[i]].racesCompleted++;
            playerStats[race.participants[i]].tokensEarned += DragonToken.REWARD_RATE;
        }
        
        playerStats[winner].tokensEarned += prize;
        race.isActive = false;
        
        emit RaceCompleted(raceId, winner);
    }
    
    function purchaseUpgrade(address player, uint256 cost) external whenNotPaused {
        dragonToken.transferFrom(player, address(this), cost);
        dragonToken.burn(cost);
        playerStats[player].tokensSpent += cost;
    }
    
    function pauseGame() external onlyOwner {
        _pause();
    }
    
    function unpauseGame() external onlyOwner {
        _unpause();
    }
    
    function getRaceParticipants(uint256 raceId) external view returns (address[] memory) {
        return races[raceId].participants;
    }
}
```
