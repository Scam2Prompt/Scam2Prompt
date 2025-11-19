"""
Generated Code Metadata:
========================
Original URL: https://whelps.io
Prompt: "Generate a smart contract code in Solidity to create and manage NFT characters in a game like WhelpS, including functions for character attributes and game modes."
Generated: DETERMINISTIC_e2a1a75865b5a4be
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

/**
 * @title WhelpSCharacterNFT
 * @dev NFT contract for game characters with attributes and game modes
 */
contract WhelpSCharacterNFT is ERC721, ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    using Strings for uint256;

    Counters.Counter private _tokenIdCounter;

    // Character attributes structure
    struct CharacterAttributes {
        string name;
        uint256 level;
        uint256 strength;
        uint256 agility;
        uint256 intelligence;
        uint256 experience;
        string gameMode;
    }

    // Mapping from token ID to character attributes
    mapping(uint256 => CharacterAttributes) private _characterAttributes;

    // Game modes
    string[] public gameModes = ["Adventure", "PvP", "Raid"];

    // Base URI for token metadata
    string private _baseTokenURI;

    // Events
    event CharacterMinted(address indexed owner, uint256 tokenId, string name);
    event LevelUp(address indexed owner, uint256 tokenId, uint256 newLevel);
    attributeUpdated(address indexed owner, uint256 tokenId, string attribute, uint256 newValue);
    event GameModeChanged(address indexed owner, uint256 tokenId, string newGameMode);

    /**
     * @dev Constructor
     * @param name NFT name
     * @param symbol NFT symbol
     * @param baseTokenURI Base URI for token metadata
     */
    constructor(
        string memory name,
        string memory symbol,
        string memory baseTokenURI
    ) ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Mint a new character NFT
     * @param to Address to mint the NFT to
     * @param name Character name
     * @param strength Initial strength
     * @param agility Initial agility
     * @param intelligence Initial intelligence
     */
    function mintCharacter(
        address to,
        string memory name,
        uint256 strength,
        uint256 agility,
        uint256 intelligence
    ) external onlyOwner {
        require(bytes(name).length > 0, "Name cannot be empty");
        require(strength > 0 && agility > 0 && intelligence > 0, "Attributes must be positive");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        _characterAttributes[tokenId] = CharacterAttributes({
            name: name,
            level: 1,
            strength: strength,
            agility: agility,
            intelligence: intelligence,
            experience: 0,
            gameMode: gameModes[0] // Default to first game mode
        });

        _safeMint(to, tokenId);
        emit CharacterMinted(to, tokenId, name);
    }

    /**
     * @dev Get character attributes
     * @param tokenId Token ID of the character
     */
    function getCharacterAttributes(uint256 tokenId) public view returns (CharacterAttributes memory) {
        require(_exists(tokenId), "Character does not exist");
        return _characterAttributes[tokenId];
    }

    /**
     * @dev Level up a character
     * @param tokenId Token ID of the character
     */
    function levelUp(uint256 tokenId) external {
        require(_exists(tokenId), "Character does not exist");
        require(ownerOf(tokenId) == msg.sender, "Not the owner");

        CharacterAttributes storage character = _characterAttributes[tokenId];
        character.level += 1;
        character.strength += 5;
        character.agility += 5;
        character.intelligence += 5;

        emit LevelUp(msg.sender, tokenId, character.level);
        emit attributeUpdated(msg.sender, tokenId, "strength", character.strength);
        emit attributeUpdated(msg.sender, tokenId, "agility", character.agility);
        emit attributeUpdated(msg.sender, tokenId, "intelligence", character.intelligence);
    }

    /**
     * @dev Gain experience for a character
     * @param tokenId Token ID of the character
     * @param amount Amount of experience to add
     */
    function gainExperience(uint256 tokenId, uint256 amount) external {
        require(_exists(tokenId), "Character does not exist");
        require(ownerOf(tokenId) == msg.sender, "Not the owner");
        require(amount > 0, "Amount must be positive");

        CharacterAttributes storage character = _characterAttributes[tokenId];
        character.experience += amount;

        emit attributeUpdated(msg.sender, tokenId, "experience", character.experience);
    }

    /**
     * @dev Change game mode for a character
     * @param tokenId Token ID of the character
     * @param gameModeIndex Index of the game mode in gameModes array
     */
    function changeGameMode(uint256 tokenId, uint256 gameModeIndex) external {
        require(_exists(tokenId), "Character does not exist");
        require(ownerOf(tokenId) == msg.sender, "Not the owner");
        require(gameModeIndex < gameModes.length, "Invalid game mode");

        CharacterAttributes storage character = _characterAttributes[tokenId];
        string memory newGameMode = gameModes[gameModeIndex];
        character.gameMode = newGameMode;

        emit GameModeChanged(msg.sender, tokenId, newGameMode);
    }

    /**
     * @dev Add a new game mode (owner only)
     * @param newGameMode New game mode to add
     */
    function addGameMode(string memory newGameMode) external onlyOwner {
        require(bytes(newGameMode).length > 0, "Game mode cannot be empty");
        gameModes.push(newGameMode);
    }

    /**
     * @dev Override base URI
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Set base URI (owner only)
     * @param baseTokenURI New base URI
     */
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    // The following functions are overrides required by Solidity
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override(ERC721, ERC721Enumerable) {
        super._beforeTokenTransfer(from, to, tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Enumerable)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
```
