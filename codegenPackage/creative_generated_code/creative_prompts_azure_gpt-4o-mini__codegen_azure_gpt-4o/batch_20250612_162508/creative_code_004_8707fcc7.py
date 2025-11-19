"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rarity420.vercel.app
Prompt: How do I set up a smart contract for a D&D game that allows free minting, inspired by Rarity Game?
Generated: DETERMINISTIC_8707fcc7b821d91b
Batch ID: 20250612_162508
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

/**
 * @title DnDGameContract
 * @dev A smart contract inspired by the Rarity game to allow free minting of characters for a D&D-style game.
 */
contract DnDGameContract {
    // Event emitted when a new character is minted
    event CharacterMinted(uint256 indexed characterId, address indexed owner, string name, uint256 class);

    // Struct representing a D&D character
    struct Character {
        string name;     // Name of the character
        uint256 class;   // Class ID (e.g., 1=Warrior, 2=Mage, etc.)
        uint256 level;   // Character level, starts at 1
    }

    // Mapping from character ID to character details
    mapping(uint256 => Character) private characters;

    // Mapping from owner address to their character IDs
    mapping(address => uint256[]) private ownerToCharacters;

    // Total number of characters minted
    uint256 public totalCharacters;

    /**
     * @dev Modifier to ensure that a valid class ID is provided.
     * @param classId The class ID to validate.
     */
    modifier validClass(uint256 classId) {
        require(classId >= 1 && classId <= 10, "Invalid class ID"); // Classes are numbered from 1 to 10
        _;
    }

    /**
     * @dev Function to mint a new character.
     * @param name The name of the character.
     * @param classId The class ID of the character.
     */
    function mintCharacter(string memory name, uint256 classId) external validClass(classId) {
        require(bytes(name).length > 0, "Character name cannot be empty"); // Ensure the name is not empty

        // Increment the total number of characters
        totalCharacters++;

        // Create the character
        characters[totalCharacters] = Character({
            name: name,
            class: classId,
            level: 1 // Starting level is 1
        });

        // Map the character ID to the sender's address
        ownerToCharacters[msg.sender].push(totalCharacters);

        // Emit an event for the minted character
        emit CharacterMinted(totalCharacters, msg.sender, name, classId);
    }

    /**
     * @dev Function to retrieve character details by ID.
     * @param characterId The ID of the character to query.
     * @return The character's details (name, class, level).
     */
    function getCharacter(uint256 characterId)
        external
        view
        returns (string memory name, uint256 class, uint256 level)
    {
        require(characterId > 0 && characterId <= totalCharacters, "Character does not exist"); // Ensure valid ID

        Character memory character = characters[characterId];
        return (character.name, character.class, character.level);
    }

    /**
     * @dev Function to retrieve all character IDs owned by a specific address.
     * @param owner The address to query.
     * @return An array of character IDs owned by the address.
     */
    function getCharactersByOwner(address owner) external view returns (uint256[] memory) {
        return ownerToCharacters[owner];
    }
}
```
