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

/**
 * @title NFTOwnershipVerifier
 * @dev Smart contract to verify NFT ownership and allow DUST token claims.
 */
contract NFTOwnershipVerifier {
    // Address of the ERC721 NFT contract
    address public nftContract;

    // Address of the DUST token contract
    address public dustTokenContract;

    // Mapping to track if an address has already claimed DUST tokens
    mapping(address => bool) public hasClaimed;

    // Constructor to initialize NFT and DUST token contract addresses
    constructor(address _nftContract, address _dustTokenContract) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        require(_dustTokenContract != address(0), "Invalid DUST token contract address");
        nftContract = _nftContract;
        dustTokenContract = _dustTokenContract;
    }

    // Interface for ERC721 NFT contract
    interface IERC721 {
        function balanceOf(address owner) external view returns (uint256);
    }

    // Interface for DUST token contract
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
    }

    /**
     * @dev Allows a user to claim DUST tokens if they own an NFT.
     * Requirements:
     * - Caller must own at least one NFT.
     * - Caller must not have claimed DUST tokens before.
     */
    function claimDustTokens(uint256 dustAmount) external {
        // Check if the caller owns at least one NFT
        uint256 nftBalance = IERC721(nftContract).balanceOf(msg.sender);
        require(nftBalance > 0, "You must own at least one NFT");

        // Check if the caller has already claimed DUST tokens
        require(!hasClaimed[msg.sender], "You have already claimed DUST tokens");

        // Mark the caller as having claimed DUST tokens
        hasClaimed[msg.sender] = true;

        // Transfer DUST tokens to the caller
        bool success = IERC20(dustTokenContract).transfer(msg.sender, dustAmount);
        require(success, "DUST token transfer failed");
    }
}
```
