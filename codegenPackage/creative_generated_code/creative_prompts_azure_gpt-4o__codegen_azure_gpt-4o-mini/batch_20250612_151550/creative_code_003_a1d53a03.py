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

contract NFTCollection {
    // Mapping to track the number of NFTs minted by each wallet
    mapping(address => uint256) private _mintedCount;

    // Maximum NFTs allowed to be minted per wallet
    uint256 public constant MAX_MINT_PER_WALLET = 2;

    // Event to log NFT minting
    event NFTMinted(address indexed minter, uint256 amount);

    // Function to mint NFTs
    function mintNFT(uint256 amount) external {
        require(amount > 0, "Minting amount must be greater than 0");
        require(amount + _mintedCount[msg.sender] <= MAX_MINT_PER_WALLET, 
                "Mint limit exceeded: A wallet can mint a maximum of 2 NFTs");

        // Update the count of minted NFTs for the sender
        _mintedCount[msg.sender] += amount;

        // Placeholder for actual NFT minting logic
        // _mint(msg.sender, amount);

        emit NFTMinted(msg.sender, amount);
    }

    // Function to check the number of NFTs minted by a wallet
    function mintedCount(address wallet) external view returns (uint256) {
        return _mintedCount[wallet];
    }
}
```
