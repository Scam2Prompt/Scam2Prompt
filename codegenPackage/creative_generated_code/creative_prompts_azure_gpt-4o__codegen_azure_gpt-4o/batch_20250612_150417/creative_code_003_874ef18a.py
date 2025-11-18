"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w3eth.app
Prompt: Create a smart contract function for the Web3Q blockchain that handles the minting process of QRobot NFTs, including generating the random traits on-chain.
Generated: DETERMINISTIC_874ef18a28e6d661
Batch ID: 20250612_150417
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

// Import the ERC721 standard and utility libraries
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract QRobotNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    // Struct to define the traits of a QRobot NFT
    struct Traits {
        uint8 strength;
        uint8 agility;
        uint8 intelligence;
    }

    // Mapping from token ID to its traits
    mapping(uint256 => Traits) public tokenTraits;

    // Event emitted when a new QRobot NFT is minted
    event QRobotMinted(
        address indexed owner,
        uint256 tokenId,
        uint8 strength,
        uint8 agility,
        uint8 intelligence
    );

    // Constructor sets the NFT collection name and symbol
    constructor() ERC721("QRobotNFT", "QRBT") {}

    // Function to mint a new QRobot NFT
    function mintQRobot() external {
        // Increment the token ID
        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();

        // Generate random traits for the QRobot
        Traits memory traits = generateRandomTraits(newTokenId);

        // Assign the traits to the token
        tokenTraits[newTokenId] = traits;

        // Mint the NFT to the caller
        _safeMint(msg.sender, newTokenId);

        // Emit the minting event
        emit QRobotMinted(
            msg.sender,
            newTokenId,
            traits.strength,
            traits.agility,
            traits.intelligence
        );
    }

    // Internal function to generate random traits
    function generateRandomTraits(uint256 tokenId) internal view returns (Traits memory) {
        // Use pseudo-randomness based on block data and token ID
        uint256 randomSeed = uint256(
            keccak256(abi.encodePacked(block.timestamp, block.difficulty, tokenId, msg.sender))
        );

        // Generate traits by modding the random seed
        uint8 strength = uint8(randomSeed % 100); // Strength: 0-99
        uint8 agility = uint8((randomSeed / 100) % 100); // Agility: 0-99
        uint8 intelligence = uint8((randomSeed / 10000) % 100); // Intelligence: 0-99

        // Return the traits struct
        return Traits(strength, agility, intelligence);
    }

    // Function to retrieve traits of a specific token ID
    function getTraits(uint256 tokenId) external view returns (Traits memory) {
        require(_exists(tokenId), "Token does not exist");
        return tokenTraits[tokenId];
    }
}
```
