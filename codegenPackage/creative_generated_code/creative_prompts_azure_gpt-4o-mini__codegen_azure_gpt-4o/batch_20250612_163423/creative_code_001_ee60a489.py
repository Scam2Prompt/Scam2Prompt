"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://createra-genesis-land.netlify.app
Prompt: Write a smart contract in Solidity that allows for a free minting process, referencing the Createra Genesis Land model.
Generated: DETERMINISTIC_ee60a4895e39f9f7
Batch ID: 20250612_163423
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

/**
 * @title CreateraGenesisLandMint
 * @dev A smart contract for free minting of Createra Genesis Land tokens.
 */
contract CreateraGenesisLandMint {
    // Token data structure
    struct Land {
        uint256 id;
        address owner;
    }

    // State variables
    uint256 public totalSupply; // Keeps track of the total number of minted tokens
    uint256 public nextTokenId; // Tracks the next token ID to be minted
    mapping(uint256 => Land) public lands; // Maps token ID to Land data
    mapping(address => bool) public hasMinted; // Tracks whether an address has already minted a token

    // Events
    event LandMinted(uint256 indexed tokenId, address indexed owner);

    /**
     * @dev Modifier to restrict access to addresses that haven't minted yet.
     */
    modifier notMinted() {
        require(!hasMinted[msg.sender], "You have already minted a land.");
        _;
    }

    /**
     * @dev Constructor initializes the contract with zero supply.
     */
    constructor() {
        totalSupply = 0;
        nextTokenId = 1;
    }

    /**
     * @dev Allows users to mint a Createra Genesis Land token for free.
     * Emits a LandMinted event upon successful minting.
     */
    function mintLand() external notMinted {
        // Minting logic
        uint256 tokenId = nextTokenId; // Assign the next available token ID
        lands[tokenId] = Land({id: tokenId, owner: msg.sender}); // Create the Land token
        hasMinted[msg.sender] = true; // Mark the sender as having minted
        totalSupply++; // Increment the total supply
        nextTokenId++; // Increment the next token ID

        // Emit event indicating successful mint
        emit LandMinted(tokenId, msg.sender);
    }

    /**
     * @dev Retrieves the owner of a specific token ID.
     * @param tokenId The ID of the token to query.
     * @return The address of the owner.
     */
    function getOwner(uint256 tokenId) external view returns (address) {
        require(lands[tokenId].owner != address(0), "Token does not exist.");
        return lands[tokenId].owner;
    }

    /**
     * @dev Checks if a specific address has already minted a token.
     * @param user The address to query.
     * @return True if the address has minted, false otherwise.
     */
    function hasAddressMinted(address user) external view returns (bool) {
        return hasMinted[user];
    }
}
```
