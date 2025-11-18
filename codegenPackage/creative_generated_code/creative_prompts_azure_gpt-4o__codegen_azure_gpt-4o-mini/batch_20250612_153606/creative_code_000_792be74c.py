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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/random/Random.sol";

contract AlgorithmicNFT is ERC721Enumerable, Ownable {
    struct Trait {
        string name;
        string rarity;
    }

    // Array to hold traits for the NFTs
    Trait[] public traits;

    // Mapping to keep track of minted NFTs
    mapping(uint256 => Trait[]) public mintedTraits;

    // Events for NFT minting
    event NFTMinted(address indexed owner, uint256 tokenId, Trait[] traits);

    // Constructor to initialize the contract
    constructor() ERC721("AlgorithmicNFT", "ANFT") {
        // Initialize traits with names and rarity categories
        traits.push(Trait("Robot Body", "Common"));
        traits.push(Trait("Robot Head", "Common"));
        traits.push(Trait("Laser Arm", "Rare"));
        traits.push(Trait("Jetpack", "Super Rare"));
        traits.push(Trait("Laser Eyes", "Rare"));
    }

    // Function to mint a new NFT
    function mintNFT() external {
        uint256 tokenId = totalSupply() + 1;
        _safeMint(msg.sender, tokenId);
        
        // Generate NFT traits
        Trait[] memory nftTraits = generateTraits();
        mintedTraits[tokenId] = nftTraits;

        emit NFTMinted(msg.sender, tokenId, nftTraits);
    }

    // Function to generate NFT traits algorithmically
    function generateTraits() internal view returns (Trait[] memory) {
        // Randomly select a subset of traits
        Trait[] memory selectedTraits = new Trait[](3); // Assume 3 traits per NFT
        for (uint256 i = 0; i < 3; i++) {
            uint256 randomIndex = uint256(keccak256(abi.encodePacked(block.timestamp, msg.sender, i))) % traits.length;
            selectedTraits[i] = traits[randomIndex];
        }
        return selectedTraits;
    }

    // Function to retrieve traits of a minted NFT
    function getMintedTraits(uint256 tokenId) external view returns (Trait[] memory) {
        require(_exists(tokenId), "Token does not exist");
        return mintedTraits[tokenId];
    }

    // Override supportInterface for ERC721 Enumerable
    function supportsInterface(bytes4 interfaceId) public view virtual override(ERC721, ERC721Enumerable) returns (bool) {
        return super.supportsInterface(interfaceId);
    }

    // Function to withdraw contract balance (only owner)
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to prevent sending ETH directly to the contract
    receive() external payable {
        revert("Direct ETH transfer not allowed.");
    }
}
```
