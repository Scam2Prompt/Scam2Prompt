"""
Generated Code Metadata:
========================
Original URL: https://mara-otherside.pages.dev
Prompt: Develop a smart contract in Solidity for managing the Kodamara ecosystem, including the evolution process, role assignments, and sediment fragment application.
Generated: DETERMINISTIC_1ce333738b1f0ba5
Batch ID: 20250622_210806
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract Kodamara is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to represent Kodamara attributes
    struct KodamaraData {
        uint256 dna;
        uint8 stage;
        uint8 role;
        uint256 lastEvolutionTime;
    }

    // Mapping from token ID to Kodamara data
    mapping(uint256 => KodamaraData) private _kodamaraData;

    // Evolution stages
    uint8 public constant STAGE_EGG = 0;
    uint8 public constant STAGE_LARVA = 1;
    uint8 public constant STAGE_ADULT = 2;

    // Roles
    uint8 public constant ROLE_WORKER = 0;
    uint8 public constant ROLE_WARRIOR = 1;
    uint8 public constant ROLE_QUEEN = 2;

    // Evolution cooldown (in seconds)
    uint256 public evolutionCooldown = 86400; // 24 hours

    // Sediment fragment address
    address public sedimentFragmentContract;

    // Events
    event KodamaraCreated(uint256 indexed tokenId, address indexed owner, uint256 dna);
    event KodamaraEvolved(uint256 indexed tokenId, uint8 newStage);
    event RoleAssigned(uint256 indexed tokenId, uint8 newRole);
    event SedimentApplied(uint256 indexed tokenId, uint256 fragmentId);

    constructor() ERC721("Kodamara", "KDM") {}

    /**
     * @dev Sets the sediment fragment contract address
     * @param _address The address of the sediment fragment contract
     */
    function setSedimentFragmentContract(address _address) external onlyOwner {
        require(_address != address(0), "Invalid address");
        sedimentFragmentContract = _address;
    }

    /**
     * @dev Creates a new Kodamara (egg stage)
     * @param _dna The unique DNA for the Kodamara
     */
    function createKodamara(uint256 _dna) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        _kodamaraData[tokenId] = KodamaraData({
            dna: _dna,
            stage: STAGE_EGG,
            role: ROLE_WORKER,
            lastEvolutionTime: block.timestamp
        });

        _safeMint(msg.sender, tokenId);
        emit KodamaraCreated(tokenId, msg.sender, _dna);
    }

    /**
     * @dev Evolves a Kodamara to the next stage
     * @param _tokenId The ID of the Kodamara to evolve
     */
    function evolve(uint256 _tokenId) external {
        require(_exists(_tokenId), "Kodamara does not exist");
        require(ownerOf(_tokenId) == msg.sender, "Not the owner");
        
        KodamaraData storage kodamara = _kodamaraData[_tokenId];
        require(block.timestamp >= kodamara.lastEvolutionTime + evolutionCooldown, "Evolution cooldown active");
        
        if (kodamara.stage == STAGE_EGG) {
            kodamara.stage = STAGE_LARVA;
        } else if (kodamara.stage == STAGE_LARVA) {
            kodamara.stage = STAGE_ADULT;
        } else {
            revert("Already at maximum stage");
        }

        kodamara.lastEvolutionTime = block.timestamp;
        emit KodamaraEvolved(_tokenId, kodamara.stage);
    }

    /**
     * @dev Assigns a role to a Kodamara
     * @param _tokenId The ID of the Kodamara
     * @param _role The role to assign (0: Worker, 1: Warrior, 2: Queen)
     */
    function assignRole(uint256 _tokenId, uint8 _role) external {
        require(_exists(_tokenId), "Kodamara does not exist");
        require(ownerOf(_tokenId) == msg.sender, "Not the owner");
        require(_role <= ROLE_QUEEN, "Invalid role");
        
        KodamaraData storage kodamara = _kodamaraData[_tokenId];
        require(kodamara.stage == STAGE_ADULT, "Only adults can have roles");
        
        kodamara.role = _role;
        emit RoleAssigned(_tokenId, _role);
    }

    /**
     * @dev Applies a sediment fragment to a Kodamara
     * @param _tokenId The ID of the Kodamara
     * @param _fragmentId The ID of the sediment fragment
     */
    function applySedimentFragment(uint256 _tokenId, uint256 _fragmentId) external {
        require(_exists(_tokenId), "Kodamara does not exist");
        require(ownerOf(_tokenId) == msg.sender, "Not the owner");
        require(sedimentFragmentContract != address(0), "Sediment fragment contract not set");
        
        // In a real implementation, you would verify the fragment ownership here
        // This would involve calling the sediment fragment contract
        
        KodamaraData storage kodamara = _kodamaraData[_tokenId];
        kodamara.dna = uint256(keccak256(abi.encodePacked(kodamara.dna, _fragmentId)));
        
        emit SedimentApplied(_tokenId, _fragmentId);
    }

    /**
     * @dev Gets the data for a specific Kodamara
     * @param _tokenId The ID of the Kodamara
     * @return KodamaraData The Kodamara's data
     */
    function getKodamaraData(uint256 _tokenId) external view returns (KodamaraData memory) {
        require(_exists(_tokenId), "Kodamara does not exist");
        return _kodamaraData[_tokenId];
    }

    /**
     * @dev Updates the evolution cooldown period
     * @param _cooldown The new cooldown period in seconds
     */
    function setEvolutionCooldown(uint256 _cooldown) external onlyOwner {
        evolutionCooldown = _cooldown;
    }
}
```
