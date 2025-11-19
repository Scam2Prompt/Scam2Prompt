"""
Generated Code Metadata:
========================
Original URL: https://t1-32y.pages.dev
Prompt: Provide an example of a smart contract function that implements a royalty percentage of 0%, as specified in the Blaze NFT collection details.
Generated: DETERMINISTIC_523635f3eaeb23bc
Batch ID: 20250612_153606
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
import "@openzeppelin/contracts/interfaces/IERC2981.sol";

contract BlazeNFT is ERC721, Ownable, IERC2981 {
    uint256 private _tokenIdCounter;

    constructor() ERC721("BlazeNFT", "BLAZE") {}

    function mint(address to) public onlyOwner {
        uint256 tokenId = _tokenIdCounter;
        _tokenIdCounter++;
        _safeMint(to, tokenId);
    }

    /**
     * @dev Implements royalty info for ERC2981 standard
     * @param tokenId The token ID (unused in this implementation)
     * @param salePrice The sale price of the NFT
     * @return receiver The address to receive royalties (address(0) for no royalties)
     * @return royaltyAmount The royalty amount (0 for 0% royalty)
     */
    function royaltyInfo(
        uint256 tokenId,
        uint256 salePrice
    ) external view override returns (address receiver, uint256 royaltyAmount) {
        // Return 0% royalty
        return (address(0), 0);
    }

    /**
     * @dev See {IERC165-supportsInterface}.
     */
    function supportsInterface(bytes4 interfaceId) public view virtual override(ERC721, IERC165) returns (bool) {
        return interfaceId == type(IERC2981).interfaceId || super.supportsInterface(interfaceId);
    }
}
```
