"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-two.vercel.app
Prompt: Develop a smart contract in Solidity that supports limited edition NFT drops (e.g., 10 editions for "The Decay"), as outlined in the content.
Generated: DETERMINISTIC_6e4af69ea84a28e9
Batch ID: 20250612_151329
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
import "@openzeppelin/contracts/utils/Counters.sol";

// LimitedEditionNFT is a smart contract for managing limited edition NFTs
contract LimitedEditionNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    
    // Structure to hold NFT details
    struct Edition {
        string name;
        uint256 totalSupply;
        uint256 minted;
    }

    // Mapping to store editions by their IDs
    mapping(uint256 => Edition) public editions;
    
    // Counter for edition IDs
    Counters.Counter private editionIdCounter;

    // Event to log the creation of a new edition
    event EditionCreated(uint256 indexed editionId, string name, uint256 totalSupply);
    
    // Event to log NFT minting
    event NFTMinted(address indexed to, uint256 indexed editionId, uint256 tokenId);

    // Constructor to initialize the NFT collection
    constructor() ERC721("LimitedEditionNFT", "LENFT") {}

    // Function to create a new limited edition NFT
    function createEdition(string memory _name, uint256 _totalSupply) external onlyOwner {
        require(_totalSupply > 0, "Total supply must be greater than 0");
        
        editionIdCounter.increment();
        uint256 newEditionId = editionIdCounter.current();
        
        editions[newEditionId] = Edition({
            name: _name,
            totalSupply: _totalSupply,
            minted: 0
        });

        emit EditionCreated(newEditionId, _name, _totalSupply);
    }

    // Function to mint an NFT from a specific edition
    function mintNFT(uint256 _editionId) external {
        Edition storage edition = editions[_editionId];

        // Check if the edition exists and has supply left
        require(edition.minted < edition.totalSupply, "All NFTs for this edition have been minted");

        // Increment the minted count and mint the NFT
        edition.minted += 1;
        uint256 tokenId = totalSupply() + 1; // Get the next token ID

        _mint(msg.sender, tokenId);
        emit NFTMinted(msg.sender, _editionId, tokenId);
    }

    // Function to get the details of an edition
    function getEditionDetails(uint256 _editionId) external view returns (string memory, uint256, uint256) {
        Edition storage edition = editions[_editionId];
        require(edition.totalSupply > 0, "Edition does not exist");

        return (edition.name, edition.totalSupply, edition.minted);
    }
}
```
