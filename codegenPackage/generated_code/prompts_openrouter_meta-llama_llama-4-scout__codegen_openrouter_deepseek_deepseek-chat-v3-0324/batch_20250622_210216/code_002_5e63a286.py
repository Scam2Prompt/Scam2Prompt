"""
Generated Code Metadata:
========================
Original URL: https://phoenixai-art.pages.dev
Prompt: "Design a smart contract for an NFT game like Phoenix Chronicle AI, including tokenomics and functionality for player versus player (PvP) battles."
Generated: DETERMINISTIC_5e63a286a0c0df10
Batch ID: 20250622_210216
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract PhoenixChronicleAI is ERC721Enumerable, Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Tokenomics constants
    uint256 public constant MINT_PRICE = 0.05 ether;
    uint256 public constant MAX_SUPPLY = 10000;
    uint256 public constant BATTLE_REWARD = 10 ether;
    uint256 public constant BATTLE_FEE = 0.01 ether;
    uint256 public constant WINNER_SHARE = 70;
    uint256 public constant LOSER_SHARE = 30;

    // Game stats
    struct Character {
        uint256 strength;
        uint256 agility;
        uint256 intelligence;
        uint256 wins;
        uint256 losses;
        uint256 lastBattleTime;
    }

    mapping(uint256 => Character) public characters;
    mapping(address => uint256) public playerBalances;

    // Events
    event CharacterMinted(address indexed owner, uint256 tokenId);
    event BattleStarted(uint256 indexed attackerId, uint256 indexed defenderId);
    event BattleResult(uint256 indexed winnerId, uint256 indexed loserId, uint256 reward);
    event RewardClaimed(address indexed player, uint256 amount);

    constructor() ERC721("PhoenixChronicleAI", "PCAI") {}

    // Mint a new character NFT
    function mintCharacter() external payable nonReentrant {
        require(totalSupply() < MAX_SUPPLY, "Max supply reached");
        require(msg.value >= MINT_PRICE, "Insufficient payment");

        uint256 tokenId = totalSupply() + 1;
        _safeMint(msg.sender, tokenId);

        // Initialize character stats with random values (simplified for demo)
        characters[tokenId] = Character({
            strength: _randomStat(10, 100),
            agility: _randomStat(10, 100),
            intelligence: _randomStat(10, 100),
            wins: 0,
            losses: 0,
            lastBattleTime: 0
        });

        emit CharacterMinted(msg.sender, tokenId);
    }

    // Engage in PvP battle
    function battle(uint256 attackerId, uint256 defenderId) external payable nonReentrant {
        require(ownerOf(attackerId) == msg.sender, "Not your character");
        require(ownerOf(defenderId) != msg.sender, "Cannot battle yourself");
        require(msg.value >= BATTLE_FEE, "Insufficient battle fee");
        require(block.timestamp - characters[attackerId].lastBattleTime >= 1 hours, "Cooldown active");
        require(block.timestamp - characters[defenderId].lastBattleTime >= 1 hours, "Defender cooldown active");

        emit BattleStarted(attackerId, defenderId);

        Character storage attacker = characters[attackerId];
        Character storage defender = characters[defenderId];

        // Calculate battle score (simplified for demo)
        uint256 attackerScore = attacker.strength + attacker.agility + attacker.intelligence;
        uint256 defenderScore = defender.strength + defender.agility + defender.intelligence;

        // Determine winner
        bool attackerWins = attackerScore > defenderScore;

        // Update stats
        if (attackerWins) {
            attacker.wins += 1;
            defender.losses += 1;
            _distributeRewards(attackerId, defenderId);
        } else {
            defender.wins += 1;
            attacker.losses += 1;
            _distributeRewards(defenderId, attackerId);
        }

        attacker.lastBattleTime = block.timestamp;
        defender.lastBattleTime = block.timestamp;
    }

    // Distribute rewards after battle
    function _distributeRewards(uint256 winnerId, uint256 loserId) private {
        address winnerOwner = ownerOf(winnerId);
        address loserOwner = ownerOf(loserId);

        uint256 winnerAmount = BATTLE_REWARD.mul(WINNER_SHARE).div(100);
        uint256 loserAmount = BATTLE_REWARD.mul(LOSER_SHARE).div(100);

        playerBalances[winnerOwner] = playerBalances[winnerOwner].add(winnerAmount);
        playerBalances[loserOwner] = playerBalances[loserOwner].add(loserAmount);

        emit BattleResult(winnerId, loserId, BATTLE_REWARD);
    }

    // Claim rewards
    function claimRewards() external nonReentrant {
        uint256 amount = playerBalances[msg.sender];
        require(amount > 0, "No rewards to claim");

        playerBalances[msg.sender] = 0;
        payable(msg.sender).transfer(amount);

        emit RewardClaimed(msg.sender, amount);
    }

    // Withdraw contract funds (owner only)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // Helper function to generate random stats (not truly random, for demo purposes)
    function _randomStat(uint256 min, uint256 max) private view returns (uint256) {
        return min + uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty))) % (max - min + 1);
    }

    // Override transfer to prevent trading during cooldown
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override {
        super._beforeTokenTransfer(from, to, tokenId);
        require(characters[tokenId].lastBattleTime + 1 hours <= block.timestamp, "Character in cooldown");
    }
}
```
