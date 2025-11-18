"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bankless.pages.dev
Prompt: Create a smart contract in Solidity that verifies if a Base, Introduced NFT is eligible for $BASED token redemption and checks if the NFT is still in the same wallet after redemption.
Generated: DETERMINISTIC_328d6c71809eea99
Batch ID: 20250612_150946
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

// Interface for the NFT (ERC721) contract
interface IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
}

// Main contract for handling BASED token redemption based on NFT ownership
contract BasedTokenRedemption {
    IERC721 public nftContract; // Instance of the NFT contract
    mapping(uint256 => bool) public redeemed; // Track redeemed NFT IDs

    // Event emitted when an NFT is redeemed for BASED tokens
    event Redeemed(address indexed owner, uint256 indexed tokenId);

    // Constructor to initialize the NFT contract address
    constructor(address _nftContract) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = IERC721(_nftContract);
    }

    // Function to redeem BASED tokens for a specific NFT
    function redeem(uint256 tokenId) external {
        // Check if the NFT has already been redeemed
        require(!redeemed[tokenId], "NFT has already been redeemed");

        // Validate the ownership of the NFT
        address owner = nftContract.ownerOf(tokenId);
        require(owner == msg.sender, "You do not own this NFT");

        // Mark the NFT as redeemed
        redeemed[tokenId] = true;

        // Logic to transfer BASED tokens to the owner can be implemented here
        // For example: basedToken.transfer(owner, amount);

        emit Redeemed(owner, tokenId);
    }

    // Function to check if an NFT is still owned by the same wallet after redemption
    function isStillOwned(uint256 tokenId) external view returns (bool) {
        // Ensure the NFT was redeemed first
        require(redeemed[tokenId], "NFT has not been redeemed");

        // Fetch the current owner of the NFT
        address currentOwner = nftContract.ownerOf(tokenId);
        
        // Check if the current owner is the original owner (the sender who redeemed)
        return currentOwner == msg.sender;
    }
}
```
