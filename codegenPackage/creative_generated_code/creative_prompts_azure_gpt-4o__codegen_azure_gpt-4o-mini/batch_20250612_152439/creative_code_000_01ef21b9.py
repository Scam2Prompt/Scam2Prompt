"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peaq-token.pages.dev
Prompt: Write a smart contract using the peaq token for minting Machine NFTs as described in the peaq documentation. Include functionality for assigning ownership within the Economy of Things.
Generated: DETERMINISTIC_01ef21b915dafc1a
Batch ID: 20250612_152439
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

// Import the ERC721 interface for NFT standard
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// PeaqToken interface for minting functionality
interface IPeaqToken {
    function mint(address to, uint256 amount) external returns (bool);
}

// Smart contract for minting Machine NFTs
contract MachineNFT is ERC721URIStorage, Ownable {
    // Token ID counter
    uint256 private _tokenIdCounter;

    // Instance of the PeaqToken contract
    IPeaqToken private _peaqToken;

    // Event for tracking machine ownership assignment
    event MachineOwnershipAssigned(uint256 indexed tokenId, address indexed newOwner);

    // Constructor to initialize the contract
    constructor(address peaqTokenAddress) ERC721("MachineNFT", "MNT") {
        require(peaqTokenAddress != address(0), "Invalid PeaqToken address");
        _peaqToken = IPeaqToken(peaqTokenAddress);
    }

    // Function to mint a new machine NFT
    function mintMachineNFT(string memory tokenURI, uint256 peaqAmount) external onlyOwner {
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");

        // Minting Peaq tokens before minting the NFT
        require(_peaqToken.mint(msg.sender, peaqAmount), "Failed to mint Peaq tokens");

        // Increment the token ID counter
        _tokenIdCounter += 1;

        // Mint the NFT
        _mint(msg.sender, _tokenIdCounter);
        _setTokenURI(_tokenIdCounter, tokenURI);
    }

    // Function to assign ownership of a machine NFT
    function assignOwnership(uint256 tokenId, address newOwner) external {
        require(_exists(tokenId), "Token does not exist");
        require(msg.sender == ownerOf(tokenId), "Caller is not the owner of the token");
        require(newOwner != address(0), "New owner cannot be the zero address");

        // Transfer the NFT to the new owner
        _transfer(msg.sender, newOwner, tokenId);

        // Emit the ownership assignment event
        emit MachineOwnershipAssigned(tokenId, newOwner);
    }

    // Function to get the current token counter
    function getCurrentTokenId() external view returns (uint256) {
        return _tokenIdCounter;
    }
}
```
