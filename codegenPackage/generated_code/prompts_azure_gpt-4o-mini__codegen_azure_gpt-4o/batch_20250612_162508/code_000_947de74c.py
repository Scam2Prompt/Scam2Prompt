"""
Generated Code Metadata:
========================
Original URL: https://rarity420.vercel.app
Prompt: How can I implement a minting function for a D&D blockchain game similar to Rarity Game?
Generated: DETERMINISTIC_947de74c261e5388
Batch ID: 20250612_162508
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

/**
 * @title DnDGameMinting
 * @dev A smart contract for minting characters in a D&D blockchain game.
 */
contract DnDGameMinting {
    // Struct to represent a character
    struct Character {
        uint256 id;
        string name;
        uint8 level;
        uint8 strength;
        uint8 dexterity;
        uint8 intelligence;
    }

    // Mapping to store characters by their ID
    mapping(uint256 => Character) public characters;

    // Mapping to track ownership of characters
    mapping(address => uint256[]) public ownerToCharacters;

    // Counter for character IDs
    uint256 private nextCharacterId;

    // Event emitted when a new character is minted
    event CharacterMinted(
        uint256 indexed id,
        address indexed owner,
        string name,
        uint8 level,
        uint8 strength,
        uint8 dexterity,
        uint8 intelligence
    );

    /**
     * @dev Mint a new character.
     * @param name The name of the character.
     * @param level The initial level of the character.
     * @param strength The strength attribute of the character.
     * @param dexterity The dexterity attribute of the character.
     * @param intelligence The intelligence attribute of the character.
     */
    function mintCharacter(
        string memory name,
        uint8 level,
        uint8 strength,
        uint8 dexterity,
        uint8 intelligence
    ) external {
        // Input validation
        require(bytes(name).length > 0, "Name cannot be empty");
        require(level > 0, "Level must be greater than 0");
        require(strength > 0, "Strength must be greater than 0");
        require(dexterity > 0, "Dexterity must be greater than 0");
        require(intelligence > 0, "Intelligence must be greater than 0");

        // Create a new character
        uint256 characterId = nextCharacterId;
        characters[characterId] = Character(
            characterId,
            name,
            level,
            strength,
            dexterity,
            intelligence
        );

        // Assign the character to the sender
        ownerToCharacters[msg.sender].push(characterId);

        // Increment the character ID counter
        nextCharacterId++;

        // Emit the minting event
        emit CharacterMinted(
            characterId,
            msg.sender,
            name,
            level,
            strength,
            dexterity,
            intelligence
        );
    }

    /**
     * @dev Get all characters owned by a specific address.
     * @param owner The address of the owner.
     * @return An array of character IDs owned by the address.
     */
    function getCharactersByOwner(address owner)
        external
        view
        returns (uint256[] memory)
    {
        return ownerToCharacters[owner];
    }

    /**
     * @dev Get details of a specific character by ID.
     * @param characterId The ID of the character.
     * @return The character details.
     */
    function getCharacterDetails(uint256 characterId)
        external
        view
        returns (Character memory)
    {
        require(
            characters[characterId].id == characterId,
            "Character does not exist"
        );
        return characters[characterId];
    }
}
```
