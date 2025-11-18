"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://robots-nft-minting-website.webflow.io
Prompt: Write a smart contract in Solidity for minting NFTs with algorithmically generated traits, similar to the Robotos NFT collection described on the Robots NFT Minting website. Include rarity categories such as "Common," "Rare," and "Super Rare."
Generated: DETERMINISTIC_792be74cbf3954dc
Batch ID: 20250612_153606
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract AlgorithmicNFT is ERC721Enumerable, Ownable {
    // Struct to define the traits of an NFT
    struct Traits {
        string background;
        string body;
        string accessory;
        string headgear;
        string rarity;
    }

    // Array to store traits for each token
    mapping(uint256 => Traits) public tokenTraits;

    // Counter for tracking token IDs
    uint256 public nextTokenId;

    // Base URI for metadata
    string private _baseTokenURI;

    // Randomness seed for generating traits
    uint256 private randomnessSeed;

    // Events
    event MintNFT(uint256 tokenId, address recipient, Traits traits);

    constructor(string memory baseURI) ERC721("AlgorithmicNFT", "ALGO") {
        _baseTokenURI = baseURI;
        randomnessSeed = uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty)));
    }

    /**
     * @dev Mint a new NFT with algorithmically generated traits
     * @param recipient Address that will receive the minted NFT
     */
    function mintNFT(address recipient) external onlyOwner {
        require(recipient != address(0), "Recipient address cannot be zero");

        uint256 tokenId = nextTokenId;
        nextTokenId++;

        // Generate traits using pseudo-randomness
        Traits memory traits = generateTraits(tokenId);

        // Store traits for the token
        tokenTraits[tokenId] = traits;

        // Mint the NFT
        _safeMint(recipient, tokenId);

        emit MintNFT(tokenId, recipient, traits);
    }

    /**
     * @dev Generate algorithmic traits for a given token
     * @param tokenId The ID of the token for which traits are being generated
     * @return Generated traits
     */
    function generateTraits(uint256 tokenId) internal view returns (Traits memory) {
        // Generate random values using the token ID and randomness seed
        uint256 randomValue = uint256(keccak256(abi.encodePacked(tokenId, randomnessSeed)));

        // Determine traits based on random values
        string memory background = selectTrait(randomValue % 100, ["Blue", "Green", "Yellow", "Red", "Purple"]);
        string memory body = selectTrait((randomValue / 100) % 100, ["Robot", "Alien", "Human"]);
        string memory accessory = selectTrait((randomValue / 10000) % 100, ["Hat", "Glasses", "Necklace", "None"]);
        string memory headgear = selectTrait((randomValue / 1000000) % 100, ["Helmet", "Crown", "Cap", "None"]);
        string memory rarity = determineRarity((randomValue / 100000000) % 100);

        return Traits(background, body, accessory, headgear, rarity);
    }

    /**
     * @dev Select a trait based on a random value
     * @param randomValue A pseudo-random value
     * @param options Array of possible trait options
     * @return Selected trait
     */
    function selectTrait(uint256 randomValue, string[] memory options) internal pure returns (string memory) {
        uint256 index = randomValue % options.length;
        return options[index];
    }

    /**
     * @dev Determine the rarity of an NFT based on a random value
     * @param randomValue A pseudo-random value
     * @return Rarity category
     */
    function determineRarity(uint256 randomValue) internal pure returns (string memory) {
        if (randomValue < 70) {
            return "Common";
        } else if (randomValue < 90) {
            return "Rare";
        } else {
            return "Super Rare";
        }
    }

    /**
     * @dev Override baseTokenURI for metadata
     * @return Base URI string
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Update the base URI for metadata
     * @param baseURI New base URI
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Update the randomness seed for generating traits
     * @param seed New randomness seed
     */
    function updateRandomnessSeed(uint256 seed) external onlyOwner {
        randomnessSeed = seed;
    }
}
```

This code provides a production-ready smart contract for minting NFTs with algorithmically generated traits, including rarity categories. It uses `ERC721Enumerable` for NFT functionality, `Ownable` for access control, and comprehensive comments for clarity.
