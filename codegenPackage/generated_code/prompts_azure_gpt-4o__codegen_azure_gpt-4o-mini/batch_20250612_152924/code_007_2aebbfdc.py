"""
Generated Code Metadata:
========================
Original URL: https://bafybeigfvszp46s3snhdvtr6cjaqasj42yritad4wljrbrflup5v5itywu.ipfs.dweb.link
Prompt: Write a Solidity smart contract for implementing the play-to-earn mechanics in the Valhalla metaverse, including NFT Vera capture, farming, and clan formation.
Generated: DETERMINISTIC_2aebbfdcd2773a71
Batch ID: 20250612_152924
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

// Importing OpenZeppelin contracts for ERC721 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Contract for the Valhalla metaverse
contract ValhallaMetaverse is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a Vera NFT
    struct Vera {
        uint256 id;
        string name;
        uint256 power;
        bool isCaptured;
    }

    // Mapping from token ID to Vera
    mapping(uint256 => Vera) public veras;

    // Counter for generating unique token IDs
    Counters.Counter private _veraIdCounter;

    // Event emitted when a Vera is captured
    event VeraCaptured(uint256 indexed veraId, address indexed owner);

    // Event emitted when a clan is formed
    event ClanFormed(address indexed clanLeader, string clanName);

    // Struct to represent a Clan
    struct Clan {
        string name;
        address leader;
        uint256 memberCount;
    }

    // Mapping from clan leader to their clan
    mapping(address => Clan) public clans;

    // Modifier to check if the Vera is captured
    modifier onlyCaptured(uint256 veraId) {
        require(veras[veraId].isCaptured, "Vera is not captured");
        _;
    }

    // Constructor to initialize the contract
    constructor() ERC721("ValhallaVera", "VVERA") {}

    // Function to capture a Vera NFT
    function captureVera(string memory name, uint256 power) external {
        _veraIdCounter.increment();
        uint256 newVeraId = _veraIdCounter.current();

        veras[newVeraId] = Vera({
            id: newVeraId,
            name: name,
            power: power,
            isCaptured: true
        });

        _mint(msg.sender, newVeraId);
        emit VeraCaptured(newVeraId, msg.sender);
    }

    // Function to form a clan
    function formClan(string memory clanName) external {
        require(bytes(clanName).length > 0, "Clan name cannot be empty");
        require(clans[msg.sender].leader == address(0), "You already have a clan");

        clans[msg.sender] = Clan({
            name: clanName,
            leader: msg.sender,
            memberCount: 1
        });

        emit ClanFormed(msg.sender, clanName);
    }

    // Function to join an existing clan
    function joinClan(address clanLeader) external {
        require(clans[clanLeader].leader != address(0), "Clan does not exist");
        require(clans[clanLeader].leader != msg.sender, "You are the clan leader");

        clans[clanLeader].memberCount += 1;
    }

    // Function to get details of a Vera
    function getVeraDetails(uint256 veraId) external view returns (Vera memory) {
        require(_exists(veraId), "Vera does not exist");
        return veras[veraId];
    }

    // Function to get clan details
    function getClanDetails(address clanLeader) external view returns (Clan memory) {
        require(clans[clanLeader].leader != address(0), "Clan does not exist");
        return clans[clanLeader];
    }
}
```
