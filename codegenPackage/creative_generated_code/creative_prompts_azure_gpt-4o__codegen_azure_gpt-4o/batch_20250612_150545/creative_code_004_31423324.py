"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stealt-mint.web.app
Prompt: Create a function to limit NFT minting to three per wallet, as per the restrictions mentioned in the Magic Box stealth mint details.
Generated: DETERMINISTIC_31423324fa945ae8
Batch ID: 20250612_150545
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

contract MagicBoxNFT {
    // Event to log whenever an NFT is minted
    event NFTMinted(address indexed wallet, uint256 tokenId);

    // Mapping to track the number of NFTs minted by each wallet
    mapping(address => uint256) private _mintCount;

    // Maximum NFTs allowed per wallet
    uint256 public constant MAX_NFTS_PER_WALLET = 3;

    // Counter for token IDs
    uint256 private _currentTokenId;

    // Owner of the contract
    address public owner;

    // Modifier to restrict certain functions to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Access restricted to contract owner");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    // Function to mint an NFT
    function mintNFT() external {
        // Check if the caller has already minted the maximum allowed NFTs
        require(
            _mintCount[msg.sender] < MAX_NFTS_PER_WALLET,
            "Minting limit reached for this wallet"
        );

        // Increment the user's mint count
        _mintCount[msg.sender] += 1;

        // Generate a new token ID
        _currentTokenId += 1;

        // Simulate minting (you can integrate ERC721 logic here)
        emit NFTMinted(msg.sender, _currentTokenId);
    }

    // Function to get the number of NFTs minted by a wallet
    function getMintCount(address wallet) external view returns (uint256) {
        return _mintCount[wallet];
    }

    // Function for the owner to reset mint limits (if needed)
    function resetMintCount(address wallet) external onlyOwner {
        _mintCount[wallet] = 0;
    }

    // Function to get the current token ID
    function getCurrentTokenId() external view returns (uint256) {
        return _currentTokenId;
    }
}
```
