"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimgift-x86.web.app
Prompt: Create a smart contract snippet in Solidity that verifies NFT ownership in a wallet and triggers the claim process for DUST tokens.
Generated: DETERMINISTIC_56c39bf978dc045a
Batch ID: 20250612_153225
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

// Import the ERC721 interface to interact with NFTs
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";

// Interface for the DUST token
interface IDUST {
    function mint(address to, uint256 amount) external;
}

// Smart contract to verify NFT ownership and trigger DUST token claims
contract NFTClaim {

    // Address of the DUST token contract
    IDUST public dustToken;

    // Mapping to track claimed status for each NFT
    mapping(address => mapping(uint256 => bool)) public hasClaimed;

    // Event to log successful claims
    event Claimed(address indexed user, address indexed nftContract, uint256 tokenId, uint256 amount);

    // Constructor to set the DUST token contract address
    constructor(address _dustToken) {
        require(_dustToken != address(0), "Invalid DUST token address");
        dustToken = IDUST(_dustToken);
    }

    // Function to claim DUST tokens for a specific NFT
    function claimDUST(address nftContract, uint256 tokenId, uint256 amount) external {
        // Check if the caller owns the specified NFT
        IERC721 nft = IERC721(nftContract);
        require(nft.ownerOf(tokenId) == msg.sender, "You do not own this NFT");

        // Verify that the user has not already claimed DUST for this NFT
        require(!hasClaimed[nftContract][tokenId], "DUST already claimed for this NFT");

        // Mark as claimed
        hasClaimed[nftContract][tokenId] = true;

        // Mint DUST tokens to the caller
        dustToken.mint(msg.sender, amount);

        // Emit an event for the successful claim
        emit Claimed(msg.sender, nftContract, tokenId, amount);
    }
}
```
