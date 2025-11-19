"""
Generated Code Metadata:
========================
Original URL: https://www.chibiheadnft.com
Prompt: Design a function in Solidity to transfer Open Head NFTs between users.
Generated: DETERMINISTIC_d3835756ef0a5962
Batch ID: 20250622_212452
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract OpenHeadNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    constructor() ERC721("OpenHeadNFT", "OHN") {}

    /**
     * @dev Safely transfers NFT from one address to another
     * @param from Current owner of the NFT
     * @param to Address to receive the NFT
     * @param tokenId ID of the NFT to transfer
     */
    function safeTransfer(
        address from,
        address to,
        uint256 tokenId
    ) external {
        require(_exists(tokenId), "OpenHeadNFT: Token does not exist");
        require(ownerOf(tokenId) == from, "OpenHeadNFT: Transfer from incorrect owner");
        require(to != address(0), "OpenHeadNFT: Transfer to the zero address");

        _safeTransfer(from, to, tokenId, "");
    }

    /**
     * @dev Mints a new NFT and assigns it to the specified address
     * @param to Address to receive the newly minted NFT
     */
    function safeMint(address to) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
    }

    /**
     * @dev Checks if a token exists
     * @param tokenId ID of the token to check
     * @return bool Whether the token exists
     */
    function exists(uint256 tokenId) external view returns (bool) {
        return _exists(tokenId);
    }
}
```
