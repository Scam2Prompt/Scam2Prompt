"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://citizwentokyo.pages.dev
Prompt: Develop a smart contract in Solidity that facilitates the minting of new identities and lands in the Neo Tokyo metaverse, adhering to the token cost specifications provided.
Generated: DETERMINISTIC_59686e4f4041df0c
Batch ID: 20250612_153400
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

// Importing the ERC721 interface and Ownable contract from OpenZeppelin
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for minting identities and lands in the Neo Tokyo metaverse
contract NeoTokyoMetaverse is ERC721, Ownable {
    // Events for minting identities and lands
    event IdentityMinted(address indexed owner, uint256 indexed tokenId);
    event LandMinted(address indexed owner, uint256 indexed tokenId);

    // Mapping to track minted identities and lands
    mapping(uint256 => bool) private _identityMinted;
    mapping(uint256 => bool) private _landMinted;

    // Cost to mint identities and lands
    uint256 public identityCost = 0.1 ether; // Set identity cost
    uint256 public landCost = 0.2 ether;      // Set land cost

    // Counter for token IDs
    uint256 private _identityTokenIdCounter;
    uint256 private _landTokenIdCounter;

    // Constructor to initialize the contract
    constructor() ERC721("NeoTokyoIdentity", "NTI") {}

    // Function to mint a new identity
    function mintIdentity() external payable {
        require(msg.value == identityCost, "Incorrect ether value sent");
        require(!_identityMinted[_identityTokenIdCounter], "Identity already minted");

        // Mint the identity
        _mint(msg.sender, _identityTokenIdCounter);
        _identityMinted[_identityTokenIdCounter] = true;

        emit IdentityMinted(msg.sender, _identityTokenIdCounter);
        _identityTokenIdCounter++; // Increment the identity token ID counter
    }

    // Function to mint new land
    function mintLand() external payable {
        require(msg.value == landCost, "Incorrect ether value sent");
        require(!_landMinted[_landTokenIdCounter], "Land already minted");

        // Mint the land
        _mint(msg.sender, _landTokenIdCounter);
        _landMinted[_landTokenIdCounter] = true;

        emit LandMinted(msg.sender, _landTokenIdCounter);
        _landTokenIdCounter++; // Increment the land token ID counter
    }

    // Function to withdraw contract balance to the owner's address
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // Function to update the cost of minting identities
    function setIdentityCost(uint256 newCost) external onlyOwner {
        identityCost = newCost;
    }

    // Function to update the cost of minting lands
    function setLandCost(uint256 newCost) external onlyOwner {
        landCost = newCost;
    }
}
```
