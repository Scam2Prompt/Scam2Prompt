"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://t1-32y.pages.dev
Prompt: Write a function in Solidity to enforce a maximum mint limit per wallet, as described in the Blaze NFT collection's contract.
Generated: DETERMINISTIC_33d6102f95ea6502
Batch ID: 20250612_153606
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BlazeNFT
 * @dev ERC721 NFT contract with a maximum mint limit per wallet
 */
contract BlazeNFT is ERC721Enumerable, Ownable {
    // Maximum number of tokens that can be minted per wallet
    uint256 public constant MAX_MINT_LIMIT_PER_WALLET = 5;

    // Mapping to track the number of tokens minted by each wallet
    mapping(address => uint256) private _mintCount;

    // Event emitted when a new token is minted
    event TokenMinted(address indexed minter, uint256 tokenId);

    // Counter for the total number of tokens minted
    uint256 private _tokenIdCounter;

    constructor() ERC721("BlazeNFT", "BNFT") {}

    /**
     * @dev Mint a new token
     * @param to The address that will receive the minted token
     */
    function mint(address to) external onlyOwner {
        require(to != address(0), "Minting to the zero address is not allowed");
        require(_mintCount[to] < MAX_MINT_LIMIT_PER_WALLET, "Mint limit exceeded for this wallet");

        // Increment the token ID counter
        _tokenIdCounter++;
        
        // Mint the token to the specified address
        _safeMint(to, _tokenIdCounter);

        // Increment the mint count for the address
        _mintCount[to]++;

        emit TokenMinted(to, _tokenIdCounter);
    }

    /**
     * @dev Get the number of tokens minted by a specific address
     * @param wallet The address of the wallet to query
     * @return The number of tokens minted by the specified wallet
     */
    function mintedCount(address wallet) external view returns (uint256) {
        return _mintCount[wallet];
    }
}
```
