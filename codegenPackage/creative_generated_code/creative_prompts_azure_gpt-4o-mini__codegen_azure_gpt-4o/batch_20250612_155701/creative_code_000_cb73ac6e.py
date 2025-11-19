"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint.fuckopensea.art
Prompt: Generate a smart contract for an NFT collection that allows minting with a supply limit of 10,000 and a maximum of 10 NFTs per transaction, ensuring no royalties are collected.
Generated: DETERMINISTIC_cb73ac6e1aac6fde
Batch ID: 20250612_155701
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
 * @title NFTCollection
 * @dev A smart contract for minting NFTs with a supply limit and restrictions.
 */
contract NFTCollection {
    // State variables
    uint256 public constant MAX_SUPPLY = 10000; // Maximum supply of NFTs
    uint256 public constant MAX_MINT_PER_TX = 10; // Maximum NFTs that can be minted per transaction
    uint256 public totalMinted; // Total number of NFTs minted
    address public owner; // Contract owner address

    // Mapping to track ownership of NFTs
    mapping(uint256 => address) private _owners;

    // Events
    event Mint(address indexed recipient, uint256 indexed tokenId);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier canMint(uint256 quantity) {
        require(quantity > 0 && quantity <= MAX_MINT_PER_TX, "Invalid minting quantity");
        require(totalMinted + quantity <= MAX_SUPPLY, "Exceeds maximum supply");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Public function to mint NFTs.
     * @param quantity The number of NFTs to mint.
     */
    function mint(uint256 quantity) external canMint(quantity) {
        for (uint256 i = 0; i < quantity; i++) {
            uint256 tokenId = totalMinted + 1;
            totalMinted++;
            _owners[tokenId] = msg.sender;

            emit Mint(msg.sender, tokenId);
        }
    }

    /**
     * @dev View function to retrieve the owner of a specific NFT.
     * @param tokenId The ID of the NFT.
     * @return The address of the owner.
     */
    function ownerOf(uint256 tokenId) external view returns (address) {
        require(tokenId > 0 && tokenId <= totalMinted, "Token does not exist");
        return _owners[tokenId];
    }

    /**
     * @dev Withdraw function for the contract owner to retrieve any funds sent to the contract.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to reject any direct Ether transfers.
     */
    receive() external payable {
        revert("Contract does not accept direct payments");
    }

    /**
     * @dev Function to update the contract owner.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        owner = newOwner;
    }
}
```
