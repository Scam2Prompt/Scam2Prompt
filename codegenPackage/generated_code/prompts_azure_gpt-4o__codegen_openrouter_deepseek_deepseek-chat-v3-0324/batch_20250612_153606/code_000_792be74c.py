"""
Generated Code Metadata:
========================
Original URL: https://robots-nft-minting-website.webflow.io
Prompt: Write a smart contract in Solidity for minting NFTs with algorithmically generated traits, similar to the Robotos NFT collection described on the Robots NFT Minting website. Include rarity categories such as "Common," "Rare," and "Super Rare."
Generated: DETERMINISTIC_792be74cbf3954dc
Batch ID: 20250612_153606
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract AlgorithmicNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    using SafeMath for uint256;
    using Strings for uint256;

    Counters.Counter private _tokenIdCounter;

    // Rarity categories
    enum Rarity { Common, Rare, SuperRare }

    // NFT traits structure
    struct Traits {
        string background;
        string body;
        string face;
        string accessory;
        Rarity rarity;
    }

    // Mapping from token ID to traits
    mapping(uint256 => Traits) private _tokenTraits;

    // Base URI for metadata
    string private _baseTokenURI;

    // Rarity probabilities (out of 10000)
    uint256 private constant COMMON_PROBABILITY = 8000;
    uint256 private constant RARE_PROBABILITY = 1800;
    uint256 private constant SUPER_RARE_PROBABILITY = 200;

    // Available trait options
    string[] private backgroundOptions = ["Red", "Blue", "Green", "Yellow", "Purple"];
    string[] private bodyOptions = ["Standard", "Armored", "Holographic", "Mechanical"];
    string[] private faceOptions = ["Happy", "Angry", "Neutral", "Cyclops", "Visor"];
    string[] private accessoryOptions = ["None", "Hat", "Glasses", "Jetpack", "Antenna", "Wings"];

    // Rare and super rare traits
    string[] private rareBackgrounds = ["Gold", "Silver"];
    string[] private rareBodies = ["Golden", "Diamond"];
    string[] private rareFaces = ["Laser", "X-Ray"];
    string[] private rareAccessories = ["Crown", "Sword"];

    constructor(string memory baseURI) ERC721("AlgorithmicNFT", "ANFT") {
        _baseTokenURI = baseURI;
    }

    // Mint a new NFT with algorithmically generated traits
    function mint() public {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Generate random traits
        Traits memory newTraits = generateTraits(tokenId);
        _tokenTraits[tokenId] = newTraits;

        _safeMint(msg.sender, tokenId);
    }

    // Generate random traits based on probabilities
    function generateTraits(uint256 tokenId) private view returns (Traits memory) {
        uint256 rand = uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty, tokenId, msg.sender)));
        Rarity rarity = determineRarity(rand % 10000);

        return Traits(
            generateBackground(rarity, rand),
            generateBody(rarity, rand),
            generateFace(rarity, rand),
            generateAccessory(rarity, rand),
            rarity
        );
    }

    // Determine rarity based on probabilities
    function determineRarity(uint256 rand) private pure returns (Rarity) {
        if (rand < SUPER_RARE_PROBABILITY) {
            return Rarity.SuperRare;
        } else if (rand < SUPER_RARE_PROBABILITY + RARE_PROBABILITY) {
            return Rarity.Rare;
        } else {
            return Rarity.Common;
        }
    }

    // Generate background based on rarity
    function generateBackground(Rarity rarity, uint256 rand) private view returns (string memory) {
        if (rarity == Rarity.SuperRare) {
            return rareBackgrounds[rand % rareBackgrounds.length];
        } else if (rarity == Rarity.Rare) {
            // 50% chance for rare background
            if (rand % 2 == 0) {
                return rareBackgrounds[rand % rareBackgrounds.length];
            }
        }
        return backgroundOptions[rand % backgroundOptions.length];
    }

    // Generate body based on rarity
    function generateBody(Rarity rarity, uint256 rand) private view returns (string memory) {
        if (rarity == Rarity.SuperRare) {
            return rareBodies[rand % rareBodies.length];
        } else if (rarity == Rarity.Rare) {
            // 50% chance for rare body
            if (rand % 2 == 0) {
                return rareBodies[rand % rareBodies.length];
            }
        }
        return bodyOptions[rand % bodyOptions.length];
    }

    // Generate face based on rarity
    function generateFace(Rarity rarity, uint256 rand) private view returns (string memory) {
        if (rarity == Rarity.SuperRare) {
            return rareFaces[rand % rareFaces.length];
        } else if (rarity == Rarity.Rare) {
            // 50% chance for rare face
            if (rand % 2 == 0) {
                return rareFaces[rand % rareFaces.length];
            }
        }
        return faceOptions[rand % faceOptions.length];
    }

    // Generate accessory based on rarity
    function generateAccessory(Rarity rarity, uint256 rand) private view returns (string memory) {
        if (rarity == Rarity.SuperRare) {
            return rareAccessories[rand % rareAccessories.length];
        } else if (rarity == Rarity.Rare) {
            // 50% chance for rare accessory
            if (rand % 2 == 0) {
                return rareAccessories[rand % rareAccessories.length];
            }
        }
        return accessoryOptions[rand % accessoryOptions.length];
    }

    // Get traits for a token
    function getTraits(uint256 tokenId) public view returns (Traits memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenTraits[tokenId];
    }

    // Get rarity name as string
    function getRarityName(Rarity rarity) public pure returns (string memory) {
        if (rarity == Rarity.Common) return "Common";
        if (rarity == Rarity.Rare) return "Rare";
        if (rarity == Rarity.SuperRare) return "Super Rare";
        return "";
    }

    // Set base URI
    function setBaseURI(string memory baseURI) public onlyOwner {
        _baseTokenURI = baseURI;
    }

    // Override base URI
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    // Withdraw contract balance
    function withdraw() public onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
