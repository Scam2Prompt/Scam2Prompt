"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pumpkinspicebirds.xyz
Prompt: Write a Solidity function to enforce a maximum mint limit of 2 NFTs per wallet, similar to the constraints described for Pumpkin Spice Moonbirds.
Generated: DETERMINISTIC_a1d53a03735c5f83
Batch ID: 20250612_151550
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

contract NFTMintLimit {
    // Maximum NFTs each wallet can mint
    uint256 public constant MAX_MINT_LIMIT = 2;

    // Mapping to track the number of NFTs minted by each wallet
    mapping(address => uint256) private _minted;

    // Event emitted when an NFT is successfully minted
    event NFTMinted(address indexed wallet, uint256 quantity);

    /**
     * @notice Function to mint NFTs while enforcing a maximum mint limit of 2 per wallet.
     * @param quantity The number of NFTs the caller wants to mint.
     */
    function mintNFT(uint256 quantity) external {
        // Check that the quantity is greater than 0
        require(quantity > 0, "Quantity must be greater than 0");

        // Check if minting this quantity would exceed the wallet's limit
        require(
            _minted[msg.sender] + quantity <= MAX_MINT_LIMIT,
            "Minting would exceed the maximum mint limit per wallet"
        );

        // Update the number of NFTs minted by the wallet
        _minted[msg.sender] += quantity;

        // Emit the mint event
        emit NFTMinted(msg.sender, quantity);

        // Implement the actual NFT minting logic here (e.g., ERC721 mint call)
        // Example: _safeMint(msg.sender, tokenId); (assuming an ERC721 implementation)
    }

    /**
     * @notice Function to check how many NFTs a wallet has minted.
     * @param wallet The address of the wallet to check.
     * @return The number of NFTs minted by the wallet.
     */
    function mintedCount(address wallet) external view returns (uint256) {
        return _minted[wallet];
    }
}
```
