"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://topgtest.vercel.app
Prompt: Outline a smart contract in Solidity for managing the distribution of 50 ETH NFTs in a fair manner.
Generated: DETERMINISTIC_fa2b0e603910e874
Batch ID: 20250612_161224
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
 * @title NFTDistribution
 * @dev A smart contract for fair distribution of 50 Ethereum-based NFTs.
 */
contract NFTDistribution {
    // Total number of NFTs available
    uint256 public constant MAX_SUPPLY = 50;

    // Price per NFT in wei
    uint256 public constant NFT_PRICE = 0.05 ether;

    // Counter for the number of NFTs sold
    uint256 public totalNFTsMinted;

    // Address of the contract owner
    address public owner;

    // Mapping to track which addresses have already minted
    mapping(address => bool) public hasMinted;

    // Event to log successful NFT minting
    event NFTMinted(address indexed minter, uint256 indexed tokenId);

    // Modifier to restrict functions to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Modifier to ensure minting conditions are met
    modifier canMint() {
        require(totalNFTsMinted < MAX_SUPPLY, "All NFTs have been minted");
        require(!hasMinted[msg.sender], "Address has already minted an NFT");
        require(msg.value == NFT_PRICE, "Incorrect ETH sent");
        _;
    }

    /**
     * @dev Constructor initializes the contract and sets the owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to mint an NFT. Ensures fair distribution.
     */
    function mintNFT() external payable canMint {
        // Increment the minted NFT count
        totalNFTsMinted++;

        // Mark the sender address as having minted
        hasMinted[msg.sender] = true;

        // Log the minting event
        emit NFTMinted(msg.sender, totalNFTsMinted);
    }

    /**
     * @dev Function to withdraw accumulated funds from the contract.
     */
    function withdraw() external onlyOwner {
        // Send the contract balance to the owner
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to prevent accidental ether transfers.
     */
    fallback() external payable {
        revert("Fallback function does not accept ETH");
    }

    /**
     * @dev Receive function to prevent accidental ether transfers.
     */
    receive() external payable {
        revert("Receive function does not accept ETH");
    }
}
```
