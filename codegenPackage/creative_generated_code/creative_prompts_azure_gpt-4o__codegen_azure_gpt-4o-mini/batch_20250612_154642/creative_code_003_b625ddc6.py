"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea-package.web.app
Prompt: Create a Solidity smart contract snippet that interacts with the OpenSea protocol to verify ownership of an NFT and approve asset usage.
Generated: DETERMINISTIC_b625ddc6b97f6c59
Batch ID: 20250612_154642
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

// Importing OpenZeppelin's ERC721 interface for interacting with NFTs
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
// Importing OpenZeppelin's safe math library for safe arithmetic operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Contract that interacts with the OpenSea protocol
contract OpenSeaNFTManager {
    using SafeMath for uint256;

    // Address of the ERC721 token contract (NFT)
    IERC721 public nftContract;

    // Event emitted when ownership is verified
    event OwnershipVerified(address indexed owner, uint256 indexed tokenId);
    // Event emitted when approval is granted for asset usage
    event ApprovalGranted(address indexed owner, address indexed operator, uint256 indexed tokenId);

    // Constructor to set the NFT contract address
    constructor(address _nftContract) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = IERC721(_nftContract);
    }

    // Function to verify ownership of an NFT
    function verifyOwnership(uint256 tokenId) external view returns (bool) {
        // Get the owner of the token with the given tokenId
        address owner = nftContract.ownerOf(tokenId);
        require(owner != address(0), "NFT does not exist");

        // Emit event for ownership verification
        emit OwnershipVerified(owner, tokenId);

        // Return true if the caller is the owner of the NFT
        return (msg.sender == owner);
    }

    // Function to approve an operator to transfer the NFT
    function approveOperator(address operator, uint256 tokenId) external {
        // Ensure that caller is the owner of the token
        require(nftContract.ownerOf(tokenId) == msg.sender, "Caller is not the owner");

        // Approve the operator for the specified token
        nftContract.approve(operator, tokenId);

        // Emit event for approval granted
        emit ApprovalGranted(msg.sender, operator, tokenId);
    }
}
```
