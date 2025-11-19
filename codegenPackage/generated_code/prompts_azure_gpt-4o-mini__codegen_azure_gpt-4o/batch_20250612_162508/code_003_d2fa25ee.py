"""
Generated Code Metadata:
========================
Original URL: https://rarity420.vercel.app
Prompt: What are the key components to consider when creating a free-to-mint game on the blockchain, as seen in Rarity Game?
Generated: DETERMINISTIC_d2fa25eec6fefb7f
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
 * @title Free-to-Mint Blockchain Game
 * @dev This contract implements a free-to-mint game inspired by Rarity Game.
 * Players can mint characters for free and interact with the game.
 */
contract FreeToMintGame {
    // Struct to represent a character in the game
    struct Character {
        uint256 id; // Unique ID for the character
        string name; // Name of the character
        uint256 level; // Level of the character
        uint256 experience; // Experience points of the character
    }

    // Mapping to store characters owned by each player
    mapping(address => Character[]) public playerCharacters;

    // Counter to generate unique IDs for characters
    uint256 private characterIdCounter;

    // Event emitted when a new character is minted
    event CharacterMinted(address indexed player, uint256 characterId, string name);

    // Event emitted when a character gains experience
    event ExperienceGained(address indexed player, uint256 characterId, uint256 experience);

    // Modifier to ensure a valid character ID is provided
    modifier validCharacterId(address player, uint256 characterId) {
        require(characterId < playerCharacters[player].length, "Invalid character ID");
        _;
    }

    /**
     * @dev Mint a new character for free.
     * @param name The name of the character.
     */
    function mintCharacter(string memory name) external {
        require(bytes(name).length > 0, "Character name cannot be empty");

        // Create a new character
        Character memory newCharacter = Character({
            id: characterIdCounter,
            name: name,
            level: 1,
            experience: 0
        });

        // Increment the character ID counter
        characterIdCounter++;

        // Add the character to the player's list
        playerCharacters[msg.sender].push(newCharacter);

        // Emit the CharacterMinted event
        emit CharacterMinted(msg.sender, newCharacter.id, name);
    }

    /**
     * @dev Gain experience for a specific character.
     * @param characterId The ID of the character to gain experience.
     * @param experience The amount of experience to gain.
     */
    function gainExperience(uint256 characterId, uint256 experience)
        external
        validCharacterId(msg.sender, characterId)
    {
        require(experience > 0, "Experience must be greater than zero");

        // Update the character's experience
        playerCharacters[msg.sender][characterId].experience += experience;

        // Emit the ExperienceGained event
        emit ExperienceGained(msg.sender, characterId, experience);
    }

    /**
     * @dev Get details of a specific character.
     * @param player The address of the player.
     * @param characterId The ID of the character to retrieve.
     * @return The character details.
     */
    function getCharacter(address player, uint256 characterId)
        external
        view
        validCharacterId(player, characterId)
        returns (Character memory)
    {
        return playerCharacters[player][characterId];
    }

    /**
     * @dev Get the total number of characters owned by a player.
     * @param player The address of the player.
     * @return The number of characters owned by the player.
     */
    function getCharacterCount(address player) external view returns (uint256) {
        return playerCharacters[player].length;
    }
}
```
