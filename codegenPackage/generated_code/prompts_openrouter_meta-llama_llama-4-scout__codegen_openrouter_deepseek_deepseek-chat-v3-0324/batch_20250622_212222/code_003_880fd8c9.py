"""
Generated Code Metadata:
========================
Original URL: https://binaryxs.org
Prompt: "Design a smart contract for a new blockchain game using Solidity, incorporating features like NFT ownership and token rewards, inspired by BinaryX's game development approach."
Generated: DETERMINISTIC_880fd8c963ed8fbb
Batch ID: 20250622_212222
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract BlockchainGame is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    
    // Game token contract
    IERC20 public gameToken;
    
    // NFT counters
    Counters.Counter private _tokenIdCounter;
    
    // Game constants
    uint256 public constant REWARD_PER_LEVEL = 100 * 10**18; // 100 tokens per level
    uint256 public constant MINT_PRICE = 0.1 ether;
    
    // NFT attributes
    struct Character {
        uint256 level;
        uint256 experience;
        uint256 lastRewardTime;
    }
    
    // Mapping from token ID to character attributes
    mapping(uint256 => Character) public characters;
    
    // Events
    event CharacterMinted(address indexed owner, uint256 tokenId);
    event LevelUp(uint256 indexed tokenId, uint256 newLevel);
    event RewardClaimed(address indexed owner, uint256 tokenId, uint256 amount);
    
    constructor(address _gameTokenAddress) ERC721("BlockchainGameCharacter", "BGC") {
        gameToken = IERC20(_gameTokenAddress);
    }
    
    // Mint a new character NFT
    function mintCharacter() external payable nonReentrant {
        require(msg.value >= MINT_PRICE, "Insufficient payment");
        require(balanceOf(msg.sender) == 0, "Already owns a character");
        
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _safeMint(msg.sender, tokenId);
        
        characters[tokenId] = Character({
            level: 1,
            experience: 0,
            lastRewardTime: block.timestamp
        });
        
        emit CharacterMinted(msg.sender, tokenId);
    }
    
    // Level up character
    function levelUp(uint256 tokenId) external {
        require(ownerOf(tokenId) == msg.sender, "Not owner of character");
        Character storage character = characters[tokenId];
        
        uint256 requiredExp = character.level * 1000;
        require(character.experience >= requiredExp, "Not enough experience");
        
        character.level += 1;
        character.experience -= requiredExp;
        
        emit LevelUp(tokenId, character.level);
    }
    
    // Claim game token rewards
    function claimRewards(uint256 tokenId) external nonReentrant {
        require(ownerOf(tokenId) == msg.sender, "Not owner of character");
        Character storage character = characters[tokenId];
        
        uint256 timeElapsed = block.timestamp - character.lastRewardTime;
        require(timeElapsed >= 1 days, "Rewards not ready yet");
        
        uint256 rewardAmount = character.level * REWARD_PER_LEVEL * (timeElapsed / 1 days);
        
        character.lastRewardTime = block.timestamp;
        
        require(gameToken.transfer(msg.sender, rewardAmount), "Reward transfer failed");
        
        emit RewardClaimed(msg.sender, tokenId, rewardAmount);
    }
    
    // Add experience to character
    function addExperience(uint256 tokenId, uint256 amount) external onlyOwner {
        require(_exists(tokenId), "Token does not exist");
        characters[tokenId].experience += amount;
    }
    
    // Withdraw contract funds
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }
    
    // Set game token address (only owner)
    function setGameTokenAddress(address _gameTokenAddress) external onlyOwner {
        gameToken = IERC20(_gameTokenAddress);
    }
    
    // Override transfer to reset reward timer
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override {
        super._beforeTokenTransfer(from, to, tokenId);
        
        if (from != address(0) && to != address(0)) {
            characters[tokenId].lastRewardTime = block.timestamp;
        }
    }
}
```
