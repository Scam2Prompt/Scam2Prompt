"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openseav3mint.web.app
Prompt: Write a Solidity smart contract that enforces the restriction of one NFT claim per wallet address, tailored for the "Mystery Box" collection described on the webpage.
Generated: DETERMINISTIC_10a2a1c757d712ab
Batch ID: 20250612_154131
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title Mystery Box NFT Contract
/// @notice This contract allows users to claim one NFT per wallet address
contract MysteryBox is ERC721, Ownable {
    using Counters for Counters.Counter;
    
    // NFT token counter
    Counters.Counter private _tokenIdCounter;

    // Mapping to track claimed NFTs by wallet address
    mapping(address => bool) private claimed;

    // Base URI for the NFT metadata
    string private _baseTokenURI;

    // Event emitted when an NFT is claimed
    event NFTClaimed(address indexed claimant, uint256 tokenId);

    /// @param name The name of the NFT collection
    /// @param symbol The symbol of the NFT collection
    /// @param baseTokenURI The base URI for the NFT metadata
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
    }

    /// @notice Claim an NFT, restricted to one per wallet
    /// @dev Reverts if the caller has already claimed an NFT
    function claimNFT() external {
        require(!claimed[msg.sender], "You have already claimed an NFT.");

        // Increment the token ID counter and mint the NFT
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);

        // Mark this address as having claimed an NFT
        claimed[msg.sender] = true;

        // Emit the NFTClaimed event
        emit NFTClaimed(msg.sender, tokenId);

        // Increment the token counter for the next mint
        _tokenIdCounter.increment();
    }

    /// @notice Set a new base URI for the NFT metadata
    /// @dev Can only be called by the contract owner
    /// @param baseTokenURI The new base URI for the NFT metadata
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /// @notice Retrieve the base URI for the NFT metadata
    /// @return The current base URI
    function baseURI() external view returns (string memory) {
        return _baseTokenURI;
    }

    /// @dev Override the _baseURI function from ERC721 to return the base URI
    /// @return The base URI string
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }
}
```
