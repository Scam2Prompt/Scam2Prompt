"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypto-claim.pages.dev
Prompt: Generate code in Solidity for a smart contract that facilitates NFT claiming based on the steps described on crypto-claim.pages.dev, including network switching and transaction confirmation.
Generated: DETERMINISTIC_1c2990fe1e46cbc7
Batch ID: 20250612_151752
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

// Importing OpenZeppelin's ERC721 implementation for NFTs 
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ClaimableNFT
 * @dev This contract allows users to claim NFTs under certain conditions.
 */
contract ClaimableNFT is ERC721, Ownable {
    // Mapping from token ID to claim status
    mapping(uint256 => bool) private _claimedTokens;
    
    // Counter for the total number of tokens minted
    uint256 private _tokenIdCounter;

    // Event emitted when an NFT is claimed
    event TokenClaimed(address indexed claimant, uint256 indexed tokenId);

    // Constructor to initialize the NFT contract
    constructor() ERC721("ClaimableNFT", "CNFT") {}

    /**
     * @dev Function to claim an NFT.
     * Requirements:
     * - The token must not have been claimed already.
     */
    function claimNFT() external {
        // Increment the token ID counter for the next NFT
        uint256 tokenId = _tokenIdCounter;

        // Ensure that the token has not been claimed
        require(!_claimedTokens[tokenId], "NFT already claimed");

        // Mint the NFT to the caller
        _safeMint(msg.sender, tokenId);
        
        // Mark the token as claimed
        _claimedTokens[tokenId] = true;

        // Increment the counter for the next claim
        _tokenIdCounter++;

        // Emit the TokenClaimed event
        emit TokenClaimed(msg.sender, tokenId);
    }

    /**
     * @dev Function to check the claim status of a token.
     * @param tokenId The ID of the token to check.
     * @return bool Indicates if the token is claimed or not.
     */
    function isTokenClaimed(uint256 tokenId) external view returns (bool) {
        return _claimedTokens[tokenId];
    }

    /**
     * @dev Function to get the total number of claimed tokens.
     * @return uint256 The total number of claimed tokens.
     */
    function totalClaimedTokens() external view returns (uint256) {
        return _tokenIdCounter;
    }

    /**
     * @dev Function to withdraw any ETH that might be sent to this contract.
     * Only the owner can call this function.
     */
    function withdraw() external onlyOwner {
        // Transfer the contract's balance to the owner
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to prevent accidental ETH sends
    receive() external payable {
        revert("Direct ETH transfer not allowed");
    }
}
```
