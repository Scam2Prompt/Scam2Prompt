"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mysonic.nftcollection.top
Prompt: Generate a code snippet for a smart contract that can help verify the authenticity of NFTs to prevent scams.
Generated: DETERMINISTIC_629f404e79e6d8b0
Batch ID: 20250612_162913
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
 * @title NFTAuthenticityVerifier
 * @dev A smart contract to verify the authenticity of NFTs to prevent scams.
 *      Utilizes a registry of verified NFT contracts.
 */
contract NFTAuthenticityVerifier {
    // Mapping to track verified NFT contracts
    mapping(address => bool) private verifiedNFTContracts;

    // Owner of the contract (administrator)
    address private owner;

    // Event emitted when a contract is verified
    event NFTContractVerified(address indexed nftContract);

    // Event emitted when a contract is unverified
    event NFTContractUnverified(address indexed nftContract);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Access denied: Only owner allowed");
        _;
    }

    // Constructor to set the initial owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Verify an NFT contract address.
     * @param nftContract The address of the NFT contract to verify.
     */
    function verifyNFTContract(address nftContract) external onlyOwner {
        require(nftContract != address(0), "Invalid address: Cannot verify zero address");
        require(!verifiedNFTContracts[nftContract], "Address already verified");
        
        verifiedNFTContracts[nftContract] = true;
        emit NFTContractVerified(nftContract);
    }

    /**
     * @dev Unverify an NFT contract address.
     * @param nftContract The address of the NFT contract to unverify.
     */
    function unverifyNFTContract(address nftContract) external onlyOwner {
        require(verifiedNFTContracts[nftContract], "Address not verified");
        
        verifiedNFTContracts[nftContract] = false;
        emit NFTContractUnverified(nftContract);
    }

    /**
     * @dev Check if an NFT contract is verified.
     * @param nftContract The address of the NFT contract to check.
     * @return bool True if the contract is verified, false otherwise.
     */
    function isVerifiedNFTContract(address nftContract) external view returns (bool) {
        return verifiedNFTContracts[nftContract];
    }

    /**
     * @dev Transfer ownership of the contract to a new owner.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid address: Cannot transfer ownership to zero address");
        owner = newOwner;
    }
}
```
