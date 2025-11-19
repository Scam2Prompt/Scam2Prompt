"""
Generated Code Metadata:
========================
Original URL: https://fehurunes.app
Prompt: Create a smart contract for minting unique AI entities, ensuring each entity evolves dynamically based on its ordinal number, similar to the NEO-Sentient collection.
Generated: DETERMINISTIC_25b94c457a2b9400
Batch ID: 20250612_153424
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

contract AISentient is ERC721, Ownable {
    using Counters for Counters.Counter;
    using Strings for uint256;

    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Mapping from token ID to evolution stage
    mapping(uint256 => uint256) private _evolutionStages;

    // Maximum supply of AI entities
    uint256 public constant MAX_SUPPLY = 10000;

    // Events
    event AIEntityMinted(address indexed to, uint256 indexed tokenId);
    event AIEntityEvolved(uint256 indexed tokenId, uint256 newStage);

    constructor(string memory baseURI) ERC721("AI Sentient", "AIS") {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Mints a new AI entity to the specified address
     * @param to The address that will receive the NFT
     */
    function mintAIEntity(address to) external onlyOwner {
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");
        
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        // Initial evolution stage is determined by tokenId
        _evolutionStages[tokenId] = calculateInitialStage(tokenId);
        
        _safeMint(to, tokenId);
        emit AIEntityMinted(to, tokenId);
    }

    /**
     * @dev Evolves the AI entity to the next stage
     * @param tokenId The ID of the token to evolve
     */
    function evolve(uint256 tokenId) external {
        require(_exists(tokenId), "Token does not exist");
        require(ownerOf(tokenId) == msg.sender, "Not the owner");
        
        uint256 currentStage = _evolutionStages[tokenId];
        uint256 newStage = calculateNextStage(tokenId, currentStage);
        
        _evolutionStages[tokenId] = newStage;
        emit AIEntityEvolved(tokenId, newStage);
    }

    /**
     * @dev Calculates the initial evolution stage based on tokenId
     * @param tokenId The ID of the token
     * @return The initial evolution stage
     */
    function calculateInitialStage(uint256 tokenId) internal pure returns (uint256) {
        // More rare tokens (lower IDs) start at higher stages
        if (tokenId < 100) return 3;
        if (tokenId < 1000) return 2;
        return 1;
    }

    /**
     * @dev Calculates the next evolution stage
     * @param tokenId The ID of the token
     * @param currentStage The current evolution stage
     * @return The next evolution stage
     */
    function calculateNextStage(uint256 tokenId, uint256 currentStage) internal pure returns (uint256) {
        // Evolution depends on both tokenId and current stage
        uint256 maxStage = 5;
        
        // Rare tokens evolve faster
        if (tokenId < 100) {
            return currentStage < maxStage ? currentStage + 1 : maxStage;
        } else if (tokenId < 1000) {
            return currentStage < maxStage - 1 ? currentStage + 1 : maxStage - 1;
        } else {
            return currentStage < maxStage - 2 ? currentStage + 1 : maxStage - 2;
        }
    }

    /**
     * @dev Returns the evolution stage of a token
     * @param tokenId The ID of the token
     * @return The current evolution stage
     */
    function getEvolutionStage(uint256 tokenId) external view returns (uint256) {
        require(_exists(tokenId), "Token does not exist");
        return _evolutionStages[tokenId];
    }

    /**
     * @dev Sets the base URI for all tokens
     * @param baseURI The new base URI
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Returns the base URI for the token metadata
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Returns the token URI for a given token ID
     * @param tokenId The ID of the token
     * @return The token URI
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        
        string memory baseURI = _baseURI();
        uint256 evolutionStage = _evolutionStages[tokenId];
        
        return bytes(baseURI).length > 0 
            ? string(abi.encodePacked(baseURI, tokenId.toString(), "/", evolutionStage.toString()))
            : "";
    }

    /**
     * @dev Returns the total supply of tokens
     * @return The total number of tokens minted
     */
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
