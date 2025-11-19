"""
Generated Code Metadata:
========================
Original URL: https://real-infected-mint.vercel.app
Prompt: Design a smart contract for the Real Infected Mint project that handles public minting of NFTs at a price of 0.89 SOL, with unlimited supply.
Generated: DETERMINISTIC_db8aa7b4c47b6a09
Batch ID: 20250622_205411
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
 * @title RealInfectedMint
 * @dev A smart contract for public minting of NFTs with unlimited supply.
 *      Each NFT costs 0.89 SOL (converted to wei for Ethereum compatibility).
 */
contract RealInfectedMint {
    // State variables
    uint256 public constant MINT_PRICE = 0.89 ether; // Price per NFT in wei
    address public owner; // Contract owner
    uint256 public totalMinted; // Total number of NFTs minted

    // Mapping to track ownership of NFTs
    mapping(uint256 => address) public nftOwners;

    // Events
    event NFTMinted(address indexed minter, uint256 indexed tokenId);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier validPayment() {
        require(msg.value == MINT_PRICE, "Incorrect payment amount");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
    }

    /**
     * @dev Public function to mint an NFT.
     *      Requires payment of 0.89 SOL (converted to wei).
     */
    function mint() external payable validPayment {
        uint256 tokenId = totalMinted + 1; // Generate a new token ID
        nftOwners[tokenId] = msg.sender; // Assign ownership of the NFT
        totalMinted++; // Increment the total minted count

        emit NFTMinted(msg.sender, tokenId); // Emit the minting event
    }

    /**
     * @dev Function to withdraw contract balance to the owner's address.
     *      Only callable by the owner.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance; // Get contract balance
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Function to transfer ownership of the contract.
     *      Only callable by the current owner.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct payments not allowed");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct payments not allowed");
    }
}
```
