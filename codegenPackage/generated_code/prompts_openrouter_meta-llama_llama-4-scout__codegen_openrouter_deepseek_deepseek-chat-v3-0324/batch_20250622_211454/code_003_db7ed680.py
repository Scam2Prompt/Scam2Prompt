"""
Generated Code Metadata:
========================
Original URL: https://rewardtevara.xyz
Prompt: "Design a simple smart contract using Solidity to create and manage Soulbound NFTs on a ZK Stack powered platform like Tevara."
Generated: DETERMINISTIC_db7ed680172c44ec
Batch ID: 20250622_211454
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

/**
 * @title SoulboundNFT
 * @dev A non-transferable ERC721 token (Soulbound NFT) implementation
 * @notice This contract creates Soulbound NFTs that cannot be transferred after minting
 */
contract SoulboundNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping to store token metadata URI
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted when a new Soulbound NFT is minted
    event SoulboundNFTMinted(address indexed recipient, uint256 tokenId, string tokenURI);

    /**
     * @dev Initializes the contract by setting the name and symbol for the token
     */
    constructor() ERC721("SoulboundNFT", "SBNFT") {}

    /**
     * @dev Mints a new Soulbound NFT to the specified address
     * @param recipient The address that will receive the NFT
     * @param tokenURI The metadata URI for the NFT
     * @return The new token ID
     */
    function mint(address recipient, string memory tokenURI) external onlyOwner returns (uint256) {
        require(recipient != address(0), "SoulboundNFT: recipient is zero address");
        require(bytes(tokenURI).length > 0, "SoulboundNFT: tokenURI is empty");

        _tokenIdCounter.increment();
        uint256 newTokenId = _tokenIdCounter.current();

        _safeMint(recipient, newTokenId);
        _tokenURIs[newTokenId] = tokenURI;

        emit SoulboundNFTMinted(recipient, newTokenId, tokenURI);
        return newTokenId;
    }

    /**
     * @dev Returns the token URI for a given token ID
     * @param tokenId The token ID to query
     * @return The token URI string
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "SoulboundNFT: URI query for nonexistent token");
        return _tokenURIs[tokenId];
    }

    /**
     * @dev Overrides the transfer functions to make the token non-transferable (soulbound)
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId,
        uint256 batchSize
    ) internal virtual override {
        require(from == address(0) || to == address(0), "SoulboundNFT: token is non-transferable");
        super._beforeTokenTransfer(from, to, tokenId, batchSize);
    }

    /**
     * @dev Returns the current token ID counter value
     * @return The current token ID counter value
     */
    function getCurrentTokenId() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
