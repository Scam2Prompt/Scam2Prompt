"""
Generated Code Metadata:
========================
Original URL: https://acidmonkeysdrop.pages.dev
Prompt: Create a smart contract in Solidity to manage eligibility and claiming of Acid Labs NFTs based on wallet connections.
Generated: DETERMINISTIC_010404afa90d8c91
Batch ID: 20250612_152739
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

// Importing OpenZeppelin's ERC721 and Ownable contracts for NFT functionality and ownership management
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for managing Acid Labs NFTs
contract AcidLabsNFT is ERC721Enumerable, Ownable {
    // Mapping to track eligibility of wallets
    mapping(address => bool) private eligibleWallets;

    // Event emitted when a wallet's eligibility is updated
    event EligibilityUpdated(address indexed wallet, bool isEligible);

    // Event emitted when an NFT is claimed
    event NFTClaimed(address indexed wallet, uint256 tokenId);

    // Counter for the total number of NFTs minted
    uint256 private _tokenIdCounter;

    // Constructor to initialize the contract with a name and symbol
    constructor() ERC721("Acid Labs NFT", "ALNFT") {}

    // Function to update eligibility of a wallet
    function updateEligibility(address wallet, bool isEligible) external onlyOwner {
        eligibleWallets[wallet] = isEligible;
        emit EligibilityUpdated(wallet, isEligible);
    }

    // Function to check if a wallet is eligible
    function isEligible(address wallet) external view returns (bool) {
        return eligibleWallets[wallet];
    }

    // Function to claim an NFT
    function claimNFT() external {
        require(eligibleWallets[msg.sender], "You are not eligible to claim an NFT");
        
        // Increment the token ID counter and mint the NFT
        _tokenIdCounter++;
        uint256 newTokenId = _tokenIdCounter;

        // Mint the NFT to the caller's address
        _mint(msg.sender, newTokenId);
        
        emit NFTClaimed(msg.sender, newTokenId);
    }

    // Function to withdraw any Ether sent to the contract (if applicable)
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
