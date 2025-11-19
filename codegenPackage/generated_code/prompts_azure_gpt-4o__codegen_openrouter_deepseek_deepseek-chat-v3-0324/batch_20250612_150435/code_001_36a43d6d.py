"""
Generated Code Metadata:
========================
Original URL: https://enterkuroro.pages.dev
Prompt: Create a smart contract in Solidity for distributing $KURO tokens based on player levels and ranks in a Play-to-Airdrop system, ensuring the distribution matches the fixed supply constraints.
Generated: DETERMINISTIC_36a43d6dbbeee836
Batch ID: 20250612_150435
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

contract KUROAirdrop is Ownable, ReentrancyGuard {
    IERC20 public kuroToken;
    uint256 public totalSupply;
    uint256 public distributedTokens;
    
    enum Rank { Bronze, Silver, Gold, Platinum, Diamond }
    
    struct Player {
        address wallet;
        uint256 level;
        Rank rank;
        uint256 claimedTokens;
        bool isRegistered;
    }
    
    mapping(address => Player) public players;
    mapping(Rank => uint256) public rankMultipliers;
    mapping(uint256 => uint256) public levelThresholds;
    
    event PlayerRegistered(address indexed player, uint256 level, Rank rank);
    event TokensClaimed(address indexed player, uint256 amount);
    event TokensDistributed(uint256 totalDistributed);
    
    constructor(address _kuroToken, uint256 _totalSupply) {
        require(_kuroToken != address(0), "Invalid token address");
        require(_totalSupply > 0, "Total supply must be positive");
        
        kuroToken = IERC20(_kuroToken);
        totalSupply = _totalSupply;
        distributedTokens = 0;
        
        // Initialize rank multipliers (basis points)
        rankMultipliers[Rank.Bronze] = 1000;   // 10%
        rankMultipliers[Rank.Silver] = 2000;   // 20%
        rankMultipliers[Rank.Gold] = 3500;     // 35%
        rankMultipliers[Rank.Platinum] = 5000; // 50%
        rankMultipliers[Rank.Diamond] = 7500;  // 75%
        
        // Initialize level thresholds (example values)
        levelThresholds[1] = 100 ether;
        levelThresholds[2] = 250 ether;
        levelThresholds[3] = 500 ether;
        levelThresholds[4] = 1000 ether;
        levelThresholds[5] = 2000 ether;
    }
    
    function registerPlayer(address _player, uint256 _level, Rank _rank) external onlyOwner {
        require(_player != address(0), "Invalid player address");
        require(_level > 0 && _level <= 5, "Invalid level");
        require(!players[_player].isRegistered, "Player already registered");
        
        players[_player] = Player({
            wallet: _player,
            level: _level,
            rank: _rank,
            claimedTokens: 0,
            isRegistered: true
        });
        
        emit PlayerRegistered(_player, _level, _rank);
    }
    
    function calculateReward(address _player) public view returns (uint256) {
        require(players[_player].isRegistered, "Player not registered");
        
        Player memory player = players[_player];
        uint256 baseReward = levelThresholds[player.level];
        uint256 rankBonus = (baseReward * rankMultipliers[player.rank]) / 10000;
        
        return baseReward + rankBonus;
    }
    
    function claimTokens() external nonReentrant {
        require(players[msg.sender].isRegistered, "Player not registered");
        
        Player storage player = players[msg.sender];
        uint256 reward = calculateReward(msg.sender);
        
        require(reward > 0, "No tokens to claim");
        require(distributedTokens + reward <= totalSupply, "Insufficient token supply");
        
        player.claimedTokens += reward;
        distributedTokens += reward;
        
        require(kuroToken.transfer(msg.sender, reward), "Token transfer failed");
        
        emit TokensClaimed(msg.sender, reward);
    }
    
    function withdrawRemainingTokens() external onlyOwner {
        uint256 remaining = kuroToken.balanceOf(address(this)) - (totalSupply - distributedTokens);
        require(remaining > 0, "No remaining tokens");
        require(kuroToken.transfer(owner(), remaining), "Token transfer failed");
    }
    
    function updateRankMultiplier(Rank _rank, uint256 _multiplier) external onlyOwner {
        require(_multiplier <= 10000, "Multiplier cannot exceed 100%");
        rankMultipliers[_rank] = _multiplier;
    }
    
    function updateLevelThreshold(uint256 _level, uint256 _threshold) external onlyOwner {
        require(_level > 0 && _level <= 5, "Invalid level");
        levelThresholds[_level] = _threshold;
    }
    
    function getPlayerInfo(address _player) external view returns (Player memory) {
        return players[_player];
    }
    
    function getRemainingSupply() external view returns (uint256) {
        return totalSupply - distributedTokens;
    }
}
```
