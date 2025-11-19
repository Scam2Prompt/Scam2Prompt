"""
Generated Code Metadata:
========================
Original URL: https://dogodoges.pages.dev
Prompt: Write code to create a decentralized NFT-based dog racing game that incorporates breeding, trading, and earning mechanics, similar to DOGO METARACE GAMES.
Generated: DETERMINISTIC_886446d0f93339b3
Batch ID: 20250612_153648
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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract DogRaceGame is ERC721, ERC721Enumerable, Ownable {
    using SafeMath for uint256;
    using Counters for Counters.Counter;

    Counters.Counter private _tokenIdCounter;

    // Game constants
    uint256 public constant BREEDING_COST = 0.1 ether;
    uint256 public constant RACE_ENTRY_FEE = 0.05 ether;
    uint256 public constant WINNER_REWARD_PERCENTAGE = 70;
    uint256 public constant OWNER_REWARD_PERCENTAGE = 30;

    // Dog attributes
    struct Dog {
        uint256 dna;
        uint256 speed;
        uint256 stamina;
        uint256 agility;
        uint256 experience;
        uint256 level;
        uint256 lastRaceTime;
        uint256 cooldownEnd;
        uint256 breedCount;
        bool isRacing;
    }

    // Mapping from token ID to dog
    mapping(uint256 => Dog) private _dogs;

    // Mapping from DNA to whether it exists
    mapping(uint256 => bool) private _dnaExists;

    // Events
    event DogMinted(address indexed owner, uint256 tokenId, uint256 dna);
    event DogBred(address indexed owner, uint256 tokenId, uint256 parent1, uint256 parent2);
    event RaceEntered(uint256 indexed raceId, uint256[] dogIds);
    event RaceCompleted(uint256 indexed raceId, uint256 winnerId, uint256 prize);
    event DogTraded(address indexed from, address indexed to, uint256 tokenId, uint256 price);

    constructor() ERC721("DogRaceGame", "DRG") {}

    // Modifiers
    modifier onlyDogOwner(uint256 tokenId) {
        require(ownerOf(tokenId) == msg.sender, "Not the dog owner");
        _;
    }

    modifier notRacing(uint256 tokenId) {
        require(!_dogs[tokenId].isRacing, "Dog is currently racing");
        _;
    }

    modifier cooldownOver(uint256 tokenId) {
        require(block.timestamp >= _dogs[tokenId].cooldownEnd, "Dog is on cooldown");
        _;
    }

    // Mint a new dog
    function mintDog() external payable {
        require(msg.value >= BREEDING_COST, "Insufficient funds for minting");
        
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        uint256 dna = _generateDna(tokenId, msg.sender);
        while (_dnaExists[dna]) {
            dna = _generateDna(tokenId, msg.sender);
        }

        _dogs[tokenId] = Dog({
            dna: dna,
            speed: _randomAttribute(50, 100),
            stamina: _randomAttribute(50, 100),
            agility: _randomAttribute(50, 100),
            experience: 0,
            level: 1,
            lastRaceTime: 0,
            cooldownEnd: 0,
            breedCount: 0,
            isRacing: false
        });

        _dnaExists[dna] = true;
        _safeMint(msg.sender, tokenId);

        emit DogMinted(msg.sender, tokenId, dna);
    }

    // Breed two dogs
    function breedDogs(uint256 parent1, uint256 parent2) 
        external 
        payable 
        onlyDogOwner(parent1) 
        onlyDogOwner(parent2)
        notRacing(parent1)
        notRacing(parent2)
        cooldownOver(parent1)
        cooldownOver(parent2)
    {
        require(msg.value >= BREEDING_COST, "Insufficient funds for breeding");
        require(_dogs[parent1].breedCount < 5 && _dogs[parent2].breedCount < 5, "Max breed count reached");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        uint256 newDna = _mixDna(_dogs[parent1].dna, _dogs[parent2].dna);
        while (_dnaExists[newDna]) {
            newDna = _mixDna(_dogs[parent1].dna, _dogs[parent2].dna);
        }

        _dogs[tokenId] = Dog({
            dna: newDna,
            speed: _inheritAttribute(_dogs[parent1].speed, _dogs[parent2].speed),
            stamina: _inheritAttribute(_dogs[parent1].stamina, _dogs[parent2].stamina),
            agility: _inheritAttribute(_dogs[parent1].agility, _dogs[parent2].agility),
            experience: 0,
            level: 1,
            lastRaceTime: 0,
            cooldownEnd: 0,
            breedCount: 0,
            isRacing: false
        });

        _dogs[parent1].breedCount++;
        _dogs[parent2].breedCount++;
        _dogs[parent1].cooldownEnd = block.timestamp + 1 days;
        _dogs[parent2].cooldownEnd = block.timestamp + 1 days;
        _dnaExists[newDna] = true;
        _safeMint(msg.sender, tokenId);

        emit DogBred(msg.sender, tokenId, parent1, parent2);
    }

    // Enter a race
    function enterRace(uint256[] memory dogIds) external payable {
        require(msg.value >= RACE_ENTRY_FEE * dogIds.length, "Insufficient funds for race entry");
        require(dogIds.length >= 2 && dogIds.length <= 8, "Invalid number of dogs for race");

        for (uint256 i = 0; i < dogIds.length; i++) {
            require(ownerOf(dogIds[i]) == msg.sender, "Not the owner of all dogs");
            require(!_dogs[dogIds[i]].isRacing, "Dog is already racing");
            require(block.timestamp >= _dogs[dogIds[i]].cooldownEnd, "Dog is on cooldown");
            _dogs[dogIds[i]].isRacing = true;
        }

        uint256 raceId = uint256(keccak256(abi.encodePacked(block.timestamp, msg.sender, dogIds)));
        emit RaceEntered(raceId, dogIds);
    }

    // Complete a race (simplified version - in reality would need oracle or chainlink VRF)
    function completeRace(uint256 raceId, uint256[] memory dogIds, uint256 winnerIndex) external onlyOwner {
        require(dogIds.length >= 2 && dogIds.length <= 8, "Invalid number of dogs");
        require(winnerIndex < dogIds.length, "Invalid winner index");

        uint256 winnerId = dogIds[winnerIndex];
        uint256 prize = RACE_ENTRY_FEE * dogIds.length * WINNER_REWARD_PERCENTAGE / 100;
        uint256 ownerCut = RACE_ENTRY_FEE * dogIds.length * OWNER_REWARD_PERCENTAGE / 100;

        for (uint256 i = 0; i < dogIds.length; i++) {
            _dogs[dogIds[i]].isRacing = false;
            _dogs[dogIds[i]].lastRaceTime = block.timestamp;
            _dogs[dogIds[i]].cooldownEnd = block.timestamp + 6 hours;
            
            if (dogIds[i] == winnerId) {
                _dogs[winnerId].experience += 10;
                if (_dogs[winnerId].experience >= _dogs[winnerId].level * 20) {
                    _dogs[winnerId].level++;
                    _dogs[winnerId].speed += 5;
                    _dogs[winnerId].stamina += 5;
                    _dogs[winnerId].agility += 5;
                }
                payable(ownerOf(winnerId)).transfer(prize);
            }
        }

        payable(owner()).transfer(ownerCut);
        emit RaceCompleted(raceId, winnerId, prize);
    }

    // Trade a dog
    function tradeDog(uint256 tokenId, uint256 price) external onlyDogOwner(tokenId) notRacing(tokenId) {
        approve(address(this), tokenId);
        emit DogTraded(msg.sender, address(0), tokenId, price);
    }

    // Buy a traded dog
    function buyTradedDog(uint256 tokenId) external payable {
        uint256 price = msg.value;
        address seller = ownerOf(tokenId);
        
        require(getApproved(tokenId) == address(this), "Dog not available
