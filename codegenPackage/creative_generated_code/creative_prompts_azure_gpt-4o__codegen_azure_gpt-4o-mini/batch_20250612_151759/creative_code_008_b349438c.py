"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multismartchain.web.app
Prompt: Create a Solidity contract to manage and troubleshoot NFTs, ensuring smooth functionality in the NFT marketplace as per MultiSmartChain's services.
Generated: DETERMINISTIC_b349438c12759ee8
Batch ID: 20250612_151759
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Pausable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title MultiSmartChainNFT
 * @dev A contract for creating and managing NFTs with functionalities for minting, burning, and pausing.
 */
contract MultiSmartChainNFT is ERC721, ERC721Burnable, ERC721Pausable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Event emitted when a new token is minted
    event TokenMinted(address indexed to, uint256 indexed tokenId);

    // Constructor to set the name and symbol of the NFT collection
    constructor() ERC721("MultiSmartChainNFT", "MSCNFT") {}

    /**
     * @dev Mint a new NFT to the specified address.
     * @param to The address to receive the minted NFT.
     * @return The ID of the minted token.
     */
    function mint(address to) external onlyOwner whenNotPaused returns (uint256) {
        require(to != address(0), "Cannot mint to the zero address");

        // Increment the token ID counter and set a new token ID
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the token
        _mint(to, tokenId);

        // Emit the token minted event
        emit TokenMinted(to, tokenId);

        return tokenId;
    }

    /**
     * @dev Pause the contract, preventing minting and transfers.
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause the contract, allowing minting and transfers.
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Override the _beforeTokenTransfer function to implement pausable functionality.
     */
    function _beforeTokenTransfer(address from, address to, uint256 tokenId) internal override(ERC721, ERC721Pausable) {
        super._beforeTokenTransfer(from, to, tokenId);
    }

    /**
     * @dev Retrieve the total number of minted NFTs.
     * @return The total supply of NFTs.
     */
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }

    /**
     * @dev Retrieve the owner of a specific token ID.
     * @param tokenId The ID of the token to query.
     * @return The address of the token owner.
     */
    function ownerOfToken(uint256 tokenId) external view returns (address) {
        return ownerOf(tokenId);
    }
}
```
