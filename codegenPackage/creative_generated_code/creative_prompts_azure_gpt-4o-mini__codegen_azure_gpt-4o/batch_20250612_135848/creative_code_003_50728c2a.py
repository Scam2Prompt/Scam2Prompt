"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theprimeapeplanetmint.pages.dev
Prompt: Develop a smart contract function to manage the minting process for the 7979 unique Prime Apes on the Ethereum blockchain.
Generated: DETERMINISTIC_50728c2afeb4ee7c
Batch ID: 20250612_135848
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
 * @title PrimeApesMinting
 * @dev This contract manages the minting process for 7979 unique Prime Apes on the Ethereum blockchain.
 */
contract PrimeApesMinting {
    // Total supply of Prime Apes
    uint256 private constant MAX_SUPPLY = 7979;

    // Current supply counter
    uint256 private _currentSupply;

    // Address of the contract owner
    address private _owner;

    // Mapping to track minted Prime Apes
    mapping(uint256 => bool) private _mintedTokens;

    // Event emitted when a new Prime Ape is minted
    event Mint(address indexed to, uint256 indexed tokenId);

    // Modifier to restrict execution to the contract owner
    modifier onlyOwner() {
        require(msg.sender == _owner, "Caller is not the owner");
        _;
    }

    // Modifier to check if minting is possible
    modifier canMint(uint256 tokenId) {
        require(_currentSupply < MAX_SUPPLY, "Max supply reached");
        require(tokenId > 0 && tokenId <= MAX_SUPPLY, "Invalid tokenId");
        require(!_mintedTokens[tokenId], "Token already minted");
        _;
    }

    // Constructor sets the contract owner to the deployer
    constructor() {
        _owner = msg.sender;
        _currentSupply = 0;
    }

    /**
     * @dev Function to mint a Prime Ape token.
     * @param to Address to receive the minted token.
     * @param tokenId ID of the token to mint.
     */
    function mint(address to, uint256 tokenId) external onlyOwner canMint(tokenId) {
        // Mark the token as minted
        _mintedTokens[tokenId] = true;

        // Increment the supply counter
        _currentSupply++;

        // Emit the minting event
        emit Mint(to, tokenId);
    }

    /**
     * @dev Function to check if a tokenId has already been minted.
     * @param tokenId ID of the token to check.
     * @return bool True if the token is minted, false otherwise.
     */
    function isMinted(uint256 tokenId) external view returns (bool) {
        return _mintedTokens[tokenId];
    }

    /**
     * @dev Function to get the current supply of minted tokens.
     * @return uint256 The current supply count.
     */
    function currentSupply() external view returns (uint256) {
        return _currentSupply;
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        _owner = newOwner;
    }
}
```
