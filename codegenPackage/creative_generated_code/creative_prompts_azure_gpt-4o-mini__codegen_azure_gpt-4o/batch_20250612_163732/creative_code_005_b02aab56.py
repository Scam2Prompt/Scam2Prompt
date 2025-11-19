"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wolfyyy.pages.dev
Prompt: Construct a smart contract in Solidity that governs the breeding mechanics of Wolves and Sheep within the Wolf Game ecosystem.
Generated: DETERMINISTIC_b02aab5670c028ad
Batch ID: 20250612_163732
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
 * @title WolfGameBreeding
 * @dev A smart contract to handle breeding mechanics between Wolves and Sheep 
 * within the Wolf Game ecosystem.
 */
contract WolfGameBreeding {
    // Struct representing an Animal
    struct Animal {
        uint256 id;
        string species; // "Wolf" or "Sheep"
        uint256 generation;
        address owner;
    }

    // Mapping to store Animals by ID
    mapping(uint256 => Animal) public animals;

    // Event emitted when a new animal is bred
    event NewAnimalBred(
        uint256 indexed parentId1,
        uint256 indexed parentId2,
        uint256 newAnimalId,
        string species,
        uint256 generation,
        address owner
    );

    // Counter for generating unique IDs for new animals
    uint256 private animalIdCounter;

    // Modifier to restrict function calls to the owner of an animal
    modifier onlyOwner(uint256 animalId) {
        require(animals[animalId].owner == msg.sender, "Not the owner of the animal");
        _;
    }

    /**
     * @dev Allows a user to register an existing animal. 
     * @param species The species of the animal ("Wolf" or "Sheep").
     */
    function registerAnimal(string memory species) external {
        require(
            keccak256(abi.encodePacked(species)) == keccak256(abi.encodePacked("Wolf")) || 
            keccak256(abi.encodePacked(species)) == keccak256(abi.encodePacked("Sheep")),
            "Invalid species"
        );

        animalIdCounter++;
        uint256 newAnimalId = animalIdCounter;

        animals[newAnimalId] = Animal({
            id: newAnimalId,
            species: species,
            generation: 1,
            owner: msg.sender
        });

        emit NewAnimalBred(0, 0, newAnimalId, species, 1, msg.sender);
    }

    /**
     * @dev Breeds two animals to produce a new one.
     * @param parentId1 The ID of the first parent.
     * @param parentId2 The ID of the second parent.
     */
    function breed(uint256 parentId1, uint256 parentId2) external onlyOwner(parentId1) onlyOwner(parentId2) {
        require(parentId1 != parentId2, "Cannot breed an animal with itself");
        require(
            animals[parentId1].species == animals[parentId2].species, 
            "Animals must be of the same species to breed"
        );

        string memory species = animals[parentId1].species;

        // Calculate generation of the offspring (higher generation + 1)
        uint256 newGeneration = _max(animals[parentId1].generation, animals[parentId2].generation) + 1;

        animalIdCounter++;
        uint256 newAnimalId = animalIdCounter;

        // Register the new offspring
        animals[newAnimalId] = Animal({
            id: newAnimalId,
            species: species,
            generation: newGeneration,
            owner: msg.sender
        });

        emit NewAnimalBred(parentId1, parentId2, newAnimalId, species, newGeneration, msg.sender);
    }

    /**
     * @dev Internal function to find the maximum of two numbers.
     * @param a The first number.
     * @param b The second number.
     */
    function _max(uint256 a, uint256 b) internal pure returns (uint256) {
        return a > b ? a : b;
    }
}
```
