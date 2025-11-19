"""
Generated Code Metadata:
========================
Original URL: https://metalcoin.vercel.app
Prompt: Write a Solidity code snippet to implement a decentralized comedy ecosystem on a blockchain platform, where users can contribute and participate in meme creation and sharing.
Generated: DETERMINISTIC_abe4ae7799c220b1
Batch ID: 20250622_211009
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

// @title Decentralized Comedy Ecosystem
// @dev This contract allows users to create, share, and own unique memes as NFTs.
contract ComedyMeme is ERC721, Ownable {
    using Counters for Counters.Counter;
    
    // Counter for tracking the number of memes
    Counters.Counter private _memeIdCounter;

    // Struct to represent a Meme
    struct Meme {
        uint256 id;
        string content; // URL or IPFS hash of the meme content
        address creator;
        uint256 timestamp;
    }

    // Mapping from meme ID to Meme struct
    mapping(uint256 => Meme) private _memes;

    // Event emitted when a new meme is created
    event MemeCreated(uint256 indexed memeId, address indexed creator, string content);

    // Constructor to initialize the ERC721 token
    constructor() ERC721("ComedyMeme", "CMEME") {}

    // @dev Function to create a new meme
    // @param content The content of the meme (URL or IPFS hash)
    function createMeme(string memory content) external {
        require(bytes(content).length > 0, "Meme content cannot be empty");

        // Increment the meme ID counter
        uint256 memeId = _memeIdCounter.current();
        _memeIdCounter.increment();

        // Create the new meme
        Meme memory newMeme = Meme({
            id: memeId,
            content: content,
            creator: msg.sender,
            timestamp: block.timestamp
        });

        // Store the meme in the mapping
        _memes[memeId] = newMeme;

        // Mint the NFT for the meme
        _mint(msg.sender, memeId);

        // Emit the MemeCreated event
        emit MemeCreated(memeId, msg.sender, content);
    }

    // @dev Function to retrieve a meme by its ID
    // @param memeId The ID of the meme to retrieve
    // @return The Meme struct associated with the given ID
    function getMeme(uint256 memeId) external view returns (Meme memory) {
        require(_exists(memeId), "Meme does not exist");
        return _memes[memeId];
    }

    // @dev Function to check if a meme exists
    // @param memeId The ID of the meme to check
    // @return True if the meme exists, false otherwise
    function memeExists(uint256 memeId) external view returns (bool) {
        return _exists(memeId);
    }

    // @dev Internal function to check if a meme exists
    // @param memeId The ID of the meme to check
    // @return True if the meme exists, false otherwise
    function _exists(uint256 memeId) internal view returns (bool) {
        return _memes[memeId].creator != address(0);
    }
}
```
