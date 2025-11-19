"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smeth.pages.dev
Prompt: Write a smart contract in Solidity that allows users to mint CryptoPunks, ensuring it adheres to the unique minting rules such as a maximum supply of 1,000 and a mint price of 0.00 ETH.
Generated: DETERMINISTIC_aa608e4a1866dc13
Batch ID: 20250612_135818
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
 * @title CryptoPunksMinting
 * @notice A smart contract for minting CryptoPunks with strict rules.
 */
contract CryptoPunksMinting {
    // Maximum supply of CryptoPunks
    uint256 public constant MAX_SUPPLY = 1000;

    // Price per CryptoPunk (free mint in this case)
    uint256 public constant MINT_PRICE = 0;

    // Total number of CryptoPunks minted
    uint256 public totalSupply;

    // Mapping to track ownership of CryptoPunks
    mapping(uint256 => address) public punkOwners;

    // Event emitted when a new CryptoPunk is minted
    event PunkMinted(uint256 indexed punkId, address indexed owner);

    /**
     * @notice Allows a user to mint a CryptoPunk if minting rules are satisfied.
     */
    function mintPunk() external {
        // Ensure the total supply has not exceeded the maximum allowed supply
        require(totalSupply < MAX_SUPPLY, "Maximum supply reached");

        // Ensure the mint price is zero (free mint)
        require(msg.value == MINT_PRICE, "Minting requires 0 ETH");

        // Generate the next punk ID
        uint256 punkId = totalSupply;

        // Assign ownership of the punk to the sender
        punkOwners[punkId] = msg.sender;

        // Increment the total supply
        totalSupply++;

        // Emit an event to notify about the minting
        emit PunkMinted(punkId, msg.sender);
    }

    /**
     * @notice Function to check ownership of a specific CryptoPunk.
     * @param punkId The ID of the CryptoPunk to check.
     * @return The address of the owner.
     */
    function ownerOf(uint256 punkId) external view returns (address) {
        // Ensure the punk ID is valid
        require(punkId < totalSupply, "Invalid punk ID");
        return punkOwners[punkId];
    }
}
```
