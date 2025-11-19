"""
Generated Code Metadata:
========================
Original URL: https://topgtest.vercel.app
Prompt: Write a smart contract in Solidity that ensures a price of 0 ETH for NFT minting and limits minting to one NFT per wallet, as described in the Masked Soldiers giveaway.
Generated: DETERMINISTIC_fd2b034341bf4d5a
Batch ID: 20250612_152511
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

/**
 * @title MaskedSoldiersNFT
 * @dev A smart contract for minting Masked Soldiers NFTs with specific rules.
 */
contract MaskedSoldiersNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking the number of minted NFTs
    Counters.Counter private _tokenIdCounter;

    // Mapping to track if an address has already minted an NFT
    mapping(address => bool) private _hasMinted;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 tokenId);

    // Constructor to set the name and symbol of the NFT collection
    constructor() ERC721("Masked Soldiers", "MSNFT") {}

    /**
     * @dev Function to mint a new NFT.
     * Can only be called once per wallet and is free of charge.
     */
    function mintNFT() external {
        // Check if the caller has already minted an NFT
        require(!_hasMinted[msg.sender], "You have already minted an NFT.");

        // Mint the NFT
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);

        // Mark the caller as having minted an NFT
        _hasMinted[msg.sender] = true;

        // Increment the token ID counter
        _tokenIdCounter.increment();

        // Emit the NFTMinted event
        emit NFTMinted(msg.sender, tokenId);
    }

    /**
     * @dev Function to check if an address has minted an NFT.
     * @param owner The address to check.
     * @return bool indicating whether the address has minted an NFT.
     */
    function hasMinted(address owner) external view returns (bool) {
        return _hasMinted[owner];
    }

    /**
     * @dev Function to withdraw any accidentally sent Ether to the contract.
     * Only the owner can call this function.
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers to the contract.
     */
    receive() external payable {
        revert("This contract does not accept Ether.");
    }
}
```
