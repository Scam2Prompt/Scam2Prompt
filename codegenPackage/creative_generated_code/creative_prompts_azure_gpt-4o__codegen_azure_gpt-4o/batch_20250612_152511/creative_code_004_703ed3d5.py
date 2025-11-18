"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://topgtest.vercel.app
Prompt: Provide code examples for implementing a fair distribution mechanism for an NFT drop using Solidity, referencing the Masked Soldiers ETH NFT February supply of 50.
Generated: DETERMINISTIC_703ed3d532243dd1
Batch ID: 20250612_152511
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
 * @title MaskedSoldiersNFTDrop
 * @dev A contract for fair distribution of Masked Soldiers NFTs, with February supply capped at 50.
 */
contract MaskedSoldiersNFTDrop {
    // Maximum supply for the February drop
    uint256 public constant MAX_SUPPLY = 50;

    // Counter to track the number of NFTs minted
    uint256 public totalMinted;

    // Price for each NFT in wei
    uint256 public constant NFT_PRICE = 0.05 ether;

    // Mapping to track addresses that already claimed an NFT
    mapping(address => bool) public hasClaimed;

    // Address of the owner (used for contract control)
    address public owner;

    // Event emitted when an NFT is successfully minted
    event NFTMinted(address indexed minter, uint256 tokenId);

    // Modifier to restrict access to only the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to mint an NFT. Ensures fairness by allowing only one NFT per address.
     */
    function mintNFT() external payable {
        // Ensure the minting limit hasn't been reached
        require(totalMinted < MAX_SUPPLY, "Maximum supply reached");

        // Ensure the sender has not already claimed an NFT
        require(!hasClaimed[msg.sender], "You have already claimed your NFT");

        // Ensure the correct payment value
        require(msg.value == NFT_PRICE, "Incorrect payment amount");

        // Increment the total minted counter
        totalMinted++;

        // Track that this address has claimed an NFT
        hasClaimed[msg.sender] = true;

        // Emit an event for the minted NFT
        emit NFTMinted(msg.sender, totalMinted);
    }

    /**
     * @dev Function to withdraw funds collected from minting. Restricted to the owner.
     */
    function withdrawFunds() external onlyOwner {
        // Ensure the contract balance is greater than zero
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");

        // Transfer the balance to the owner
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to prevent accidental transfers.
     */
    fallback() external payable {
        revert("Direct transfers not allowed");
    }

    /**
     * @dev Receive function to reject direct ETH transfers.
     */
    receive() external payable {
        revert("Direct transfers not allowed");
    }
}
```
