"""
Generated Code Metadata:
========================
Original URL: https://ronin-cyberkongz.pages.dev
Prompt: Write a Solidity contract that utilizes the Guardian Contract for on-chain two-factor authentication for NFTs.
Generated: DETERMINISTIC_e244dd1c47d6ae35
Batch ID: 20250612_160804
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
 * @title TwoFactorNFT
 * @dev A contract that uses a guardian contract for on-chain two-factor authentication for NFT transfers.
 */
contract TwoFactorNFT {
    // State variables
    address public owner; // Owner of the contract
    address public guardianContract; // Address of the guardian contract

    // Mapping to store NFT ownership
    mapping(uint256 => address) public nftOwners;

    // Events
    event NFTMinted(uint256 indexed tokenId, address indexed owner);
    event NFTTransferred(uint256 indexed tokenId, address indexed from, address indexed to);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier onlyNFTOwner(uint256 tokenId) {
        require(nftOwners[tokenId] == msg.sender, "Caller is not the NFT owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _guardianContract Address of the guardian contract.
     */
    constructor(address _guardianContract) {
        require(_guardianContract != address(0), "Invalid guardian contract address");
        owner = msg.sender;
        guardianContract = _guardianContract;
    }

    /**
     * @dev Function to mint a new NFT.
     * @param tokenId The ID of the NFT to mint.
     * @param to The address to assign ownership of the NFT.
     */
    function mintNFT(uint256 tokenId, address to) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(nftOwners[tokenId] == address(0), "Token ID already exists");

        nftOwners[tokenId] = to;
        emit NFTMinted(tokenId, to);
    }

    /**
     * @dev Function to transfer an NFT with two-factor authentication.
     * @param tokenId The ID of the NFT to transfer.
     * @param to The address to transfer the NFT to.
     * @param guardianApproval A boolean indicating guardian approval.
     */
    function transferNFT(uint256 tokenId, address to, bool guardianApproval) external onlyNFTOwner(tokenId) {
        require(to != address(0), "Invalid address");
        require(guardianApproval, "Guardian approval required");

        // Call the guardian contract to verify approval
        (bool success, bytes memory data) = guardianContract.call(
            abi.encodeWithSignature("verifyTransfer(address,uint256)", msg.sender, tokenId)
        );
        require(success, "Guardian contract verification failed");
        require(abi.decode(data, (bool)), "Guardian contract denied transfer");

        // Transfer ownership
        address previousOwner = nftOwners[tokenId];
        nftOwners[tokenId] = to;

        emit NFTTransferred(tokenId, previousOwner, to);
    }

    /**
     * @dev Function to update the guardian contract address.
     * @param _guardianContract The new guardian contract address.
     */
    function updateGuardianContract(address _guardianContract) external onlyOwner {
        require(_guardianContract != address(0), "Invalid guardian contract address");
        guardianContract = _guardianContract;
    }
}
```
