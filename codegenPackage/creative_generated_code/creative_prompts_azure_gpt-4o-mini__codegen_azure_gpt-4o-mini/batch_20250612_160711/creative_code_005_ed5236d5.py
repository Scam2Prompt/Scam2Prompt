"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binaryxe.org
Prompt: Write a Solidity contract that enables players to earn rewards while playing CyberDragon, detailing the mechanics of in-game asset ownership.
Generated: DETERMINISTIC_ed5236d5f8f79a13
Batch ID: 20250612_160711
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Contract representing the CyberDragon game
contract CyberDragon is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Struct to store information about each dragon
    struct Dragon {
        uint256 id;
        string name;
        uint256 rewards;
    }

    // Mapping from dragon ID to Dragon struct
    mapping(uint256 => Dragon) private dragons;

    // Mapping from player address to their dragon IDs
    mapping(address => uint256[]) private playerDragons;

    // Event emitted when a new dragon is minted
    event DragonMinted(address indexed player, uint256 indexed dragonId, string name);

    // Counter for dragon IDs
    Counters.Counter private _dragonIdCounter;

    /**
     * @dev Constructor that initializes the contract with a name and symbol
     */
    constructor() ERC721("CyberDragon", "CDR") {}

    /**
     * @dev Function for players to mint a new dragon
     * @param _name The name of the new dragon
     */
    function mintDragon(string memory _name) external {
        require(bytes(_name).length > 0, "Dragon name cannot be empty");

        // Increment the dragon ID counter and create a new dragon
        uint256 newDragonId = _dragonIdCounter.current();
        _dragonIdCounter.increment();

        Dragon memory newDragon = Dragon({
            id: newDragonId,
            name: _name,
            rewards: 0
        });

        dragons[newDragonId] = newDragon;
        playerDragons[msg.sender].push(newDragonId);
        
        // Mint the NFT representing the dragon
        _safeMint(msg.sender, newDragonId);

        emit DragonMinted(msg.sender, newDragonId, _name);
    }

    /**
     * @dev Function for players to collect rewards for their dragons
     * @param dragonId The ID of the dragon for which rewards are to be collected
     */
    function collectRewards(uint256 dragonId) external {
        require(_exists(dragonId), "This dragon does not exist");
        require(ownerOf(dragonId) == msg.sender, "You do not own this dragon");

        // Logic to calculate and distribute rewards (placeholder logic)
        uint256 rewards = calculateRewards(dragonId);
        dragons[dragonId].rewards += rewards;

        // Transfer the rewards to the player (placeholder for reward transfer logic)
        // In a real scenario, rewards could be in the form of ERC20 tokens
        // ERC20(rewardTokenAddress).transfer(msg.sender, rewards);
    }

    /**
     * @dev Internal function to calculate rewards based on the dragon's attributes
     * @param dragonId The ID of the dragon
     * @return rewardAmount The amount of rewards to be given
     */
    function calculateRewards(uint256 dragonId) internal view returns (uint256 rewardAmount) {
        // Placeholder logic for reward calculation
        // For example, you could base it on the dragon's attributes or time held
        return 10; // Fixed reward for demonstration
    }

    /**
     * @dev Function to retrieve a player's dragons
     * @param player The address of the player
     * @return The list of dragon IDs owned by the player
     */
    function getPlayerDragons(address player) external view returns (uint256[] memory) {
        return playerDragons[player];
    }

    /**
     * @dev Function to get details of a dragon by its ID
     * @param dragonId The ID of the dragon
     * @return The Dragon struct containing details of the dragon
     */
    function getDragonDetails(uint256 dragonId) external view returns (Dragon memory) {
        require(_exists(dragonId), "This dragon does not exist");
        return dragons[dragonId];
    }
}
```
