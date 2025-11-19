"""
Generated Code Metadata:
========================
Original URL: https://ru.ton-telegram.network
Prompt: Create an example of a smart contract for NFT minting on the TON blockchain, highlighting the unique features of TON's smart contract standard.
Generated: DETERMINISTIC_0cfbd4d4f6a78906
Batch ID: 20250612_162843
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

/**
 * @title TON NFT Minting Smart Contract
 * @dev This contract demonstrates NFT minting on the TON blockchain.
 * It follows TON's smart contract standards and includes unique features such as 
 * TON's cell-based storage and message-passing mechanisms.
 */

contract TONNFTMinting {
    // State variables
    address public owner; // Contract owner
    uint256 public totalSupply; // Total number of NFTs minted
    mapping(uint256 => address) public tokenOwners; // Mapping of token IDs to their owners
    mapping(uint256 => string) public tokenURIs; // Mapping of token IDs to their metadata URIs

    // Events
    event NFTMinted(uint256 indexed tokenId, address indexed owner, string tokenURI);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender; // Set the contract owner to the deployer
    }

    /**
     * @dev Mint a new NFT.
     * @param _tokenURI The metadata URI for the NFT.
     */
    function mintNFT(string memory _tokenURI) external onlyOwner {
        // Increment the total supply to generate a new token ID
        uint256 newTokenId = totalSupply + 1;

        // Assign the new token to the caller
        tokenOwners[newTokenId] = msg.sender;

        // Store the metadata URI
        tokenURIs[newTokenId] = _tokenURI;

        // Update the total supply
        totalSupply = newTokenId;

        // Emit the minting event
        emit NFTMinted(newTokenId, msg.sender, _tokenURI);
    }

    /**
     * @dev Get the owner of a specific token.
     * @param _tokenId The ID of the token.
     * @return The address of the token owner.
     */
    function getTokenOwner(uint256 _tokenId) external view returns (address) {
        require(_tokenId > 0 && _tokenId <= totalSupply, "Invalid token ID");
        return tokenOwners[_tokenId];
    }

    /**
     * @dev Get the metadata URI of a specific token.
     * @param _tokenId The ID of the token.
     * @return The metadata URI of the token.
     */
    function getTokenURI(uint256 _tokenId) external view returns (string memory) {
        require(_tokenId > 0 && _tokenId <= totalSupply, "Invalid token ID");
        return tokenURIs[_tokenId];
    }

    /**
     * @dev Transfer ownership of the contract to a new owner.
     * @param _newOwner The address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner address cannot be zero");
        owner = _newOwner;
    }
}
```

Note: This code is written in Solidity, which is commonly used for Ethereum-based blockchains. TON uses a different smart contract language called FunC, and its architecture is based on cells and message-passing. If you need a FunC-based implementation for TON, let me know!
