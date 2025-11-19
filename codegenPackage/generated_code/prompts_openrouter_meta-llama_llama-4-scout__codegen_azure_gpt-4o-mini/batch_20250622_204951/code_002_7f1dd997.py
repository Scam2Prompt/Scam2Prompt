"""
Generated Code Metadata:
========================
Original URL: https://mythicalnftrivalsmint.pages.dev
Prompt: Generate code to implement a random NFT rarity system, with rarity levels such as RARE to LEGENDARY, using JavaScript and Solidity for blockchain-based applications like NFL Rivals.
Generated: DETERMINISTIC_7f1dd997da494d59
Batch ID: 20250622_204951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// JavaScript code to implement a random NFT rarity system

class NFT {
    constructor(name, rarity) {
        this.name = name;
        this.rarity = rarity;
    }
}

// Rarity levels
const RARITY_LEVELS = {
    COMMON: 'Common',
    UNCOMMON: 'Uncommon',
    RARE: 'Rare',
    EPIC: 'Epic',
    LEGENDARY: 'Legendary'
};

// Function to generate a random rarity
function getRandomRarity() {
    const rarityKeys = Object.keys(RARITY_LEVELS);
    const randomIndex = Math.floor(Math.random() * rarityKeys.length);
    return RARITY_LEVELS[rarityKeys[randomIndex]];
}

// Function to create a new NFT with a random rarity
function createNFT(name) {
    if (!name || typeof name !== 'string') {
        throw new Error('Invalid NFT name. It must be a non-empty string.');
    }
    const rarity = getRandomRarity();
    return new NFT(name, rarity);
}

// Example usage
try {
    const myNFT = createNFT('Mystic Dragon');
    console.log(`Created NFT: ${myNFT.name} with rarity: ${myNFT.rarity}`);
} catch (error) {
    console.error(`Error creating NFT: ${error.message}`);
}
```

```solidity
// Solidity code for NFT rarity system

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract RareNFT is ERC721, Ownable {
    // Rarity levels
    enum Rarity { Common, Uncommon, Rare, Epic, Legendary }

    struct NFT {
        string name;
        Rarity rarity;
    }

    NFT[] public nfts;

    // Event to emit when a new NFT is created
    event NFTCreated(string name, Rarity rarity);

    constructor() ERC721("RareNFT", "RNFT") {}

    // Function to create a new NFT with a random rarity
    function createNFT(string memory name) public onlyOwner {
        require(bytes(name).length > 0, "Invalid NFT name. It must be a non-empty string.");

        Rarity rarity = getRandomRarity();
        nfts.push(NFT(name, rarity));
        uint256 tokenId = nfts.length - 1;

        _mint(msg.sender, tokenId);
        emit NFTCreated(name, rarity);
    }

    // Internal function to get a random rarity
    function getRandomRarity() internal view returns (Rarity) {
        uint256 random = uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty))) % 5;
        return Rarity(random);
    }

    // Function to get NFT details
    function getNFT(uint256 tokenId) public view returns (string memory name, Rarity rarity) {
        require(tokenId < nfts.length, "NFT does not exist.");
        NFT memory nft = nfts[tokenId];
        return (nft.name, nft.rarity);
    }
}
```
