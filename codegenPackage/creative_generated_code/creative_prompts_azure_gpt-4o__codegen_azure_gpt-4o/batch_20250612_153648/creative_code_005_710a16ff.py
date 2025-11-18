"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cyberlamas.pages.dev
Prompt: Develop a Solidity smart contract that includes circulation-limiting mechanisms for NFTs, as described in the Cyber Lama NFT collection roadmap.
Generated: DETERMINISTIC_710a16ff142e91e1
Batch ID: 20250612_153648
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
 * @title CyberLamaNFT
 * @dev A smart contract for managing the minting and circulation of Cyber Lama NFTs,
 * including mechanisms to limit the total supply based on the project roadmap.
 */
contract CyberLamaNFT {
    // Events
    event NFTMinted(address indexed to, uint256 tokenId);

    // State variables
    uint256 public constant MAX_SUPPLY = 10000; // Maximum number of NFTs allowed
    uint256 public currentSupply; // Tracks the current number of minted NFTs
    uint256 private nextTokenId; // Tracks the next token ID to be minted
    address public owner; // Contract owner

    // Mapping to store token ownership
    mapping(uint256 => address) private tokenOwners;

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier canMint(uint256 amount) {
        require(currentSupply + amount <= MAX_SUPPLY, "Exceeds maximum supply of NFTs");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender; // Set the deployer as the owner
        nextTokenId = 1; // Start token IDs at 1
    }

    /**
     * @dev Mint new NFTs
     * @param to Address to receive the minted NFTs
     * @param amount Number of NFTs to mint
     */
    function mint(address to, uint256 amount) external onlyOwner canMint(amount) {
        require(to != address(0), "Minting address cannot be zero");

        for (uint256 i = 0; i < amount; i++) {
            uint256 tokenId = nextTokenId;
            tokenOwners[tokenId] = to;
            nextTokenId++;
            currentSupply++;

            emit NFTMinted(to, tokenId); // Emit minting event
        }
    }

    /**
     * @dev Get the owner of a specific token
     * @param tokenId The ID of the token to query
     * @return Address of the owner, or zero address if token doesn't exist
     */
    function ownerOf(uint256 tokenId) external view returns (address) {
        address tokenOwner = tokenOwners[tokenId];
        require(tokenOwner != address(0), "Token does not exist");
        return tokenOwner;
    }

    /**
     * @dev Get total NFTs minted so far
     * @return The current total supply of minted NFTs
     */
    function totalSupply() external view returns (uint256) {
        return currentSupply;
    }

    /**
     * @dev Transfer ownership of the contract
     * @param newOwner The address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be zero address");
        owner = newOwner;
    }
}
```
